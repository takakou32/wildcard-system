# カスタムシーン作成ガイド

このガイドでは、`custom_scene_template.yaml` を使用して、新しい場所のシーンファイルを効率的に作成する方法を説明します。

---

## 🎯 目標

- **既存の検証済み構造を再利用**して、試行錯誤を80%削減
- **テンプレートベース生成**により、高品質なシーンを短時間で作成
- **クイック検証**により、テスト時間を最小化

---

## 📋 準備

### 必要なファイル

1. `custom_scene_template.yaml` - ベーステンプレート
2. `scene_creation_golden_rules.md` - 黄金律の参照
3. `scene_category_codes.md` - カテゴリ略称の参照
4. `scene_structure_patterns.yaml` - パターンの参照

### 作成前の質問

新しいシーンを作成する前に、以下を明確にします：

1. **場所は？** (例: プール、学校、電車、公園)
2. **テーマタイプは？** (例: リゾート、日常、冒険)
3. **主な活動は？** (例: 泳ぐ、勉強する、移動する)
4. **雰囲気は？** (例: 明るい、静か、活発)
5. **何シーン必要？** (推奨: 6-8シーン)

---

## 🚀 ステップバイステップ手順

### ステップ1: テンプレートをコピー

```bash
# テンプレートをコピーして新しいファイル名にする
cp custom_scene_template.yaml pose_scenes_[場所名].yaml

# 例
cp custom_scene_template.yaml pose_scenes_pool.yaml
cp custom_scene_template.yaml pose_scenes_school.yaml
cp custom_scene_template.yaml pose_scenes_train.yaml
```

---

### ステップ2: 必須置換を実行

新しいファイルを開き、以下のプレースホルダーを置換します。

#### 2.1 基本情報の置換

| プレースホルダー | 置換内容 | 例 |
|----------------|---------|-----|
| `[LOCATION]` | 場所名（英語） | `pool` |
| `[LOCATION_JP]` | 場所名（日本語） | `プール` |
| `[THEME_TYPE]` | テーマタイプ | `resort` |

**置換例:**
```yaml
# Before
scene_[LOCATION]_arrival:
  - 01_ar_001,1girl,[LOCATION],entering,looking around,...

# After
scene_pool_arrival:
  - 01_ar_001,1girl,pool,entering,looking around,...
```

---

### ステップ3: 場所固有の要素を追加

テンプレートの各シーンに、場所固有の要素を追加します。

#### 3.1 場所固有プレースホルダーの置換

| プレースホルダー | 説明 | プール例 | 学校例 |
|----------------|------|---------|--------|
| `[LANDMARK]` | 目印 | `pool entrance` | `school gate` |
| `[SPECIFIC_LOCATION]` | 具体的な小場所 | `poolside` | `classroom` |
| `[REST_AREA]` | 休憩エリア | `pool cafe` | `cafeteria` |
| `[SPECIAL_SPOT]` | 特別な場所 | `sunset poolside` | `rooftop` |
| `[PRIVATE_SPACE]` | プライベート空間 | `private cabana` | `empty classroom` |

#### 3.2 動作プレースホルダーの置換

**ソロ動作 (ACTION_1 〜 ACTION_9)**

| 場所 | ACTION_1 | ACTION_2 | ACTION_3 | ACTION_4 | ACTION_5 |
|------|----------|----------|----------|----------|----------|
| プール | swimming | splashing water | sitting on edge | floating | diving |
| 学校 | writing at desk | reading textbook | standing by window | walking in hallway | sitting on desk |
| 電車 | looking out window | holding handrail | sitting on seat | standing in aisle | checking phone |
| 公園 | walking on path | sitting on bench | feeding birds | reading book | jogging |

**カップル動作 (COUPLE_ACTION_1 〜 COUPLE_ACTION_5)**

| 場所 | COUPLE_ACTION_1 | COUPLE_ACTION_2 | COUPLE_ACTION_3 |
|------|----------------|----------------|----------------|
| プール | swimming together | splashing playfully | sitting on edge together |
| 学校 | studying together | sharing textbook | walking in hallway together |
| 電車 | sitting together | holding hands on handrail | looking at scenery together |
| 公園 | walking hand in hand | sitting on bench together | having picnic together |

#### 3.3 その他の置換

| プレースホルダー | 説明 | 例 |
|----------------|------|-----|
| `[DETAIL]` | 詳細要素 | `water droplets glistening` |
| `[BEVERAGE]` | 飲み物 | `tropical drink` |
| `[OBJECT]` | オブジェクト | `towel`, `book` |
| `[ITEM]` | アイテム | `drink`, `snack` |
| `[SCENERY]` | 景色 | `pool view`, `city skyline` |
| `[BACKGROUND]` | 背景 | `sunset`, `cherry blossoms` |
| `[DRAMATIC_ACTION]` | ドラマチックな動作 | `jumping into pool`, `running` |

---

### ステップ4: カテゴリ略称の確認と調整

各シーンの連番カテゴリ略称（CC部分）を確認します。

**`scene_category_codes.md`を参照:**

| シーン内容 | 推奨カテゴリ | 略称 | 例 |
|-----------|------------|------|-----|
| 到着 | arrival | ar | `01_ar_001` |
| メイン活動 | activity | ac | `02_ac_001` |
| 休憩 | relaxing | rx | `04_rx_001` |
| 特別な瞬間 | special_moment | sm | `05_sm_001` |
| 親密 | intimate | in | `06_in_001` |

**必要に応じて調整:**

もし場所固有のカテゴリがあれば、適切な略称に変更します。

例: プールシーンの場合
- `02_ac_001` → `02_ps_001` (poolside)
- `03_ab_001` → `03_sw_001` (swimming)

---

### ステップ5: 黄金律チェック

`scene_creation_golden_rules.md`のチェックリストで確認します。

#### ✅ 構造的バリデーション

- [ ] ソロ/カップル比率は50-65% / 35-50%か？
- [ ] カメラアングルは最低6種類あるか？
- [ ] 動作バリエーションは最低8種類あるか？
- [ ] 1シーンのプロンプト数は6-15個の範囲か？
- [ ] 連番フォーマット（SS_CC_NNN）を正しく使用しているか？

#### ✅ 品質確認

- [ ] 同じ動作・アングルの連続はないか？
- [ ] プロンプトは具体的で明確か？
- [ ] 場所情報は一貫しているか？

---

### ステップ6: クイック検証

**全プロンプトをテストする前に**、代表的な3つだけをテストします。

#### 6.1 選択する3つのプロンプト

1. **最初のプロンプト** - シーン導入が適切か
   - 例: `01_ar_001`
   
2. **中間のプロンプト** - バリエーションが機能するか
   - 例: `03_ab_006`
   
3. **最後のプロンプト** - シーン締めくくりが適切か
   - 例: `06_in_010`

#### 6.2 判断基準

| 結果 | 判断 | 次のアクション |
|------|------|--------------|
| ✅ 3つ全てOK | 成功 | 本番投入（確率90%で残りも問題なし） |
| ⚠️ 1つに問題 | 部分修正 | 該当プロンプトのみ修正 |
| ❌ 2つ以上に問題 | 構造見直し | シーン構造を再検討 |

#### 6.3 効果

```
従来: 全50プロンプトをテスト → 問題発見 → 再作成 → 再テスト
      ⏱️ 時間: 数時間〜1日

クイック検証: 3プロンプトのみテスト → 問題なし → 本番投入
              ⏱️ 時間: 10-15分

⚡ 時短効果: 80%削減
```

---

## 📊 完全な例: プールシーン

### Before (テンプレート)

```yaml
scene_[LOCATION]_arrival:
  - 01_ar_001,1girl,[LOCATION],entering,looking around,cowboy shot,arrival scene
```

### After (完成)

```yaml
scene_pool_arrival:
  - 01_ar_001,1girl,pool,entering,looking around,cowboy shot,arrival scene
  - 01_ar_002,1girl,pool,standing,first impression,wide shot,full body,taking in surroundings
  - 01_ar_003,1girl,pool entrance,walking in,carrying beach bag,pov,first person view,entering
  - 01_ar_004,1girl,pool,standing by entrance gate,looking around,from behind,over shoulder,exploring
  - 01_ar_005,1girl,1boy,pool,entering together,holding hands,wide shot,arrival
  - 01_ar_006,1girl,1boy,pool entrance,walking in together,from behind,full body,together
  - 01_ar_007,1girl,1boy,pool,standing close,discussing,cowboy shot,planning together
```

---

## 🎨 カスタマイズのヒント

### 場所のタイプ別アプローチ

#### アクティブな場所（プール、ジム、遊園地）
- 動的アングル（dutch angle）を多めに
- 動的ポーズ（jumping, running）を増やす
- エネルギッシュな雰囲気

#### 静かな場所（図書館、美術館、寺社）
- 静的アングル（close-up, pov）を多めに
- 静的ポーズ（sitting, standing, looking）を増やす
- 落ち着いた雰囲気

#### 移動系（電車、バス、飛行機）
- 限られた空間に合わせた動作
- 窓の外を見る、座る、立つなど
- 狭い空間での親密さ

---

## 🔄 既存シーンの活用

### 類似シーンからの流用

新しい場所が既存シーンに似ている場合、そちらをベースにすることも可能です。

| 新しい場所 | 類似する既存シーン | 理由 |
|-----------|-----------------|------|
| プール | `pose_scenes_beach.yaml` | 水辺、リゾート系 |
| 学校 | `pose_scenes_office.yaml` | 施設内、デスクワーク |
| 公園 | `pose_scenes_onsen.yaml` (散策部分) | 屋外散策 |
| カフェ | `pose_scenes_beach.yaml` (カフェ部分) | 飲食、リラックス |
| ジム | `pose_scenes_beach.yaml` (活動部分) | アクティブ、運動 |

**方法:**
1. 既存シーンファイルをコピー
2. 場所名を一括置換
3. 場所固有の動作を追加
4. 連番を更新

---

## ✅ チェックリスト（まとめ）

作成完了前に、以下を確認してください：

### 基本
- [ ] 全ての `[PLACEHOLDER]` を置換した
- [ ] 場所名が一貫している
- [ ] 連番フォーマット（SS_CC_NNN）が正しい

### 構造
- [ ] ソロ/カップル比率が適切
- [ ] アングルバリエーションが十分（最低6種類）
- [ ] 動作バリエーションが十分（最低8種類）
- [ ] プロンプト数が適切（6-15個/シーン）

### 品質
- [ ] 同じ動作・アングルが連続していない
- [ ] プロンプトが具体的で明確
- [ ] 時系列に矛盾がない

### 検証
- [ ] 代表プロンプト3つでクイック検証を実施
- [ ] 問題がある場合は修正済み
- [ ] 本番投入の準備完了

---

## 🚀 次のステップ

1. **サンプルシーンを確認**
   - `themes/lovey/pose_scenes_*.yaml` に10種類のサンプル
   
2. **テーマに統合**
   - `main.yaml` で新しいシーンファイルを参照
   
3. **実際に使用**
   - プロンプト生成してテスト
   
4. **フィードバック**
   - 問題があれば微調整

---

## 📚 関連ドキュメント

- `scene_creation_golden_rules.md` - 黄金律の詳細
- `scene_structure_patterns.yaml` - 構造パターンの定義
- `scene_category_codes.md` - カテゴリ略称の一覧
- `custom_scene_template.yaml` - ベーステンプレート

---

**作成日**: 2026-01-01  
**バージョン**: 1.0  
**対象**: カスタムシーン作成者向け

