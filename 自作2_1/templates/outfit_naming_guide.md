# 服装パラメータ命名規則ガイド
バージョン: 2.0  
更新日: 2026-01-02

## 概要

このガイドでは、服装パラメータの新しい命名規則について説明します。
シーンに紐づいた名称から、服装の内訳に基づくシンプルな短縮名称に変更されました。

---

## 命名規則の変更点

### 旧命名規則（〜2026-01-01）
シーンや用途に基づいた名称：
- `outfit_casual_day` - 日常カジュアル
- `outfit_casual_shopping` - ショッピング用カジュアル
- `outfit_house_clothes` - 室内着
- `outfit_house_with_apron` - エプロン付き室内着

**問題点:**
- シーン名が含まれるため、他のシーンで使いにくい
- 同じ服装でも用途が異なると別名になる
- 服装の統一性を保つのが困難

### 新命名規則（2026-01-02〜）
服装の主要アイテムの組み合わせを短縮名称として使用：
- `blouse_skirt` - ブラウス+スカート
- `blouse_skirt_bag` - ブラウス+スカート+買い物袋
- `sweater_jeans` - セーター+ジーンズ
- `apron_sweater_jeans` - エプロン+セーター+ジーンズ

**利点:**
- 服装の内容が一目で分かる
- シーンを問わず使用可能
- 服装の統一性を保ちやすい

---

## 命名規則の詳細

### 基本ルール

1. **主要アイテムの組み合わせ**  
   服装を構成する主要なアイテムをアンダースコア（`_`）で連結

2. **順序**  
   上から下へ（トップス → ボトムス → 小物）

3. **シンプルさ**  
   2〜3単語程度に抑える

4. **具体性**  
   色や素材は含めず、アイテムの種類のみ

### 命名パターン

#### パターン1: 2アイテム組み合わせ
```
トップス_ボトムス
例: blouse_skirt, sweater_jeans
```

#### パターン2: 3アイテム組み合わせ
```
小物_トップス_ボトムス
例: apron_sweater_jeans

トップス_ボトムス_小物
例: blouse_skirt_bag, blouse_skirt_blazer
```

#### パターン3: 単一アイテム
```
アイテム名のみ
例: swimsuit, pajamas, yukata, towel, nude
```

---

## 服装パラメータ一覧

### 外出着系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `blouse_skirt` | ブラウス+スカート | 基本的な外出着 |
| `blouse_skirt_bag` | ブラウス+スカート+買い物袋 | ショッピングシーン |

### 室内着系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `sweater_jeans` | セーター+ジーンズ | 基本的な室内着 |
| `apron_sweater_jeans` | エプロン+セーター+ジーンズ | 料理シーン |

### ビジネス系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `blouse_skirt_blazer` | ブラウス+スカート+ブレザー | ビジネスウェア |
| `office_lady` | オフィスレディ（正式） | ビジネスシーン |
| `blouse_slacks` | ブラウス+スラックス | ビジネスカジュアル |

### 和装系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `yukata` | 浴衣 | 神社、夏祭り |
| `kimono` | 着物 | フォーマル和装 |
| `furisode` | 振袖 | 成人式、初詣 |

### スポーツ・アクティブ系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `sportswear` | スポーツウェア | ジム、運動 |
| `swimsuit` | 水着 | ビーチ、プール |

### ナイトウェア系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `pajamas` | パジャマ | 就寝前後 |
| `nightgown` | ナイトガウン | 就寝時 |
| `bathrobe` | バスローブ | 入浴後 |

### 下着・裸系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `underwear` | 下着 | 親密シーン |
| `towel` | タオル | 入浴シーン |
| `nude` | 裸 | 入浴、親密シーン |

### 特殊・職業系
| パラメータ名 | 内容 | 用途 |
|------------|------|------|
| `nurse_uniform` | ナース服 | 病院シーン |
| `maid_dress` | メイド服 | メイド喫茶等 |
| `school_uniform` | 学校制服 | 学校シーン |

---

## 服装統一のベストプラクティス

### 1. シーン進行に応じた段階的な服装変更

テーマのストーリー展開に合わせて、自然なタイミングで服装を変更します。

**例: 近所の人妻とスーパーから寝室まで**
```yaml
# Scene 01-03: 外出シーン - 同じ外出着
blouse_skirt_bag

# Scene 04: 料理 - エプロン追加
apron_sweater_jeans

# Scene 05-06: 食事〜リラックス - 室内着
sweater_jeans

# Scene 07: 親密 - 下着
underwear

# Scene 08: 入浴 - 裸
nude
```

### 2. 全シーン統一（シンプル）

テーマ全体で同じ服装を維持する場合に適しています。

**例: ビーチリゾート**
```yaml
# Scene 01-05: 全て水着統一
swimsuit
```

**例: 神社参拝**
```yaml
# Scene 01-06: 全て浴衣統一
yukata
```

### 3. 時間帯ベースの服装変更

時間帯に応じて服装を変更します。

```yaml
# 昼: 外出着
blouse_skirt

# 夕方: 室内着
sweater_jeans

# 夜: パジャマ
pajamas
```

---

## 移行ガイド

### 既存テーマの更新方法

#### ステップ1: 服装パラメータの置換

旧パラメータ → 新パラメータ
```yaml
outfit_casual_day        → blouse_skirt
outfit_casual_shopping   → blouse_skirt_bag
outfit_house_clothes     → sweater_jeans
outfit_house_with_apron  → apron_sweater_jeans
outfit_business          → blouse_skirt_blazer
outfit_sportswear        → sportswear
outfit_swimsuit          → swimsuit
outfit_pajamas           → pajamas
outfit_yukata            → yukata
outfit_kimono            → kimono
outfit_underwear         → underwear
outfit_towel             → towel
outfit_nude              → nude
outfit_bathrobe          → bathrobe
outfit_nightgown         → nightgown
```

#### ステップ2: pose_play_sfw.yamlの更新

```yaml
# 旧
- __自作2_1/themes/lovey/scene_outdoor_shopping__,__自作2_1/params/male_type_default__,__自作2_1/params/outfit_casual_shopping__,...

# 新
- __自作2_1/themes/lovey/scene_outdoor_shopping__,__自作2_1/params/male_type_default__,__自作2_1/params/blouse_skirt_bag__,...
```

#### ステップ3: 服装統一の確認

連続するシーンで服装が一貫しているか確認します。

---

## トラブルシューティング

### Q: 服装が違和感なくシーン間で変わっているか？

**A:** 着替えのタイミングが自然な場所で変更しましょう。

✅ 良い例:
- 帰宅後に外出着 → 室内着
- 料理開始時に室内着 → エプロン付き室内着
- 入浴時に室内着 → タオル → 裸

❌ 悪い例:
- ショッピング中にいきなり室内着
- 連続シーンで理由なく服装が変わる

### Q: 服装の種類が多すぎる？

**A:** 1テーマあたり3〜4種類程度が適切です。

✅ 良い例:
- 外出着 → 室内着 → 下着 → 裸（4種類）

❌ 悪い例:
- 毎シーン異なる服装（8種類以上）

### Q: 旧パラメータ名を使い続けても動作する？

**A:** 動作しません。`character_outfits.yaml`で旧名称は削除されているため、新名称に更新する必要があります。

---

## まとめ

- ✅ 服装の内訳に基づくシンプルな短縮名称を使用
- ✅ シーン進行に応じた服装統一で違和感を解消
- ✅ `character_outfits.yaml`が単一の真実の情報源
- ✅ テンプレート（`pose_play_sfw_template.yaml`）を活用

---

## 参考ファイル

- `params/character_outfits.yaml` - 服装パラメータ定義
- `templates/pose_play_sfw_template.yaml` - SFWテーマテンプレート
- `templates/scene_outfit_mapping.md` - シーン→服装マッピング

---

作成日: 2026-01-02  
バージョン: 2.0

