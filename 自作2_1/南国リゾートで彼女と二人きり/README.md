# 南国リゾートで彼女と二人きり

## テーマ概要

- **テーマ名**: 南国リゾートで彼女と二人きり
- **ベース**: lovey (ラブラブ)
- **タイプ**: beach (ビーチ・リゾート系)
- **時系列**: あり（昼 → 夜）
- **男性タイプ**: デフォルト (male_type_default)
- **Sex場所**: hotel_room (リゾートホテル客室)
- **NSFW統合**: あり（選択したシーンにLight/Moderate/Heavy NSFWを混ぜる）

---

## シーンフロー

### Poseシーン（6シーン - SFW + NSFW統合）

**SFWのみのシーン（3シーン）：**

1. **昼 - ビーチ到着・散策** (`beach_arrival`)
   - 服装: カジュアル外出着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: リゾートビーチに到着、海を眺める、砂浜を散歩
   - **NSFW**: なし（完全SFW）

2. **昼 - ビーチでの活動** (`beach_activity`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: カジュアル
   - 内容: 海で泳ぐ、砂浜で遊ぶ、ビーチボール、日光浴
   - **NSFW**: なし（完全SFW）

3. **午後 - ビーチカフェ・ビーチハウス** (`beach_cafe`)
   - 服装: 水着
   - 表情: カジュアル
   - 雰囲気: 居心地の良い
   - 内容: カフェでドリンク、休憩、海を眺めながら食事
   - **NSFW**: なし（完全SFW）

**NSFW統合シーン（3シーン）：**

4. **午後 - 海水浴場シャワー（屋外・水着着用）** (`beach_outdoor_shower`) + **NSFW Light**
   - 服装: 水着
   - 表情: カジュアル / 親密
   - 雰囲気: カジュアル / ロマンチック
   - 内容: 屋外シャワーで海水を洗い流す、濡れた体
   - **NSFW**: **Light**（キス、抱擁、愛撫、胸タッチ）

5. **夕方 - 夕暮れビーチ** (`beach_sunset`) + **NSFW Moderate**
   - 服装: 水着
   - 表情: 親密 / 興奮
   - 雰囲気: ロマンチック / セクシー
   - 内容: サンセットビーチ、ロマンチックな雰囲気、夕日を眺める
   - **NSFW**: **Moderate**（手コキ、パイズリ、指マン、クンニ、フェラ軽め）

6. **夜 - ホテル・リゾート客室** (`resort_room`) + **NSFW Heavy**
   - 服装: 室内着 / 下着 / 裸
   - 表情: 親密 / 興奮 / アヘ顔
   - 雰囲気: 居心地の良い / セクシー / 蒸し暑い
   - 内容: 客室でくつろぐ、バルコニー、ベッド
   - **NSFW**: **Heavy**（本格的な前戯全般 - キス/ハグ、愛撫、手コキ、指マン、クンニ）

### Sexシーン（6段階 - NSFW）

- **場所**: hotel_room (リゾートホテル客室)
- **男性タイプ**: デフォルト
- **段階**: intro_gentle → moderate → intense → extreme → creampie → after

### Fellatioシーン（8段階 - NSFW）

- **場所**: hotel_room (リゾートホテル客室)
- **男性タイプ**: デフォルト
- **段階**: intro_tease → start_licking → moderate_gentle → intense_passionate → climax_deep → finish_ejaculation → after_swallow → extra_intimate

---

## 使用方法

### 🎨 Poseシーン（SFWのみ）

```
__自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
```

### 🔞 Poseシーン（NSFWのみ - Light/Moderate/Heavy）

```
__自作2_1/南国リゾートで彼女と二人きり/pose_play_nsfw__
```

### 💕 Sexシーンのみ（NSFW）

```
__自作2_1/南国リゾートで彼女と二人きり/sex_play__
```

### 💋 Fellatioシーンのみ（NSFW）

```
__自作2_1/南国リゾートで彼女と二人きり/fellatio_play__
```

### 🌊 全シーン統合（推奨）

```
__自作2_1/南国リゾートで彼女と二人きり/main__
```

**デフォルトバランス: SFW 50% / NSFW 50%**
- pose_play_sfw: 3行（50%）
- pose_play_nsfw: 1行（17%）
- sex_play: 1行（17%）
- fellatio_play: 1行（17%）

### ⚖️ バランス調整

`main.yaml` で SFW/NSFW の比率を調整できます：

**SFW重視（SFW 60% / NSFW 40%）:**
```yaml
main:
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__  # 4行
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_nsfw__  # 1行
  - __自作2_1/南国リゾートで彼女と二人きり/sex_play__         # 1行
  - __自作2_1/南国リゾートで彼女と二人きり/fellatio_play__    # 1行
```

**NSFW重視（SFW 30% / NSFW 70%）:**
```yaml
main:
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__  # 2行
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_nsfw__  # 2行
  - __自作2_1/南国リゾートで彼女と二人きり/pose_play_nsfw__
  - __自作2_1/南国リゾートで彼女と二人きり/sex_play__         # 2行
  - __自作2_1/南国リゾートで彼女と二人きり/sex_play__
  - __自作2_1/南国リゾートで彼女と二人きり/fellatio_play__    # 2行
  - __自作2_1/南国リゾートで彼女と二人きり/fellatio_play__
```

---

## ファイル構成

```
南国リゾートで彼女と二人きり/
├── theme.txt          # テーマ名
├── config.yaml        # 設定（参考用、ワイルドカードとして使用しない）
├── pose_play_sfw.yaml # Poseシーン定義 - SFW（6シーン全て）
├── pose_play_nsfw.yaml# Poseシーン定義 - NSFW（Scene 04, 05, 06のみ）
├── sex_play.yaml      # Sexシーン定義（6段階 - NSFW）
├── fellatio_play.yaml # Fellatioシーン定義（8段階 - NSFW）
├── main.yaml          # 統合エントリーポイント（バランス調整用）
└── README.md          # このファイル
```

---

## 特徴

### NSFW統合の段階的設計

このテーマでは、3つのシーンにそれぞれ異なるレベルのNSFWを統合しています：

1. **Scene 04（シャワー）**: Light - キス、抱擁、愛撫などの軽度な親密行為
2. **Scene 05（サンセット）**: Moderate - 手コキ、フェラ軽め、指マンなどの中度な前戯
3. **Scene 06（客室）**: Heavy - 本格的な前戯（キス/ハグ → 愛撫 → 手コキ → 指マン → クンニ）

これにより、時間の流れに沿って徐々に親密度が増していく自然な展開を実現しています。

### 連番システム

NSFW統合時は、SFWシーンの最終連番に続く形でNSFWプロンプトに連番が付与されています：

- Scene 04: SFW最終 `04_os_009` → NSFW開始 `04_os_010`
- Scene 05: SFW最終 `05_ss_008` → NSFW開始 `05_ss_009`
- Scene 06: SFW最終 `06_rr_007` → NSFW開始 `06_rr_008`

これにより、出力画像のファイル名が連番順に整理されます。

---

## カスタマイズ

### 服装を変更したい場合

`pose_play_sfw.yaml` および `pose_play_nsfw.yaml` の各シーンで `outfit_xxx` を変更してください。

利用可能な服装パラメータ：
- `outfit_swimsuit` - 水着
- `outfit_casual_day` - カジュアル外出着
- `outfit_house_clothes` - 室内着
- `outfit_underwear` - 下着
- `outfit_nude` - 裸
- その他、`params/character_outfits.yaml` 参照

### 時間帯を変更したい場合

`pose_play_sfw.yaml` および `pose_play_nsfw.yaml` の各シーンで `time_xxx` を変更してください。

利用可能な時間帯：
- `time_morning` - 朝
- `time_day` - 昼
- `time_afternoon` - 午後
- `time_evening` - 夕方
- `time_night` - 夜
- その他、`params/pose_times.yaml` 参照

### 表情・雰囲気を変更したい場合

loveyテーマで利用可能：
- 表情: `lovey_face_casual`, `lovey_face_intimate`, `lovey_face_lewd`, `lovey_face_ahegao`
- 雰囲気: `lovey_atmosphere_casual`, `lovey_atmosphere_cozy`, `lovey_atmosphere_romantic`, `lovey_atmosphere_sexy`, `lovey_atmosphere_steamy`

### Sex場所を変更したい場合

`sex_play.yaml` と `fellatio_play.yaml` で `place_hotel_room` を他の場所に変更できます。

利用可能な場所：
- `place_hotel_room` - ホテル客室（現在の設定）
- `place_beach` - ビーチ
- `place_beach_house` - ビーチハウス
- `place_home_bedroom` - 自宅寝室
- その他、`params/pose_places.yaml` 参照

### NSFW統合レベルを調整したい場合

**特定シーンのNSFWを削除したい場合:**
`pose_play_nsfw.yaml` から該当シーンのセクションを削除してください。

**NSFWレベルを変更したい場合:**
各シーンで使用しているNSFWライブラリを変更してください：
- Light → `nsfw_light_all`
- Moderate → `nsfw_moderate_all`
- Heavy → `foreplay_kiss_hug`, `foreplay_touch_caress`, `foreplay_handjob`, `foreplay_fingering`, `foreplay_cunnilingus`

---

## 注意事項

- `config.yaml` はワイルドカードとして使用されません（参考用）
- 循環参照を避けるため、`main.yaml` 内で `main` 自身を参照しないでください
- NSFW統合により、`pose_play_nsfw`には段階的に激しくなる前戯要素が含まれます
- 連番システムにより、出力画像はシーン順・時系列順に整理されます

---

## 制作情報

- 作成日: 2025年1月
- ベースライブラリ: 
  - `themes/lovey/pose_scenes_beach.yaml`
  - `themes/lovey/nsfw_light.yaml`
  - `themes/lovey/nsfw_moderate.yaml`
  - `themes/lovey/foreplay_prompts.yaml`
- テーマベース: lovey（ラブラブ）
- シチュエーション: 南国リゾートで彼女と二人きりのバカンス、昼から夜まで

---

## 使用例

### ケース1: SFWのみ生成したい

```
__自作2_1/南国リゾートで彼女と二人きり/pose_play_sfw__
```

ビーチ到着、海水浴、カフェ、シャワー、サンセット、客室の全6シーンが完全SFWで生成されます。

### ケース2: NSFWのみ生成したい（前戯〜本番）

```
__自作2_1/南国リゾートで彼女と二人きり/pose_play_nsfw__
```

シャワー（Light）、サンセット（Moderate）、客室（Heavy）の3シーンのNSFW部分が生成されます。

### ケース3: 全体のストーリーとして生成したい（推奨）

```
__自作2_1/南国リゾートで彼女と二人きり/main__
```

SFW + NSFW前戯 + Sex + Fellatioが適度なバランスで生成されます。`main.yaml`の行数を調整することで、SFW/NSFW比率を変更できます。

---

お楽しみください！🌴🌊

