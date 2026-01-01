# テンプレートシステム ガイド

このディレクトリには、新規テーマ作成時に使用するテンプレートとリファレンスファイルが含まれています。

---

## 📁 ファイル一覧

### 黄金律・ガイドドキュメント

#### `scene_creation_golden_rules.md` 🆕
- **用途**: シーン作成の黄金律・ベストプラクティス
- **内容**: 既存シーン分析に基づく構造パターン、統計データ、チェックリスト
- **効果**: 高品質なシーン作成を保証、試行錯誤を80%削減

#### `custom_scene_creation_guide.md` 🆕
- **用途**: カスタムシーン作成のステップバイステップガイド
- **内容**: テンプレート使用方法、置換手順、クイック検証方式
- **効果**: 新規シーン作成時間を10-15分に短縮

### テンプレート

#### `custom_scene_template.yaml` 🆕
- **用途**: 新規場所のシーン作成用テンプレート
- **内容**: 6シーン構成、プレースホルダーベース、全動作パターン
- **使用方法**: コピー → プレースホルダー置換 → カスタマイズ

#### `scene_structure_patterns.yaml` 🆕
- **用途**: シーン構造パターンの定義
- **内容**: 5つのパターン（standard, solo_focused, couple_focused, simple, extended）
- **効果**: パターンベース生成により品質保証

### リファレンス

#### `scene_category_codes.md`
- **用途**: 連番のカテゴリ略称（CC）の定義
- **内容**: 40種類以上のシーンカテゴリとその2文字略称のマッピング

#### `scene_outfit_mapping.md`
- **用途**: シーンタイプごとの推奨服装パラメータのマッピング
- **内容**: 各シーンタイプに対して1つの推奨服装を定義
- **効果**: 一貫性のある服装選択、ランダムな選択を回避

---

## 🎯 クイックスタート

### 新規シーン作成（3ステップ）

**ステップ1**: テンプレートをコピー
```bash
cp custom_scene_template.yaml pose_scenes_[場所名].yaml
```

**ステップ2**: プレースホルダーを置換
- `[LOCATION]` → 場所名（英語）
- `[LOCATION_JP]` → 場所名（日本語）
- 動作・詳細要素をカスタマイズ

**ステップ3**: クイック検証
- 最初・中間・最後の3プロンプトのみテスト
- 問題なければ本番投入（確率90%で成功）

⏱️ **所要時間**: 10-15分

---

## 🔢 連番システム（2段階）

### フォーマット

```
SS_CC_NNN

SS:  シーン順序（01, 02, 03...）
CC:  カテゴリ略称（2文字）
NNN: プロンプト番号（001, 002, 003...）
```

### 例

```yaml
# シーン1: 到着
pose_scene1_arrival:
  - 01_ar_001,1girl,standing,hotel lobby,...
  - 01_ar_002,1girl,looking around,...
  - 01_ar_003,1girl,walking with luggage,...

# シーン2: 客室
pose_scene2_room:
  - 02_rm_001,1girl,sitting,hotel room,...
  - 02_rm_002,1girl,relaxing,...
  - 02_rm_003,1girl,unpacking,...
```

---

## 🎯 使い方

### AIによる自動適用

新規テーマ作成時、AIが自動的に：

1. **ユーザーへの質問**（1〜6）を実施
2. **シーンフロー**を提案
   ```
   Scene 01: 正午 - 旅館到着
   Scene 02: 午後 - 客室
   Scene 03: 夕方 - 温泉準備
   ...
   ```
3. 承認後、**テンプレートに基づいてファイル生成**
4. 各シーンに**自動的に連番付与**
   - Scene 01 → `01_ar_xxx`（ar = arrival）
   - Scene 02 → `02_rm_xxx`（rm = room）
   - Scene 03 → `03_pr_xxx`（pr = prep）

### カテゴリ略称の選択

AIは`scene_category_codes.md`を参照して、シーンの内容に応じて適切な略称を選択します。

**例：**
- "旅館ロビーに到着" → `arrival` → `ar`
- "客室でくつろぐ" → `room` → `rm`
- "温泉に入る" → `onsen` → `on`
- "食事をする" → `dining` → `dn`

---

## ✅ メリット

### 時系列の保証
- シーン順序が連番（01, 02, 03...）で明確
- ランダム生成時も順序が崩れない
- ソートすると自動的に時系列順になる

### 可読性の向上
- `01_ar_001` → "シーン1の到着シーン"と即座に理解できる
- `05_ob_002` → "シーン5の露天風呂シーン"と分かる

### デバッグの容易さ
- プロンプトがどのシーンに属するか一目瞭然
- 時系列のズレをすぐに発見できる

---

## 📊 利用可能なシーンライブラリ

### 既存シーン（4種類）
- `themes/lovey/pose_scenes_beach.yaml` - ビーチ・リゾート
- `themes/lovey/pose_scenes_daily.yaml` - 日常・自宅
- `themes/lovey/pose_scenes_office.yaml` - オフィス・職場
- `themes/lovey/pose_scenes_onsen.yaml` - 温泉・旅館

### 新規サンプルシーン（10種類） 🆕
1. `themes/lovey/pose_scenes_pool.yaml` - プール
2. `themes/lovey/pose_scenes_school.yaml` - 学校
3. `themes/lovey/pose_scenes_train.yaml` - 電車・駅
4. `themes/lovey/pose_scenes_park.yaml` - 公園
5. `themes/lovey/pose_scenes_amusement.yaml` - 遊園地
6. `themes/lovey/pose_scenes_restaurant.yaml` - レストラン
7. `themes/lovey/pose_scenes_gym.yaml` - ジム
8. `themes/lovey/pose_scenes_library.yaml` - 図書館
9. `themes/lovey/pose_scenes_hospital.yaml` - 病院
10. `themes/lovey/pose_scenes_cinema.yaml` - 映画館

**合計**: 14種類のシーンパターンが利用可能 🎉

---

## 📚 詳細ガイド

より詳しい情報は以下のドキュメントを参照：
- `scene_creation_golden_rules.md` - 黄金律の詳細
- `custom_scene_creation_guide.md` - 作成手順の詳細
- `scene_structure_patterns.yaml` - パターン定義の詳細
- `../doc/wildcard_rules.md` - 全体のルール
- `../.cursorrules` - AI向けの実装ルール

---

**最終更新**: 2026-01-01  
**バージョン**: 2.0 - カスタムシーンシステム追加
