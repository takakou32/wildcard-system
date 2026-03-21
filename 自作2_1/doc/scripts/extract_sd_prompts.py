"""
extract_sd_prompts.py
Easy Reforge (SD WebUI系) の PNG / WebP ファイルからプロンプトメタデータを抽出する。

使い方:
    python extract_sd_prompts.py <directory> [--limit N]

出力:
    JSON (stdout) - 抽出結果リスト（更新時刻降順）
"""

import json
import struct
import zlib
from pathlib import Path
from datetime import datetime


# ---------------------------------------------------------------------------
# PNG パーサ（PIL 不要）
# ---------------------------------------------------------------------------

def read_png_text_chunks(filepath):
    """PNG ファイルの tEXt/iTXt チャンクを辞書で返す。"""
    chunks = {}
    try:
        with open(filepath, "rb") as f:
            if f.read(8) != b"\x89PNG\r\n\x1a\n":
                return chunks
            while True:
                header = f.read(8)
                if len(header) < 8:
                    break
                length = struct.unpack(">I", header[:4])[0]
                chunk_type = header[4:8].decode("ascii", errors="ignore")
                data = f.read(length)
                f.read(4)  # CRC

                if chunk_type == "tEXt":
                    null_pos = data.find(b"\x00")
                    if null_pos != -1:
                        key = data[:null_pos].decode("latin-1", errors="ignore")
                        value = data[null_pos + 1:].decode("latin-1", errors="ignore")
                        chunks[key] = value

                elif chunk_type == "iTXt":
                    null1 = data.find(b"\x00")
                    if null1 == -1:
                        continue
                    key = data[:null1].decode("latin-1", errors="ignore")
                    rest = data[null1 + 1:]
                    comp_flag = rest[0] if len(rest) > 0 else 0
                    idx = 1
                    for _ in range(3):
                        n = rest.find(b"\x00", idx)
                        if n == -1:
                            idx = len(rest)
                            break
                        idx = n + 1
                    raw_text = rest[idx:]
                    if comp_flag == 1:
                        try:
                            raw_text = zlib.decompress(raw_text)
                        except Exception:
                            pass
                    chunks[key] = raw_text.decode("utf-8", errors="ignore")

                if chunk_type == "IEND":
                    break
    except Exception:
        pass
    return chunks


# ---------------------------------------------------------------------------
# WebP / EXIF パーサ
# ---------------------------------------------------------------------------

def read_webp_parameters(filepath):
    """
    WebP ファイルから SD パラメータ文字列を取得する。
    優先順位: PIL EXIF UserComment → PIL info['parameters'] → ファイル名フォールバック
    """
    # --- PIL で試みる ---
    try:
        from PIL import Image
        img = Image.open(filepath)

        # 1) info['parameters'] キー（Forge/A1111 が WebP に埋める場合）
        params = img.info.get("parameters", "")
        if params:
            return params

        # 2) ExifIFD > UserComment (tag 37510 = 0x9286)
        try:
            exif = img.getexif()
            # ExifIFD はネストしているので get_ifd(0x8769) で取得
            exif_ifd = exif.get_ifd(0x8769)
            user_comment = exif_ifd.get(37510) or exif.get(0x9286, b"")
            if isinstance(user_comment, bytes) and len(user_comment) > 8:
                header = user_comment[:8]
                payload = user_comment[8:]
                if header.startswith(b"UNICODE"):
                    # WebP の EXIF は UTF-16-BE で格納される
                    text = payload.decode("utf-16-be", errors="ignore").strip("\x00").strip()
                elif header.startswith(b"ASCII"):
                    text = payload.decode("ascii", errors="ignore").strip("\x00").strip()
                else:
                    # BOM なし UTF-8 として試みる
                    text = user_comment.decode("utf-8", errors="ignore").strip("\x00").strip()
            else:
                text = str(user_comment).strip() if user_comment else ""
            if text:
                return text
        except Exception:
            pass

        # 3) その他の info キー
        for k, v in img.info.items():
            if isinstance(v, str) and ("Steps:" in v or "Negative prompt:" in v):
                return v

    except ImportError:
        pass  # PIL なし → ファイル名フォールバックへ
    except Exception:
        pass

    return ""


def read_png_parameters(filepath):
    """PNG から SD パラメータ文字列を取得する。"""
    chunks = read_png_text_chunks(filepath)
    raw = chunks.get("parameters") or chunks.get("Parameters") or ""
    if not raw:
        for k, v in chunks.items():
            if "prompt" in k.lower() or "param" in k.lower():
                raw = v
                break

    # PIL フォールバック
    if not raw:
        try:
            from PIL import Image
            img = Image.open(filepath)
            raw = img.info.get("parameters", "")
        except Exception:
            pass

    return raw


# ---------------------------------------------------------------------------
# ファイル名からプロンプトを推測するフォールバック
# ---------------------------------------------------------------------------

def extract_from_filename(filepath):
    """
    Easy Reforge はプロンプトをファイル名に埋め込む設定がある。
    形式: {index}-{prompt_truncated}{hash}.ext
    """
    stem = Path(filepath).stem  # 拡張子なし
    # 先頭の "{数字}-" を除去
    import re
    stem = re.sub(r"^\d+-", "", stem)
    # 末尾のハッシュ（8文字の hex）を除去
    stem = re.sub(r"[0-9a-f]{8}$", "", stem).strip()
    if len(stem) > 10:
        return stem
    return ""


# ---------------------------------------------------------------------------
# SD パラメータ文字列のパース
# ---------------------------------------------------------------------------

def parse_sd_params(params_str):
    """SD WebUI 形式のパラメータ文字列を解析して構造化データを返す。"""
    if not params_str or not params_str.strip():
        return None

    lines = params_str.strip().splitlines()
    positive_lines = []
    negative_lines = []
    settings_line = ""
    mode = "positive"

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Negative prompt:"):
            mode = "negative"
            neg = stripped[len("Negative prompt:"):].strip()
            if neg:
                negative_lines.append(neg)
        elif mode != "positive" and any(
            stripped.startswith(k) for k in ("Steps:", "Sampler:", "CFG scale:", "Seed:")
        ):
            mode = "settings"
            settings_line = stripped
        elif mode == "settings":
            settings_line += " " + stripped
        elif mode == "positive":
            positive_lines.append(stripped)
        elif mode == "negative":
            negative_lines.append(stripped)

    positive = "\n".join(l for l in positive_lines if l).strip()
    negative = "\n".join(l for l in negative_lines if l).strip()

    settings = {}
    for part in settings_line.split(","):
        part = part.strip()
        if ":" in part:
            k, v = part.split(":", 1)
            settings[k.strip()] = v.strip()

    if not positive:
        return None

    return {"positive": positive, "negative": negative, "settings": settings}


# ---------------------------------------------------------------------------
# メイン処理
# ---------------------------------------------------------------------------

def extract_from_dir(directory, limit=None):
    dir_path = Path(directory)
    if not dir_path.exists():
        return {"error": f"Directory not found: {directory}"}

    # PNG と WebP を両方収集
    files = list(dir_path.glob("*.png")) + list(dir_path.glob("*.webp"))
    files = sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)

    if limit:
        files = files[:limit]

    results = []
    for img_file in files:
        ext = img_file.suffix.lower()

        if ext == ".png":
            raw = read_png_parameters(img_file)
        elif ext == ".webp":
            raw = read_webp_parameters(img_file)
        else:
            raw = ""

        # メタデータがなければファイル名から推測
        if not raw:
            raw = extract_from_filename(img_file)
            source = "filename"
        else:
            source = "metadata"

        if not raw:
            continue

        parsed = parse_sd_params(raw)

        # ファイル名由来の場合は positive のみで構造化
        if not parsed and source == "filename":
            parsed = {"positive": raw, "negative": "", "settings": {}}

        if not parsed or not parsed["positive"]:
            continue

        mtime = img_file.stat().st_mtime
        results.append({
            "file": img_file.name,
            "path": str(img_file),
            "mtime": mtime,
            "mtime_str": datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M"),
            "source": source,
            "positive": parsed["positive"],
            "negative": parsed["negative"],
            "settings": parsed["settings"],
        })

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Extract SD prompts from PNG/WebP files")
    parser.add_argument("directory", help="Directory containing image files")
    parser.add_argument("--limit", type=int, default=None, help="Max number of files to process")
    args = parser.parse_args()

    result = extract_from_dir(args.directory, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
