# ビーチリゾートで彼女とバカンス

## テーマ概要

- **テーマ名**: ビーチリゾートで彼女とバカンス
- **ベース**: lovey (ラブラブ)
- **タイプ**: beach (ビーチ・リゾート系)
- **時系列**: あり（朝 → 夜）
- **男性タイプ**: デフォルト (male_type_default)
- **Sex場所**: shower_room (シャワールーム)
- **NSFW統合**: 完全分離

---

## シーンフロー

### Poseシーン（5シーン - SFWのみ）

1. **朝 - リゾート到着、チェックイン** (`resort_arrival`)
   - 服装: カジュアル外出着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: リゾートに到着、ビーチを眺める、チェックイン

2. **昼 - ビーチで遊ぶ、海水浴** (`beach_play`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: 海で泳ぐ、砂浜で遊ぶ、水遊び

3. **午後 - プールサイドでリラックス** (`poolside`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: 居心地の良い
   - 内容: プールサイドで休憩、ドリンクを楽しむ

4. **夕方 - シャワールームで二人きり（SFW）** (`shower_sfw`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: シャワーで海水を洗い流す、リフレッシュ

5. **夜 - ディナー、客室でくつろぐ** (`resort_room`)
   - 服装: 室内着
   - 表情: 親密
   - 雰囲気: 居心地の良い
   - 内容: リゾート客室でくつろぐ、夜景を楽しむ

### Sexシーン（6段階 - NSFW）

- **場所**: シャワールーム
- **男性タイプ**: デフォルト
- **段階**: intro_gentle → moderate → intense → extreme → creampie → after

### Fellatioシーン（8段階 - NSFW）

- **場所**: シャワールーム
- **男性タイプ**: デフォルト
- **段階**: intro_tease → start_licking → moderate_gentle → intense_passionate → climax_deep → finish_ejaculation → after_swallow → extra_intimate

---

## 使用方法

### 🎨 Poseシーンのみ（SFW）

```
__自作2_1/ビーチリゾートで彼女とバカンス/pose_play__
```

### 💕 Sexシーンのみ（NSFW）

```
__自作2_1/ビーチリゾートで彼女とバカンス/sex_play__
```

### 💋 Fellatioシーンのみ（NSFW）

```
__自作2_1/ビーチリゾートで彼女とバカンス/fellatio_play__
```

### 🌊 全シーン（Pose + Sex + Fellatio）

```
__自作2_1/ビーチリゾートで彼女とバカンス/main__
```

### ⚖️ バランス調整

`main.yaml` で SFW/NSFW の比率を調整できます：
- SFW重視: `pose_play` を 4-5行に増やす
- NSFW重視: `sex_play` や `fellatio_play` を 2-3行に増やす

---

## ファイル構成

```
ビーチリゾートで彼女とバカンス/
├── theme.txt          # テーマ名
├── config.yaml        # 設定（参考用、ワイルドカードとして使用しない）
├── pose_play.yaml     # Poseシーン定義（5シーン - SFW）
├── sex_play.yaml      # Sexシーン定義（6段階 - NSFW）
├── fellatio_play.yaml # Fellatioシーン定義（8段階 - NSFW）
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
- `time_morning` - 朝
- `time_afternoon` - 午後
- `time_evening` - 夕方
- `time_night` - 夜
- その他、`params/pose_times.yaml` 参照

### 表情・雰囲気を変更したい場合

loveyテーマで利用可能：
- 表情: `lovey_face_casual`, `lovey_face_intimate`, `lovey_face_bathing_prep`, `lovey_face_bathing`
- 雰囲気: `lovey_atmosphere_casual`, `lovey_atmosphere_cozy`, `lovey_atmosphere_romantic`, `lovey_atmosphere_steamy`

### Sex場所を変更したい場合

`sex_play.yaml` と `fellatio_play.yaml` で `place_shower_room` を他の場所に変更できます。

利用可能な場所：
- `place_shower_room` - シャワールーム（現在の設定）
- `place_hotel_room` - ホテル客室
- `place_beach_house` - ビーチハウス
- `place_home_shower` - 自宅シャワー
- その他、`params/pose_places.yaml` 参照

---

## 注意事項

- `config.yaml` はワイルドカードとして使用されません（参考用）
- 循環参照を避けるため、`main.yaml` 内で `main` 自身を参照しないでください
- NSFW統合は「完全分離」のため、SFWシーンには性的要素が含まれません

---

## 制作情報

- 作成日: 2025年1月
- ベースライブラリ: `themes/lovey/pose_scenes_beach.yaml`
- テーマベース: lovey（ラブラブ）
- シチュエーション: ビーチリゾートでのバカンス

