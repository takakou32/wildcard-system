# テスト温泉

## テーマ概要

温泉・旅館系のラブラブテーマです。旅館到着から露天風呂まで、時系列に沿ったシーン展開となっています。

## 設定

- **ベース**: lovey（ラブラブ）
- **テーマタイプ**: 温泉・旅館系
- **時系列**: time_day (昼) → time_night (夜)
- **男性タイプ**: デフォルト (faceless male)
- **Sex場所**: place_ryokan_room（旅館客室）
- **Sex/Fellatio服装**: yukata（青い浴衣、白い帯）

## シーンフロー

1. **Scene 01: time_day (昼) - 旅館到着**
   - シーン: `scene_ryokan_arrival`
   - 服装: blouse_skirt（外出着）

2. **Scene 02: time_day (昼) - 客室でくつろぐ** ※NSFW: Light
   - シーン: `scene_ryokan_room`
   - 服装: yukata（浴衣）
   - NSFW: キス、抱擁、愛撫、胸タッチ

3. **Scene 03: time_day (昼) - 温泉街散策**
   - シーン: `scene_onsen_town`
   - 服装: yukata（浴衣）

4. **Scene 04: time_evening (夕方) - 旅館食事処**
   - シーン: `scene_ryokan_dining`
   - 服装: yukata（浴衣）

5. **Scene 05: time_evening (夕方) - 温泉脱衣所**
   - シーン: `scene_onsen_changing_room`
   - 服装: towel（バスタオル）

6. **Scene 07: time_night (夜) - 露天風呂** ※NSFW: Moderate
   - シーン: `scene_outdoor_bath`
   - 服装: nude（裸）
   - NSFW: 手コキ、パイズリ、指マン、クンニ、フェラ軽め

## 使用方法

### 個別シーンの使用

#### SFWシーンのみ
```
__自作2_1/テスト温泉/pose_play_sfw__
```

#### NSFW前戯シーンのみ
```
__自作2_1/テスト温泉/pose_play_nsfw__
```

#### Sexシーンのみ
```
__自作2_1/テスト温泉/sex_play__
```

#### Fellatioシーンのみ
```
__自作2_1/テスト温泉/fellatio_play__
```

### 全シーン統合（推奨）

#### 全シーン（バランス調整済み）
```
__自作2_1/テスト温泉/main__
```

**注意：** `main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

## バランス調整

`main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

### バランス例

- **SFW 50% / NSFW 50%**: sfw 3行 / nsfw 1行 / sex 1行 / fella 1行
- **SFW 30% / NSFW 70%**: sfw 2行 / nsfw 2行 / sex 2行 / fella 2行
- **SFW 20% / NSFW 80%**: sfw 1行 / nsfw 2行 / sex 2行 / fella 2行

現在の設定は **SFW 50% / NSFW 50%** です。

