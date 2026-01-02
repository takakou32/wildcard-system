# 神社へ

## テーマ概要

神社でデートを楽しみ、回廊や庭園で親密な時間を過ごすテーマです。

- **テーマベース**: lovey (ラブラブ)
- **テーマタイプ**: 神社系
- **時系列**: 昼（time_day） → 夜（time_night）
- **男性タイプ**: デフォルト
- **Sex場所**: 神社の建物内
- **Sex服装**: outfit_furisode

---

## シーンフロー

### Scene 01: 昼 - 神社境内を歩く（SFW）
鳥居をくぐり、石畳を歩きながら境内を散策。石灯籠や本殿を眺めつつ、ゆっくりとした参拝の時間。

### Scene 02: 昼 - お参り・お賽銭を投げる（SFW）
お賽銭を投げ、手を合わせてお祈り。鈴を鳴らし、二人で願い事をする神聖な瞬間。

### Scene 03: 昼〜夕方 - 神社の回廊でいちゃつく様子（SFW + NSFW Light）
人目につかない回廊で二人きりの時間。優しい雰囲気の中、徐々に親密な関係へ。
- **NSFW要素**: キス、抱擁、愛撫、胸タッチ

### Scene 05: 夕方 - お守り・絵馬エリア（SFW）
お守りを選んだり、絵馬に願い事を書いたり。二人でお守りを交換する甘い時間。

### Scene 06: 夕方〜夜 - 神社の庭園・自然（SFW + NSFW Moderate）
夜の静かな庭園で、月明かりの下、池のほとりで親密な時間を過ごす。
- **NSFW要素**: 手コキ、パイズリ、指マン、クンニ、フェラ軽め

---

## 使用方法

### 📂 個別シーンの使用

#### SFWシーンのみ
```
__自作2_1/神社へ/pose_play_sfw__
```

#### NSFW前戯シーンのみ
```
__自作2_1/神社へ/pose_play_nsfw__
```

#### Sexシーンのみ
```
__自作2_1/神社へ/sex_play__
```

#### Fellatioシーンのみ
```
__自作2_1/神社へ/fellatio_play__
```

---

### 🎯 全シーン統合（推奨）

#### 全シーン（バランス調整済み）
```
__自作2_1/神社へ/main__
```

**デフォルト設定**: SFW 50% / NSFW 50%
- SFWシーン: 3行（50%）
- NSFW軽〜中度: 1行（17%）
- Sex: 1行（17%）
- Fellatio: 1行（17%）

---

## バランス調整方法

`main.yaml` の行数を変更することで、SFW/NSFW比率を簡単に調整できます。

### 調整例

**SFW 70% / NSFW 30%**（SFW多め）
```yaml
main:
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_nsfw__
  - __自作2_1/神社へ/sex_play__
  - __自作2_1/神社へ/fellatio_play__
```

**SFW 30% / NSFW 70%**（NSFW多め）
```yaml
main:
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_sfw__
  - __自作2_1/神社へ/pose_play_nsfw__
  - __自作2_1/神社へ/pose_play_nsfw__
  - __自作2_1/神社へ/sex_play__
  - __自作2_1/神社へ/sex_play__
  - __自作2_1/神社へ/fellatio_play__
  - __自作2_1/神社へ/fellatio_play__
```

---

## ファイル構成

```
神社へ/
├── theme.txt                  # テーマ名
├── config.yaml                # 設定（参考用）
├── pose_play_sfw.yaml         # SFWシーン（全5シーン）
├── pose_play_nsfw.yaml        # NSFWシーン（Scene 03, 06のみ）
├── sex_play.yaml              # Sexシーン
├── fellatio_play.yaml         # Fellatioシーン
├── main.yaml                  # メインエントリーポイント
└── README.md                  # このファイル
```

---

## NSFW統合の詳細

### Scene 03: 神社の回廊でいちゃつく様子（Light）
- **連番**: `03_co_021`（SFW最終 `03_co_020` の次）
- **レベル**: Light
- **内容**: キス、抱擁、愛撫、胸タッチ
- **使用ライブラリ**: `nsfw_light_all`
- **行数**: 約20行

### Scene 06: 神社の庭園・自然（Moderate）
- **連番**: `06_gd_011`（SFW最終 `06_gd_010` の次）
- **レベル**: Moderate
- **内容**: 手コキ、パイズリ、指マン、クンニ、フェラ軽め
- **使用ライブラリ**: `nsfw_moderate_all`
- **行数**: 約30行

---

## 注意事項

1. **連番の連続性**: NSFWプロンプトはSFWの最終連番+1から開始され、ファイル名順でシームレスに並びます
2. **服装の継続性**: 同じシーン内でSFWからNSFWへ移行する際、服装は振袖（シーンライブラリに含まれる）で継続されます
3. **時間帯の継続性**: Scene 03は`time_day`、Scene 06は`time_evening`→`time_night`で統一されています
4. **場所情報**: NSFWプロンプトには場所情報（shrine corridor, shrine garden, 神社の建物内）が含まれています

---

## 推奨設定

- **キャラクター**: 人妻、既婚女性
- **服装**: 振袖（シーンライブラリに含まれる）
- **シチュエーション**: 神社デート、初詣、夜の密会

---

## カスタマイズ

### 時系列の変更
`pose_play_sfw.yaml` の時間パラメータ（`time_day`, `time_evening`, `time_night`）を変更することで、時間帯を調整できます。

### 男性タイプの変更
全ファイルの `male_type_default` を以下に変更可能：
- `male_type_dark_skin` - 黒肌チャラ男
- `male_type_shota` - ショタ
- `male_type_muscular` - 筋肉質
- `male_type_old_man` - おっさん

### Sex場所の変更
`sex_play.yaml` と `fellatio_play.yaml` の場所パラメータを変更可能：
- 現在: 神社の建物内（カスタム場所）
- 他の選択肢: `place_home_bedroom`, `place_hotel_room`, `place_car` など

---

**作成日**: 2026-01-01  
**バージョン**: 1.0  
**システムバージョン**: 2.0 - NSFW統合システム対応

