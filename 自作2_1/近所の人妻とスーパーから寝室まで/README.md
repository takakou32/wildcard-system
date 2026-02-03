# 近所の人妻とスーパーから寝室まで

## テーマ概要

日常系のラブラブテーマです。スーパーでのショッピングから始まり、帰宅、料理、リビングでのリラックス、親密な時間、そして入浴まで、一日の流れを描いたシーン展開となっています。

## 設定

- **ベース**: lovey（ラブラブ）
- **テーマタイプ**: 日常系
- **時系列**: time_day（昼）→ time_night（夜）
- **男性タイプ**: デフォルト (faceless male)
- **Sex場所**: place_home_bedroom（自宅寝室）
- **Sex/Fellatio服装**: outfit_underwear（白いブラ、白いパンティー）

## シーンフロー

1. **Scene 01: time_day (昼) - 外出先でのショッピング・散策**
   - シーン: `scene_outdoor_shopping`
   - 服装: blouse_skirt_bag（ショッピング向けカジュアル）

2. **Scene 02: time_day (昼) - 帰宅中（街を歩く）**
   - シーン: `scene_street_walking`
   - 服装: blouse_skirt（基本的な外出着）

3. **Scene 03: time_day (昼) - 玄関到着**
   - シーン: `scene_home_entrance`
   - 服装: blouse_skirt（基本的な外出着）

4. **Scene 04: time_day (昼) - 料理中（食事準備）**
   - シーン: `scene_kitchen_cooking`
   - 服装: apron_sweater_jeans（エプロン付き）

5. **Scene 05: time_evening (夕方) - 自宅でのひと時（リラックス）**
   - シーン: `scene_living_room_relaxing`
   - 服装: sweater_jeans（基本的な室内着）

6. **Scene 06: time_night (夜) - 親密な時間（距離が近い）** ※NSFW: Light
   - シーン: `scene_intimate_moment`
   - 服装: sweater_jeans（リラックスシーンと同じ室内着）
   - NSFW: nsfw_light_all（キス、抱擁、愛撫、胸タッチ）

7. **Scene 07: time_night (夜) - 入浴（脱衣からシャワーまで）** ※NSFW: Moderate
   - シーン: `scene_bathroom_bathing`
   - 服装: nude（裸）
   - NSFW: nsfw_moderate_all（手コキ、パイズリ、指マン、クンニ、フェラ軽め等）

## 使用方法

### 個別シーンの使用

#### SFWシーンのみ
```
__自作2_1/近所の人妻とスーパーから寝室まで/pose_play_sfw__
```

#### NSFW前戯シーンのみ
```
__自作2_1/近所の人妻とスーパーから寝室まで/pose_play_nsfw__
```

#### Sexシーンのみ
```
__自作2_1/近所の人妻とスーパーから寝室まで/sex_play__
```

#### Fellatioシーンのみ
```
__自作2_1/近所の人妻とスーパーから寝室まで/fellatio_play__
```

#### サムネイル用プロンプト（手動実行用）
```
__自作2_1/近所の人妻とスーパーから寝室まで/thumbnail__
```

### 全シーン統合（推奨）

#### 全シーン（バランス調整済み）
```
__自作2_1/近所の人妻とスーパーから寝室まで/main__
```

**注意：** `main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

## バランス調整

`main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

### バランス例

- **SFW 50% / NSFW 50%**: sfw 3行 / nsfw 1行 / sex 1行 / fella 1行
- **SFW 30% / NSFW 70%**: sfw 2行 / nsfw 2行 / sex 2行 / fella 2行
- **SFW 20% / NSFW 80%**: sfw 1行 / nsfw 2行 / sex 2行 / fella 2行

現在の設定は **SFW 50% / NSFW 50%** です。
