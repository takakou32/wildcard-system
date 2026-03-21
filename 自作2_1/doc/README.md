# doc フォルダ 目次

## ドキュメント一覧

| ファイル | 内容 |
|---------|------|
| [verified_scene_patterns.md](verified_scene_patterns.md) | 検証済みシーンパターンカタログ。全プロンプトの正典。セクション別にIDで管理 |
| [wildcard_rules.md](wildcard_rules.md) | ワイルドカード運用ルール。プロンプト生成時の基本方針 |
| [common_library_creation_rules.md](common_library_creation_rules.md) | 共通ライブラリ作成ルール。YAMLファイル作成時の規約 |
| [画像からプロンプト回収するコマンドのマニュアル.md](画像からプロンプト回収するコマンドのマニュアル.md) | `/collect-prompts` の使い方マニュアル |
| [scripts/extract_sd_prompts.py](scripts/extract_sd_prompts.py) | PNG/WebP からSD生成プロンプトを抽出するスクリプト |

## よく使うコマンド

### プロンプト収集（PNG → verified_scene_patterns.md）
```
/collect-prompts <画像フォルダパス>
```

### プロンプト開発（バリエーション生成）
```
/develop-prompts [エントリID or キーワード]
```

### テーマ別プロンプト生成
`../.agent/workflows/theme_prompt_pipeline.md` のワークフローに従う。

---

## PC操作（リモート）

### VS Code Tunnel（モバイルやサブPCからアクセス）

**起動コマンド:**
```
code tunnel --accept-server-license-terms
```

**接続URL:**
```
https://vscode.dev/tunnel/pc3
```

初回のみ GitHub 認証が必要。2回目以降は起動するだけで接続可能。
