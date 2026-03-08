# プロンプト作成用ライブラリ

本ライブラリは、`bef_sex_param.yaml`、`fellatio_param.yaml`、`sex_param.yaml` 内のプロンプトを分析し、「カメラアングル・構図」「ポーズ・動作・体位」「表情・視線」の観点で分割・抽出したものです。
Antigravityがプロンプトを作成する際の構成要素データとして活用できます。ユーザーからの指示（例：「正常位で激しく」など）から適切なベースプロンプトを検索できるように、日本語の説明（シチュエーション）を併記しています。

## 1. 共通タグライブラリ (構成要素の一覧)

### カテゴリ別頻出タグ
プロンプトを新規作成または改変する際に自由に組み合わせ可能なタグ一覧です。

**カメラアングル・構図 (Camera Angle & Composition)**
- `from above` (俯瞰), `from below` (煽り), `from side` (横から), `from center` (正面から), `from behind` (後ろから)
- `pov` (主観視点), `pov crotch` (股間視点), `overhead shot` (真上から)
- `closeup face` (顔アップ), `closeup pussy` (局部アップ), `closeup mouth` (口アップ), `closeup breasts` (胸アップ), `ass focus` (尻フォーカス)
- `upper body` (上半身), `motion lines` (集中線/動き), `steam` (蒸気)

**ポーズ・動作・体位 (Pose, Action & Position)**
- **基本姿勢**: `sitting` (座り), `standing` (立ち), `lying`, `on back` (仰向け), `on side` (横向き), `spread legs` (開脚), `squatting` (しゃがみ)
- **手・身体の接触**: `hug`, `hug from behind` (後ろからハグ), `holding hands`, `grabbing breasts`, `hand on erection`, `face to face` (対面), `spooning` (スプーン位)
- **前戯・フェラ**: `french kiss`, `hand job` (手コキ), `fingering` (手マン), `licking penis`, `vacuum fellatio`, `irrumatio`, `deepthroat`, `saliva trail` (唾液の糸)
- **体位**: `sex`, `missionary` (正常位), `girl on top` / `cowgirl position` (騎乗位), `reverse cowgirl position`, `sex from behind` / `doggystyle` (バック), `mating press` (種付けプレス), `suspended congress` (駅弁)
- **状態・派生**: `trembling` (震え), `sweat` (汗), `cum in pussy` (中出し), `cum on face`, `bukkake`, `pussy juice` (愛液)

**表情・視線 (Expression & Gaze)**
- **視線**: `looking at viewer` (カメラ目線), `looking at another` (相手を見る), `looking at penis`, `looking back` (振り返る), `looking up` (見上げる), `closed eyes` (目を閉じる), `half open eyes` (半目)
- **表情・口元**: `smile` (笑顔), `torogao` (とろけ顔), `blush` (赤面), `nose blush`, `open mouth`, `wide open mouth`, `tongue out` (舌出し), `biting lips` (唇を噛む), `clenched teeth` (歯を食いしばる), `screaming` (絶叫), `tearing up` (涙ぐむ)

---

## 2. プロンプトベース（テンプレート）一覧

ユーザーからの日本語指示（例：「正常位」や「バックで尻アップ」）に該当するベースプロンプトを探すための辞書です。

### 前戯 (bef_sex_param.yaml)

1. **35_bs001_0 (顔撫で・照れ)**
   - カメラアングル・構図: (closeup face:2.8), from center, pov
   - ポーズ・動作・体位: bare hand on another's face | bare hand on another's head | bare hand on another's ear
   - 表情・視線: looking at viewer, smile, light smile, blush, nose blush

2. **35_bs001_1 (ハグ・密着)**
   - カメラアングル・構図: from side, upper body
   - ポーズ・動作・体位: (hug:1.5), couple, face to face
   - 表情・視線: blush

3. **35_bs001_4 (ディープキス・舌出し)**
   - カメラアングル・構図: (closeup face:2)
   - ポーズ・動作・体位: oral
   - 表情・視線: looking at viewer, smile, wide open mouth, tongue out

4. **35_bs001_7_1 (キス待ち・目を閉じる)**
   - カメラアングル・構図: (closeup face:2)
   - ポーズ・動作・体位: incoming kiss
   - 表情・視線: facing viewer, open mouth, closed eyes, puckered lips

5. **35_bs002 (仰向け手マン)**
   - カメラアングル・構図: pov, from above | (from below, closeup)
   - ポーズ・動作・体位: fingering, spread legs, lying on back, couple
   - 表情・視線: light smile, blush | open mouth, torogao, tongue out, closed eyes

6. **35_bs002_1 (後ろから胸揉み・首キス)**
   - カメラアングル・構図: (from below:1.2)
   - ポーズ・動作・体位: grabbing another's breast from behind, breast press, groping, spread legs, sitting, kiss to neck, face to face, couple
   - 表情・視線: blush, looking at another, light smile

7. **35_bs004_1 (添い寝・見つめ合い)**
   - カメラアングル・構図: (overhead shot, from above:1.5)
   - ポーズ・動作・体位: lying on back, face to face, couple, hand on erection
   - 表情・視線: smile

8. **35_bs005_1 (後ろ手マン・仰向け)**
   - カメラアングル・構図: (closeup pussy:1.8), from front
   - ポーズ・動作・体位: hug from behind, spread legs, lying on back, sweat
   - 表情・視線: blush, closed mouth, torogao


### フェラチオ (fellatio_param.yaml)

1. **20_fe1 (添い寝フェラ前・着衣)**
   - カメラアングル・構図: pov, (closeup face:1.5)
   - ポーズ・動作・体位: precum, erection, girl lying on boy, on side, couple
   - 表情・視線: half open eyes, nose blush

2. **20_fe3_0 (ちん嗅ぎ・匂い嗅ぎ)**
   - カメラアングル・構図: pov, (closeup face:2)
   - ポーズ・動作・体位: oral, fellatio, smelling testicles, girl is sitting, boy is standing, sweat, heavy breathing
   - 表情・視線: looking up, blush, half open eyes / smile

3. **20_fe3_2_1_1 (亀頭舐め・舌使い)**
   - カメラアングル・構図: pov, from above, closeup mouth
   - ポーズ・動作・体位: bending tongue, penis licking, glans licking, holding penis
   - 表情・視線: torogao, tongue out, wide open mouth, oral invitation

4. **20_fe3_6_3_1 (ひょっとこフェラ・フィニッシュ)**
   - カメラアングル・構図: (closeup face:1.5), sitting, from above
   - ポーズ・動作・体位: vacuum fellatio, holding hands / hands on thighs, cum
   - 表情・視線: looking up, looking at viewer, half open eyes, nose blush

5. **20_fe3_8_4_1 (口周り射精後・ぶっかけ後)**
   - カメラアングル・構図: (closeup mouth:2), from above
   - ポーズ・動作・体位: cum on mouth, cum on face
   - 表情・視線: looking at viewer, closed mouth

6. **20_fe3_8_5_1 (アナル舐め)**
   - カメラアングル・構図: pov, (closeup face:1.5)
   - ポーズ・動作・体位: anilingus, tongue in anus, licking, girl on boy, lying on back, spread legs, hand job
   - 表情・視線: looking at viewer, open mouth, tongue out


### 本番・挿入 (sex_param.yaml)

1. **40_se100 (正常位 挿入前・クパァ)**
   - カメラアングル・構図: from below, close up
   - ポーズ・動作・体位: lying on back, spread legs, sweat, pussy juice
   - 表情・視線: light smile, blush | closed eyes

2. **40_se102_1 (ゆっくり挿入・苦悶)**
   - カメラアングル・構図: (指定なし/全体)
   - ポーズ・動作・体位: inserting tip, slow penetration, lying on back, spread legs, sweat, heavy breathing
   - 表情・視線: grimace, biting lower lip, tearing up, painful expression

3. **40_se104 (正常位 激しく)**
   - カメラアングル・構図: (motion lines:2)
   - ポーズ・動作・体位: sex, lying on back, bouncing breasts, trembling
   - 表情・視線: open mouth wild, torogao, tongue out, saliva

4. **40_se108 (正常位 中出しPOV・絶頂)**
   - カメラアングル・構図: pov, from above, (motion lines:2)
   - ポーズ・動作・体位: sex, lying on back, spread legs, holding waist, bouncing breasts, cum
   - 表情・視線: head back, screaming | clenched teeth, biting lips

5. **40_se112 (種付けプレス)**
   - カメラアングル・構図: (closeup pussy:1.5), (motion lines:2)
   - ポーズ・動作・体位: mating press, missionary, boy on top, lying on back, sweat, sheet grab
   - 表情・視線: open mouth wild, torogao

6. **40_se201 (側背位 挿入・横向き)**
   - カメラアングル・構図: (motion lines:2)
   - ポーズ・動作・体位: sex, lying on side, spread legs, couple
   - 表情・視線: closed eyes, biting lips, saliva, clenched teeth

7. **40_se300 (バック・尻アップ・後背位)**
   - カメラアングル・構図: from behind, from below, (ass focus:1.8), solo focus
   - ポーズ・動作・体位: spread own anus / spread own ass, hands on own ass, sweat, puckered anus
   - 表情・視線: (指定位置上は体の背面のため無し)

8. **40_se303_1 (バック・背中反らし)**
   - カメラアングル・構図: (指定なし)
   - ポーズ・動作・体位: arched back, clutching sheets, toes curling, doggystyle, sweat
   - 表情・視線: hidden face

9. **40_se400 (騎乗位 M字開脚)**
   - カメラアングル・構図: pov, (from below:1.5), solo focus
   - ポーズ・動作・体位: girl on top, squatting, vaginal, spread legs, sweat
   - 表情・視線: looking at viewer, blush

10. **40_se503 (駅弁フルネルソン・立ちバック)**
    - カメラアングル・構図: from below, solo focus, (motion lines:2)
    - ポーズ・動作・体位: sex from behind, full nelson, vaginal, spread legs, sweat, cum in pussy
    - 表情・視線: looking at viewer, head back, tongue out

11. **40_se900 (事後・呆然・放心)**
    - カメラアングル・構図: from above
    - ポーズ・動作・体位: after sex, lying on back, spread legs, trembling, cum pool
    - 表情・視線: head back, screaming | tongue out

12. **40_se923 (事後顔射・精子掃除)**
    - カメラアングル・構図: cleaning fellatio pov
    - ポーズ・動作・体位: licking penis clean, bukkake, semen on face, tongue connection
    - 表情・視線: (視線主観)
