# ヘルスチェック確認観点

このドキュメントは、テンプレート、theme、ruleのヘルスチェックを行う際の確認観点を定義します。

**対象**: 新規テーマ作成後のチェックではなく、**その元となるもの**（共通ライブラリ、params、templates、ルールファイル）へのチェック

---

## 📋 確認観点（4項目）

### 観点1: scene mappingとthemeのシーンの流れが一致しているか

**目的**: シーンマッピング（scene_outfit_mapping.md）と実際のthemeファイル（themes/lovey/pose_scenes_*.yaml）のシーン構成が一致しているか確認

#### チェック項目

1. **シーンライブラリの網羅性**
   - `wildcard_rules.md`で説明されているシーンライブラリ（例: 日常系、温泉系、ビーチ系など）が実際に存在するか
   - 各テーマタイプに対応する`pose_scenes_*.yaml`ファイルが存在するか

2. **シーン数の一致**
   - `wildcard_rules.md`に記載されたシーン数（例: 日常系は7シーン）と実際のyamlファイル内のシーン定義数が一致するか
   - 各シーンライブラリのシーン構成がドキュメントと一致しているか

3. **シーン名の整合性**
   - ドキュメントで説明されているシーン名（例: "ショッピング、公園、街歩き..."）と実際のキー名（`scene_shopping`, `scene_park`など）が対応しているか
   - シーンキー名が一貫しているか

4. **シーンフローの時系列整合性**
   - 各シーンライブラリ内で、シーンの順序が時系列的に自然か
   - シーン間の流れに矛盾がないか

5. **scene_outfit_mapping.mdとの整合性**
   - `templates/scene_outfit_mapping.md`で定義されているシーンタイプと、実際のシーンライブラリのシーンが対応しているか
   - カテゴリ略称（CC部分）がマッピング表と一致しているか

#### 確認対象ファイル

- `templates/scene_outfit_mapping.md` - シーン→服装マッピング
- `themes/lovey/pose_scenes_*.yaml` - 各シーンライブラリ
- `themes/ntr/pose_scenes_*.yaml` - NTRテーマのシーンライブラリ（存在する場合）
- `doc/wildcard_rules.md` - シーンライブラリの説明（行167-246）

---

### 観点2: themeがparamsにないパラメータを参照していないか

**目的**: themeファイル（themes/lovey/*.yaml, themes/ntr/*.yaml）で参照されているパラメータが、実際にparamsディレクトリに定義されているか確認

#### チェック項目

1. **服装パラメータの存在確認**
   - themeファイルで参照している服装名（例: `outfit_yukata`, `sweater_jeans`, `blouse_skirt`）が`params/character_outfits.yaml`に定義されているか
   - 参照形式が正しいか（`__自作2_1/params/outfit_xxx__` または `__自作2_1/params/character_outfits/outfit_xxx__`）

2. **場所パラメータの存在確認**
   - `sex_play.yaml`や`fellatio_play.yaml`の例で参照される場所（例: `place_home_bedroom`, `place_ryokan_room`）が`params/pose_places.yaml`に定義されているか
   - 参照形式が正しいか（`__自作2_1/params/place_xxx__`）

3. **時間帯パラメータの存在確認**
   - 参照される時間帯（例: `time_morning`, `time_day`, `time_evening`）が`params/pose_times.yaml`に定義されているか
   - 参照形式が正しいか（`__自作2_1/params/time_xxx__`）

4. **男性タイプの存在確認**
   - 参照される男性タイプ（例: `male_type_default`, `male_type_dark_skin`, `male_type_shota`）が`params/character_male_type.yaml`に定義されているか
   - 参照形式が正しいか（`__自作2_1/params/male_type_xxx__`）

5. **アングルパラメータの存在確認**
   - NSFW統合時に使用されるアングル（例: `angle_closeup_face`, `angle_from_side`, `angle_upper_body`）が`params/angles.yaml`に定義されているか
   - 参照形式が正しいか（`__自作2_1/params/angle_xxx__`）

6. **表情・雰囲気パラメータの存在確認**
   - 参照される表情（例: `lovey_face_casual`, `ntr_face_reluctant`）が`themes/lovey/pose_faces.yaml`または`themes/ntr/pose_faces.yaml`に定義されているか
   - 参照される雰囲気（例: `lovey_atmosphere_casual`, `ntr_atmosphere_tense`）が`themes/lovey/pose_atmosphere.yaml`または`themes/ntr/pose_atmosphere.yaml`に定義されているか

#### 確認対象ファイル

- `themes/lovey/*.yaml` - loveyテーマの全ファイル
- `themes/ntr/*.yaml` - ntrテーマの全ファイル
- `params/character_outfits.yaml` - 服装パラメータ
- `params/pose_places.yaml` - 場所パラメータ
- `params/pose_times.yaml` - 時間帯パラメータ
- `params/character_male_type.yaml` - 男性タイプパラメータ
- `params/angles.yaml` - アングルパラメータ

---

### 観点3: wildcard_rules.md、common_library_creation_rules.mdの例が実際のthemeやparamsやtemplateと矛盾していないか

**目的**: ルールファイル内で例示されている内容が、実際のファイル構造や定義と一致しているか確認

#### チェック項目

1. **例示されているキー名の存在**
   - `wildcard_rules.md`内で例として挙げられているキー名（例: `lovey_face_casual`, `scene_ryokan_arrival`, `nsfw_light_all`）が実際のyamlファイルに定義されているか
   - `common_library_creation_rules.md`内で例として挙げられているキー名が実際に存在するか

2. **パスの正確性**
   - 例示されている参照パス（例: `__自作2_1/themes/lovey/scene_ryokan_arrival__`）が実際のファイル構造と一致しているか
   - ディレクトリ構造が正しく記載されているか

3. **連番の実例との整合性**
   - NSFW統合時の連番例（例: `02_rm_008`がSFW最終+1）が実際のシーンライブラリの連番と整合しているか
   - 連番フォーマット（SS_CC_NNN）の例が実際のファイルと一致しているか

4. **服装命名規則の一致**
   - ドキュメントで推奨される服装名（例: `sweater_jeans`, `yukata`, `blouse_skirt`）が実際の`params/character_outfits.yaml`のキー名と一致しているか
   - 旧命名規則（`outfit_xxx`）を使用していないか

5. **場所リストの一致**
   - `wildcard_rules.md`の質問5パート2で列挙されている場所リスト（1-25番）が実際の`params/pose_places.yaml`の内容と一致しているか
   - 場所名の表記が統一されているか

6. **テンプレートファイルの存在**
   - `common_library_creation_rules.md`で参照されているテンプレートファイル（`custom_scene_template.yaml`など）が実際に存在するか
   - テンプレートファイルの構造が説明と一致しているか

7. **質問番号の一貫性**
   - `wildcard_rules.md`内の質問番号が正しく連続しているか
   - ステップ番号が正しく区別されているか（例: NSFW統合なしの場合はステップ7、統合ありの場合はステップ9）

8. **ファイル構成の一致**
   - ドキュメントで説明されているファイル構成（3層構造など）が実際のディレクトリ構造と一致しているか
   - 必須ファイルが実際に存在するか

#### 確認対象ファイル

- `doc/wildcard_rules.md` - 新規テーマ作成ルール
- `doc/common_library_creation_rules.md` - 共通ライブラリ作成ルール
- `themes/lovey/*.yaml` - 実際のthemeファイル
- `themes/ntr/*.yaml` - 実際のntrテーマファイル
- `params/*.yaml` - 実際のparamsファイル
- `templates/*.yaml`, `templates/*.md` - 実際のテンプレートファイル

---

### 観点4: 各フローでまったく使用されていない不要ファイルがないか

**目的**: どのフローでも参照されていない不要なファイルが存在しないか確認

#### チェック項目

1. **新規テーマ作成フローでの参照確認**
   - `wildcard_rules.md`で参照されているファイルが実際に存在するか
   - 参照されていないファイルが`templates/`や`params/`に存在しないか

2. **共通ライブラリ作成フローでの参照確認**
   - `common_library_creation_rules.md`で参照されているファイルが実際に存在するか
   - 参照されていないファイルが`templates/`に存在しないか

3. **実際のthemeファイルでの参照確認**
   - 各themeファイル（`themes/lovey/*.yaml`, `themes/ntr/*.yaml`）で参照されているファイルが実際に存在するか
   - 参照されていないファイルが`themes/`に存在しないか

4. **paramsファイルでの参照確認**
   - 各paramsファイルで参照されているファイルが実際に存在するか
   - 参照されていないファイルが`params/`に存在しないか

5. **テンプレートファイルの使用確認**
   - `templates/`ディレクトリ内のファイルが、どちらかのフローで参照されているか
   - 完全に未使用のテンプレートファイルがないか

6. **ドキュメントファイルの参照確認**
   - `doc/`ディレクトリ内のファイルが、どちらかのフローで参照されているか
   - 完全に未使用のドキュメントファイルがないか

#### 確認対象ディレクトリ

- `doc/` - ルールファイル
- `templates/` - テンプレートファイル
- `params/` - パラメータファイル
- `themes/lovey/` - loveyテーマファイル
- `themes/ntr/` - ntrテーマファイル

#### 確認方法

1. **参照元の収集**
   - `wildcard_rules.md`内で参照されているファイルパスを抽出
   - `common_library_creation_rules.md`内で参照されているファイルパスを抽出
   - 各themeファイル内で参照されているファイルパスを抽出

2. **存在確認**
   - 参照されているファイルが実際に存在するか確認
   - 存在しないファイルへの参照がないか確認

3. **未使用ファイルの検出**
   - 実際に存在するファイルのうち、どのファイルも参照していないものを検出
   - ただし、以下のファイルは除外：
     - `README.md`（説明用）
     - `config.yaml`（参考用、ワイルドカードとして使用されない）

---

## 🔍 チェック実行方法

### 手動チェック

各観点について、以下の手順で確認：

1. **観点1**: `scene_outfit_mapping.md`と`pose_scenes_*.yaml`を比較
2. **観点2**: themeファイル内の参照を抽出し、paramsファイルの存在を確認
3. **観点3**: ルールファイル内の例を抽出し、実際のファイルと比較
4. **観点4**: 全ファイルの参照関係をマッピングし、未使用ファイルを検出

### 自動チェック（推奨）

将来的にスクリプトやツールで自動化可能：

1. **観点1**: YAMLパーサーでシーン構成を抽出し、マッピング表と比較
2. **観点2**: 正規表現で参照パスを抽出し、ファイル存在を確認
3. **観点3**: ルールファイルから例を抽出し、実際のファイルと照合
4. **観点4**: 依存関係グラフを構築し、未使用ノードを検出

---

## 📝 チェック結果の記録

各観点について、以下の形式で結果を記録：

```markdown
## 観点1: scene mappingとthemeのシーンの流れが一致しているか

### 確認日時
2026-01-XX

### 結果
✅ 問題なし / ⚠️ 軽微な問題あり / ❌ 重大な問題あり

### 詳細
- [確認項目1]: ✅/⚠️/❌
- [確認項目2]: ✅/⚠️/❌
- ...

### 発見された問題
1. [問題の説明]
2. [問題の説明]
...

### 修正が必要なファイル
- `path/to/file.yaml` - [修正内容]
- `path/to/file.md` - [修正内容]
...
```

---

## 🔄 定期チェック

以下のタイミングでヘルスチェックを実施：

1. **新規シーンライブラリ追加時** - 観点1, 2, 4を確認
2. **新規params追加時** - 観点2, 3を確認
3. **ルールファイル更新時** - 観点3を確認
4. **テンプレートファイル更新時** - 観点3, 4を確認
5. **定期的な全体チェック** - 全観点を確認（月1回推奨）

---

**作成日**: 2026-01-01  
**バージョン**: 1.0  
**対象**: システム全体のヘルスチェック

