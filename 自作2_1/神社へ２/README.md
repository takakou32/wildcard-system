# 神社へ２

## テーマ概要

神社でデートを楽しみ、夜の庭園で親密な時間を過ごすテーマです。

## 設定

- **ベース**: lovey (ラブラブ)
- **テーマタイプ**: 神社系
- **時系列**: time_day (昼) → time_night (夜)
- **男性タイプ**: デフォルト
- **Sex場所**: place_shrine_building_interior (神社建物内)
- **Sex/Fellatio服装**: outfit_furisode (振袖)

## シーンフロー

1. **Scene 01: time_day (昼) - 神社境内を歩く**
   - シーン: `scene_shrine_grounds_walking`
   - 服装: furisode（振袖）

2. **Scene 02: time_day (昼) - お参り・お賽銭**
   - シーン: `scene_shrine_prayer_offering`
   - 服装: furisode（振袖）

3. **Scene 03: time_evening (夕方) - 回廊でいちゃつく** ※NSFW: Light
   - シーン: `scene_shrine_corridor_flirting`
   - 服装: furisode（振袖）
   - NSFW: キス、抱擁、愛撫、胸タッチ

4. **Scene 04: time_evening (夕方) - お守り・絵馬エリア**
   - シーン: `scene_shrine_omamori`
   - 服装: furisode（振袖）

5. **Scene 05: time_night (夜) - 庭園・自然** ※NSFW: Moderate
   - シーン: `scene_shrine_garden`
   - 服装: furisode（振袖）
   - NSFW: 手コキ、パイズリ、指マン、クンニ、フェラ軽め

## 使用方法

### 個別シーンの使用

#### SFWシーンのみ
```
__自作2_1/神社へ２/pose_play_sfw__
```

#### NSFW前戯シーンのみ
```
__自作2_1/神社へ２/pose_play_nsfw__
```

#### Sexシーンのみ
```
__自作2_1/神社へ２/sex_play__
```

#### Fellatioシーンのみ
```
__自作2_1/神社へ２/fellatio_play__
```

### 全シーン統合（推奨）

#### 全シーン（バランス調整済み）
```
__自作2_1/神社へ２/main__
```

**注意：** `main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

## バランス調整

`main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

### バランス例

- **SFW 50% / NSFW 50%**: sfw 3行 / nsfw 1行 / sex 1行 / fella 1行
- **SFW 30% / NSFW 70%**: sfw 2行 / nsfw 2行 / sex 2行 / fella 2行
- **SFW 20% / NSFW 80%**: sfw 1行 / nsfw 2行 / sex 2行 / fella 2行

現在の設定は **SFW 50% / NSFW 50%** です。
