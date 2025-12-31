# Stable Diffusion Wildcard System

Stable Diffusion用のDynamic Prompts Wildcard管理システムです。

## 📁 構造

```
自作2_1/
├── params/              # 汎用パラメータ（全テーマ共通）
│   ├── character_male_type.yaml
│   ├── character_outfits.yaml
│   ├── pose_times.yaml
│   └── pose_places.yaml
│
├── themes/              # テーマテンプレート
│   ├── lovey/          # ラブラブテーマ
│   │   ├── pose_scenes_daily.yaml
│   │   ├── pose_scenes_onsen.yaml
│   │   ├── pose_scenes_beach.yaml
│   │   ├── pose_scenes_office.yaml
│   │   ├── pose_faces.yaml
│   │   ├── pose_atmosphere.yaml
│   │   ├── sex_prompts.yaml
│   │   ├── sex_faces.yaml
│   │   └── sex_sounds.yaml
│   │
│   └── ntr/            # NTRテーマ（未実装）
│
├── templates/          # テンプレート・参考資料
│   ├── scene_category_codes.md
│   ├── scene_outfit_mapping.md
│   └── README.md
│
├── doc/                # ドキュメント
│   └── wildcard_rules.md
│
└── [テーマ名]/         # 個別テーマ実装
    ├── theme.txt
    ├── config.yaml
    ├── pose_play.yaml
    ├── sex_play.yaml
    ├── fellatio_play.yaml (optional)
    ├── main.yaml
    └── README.md
```

## 🚀 使い方

### 新しいテーマを作成する

AIアシスタントに以下のように伝えてください：

```
新しいテーマを作りたいです
```

AIが5つの質問を順番に行います：
1. テーマベース（lovey/ntr）
2. テーマタイプ（daily/onsen/beach/office）
3. テーマ名
4. 時系列変化
5. 男性タイプ & Sex場所

### 既存テーマを使用する

Stable Diffusion WebUIのDynamic Promptsで以下のように参照：

```
# Poseシーンのみ（SFW）
__自作2_1/[テーマ名]/pose_play__

# Sexシーンのみ（NSFW）
__自作2_1/[テーマ名]/sex_play__

# 全シーン（Pose + Sex）
__自作2_1/[テーマ名]/main__
```

## 📚 ドキュメント

詳細は以下を参照：
- [完全なルール・仕様](./doc/wildcard_rules.md)
- [テンプレート使用方法](./templates/README.md)
- [AIアシスタント用ルール](./.cursorrules)

## 🎯 特徴

- **3層アーキテクチャ**: 汎用パラメータ、テーマテンプレート、個別実装の分離
- **自動服装選択**: シーンタイプに応じた自動マッピング
- **豊富なシーンライブラリ**: 日常、温泉、ビーチ、オフィス対応
- **柔軟な時系列管理**: 時間の流れを自然に表現
- **完全な自己完結型**: 場所情報込みのシーンプロンプト

## 🔧 システム要件

- Stable Diffusion WebUI
- Dynamic Prompts Extension
- YAML対応ワイルドカードシステム

## 📝 ライセンス

個人利用・改変自由

## 🤝 貢献

プルリクエスト歓迎！特に以下の項目：
- NTRテーマテンプレートの作成
- 新しいシーンライブラリの追加
- 既存シーンの改善・拡充

## 📅 更新履歴

- 2025-01-01: 初版リリース
  - Loveyテーマ完成（4種類のシーンライブラリ）
  - 5問インタビューシステム実装
  - 自動服装選択機能実装

