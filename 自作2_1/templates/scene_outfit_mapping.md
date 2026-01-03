# シーン→服装のデフォルトマッピング

このファイルは、共通ライブラリから服装を自動選択する際の推奨マッピングです。

---

## 基本ルール

- 各シーンタイプに対して**1つの推奨服装パラメータ**を定義
- これにより一貫性のある服装選択が可能
- カスタマイズが必要な場合は`params_override/`で上書き

---

## 服装パラメータ命名規則（2026-01-02更新）

服装の主要アイテムの組み合わせを短縮名称として使用します：

### 外出着系
- `blouse_skirt` - ブラウス+スカート
- `blouse_skirt_bag` - ブラウス+スカート+買い物袋

### 室内着系
- `sweater_jeans` - セーター+ジーンズ
- `apron_sweater_jeans` - エプロン+セーター+ジーンズ

### ビジネス系
- `blouse_skirt_blazer` - ブラウス+スカート+ブレザー
- `office_lady` - オフィスレディ（正式）
- `blouse_slacks` - ブラウス+スラックス

### その他
- `swimsuit` - 水着
- `pajamas` - パジャマ
- `yukata` - 浴衣
- `kimono` - 着物
- `furisode` - 振袖
- `underwear` - 下着
- `nude` - 裸
- `towel` - タオル
- `sportswear` - スポーツウェア
- `nurse_uniform` - ナース服
- `maid_dress` - メイド服
- `school_uniform` - 学校制服
- `bathrobe` - バスローブ
- `nightgown` - ナイトガウン

---

## シーンタイプ別の推奨服装

### 外出・移動系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 到着・出発 | ar, dp | `blouse_skirt` | 基本的な外出着 |
| ショッピング | od, sp, sm | `blouse_skirt_bag` | ショッピング向けカジュアル |
| 街歩き・散歩 | st, wk | `blouse_skirt` | 基本的な外出着 |
| 公園 | pk | `blouse_skirt` | 基本的な外出着 |
| 玄関到着 | en | `blouse_skirt` | 基本的な外出着（帰宅時） |

### 室内・居住系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| リビング | lr | `sweater_jeans` | 基本的な室内着 |
| 料理・キッチン | kt | `apron_sweater_jeans` | エプロン付き |
| 食事 | dn | `sweater_jeans` | 基本的な室内着 |
| 寝室（日中） | bd | `sweater_jeans` | 基本的な室内着 |
| 寝室（夜） | bd | `pajamas` | パジャマ |
| 客室・ホテル | rm | `sweater_jeans` | 基本的な室内着 |

### 入浴・温泉系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 準備・着替え | pr, cr | `towel` | タオル姿 |
| 入浴・温泉 | bt, on | `nude` | 裸 |
| シャワー | sh | `nude` | 裸 |
| 露天風呂 | ob | `nude` | 裸 |
| バスローブ | - | `bathrobe` | バスローブ |

### ビーチ・リゾート系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| ビーチ到着・散策 | ba | `swimsuit` | 水着 |
| ビーチ活動 | bc | `swimsuit` | 水着 |
| ビーチカフェ | cf | `blouse_skirt` | カジュアル外出着 |
| ビーチ屋外シャワー | os | `swimsuit` | 水着（シャワー中） |
| ビーチ更衣室 | ch | `swimsuit` | 水着 |
| 夕暮れビーチ | ss | `swimsuit` | 水着 |
| リゾート客室 | rr | `sweater_jeans` | 室内着 |

### オフィス・職場系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| オフィス勤務 | of | `blouse_skirt_blazer` | ビジネスウェア |
| 会議室 | mt | `blouse_skirt_blazer` | ビジネスウェア |
| 休憩室 | br | `blouse_skirt_blazer` | ビジネスウェア |
| 残業 | ot | `blouse_skirt_blazer` | ビジネスウェア |
| エレベーター・階段 | el | `blouse_skirt_blazer` | ビジネスウェア |
| 個室 | pr | `blouse_skirt_blazer` | ビジネスウェア |
| 帰宅・駐車場 | lv | `blouse_skirt_blazer` | ビジネスウェア |

### 温泉・旅館系

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 旅館到着 | ar | `blouse_skirt` | 外出着 |
| 旅館客室 | rm | `yukata` | 浴衣 |
| 温泉街散策 | ot | `yukata` | 浴衣 |
| 旅館食事処 | dn | `yukata` | 浴衣 |
| 温泉脱衣所 | ch | `towel` | タオル姿 |
| 温泉入浴 | on | `nude` | 裸 |
| 露天風呂 | ob | `nude` | 裸 |

### その他特殊シーン

| シーンタイプ | カテゴリ略称 | 推奨服装パラメータ | 説明 |
|------------|------------|-----------------|------|
| 親密シーン（日常系） | in | `sweater_jeans` | リラックスシーンと同じ室内着（日常系テーマ用） |
| リラックス | rx | `sweater_jeans` | 室内着 |
| ジム・運動 | gm | `sportswear` | スポーツウェア |
| 入浴・シャワー（日常系） | bt | `nude` | 裸（入浴シーン） |

---

## 実装例

### AIがテーマ生成時に使用

```yaml
# シーン: 料理中（kitchen, kt）
# → 自動的に apron_sweater_jeans を選択

pose_scene3_kitchen:
  - 03_kt_001,__apron_sweater_jeans__,__scene_base_cooking__,...
  - 03_kt_002,__apron_sweater_jeans__,__scene_base_cooking__,...
```

### 服装の一貫性

同じシーンタイプでは常に同じ服装パラメータを使用：

```yaml
# すべてのキッチンシーンで apron_sweater_jeans を使用
pose_scene3_kitchen_cooking:
  - __apron_sweater_jeans__,...

pose_scene5_kitchen_cleanup:
  - __apron_sweater_jeans__,...  # 同じパラメータ
```

---

## カスタマイズ方法

デフォルトマッピングを変更したい場合：

### 方法1：テーマ作成時に「シーンごとに指定」を選択

質問6で「2. シーンごとに服装を指定」を選び、カスタム服装を定義。

### 方法2：params_overrideで上書き

```yaml
# params_override/character_outfits.yaml

# デフォルトの apron_sweater_jeans を上書き
apron_sweater_jeans:
  - custom white apron,red sweater,black jeans,specific style
  - custom pink apron,blue shirt,denim pants,custom look
```

### 方法3：エイリアスを作成

```yaml
# params_override/character_outfits.yaml

# テーマ専用のエイリアス
outfit_theme_cooking:
  - __apron_sweater_jeans__  # 既存のパラメータを参照
```

---

## 時間帯による服装変化

時間帯によって服装を変える場合：

| 時間帯 | 推奨服装 |
|--------|----------|
| 早朝〜午前 | `sweater_jeans` or `pajamas` |
| 正午〜夕方 | `blouse_skirt` |
| 夜 | `sweater_jeans` or `pajamas` |
| 深夜 | `pajamas` or `nightgown` |

---

## まとめ

- ✅ 各シーンタイプに推奨服装を1つ定義
- ✅ AIはこのマッピングに従って服装を選択
- ✅ 一貫性のある服装パラメータ使用
- ✅ カスタマイズも可能

