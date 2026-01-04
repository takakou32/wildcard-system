# 電車内

## テーマ概要

電車・交通系のラブラブテーマです。駅到着から電車内、駅コンコースまで、電車内でのシーン展開となっています。

## 設定

- **ベース**: lovey（ラブラブ）
- **テーマタイプ**: 電車・交通系
- **時系列**: なし（特定の時間帯に固定 - time_day）
- **男性タイプ**: デフォルト (faceless male)
- **Sex場所**: public toilet（カスタム）
- **Sex/Fellatio服装**: blouse_skirt_blazer（カスタム）

## シーンフロー

1. **Scene 01: time_day (昼) - 駅到着**
   - シーン: `scene_station_arrival`
   - 服装: blouse_skirt_blazer（ビジネスウェア）

2. **Scene 02: time_day (昼) - プラットホーム**
   - シーン: `scene_train_platform`
   - 服装: blouse_skirt_blazer（ビジネスウェア）

3. **Scene 03: time_day (昼) - 電車内（混雑）** ※NSFW: Light（scene_train_chikan使用）
   - シーン: `scene_train_crowded`
   - 服装: blouse_skirt_blazer（ビジネスウェア）
   - NSFW: scene_train_chikanのプロンプトを使用（軽度〜重度の痴漢プレイ）

4. **Scene 04: time_day (昼) - 駅コンコース**
   - シーン: `scene_station_concourse`
   - 服装: blouse_skirt_blazer（ビジネスウェア）

## 使用方法

### 個別シーンの使用

#### SFWシーンのみ
```
__自作2_1/電車内/pose_play_sfw__
```

#### NSFW前戯シーンのみ
```
__自作2_1/電車内/pose_play_nsfw__
```

#### Sexシーンのみ
```
__自作2_1/電車内/sex_play__
```

#### Fellatioシーンのみ
```
__自作2_1/電車内/fellatio_play__
```

### 全シーン統合（推奨）

#### 全シーン（バランス調整済み）
```
__自作2_1/電車内/main__
```

**注意：** `main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

## バランス調整

`main.yaml`の行数を変更することで、SFW/NSFWの比率を調整できます。

### バランス例

- **SFW 50% / NSFW 50%**: sfw 3行 / nsfw 1行 / sex 1行 / fella 1行
- **SFW 30% / NSFW 70%**: sfw 2行 / nsfw 2行 / sex 2行 / fella 2行
- **SFW 20% / NSFW 80%**: sfw 1行 / nsfw 2行 / sex 2行 / fella 2行

現在の設定は **SFW 50% / NSFW 50%** です。

