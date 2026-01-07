# テストビーチで二人きり

## テーマ概要

- **テーマ名**: テストビーチで二人きり
- **ベース**: lovey (ラブラブ)
- **タイプ**: beach (ビーチ・リゾート系)
- **時系列**: あり（朝 → 夜）
- **男性タイプ**: デフォルト (male_type_default)
- **Sex場所**: hotel_room (客室)
- **NSFW統合**: 軽度混合（SFWシーンにキス・抱擁などのLight NSFWを少し混ぜる）

---

## シーンフロー

### Poseシーン（7シーン - SFW + Light NSFW混合）

1. **朝 - リゾート到着（ロビー・エントランス）** (`resort_arrival`)
   - 服装: カジュアル外出着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: リゾートに到着、ビーチを眺める、チェックイン
   - **NSFW**: なし（完全SFW）

2. **昼 - 客室チェックイン＆くつろぎ + NSFW Light** (`room_with_nsfw`)
   - 服装: カジュアル外出着
   - 表情: カジュアル / 親密
   - 雰囲気: 居心地の良い / ロマンチック
   - 内容: 客室でくつろぐ、荷物を整理
   - **NSFW**: キス、抱擁、タッチ（軽度）

3. **昼 - ビーチでアクティビティ（海辺、砂浜）** (`beach_activity`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: 海で泳ぐ、砂浜で遊ぶ、水遊び
   - **NSFW**: なし（完全SFW）

4. **午後 - プールサイドでリラックス + NSFW Light** (`poolside_with_nsfw`)
   - 服装: 水着
   - 表情: カジュアル / 親密
   - 雰囲気: 居心地の良い / ロマンチック
   - 内容: プールサイドで休憩、ドリンクを楽しむ
   - **NSFW**: キス、抱擁（軽度）

5. **夕方 - 夕暮れのビーチ散歩（ロマンチック）** (`sunset_beach`)
   - 服装: 水着
   - 表情: 親密
   - 雰囲気: ロマンチック
   - 内容: 夕暮れのビーチを散歩、夕日を眺める
   - **NSFW**: なし（完全SFW）

6. **夕方 - シャワールーム（着替え・準備）** (`shower_prep`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: シャワーで海水を洗い流す、リフレッシュ
   - **NSFW**: なし（完全SFW）

7. **夜 - 客室でディナー + NSFW Light** (`dinner_with_nsfw`)
   - 服装: 室内着
   - 表情: 親密
   - 雰囲気: 居心地の良い / ロマンチック
   - 内容: 客室でディナー、夜景を楽しむ
   - **NSFW**: キス、抱擁、タッチ（軽度）

### Sexシーン（6段階 - NSFW）

- **場所**: 客室 (hotel_room)
- **男性タイプ**: デフォルト
- **段階**: intro_gentle → moderate → intense → extreme → creampie → after

### Fellatioシーン（8段階 - NSFW）

- **場所**: 客室 (hotel_room)
- **男性タイプ**: デフォルト
- **段階**: intro_tease → start_licking → moderate_gentle → intense_passionate → climax_deep → finish_ejaculation → after_swallow → extra_intimate

---

## 使用方法

### 🎨 Poseシーンのみ（SFW + Light NSFW混合）

```
__自作2_1/テストビーチで二人きり/pose_play__
```

### 💕 Sexシーンのみ（NSFW）

```
__自作2_1/テストビーチで二人きり/sex_play__
```

### 💋 Fellatioシーンのみ（NSFW）

```
__自作2_1/テストビーチで二人きり/fellatio_play__
```

### 🌊 全シーン（Pose + Sex + Fellatio）

```
__自作2_1/テストビーチで二人きり/main__
```

### ⚖️ バランス調整

`main.yaml` で SFW/NSFW の比率を調整できます：
- SFW重視: `pose_play` を 4-5行に増やす
- NSFW重視: `sex_play` や `fellatio_play` を 2-3行に増やす

---

## ファイル構成

```
テストビーチで二人きり/
├── theme.txt          # テーマ名
├── config.yaml        # 設定（参考用、ワイルドカードとして使用しない）
├── pose_play.yaml     # Poseシーン定義（7シーン - SFW + Light NSFW混合）
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
- `time_day` - 昼
- `time_afternoon` - 午後
- `time_evening` - 夕方
- `time_night` - 夜
- その他、`params/pose_times.yaml` 参照

### 表情・雰囲気を変更したい場合

loveyテーマで利用可能：
- 表情: `lovey_face_casual`, `lovey_face_intimate`, `lovey_face_bathing_prep`, `lovey_face_bathing`
- 雰囲気: `lovey_atmosphere_casual`, `lovey_atmosphere_cozy`, `lovey_atmosphere_romantic`, `lovey_atmosphere_steamy`

### Sex場所を変更したい場合

`sex_play.yaml` と `fellatio_play.yaml` で `place_hotel_room` を他の場所に変更できます。

利用可能な場所：
- `place_hotel_room` - ホテル客室（現在の設定）
- `place_shower_room` - シャワールーム
- `place_beach_house` - ビーチハウス
- `place_home_shower` - 自宅シャワー
- その他、`params/pose_places.yaml` 参照

### NSFW統合レベルを調整したい場合

`pose_play.yaml` の各シーンで、NSFW Lightの行を削除または追加することで調整できます：

- **完全SFWにしたい場合**: Scene 02, 04, 07のNSFW Light行を削除
- **NSFW比率を上げたい場合**: 他のシーンにもNSFW Light行を追加

---

## 注意事項

- `config.yaml` はワイルドカードとして使用されません（参考用）
- 循環参照を避けるため、`main.yaml` 内で `main` 自身を参照しないでください
- NSFW統合は「軽度混合」のため、pose_playにはキス・抱擁などの軽度NSFW要素が含まれます

---

## 制作情報

- 作成日: 2025年1月
- ベースライブラリ: `themes/lovey/pose_scenes_beach.yaml`, `themes/lovey/nsfw_light.yaml`
- テーマベース: lovey（ラブラブ）
- シチュエーション: プライベートビーチで二人きりのバカンス



