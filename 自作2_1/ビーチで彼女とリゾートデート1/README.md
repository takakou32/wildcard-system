# ビーチで彼女とリゾートデート1

## テーマ概要

- **テーマ名**: ビーチで彼女とリゾートデート1
- **ベース**: lovey (ラブラブ)
- **タイプ**: beach (ビーチ・リゾート系)
- **時系列**: あり（午後 → 夜）
- **男性タイプ**: デフォルト (faceless male)
- **Sex場所**: hotel_room (ホテル客室)

---

## シーンフロー

### Poseシーン（6シーン）

1. **午後 - ビーチ到着・散策** (`beach_arrival`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: ビーチに到着、砂浜を歩く、波打ち際でのんびり

2. **午後 - ビーチでの活動** (`beach_activity`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: 水遊び、砂浜でリラックス、日光浴

3. **午後 - ビーチカフェ** (`beach_cafe`)
   - 服装: カジュアル外出着
   - 表情: カジュアル
   - 雰囲気: 居心地の良い
   - 内容: カフェで休憩、ドリンクを楽しむ

4. **夕方 - 夕暮れビーチ** (`beach_sunset`)
   - 服装: 水着
   - 表情: 親密
   - 雰囲気: ロマンチック
   - 内容: 夕日を眺める、ロマンチックな散歩

5. **夕方～夜 - 更衣室・シャワー** (`beach_changing`)
   - 服装: タオル
   - 表情: 入浴準備
   - 雰囲気: カジュアル
   - 内容: 着替え、シャワーで砂を洗い流す

6. **夜 - リゾート客室** (`resort_room`)
   - 服装: 室内着
   - 表情: 親密
   - 雰囲気: 居心地の良い
   - 内容: ホテルの部屋でくつろぐ、バルコニーからの景色

### Sexシーン（6段階）

- **場所**: ホテル客室
- **男性タイプ**: デフォルト
- **段階**: intro_gentle → moderate → intense → extreme → creampie → after

---

## 使用方法

### 🎨 Poseシーンのみ（SFW）

```
__自作2_1/ビーチで彼女とリゾートデート1/pose_play__
```

### 💕 Sexシーンのみ（NSFW）

```
__自作2_1/ビーチで彼女とリゾートデート1/sex_play__
```

### 🌊 全シーン（Pose + Sex）

```
__自作2_1/ビーチで彼女とリゾートデート1/main__
```

---

## ファイル構成

```
ビーチで彼女とリゾートデート1/
├── theme.txt          # テーマ名
├── config.yaml        # 設定（参考用、ワイルドカードとして使用しない）
├── pose_play.yaml     # Poseシーン定義（6シーン）
├── sex_play.yaml      # Sexシーン定義（6段階）
├── main.yaml          # 統合エントリーポイント
└── README.md          # このファイル
```

---

## カスタマイズ

### 服装を変更したい場合

`pose_play.yaml` の各シーンで `outfit_xxx` を変更してください。

利用可能な服装パラメータ：
- `outfit_swimsuit` - 水着
- `outfit_casual_day` - カジュアル外出着
- `outfit_house_clothes` - 室内着
- `outfit_towel` - タオル
- `outfit_nude` - 裸
- その他、`params/character_outfits.yaml` 参照

### 時間帯を変更したい場合

`pose_play.yaml` の各シーンで `time_xxx` を変更してください。

利用可能な時間帯：
- `time_afternoon` - 午後
- `time_evening` - 夕暮れ
- `time_night` - 夜
- その他、`params/pose_times.yaml` 参照

### 表情・雰囲気を変更したい場合

loveyテーマで利用可能：
- 表情: `lovey_face_casual`, `lovey_face_intimate`, `lovey_face_bathing_prep`, `lovey_face_bathing`
- 雰囲気: `lovey_atmosphere_casual`, `lovey_atmosphere_cozy`, `lovey_atmosphere_romantic`, `lovey_atmosphere_steamy`

---

## 注意事項

- `config.yaml` はワイルドカードとして使用されません（参考用）
- 循環参照を避けるため、`main.yaml` 内で `main` 自身を参照しないでください
- Sex場所は `params/pose_places.yaml` から選択してください

---

## 制作情報

- 作成日: 2025年
- ベースライブラリ: `themes/lovey/pose_scenes_beach.yaml`
- 連番システム: SS_CC_NNN形式（シーン順序_カテゴリ略称_プロンプト番号）

