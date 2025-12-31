# ビーチで彼女とリゾートデート3（NSFW統合版サンプル）

## 概要
このテーマは**SFWシーンとNSFWシーンを自然に統合する実装例**です。

従来のテーマでは、SFW（pose_play）とNSFW（sex_play）が完全に分離されていましたが、本テーマではSFWシーンの合間に段階的にNSFWシーンを混ぜ込むことで、よりシームレスで自然な流れを実現しています。

## シーン構成

### Scene 01: ビーチ到着・散策（SFW）
- 純粋なSFWシーン
- ビーチに到着し、散策を楽しむ

### Scene 02: ビーチでの活動 + 軽いイチャつき（SFW→NSFW Light）
- SFWのビーチ活動シーン
- **→ NSFW Light: 抱擁・密着**を追加

### Scene 03: ビーチカフェ + キス（SFW→NSFW Light）
- SFWのカフェシーン
- **→ NSFW Light: キス**を追加

### Scene 04: 夕暮れビーチ + 愛撫（SFW→NSFW Light）
- SFWの夕暮れシーン
- **→ NSFW Light: 愛撫・胸タッチ**を追加

### Scene 05: シャワー + 手コキ・フェラ（SFW→NSFW Moderate）
- SFWのシャワーシーン
- **→ NSFW Moderate: 手コキ**
- **→ NSFW Moderate: フェラ（軽め）**

### Scene 06: リゾート客室 + 本格NSFW
- SFWの客室シーン
- **→ NSFW Light: キス、愛撫**
- **→ 本格NSFW: sex_play（セックス全編）**

## 使用している共通ライブラリ

### NSFW Light（軽度）
- `themes/lovey/nsfw_kiss.yaml` - キス
- `themes/lovey/nsfw_embrace.yaml` - 抱擁・密着
- `themes/lovey/nsfw_touch.yaml` - 愛撫・タッチ
- `themes/lovey/nsfw_breast_touch.yaml` - 胸タッチ

### NSFW Moderate（中度）
- `themes/lovey/nsfw_handjob_light.yaml` - 手コキ（軽め）
- `themes/lovey/nsfw_handjob_intense.yaml` - 手コキ（激しめ）
- `themes/lovey/nsfw_fellatio_light.yaml` - フェラ（軽め）
- `themes/lovey/nsfw_fellatio_intense.yaml` - フェラ（本格的）

### NSFW Heavy（本格的）
- `themes/lovey/foreplay_prompts.yaml` - 前戯全般
- `themes/lovey/paizuri_prompts.yaml` - パイズリ
- `themes/lovey/fellatio_prompts.yaml` - フェラチオ
- `themes/lovey/sex_prompts.yaml` - セックス

## 実行方法

### 全体実行
```
__自作2_1/ビーチで彼女とリゾートデート3/main__
```

### 個別実行
```
__自作2_1/ビーチで彼女とリゾートデート3/pose_play__  （SFW + NSFW統合）
__自作2_1/ビーチで彼女とリゾートデート3/sex_play__   （本格NSFW）
__自作2_1/ビーチで彼女とリゾートデート3/fellatio_play__  （フェラ重点）
```

## 設計のポイント

### 1. 段階的なNSFW導入
SFWシーンから徐々にNSFW度合いを上げることで、自然な流れを実現

### 2. アングルの統一
NSFWプロンプトからアングル情報を外部化し、SFWシーンと同じアングルパラメータを使用

### 3. 時間帯・衣装の連続性
各シーンで時間帯と衣装を連続させることで、一貫したストーリーを構築

### 4. モジュール式設計
共通NSFWライブラリを使用することで、他のテーマでも同様の統合が可能

## 新規テーマ作成への応用

このサンプルを参考に、以下のような質問を追加することで、NSFW統合テーマを簡単に作成できます：

**質問6: SFWシーンにNSFWシーンを混ぜますか？**
1. なし（従来通り、SFWとNSFWを完全分離）
2. 軽度のみ（キス、抱擁）
3. 中度まで（手コキ、フェラ軽め）
4. 全て混ぜる（このサンプルと同様）

**質問7: どのシーンにNSFWを混ぜますか？**
- シーン2: ビーチ活動
- シーン3: カフェ
- シーン4: 夕暮れ
- シーン5: シャワー
- etc...

## 今後の拡張

- NTRテーマでの統合例
- 複数男性対応
- 服装の段階的変化との組み合わせ
- カスタムシーンへの対応


