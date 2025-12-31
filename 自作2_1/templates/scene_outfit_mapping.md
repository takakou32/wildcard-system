# シーン→服装のデフォルトマッピング

このファイルは、共通ライブラリから服装を自動選択する際の推奨マッピングです。

---

## 基本ルール

- 各シーンタイプに対して**1つの推奨服装パラメータ**を定義
- これにより一貫性のある服装選択が可能
- カスタマイズが必要な場合は`params_override/`で上書き

---

## シーンタイプ別の推奨服装

### 外出・移動系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 到着・出発 | ar, dp | `outfit_casual_day` | 基本的な外出着 |
| ショッピング | sp, sm | `outfit_casual_shopping` | ショッピング向けカジュアル |
| 街歩き・散歩 | st, wk | `outfit_casual_day` | 基本的な外出着 |
| 公園 | pk | `outfit_casual_day` | 基本的な外出着 |

### 室内・居住系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| リビング | lr | `outfit_house_clothes` | 基本的な室内着 |
| 料理・キッチン | kt | `outfit_house_with_apron` | エプロン付き |
| 食事 | dn | `outfit_house_clothes` | 基本的な室内着 |
| 寝室（日中） | bd | `outfit_house_clothes` | 基本的な室内着 |
| 寝室（夜） | bd | `outfit_pajamas` | パジャマ |
| 客室・ホテル | rm | `outfit_house_clothes` | 基本的な室内着 |

### 入浴・温泉系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 準備・着替え | pr, cr | `outfit_towel` | タオル姿 |
| 入浴・温泉 | bt, on | `outfit_nude` | 裸 |
| シャワー | sh | `outfit_nude` | 裸 |
| 露天風呂 | ob | `outfit_nude` | 裸 |
| バスローブ | - | `outfit_bathrobe` | バスローブ |

### ビーチ・リゾート系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| ビーチ到着・散策 | ba | `outfit_swimsuit` | 水着 |
| ビーチ活動 | bc | `outfit_swimsuit` | 水着 |
| ビーチカフェ | cf | `outfit_casual_day` | カジュアル外出着 |
| ビーチ更衣室 | ch | `outfit_towel` | タオル姿 |
| 夕暮れビーチ | ss | `outfit_swimsuit` | 水着 |
| リゾート客室 | rr | `outfit_house_clothes` | 室内着 |

### オフィス・職場系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| オフィス勤務 | of | `outfit_business` | ビジネスウェア |
| 会議室 | mt | `outfit_business` | ビジネスウェア |
| 休憩室 | br | `outfit_business` | ビジネスウェア |
| 残業 | ot | `outfit_business` | ビジネスウェア |
| エレベーター・階段 | el | `outfit_business` | ビジネスウェア |
| 個室 | pr | `outfit_business` | ビジネスウェア |
| 帰宅・駐車場 | lv | `outfit_business` | ビジネスウェア |

### 温泉・旅館系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 旅館到着 | ar | `outfit_casual_day` | 外出着 |
| 旅館客室 | rm | `outfit_yukata` | 浴衣 |
| 温泉街散策 | ot | `outfit_yukata` | 浴衣 |
| 旅館食事処 | dn | `outfit_yukata` | 浴衣 |
| 温泉脱衣所 | ch | `outfit_towel` | タオル姿 |
| 温泉入浴 | on | `outfit_nude` | 裸 |
| 露天風呂 | ob | `outfit_nude` | 裸 |

### その他特殊シーン

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 親密シーン | in | `outfit_underwear` | 下着 |
| リラックス | rx | `outfit_house_clothes` | 室内着 |

---

## 実装例

### AIがテーマ生成時に使用

```yaml
# シーン: 料理中（kitchen, kt）
# → 自動的に outfit_house_with_apron を選択

pose_scene3_kitchen:
  - 03_kt_001,__outfit_house_with_apron__,__scene_base_cooking__,...
  - 03_kt_002,__outfit_house_with_apron__,__scene_base_cooking__,...
```

### 服装の一貫性

同じシーンタイプでは常に同じ服装パラメータを使用：

```yaml
# すべてのキッチンシーンで outfit_house_with_apron を使用
pose_scene3_kitchen_cooking:
  - __outfit_house_with_apron__,...

pose_scene5_kitchen_cleanup:
  - __outfit_house_with_apron__,...  # 同じパラメータ
```

---

## カスタマイズ方法

デフォルトマッピングを変更したい場合：

### 方法1：テーマ作成時に「シーンごとに指定」を選択

質問6で「2. シーンごとに服装を指定」を選び、カスタム服装を定義。

### 方法2：params_overrideで上書き

```yaml
# params_override/character_outfits.yaml

# デフォルトの outfit_house_with_apron を上書き
outfit_house_with_apron:
  - custom white apron,red sweater,black jeans,specific style
  - custom pink apron,blue shirt,denim pants,custom look
```

### 方法3：エイリアスを作成

```yaml
# params_override/character_outfits.yaml

# テーマ専用のエイリアス
outfit_theme_cooking:
  - __outfit_house_with_apron__  # 既存のパラメータを参照
```

---

## 時間帯による服装変化

時間帯によって服装を変える場合：

| 時間帯 | 推奨服装 |
|--------|----------|
| 早朝〜午前 | `outfit_house_clothes` or `outfit_pajamas` |
| 正午〜夕方 | `outfit_casual_day` |
| 夜 | `outfit_house_clothes` or `outfit_pajamas` |
| 深夜 | `outfit_pajamas` or `outfit_nightgown` |

---

## まとめ

- ✅ 各シーンタイプに推奨服装を1つ定義
- ✅ AIはこのマッピングに従って服装を選択
- ✅ 一貫性のある服装パラメータ使用
- ✅ カスタマイズも可能

