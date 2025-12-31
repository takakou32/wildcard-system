# テスト温泉旅館で彼女と一夜

## 📝 テーマ情報

- **テーマ名**: テスト温泉旅館で彼女と一夜
- **ベース**: lovey（ラブラブ）
- **テーマタイプ**: onsen（温泉・旅館系）
- **男性タイプ**: male_type_default（デフォルト）
- **時系列**: time_morning（朝）→ time_night（夜）
- **Sex場所**: ryokan_room（旅館客室）
- **NSFW統合**: あり（全て混ぜる）

## 🎬 シーンフロー

### Scene 01: 朝 - 旅館到着
- チェックイン、玄関、ロビーでの到着シーン
- 服装: `outfit_casual_day`
- NSFW: なし

### Scene 02: 昼 - 客室でくつろぐ + NSFW Light
- 旅館の部屋でリラックス、窓辺、畳の上
- 服装: `outfit_yukata`
- NSFW統合: Light（キス、抱擁、タッチ）

### Scene 03: 昼 - 温泉街散策
- 浴衣姿で温泉街を歩く、お土産屋、景色
- 服装: `outfit_yukata`
- NSFW: なし

### Scene 04: 夕方 - 食事処
- 旅館の食事処で夕食、懐石料理
- 服装: `outfit_yukata`
- NSFW: なし

### Scene 05: 夕方 - 脱衣所
- 温泉前の脱衣所、着替え
- 服装: `outfit_towel`
- NSFW: なし

### Scene 06: 夕方 - 温泉 + NSFW Heavy
- 温泉に浸かる、湯気、リラックス
- 服装: `outfit_nude`
- NSFW統合: Heavy（前戯全般 - キス・ハグ、愛撫、手コキ、指マン、クンニ）

### Scene 07: 夜 - 露天風呂 + NSFW Heavy
- 夜の露天風呂、星空、月明かり
- 服装: `outfit_nude`
- NSFW統合: Heavy（前戯全般 - キス・ハグ、愛撫、手コキ、指マン、クンニ）

## 🚀 使い方

### Poseシーンのみ（SFW + NSFW統合版）
```
__wildcard-system/自作2_1/テスト温泉旅館で彼女と一夜/pose_play__
```

### Sexシーンのみ（NSFW）
```
__wildcard-system/自作2_1/テスト温泉旅館で彼女と一夜/sex_play__
```

### Fellatioシーンのみ（NSFW）
```
__wildcard-system/自作2_1/テスト温泉旅館で彼女と一夜/fellatio_play__
```

### 全シーン（Pose + Sex + Fellatio）
```
__wildcard-system/自作2_1/テスト温泉旅館で彼女と一夜/main__
```

## 📚 使用ライブラリ

### 共通パラメータ（params/）
- `male_type_default` - 男性キャラクタータイプ
- `outfit_casual_day`, `outfit_yukata`, `outfit_towel`, `outfit_nude` - 服装
- `time_morning`, `time_day`, `time_evening`, `time_night` - 時系列
- `place_ryokan_room`, `place_onsen`, `place_outdoor_bath` - 場所
- `angle_*` - カメラアングル

### テーマライブラリ（themes/lovey/）
- **シーン**: `scene_ryokan_arrival`, `scene_ryokan_room`, `scene_onsen_town`, `scene_ryokan_dining`, `scene_onsen_changing_room`, `scene_onsen_bathing`, `scene_outdoor_bath`
- **表情**: `lovey_face_casual`, `lovey_face_intimate`, `lovey_face_bathing_prep`, `lovey_face_bathing`
- **雰囲気**: `lovey_atmosphere_casual`, `lovey_atmosphere_cozy`, `lovey_atmosphere_romantic`, `lovey_atmosphere_steamy`
- **NSFW Light**: `nsfw_kiss`, `nsfw_embrace`, `nsfw_touch`
- **NSFW Heavy**: `foreplay_kiss_hug`, `foreplay_touch_caress`, `foreplay_handjob`, `foreplay_fingering`, `foreplay_cunnilingus`
- **Sex**: `sex_intro_gentle`, `sex_moderate`, `sex_intense`, `sex_extreme`, `sex_creampie`, `sex_after`
- **Fellatio**: `fellatio_intro_tease`, `fellatio_start_licking`, `fellatio_moderate_gentle`, `fellatio_intense_passionate`, `fellatio_climax_deep`, `fellatio_finish_ejaculation`, `fellatio_after_swallow`, `fellatio_extra_intimate`

## 💡 特徴

- **NSFW統合**: SFWシーンにNSFWを自然に混ぜ込み、シームレスな流れを実現
- **時系列変化**: 朝から夜まで、自然な時間の流れ
- **温泉旅館テーマ**: 旅館到着から温泉、露天風呂まで、温泉旅行の雰囲気を完全再現
- **連番管理**: ファイル名ソート時に時系列順で出力される

## 📅 作成日

2025-01-01

