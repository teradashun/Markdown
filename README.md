# 🤖 LLM-Ready Web Scraper (Dockerized with Firecrawl)

## 📖 1. プロジェクト概要 (Overview)
Webサイトの情報を生成AI（LLM）の学習・RAG（検索拡張生成）用に最適化して抽出する**AI用Webスクレイピング自動化ツール**である。
スクレイピングエンジンに「Firecrawl」を採用し、Docker上で動作させることで、環境に依存せず誰でも高品質なMarkdownデータを取得できる。

### 🚀 解決した課題
* **Before:** Webサイトの情報をLLMに入力する際、手動コピーではHTMLタグや広告などのノイズが混入し、トークン数の浪費やAIの回答精度低下を招いていた。
* **After:** URLリストを用意するだけで、LLMが解釈しやすい**クリーンなMarkdown形式**として自動収集・整形が可能に。

---

## 🛠 2. 技術スタックと選定理由 (Tech Stack)

| Category | Tech | Why Selected? |
| :--- | :--- | :--- |
| **Container** | **Docker** | チーム開発や異なるOS間でも**環境差異によるエラーを防ぎ、完全な再現性を担保**するため。 |
| **Scraper** | **Firecrawl** | 一般的なライブラリ（BeautifulSoup等）と比較し、LLM向けに特化したMarkdown変換精度が高く、メンテナンスコストを低減できるため。 |
| **Lang** | **Python 3.x** | データ処理ライブラリが豊富で、API連携の実装が容易なため。 |

---

## 💡 3. こだわった技術的ポイント (Technical Highlights)

### ① Dockerにおけるファイル権限管理（Root問題の解決）
**課題:**
当初、コンテナ内で生成されたファイルの所有者が `root` になってしまい、ホスト側（ローカル環境）で削除や編集ができない権限エラーが発生した。

**解決策:**
`docker-compose.yml` および `.env` でユーザーID（UID）とグループID（GID）を動的に渡す設計を実装。
実行ユーザーの権限をコンテナ内に継承させることで、**ホスト側からでも自由にファイルを操作できる利便性**を確保した。

### ② 最小限の構成で即座に利用可能
複雑な設定を排除し、`.env` にAPIキーを設定するだけの「2ステップ」で動作するように設計。エラーハンドリングも実装し、スクレイピング失敗時に原因（無効なURL、API制限など）が即座に分かるようにしている。
---

## 📂 4. ディレクトリ構成
```text
.
├── Dockerfile
├── docker-compose.yml
├── main.py             # スクレイピング実行スクリプト
├── urls.txt            # 読み込ませたいWebサイトのURLリスト
├── .env                # 環境変数（APIキー, UID, GID）
├── requirements.txt
└── data/               # 出力ディレクトリ
    └── raw/            # 取得データの保存先
```

## ⚙️ 5. セットアップ (Setup)

### 前提条件
* Docker Desktop がインストールされていること
* Firecrawl のAPIキーを取得済みであること

### 手順
1. **リポジトリのクローン**
   ```bash
   git clone [repository-url]
   cd [repository-name]

2. **ユーザーID/グループIDの確認 (Linux/Mac)**
   ```bash
   id -u
   id -g
   ```

   .envファイルを作成し、以下を記述
   ```bash    
    API_KEY=fc_sk_xxxxxxxxxxxx  # Firecrawl API Key
    UID=1000                    # 確認したユーザーID
    GID=1000                    # 確認したグループID
    FILE_NAME=output.md         # 出力したいファイル名

3. URLリストの準備 urls.txt に対象のURLを改行区切りで入力

---

## 💻 6. 実行方法 (Usage)
コンテナを起動し、スクレイピングを実行


1. コンテナのビルドと起動

- `docker compose up -d`

2. コンテナに入りスクリプトを実行

- `docker compose exec scraper bash`

- `python main.py --name [任意のファイル名]`

---

## 🔮 7. 今後の展望 (Future Roadmap)
**Vector Databaseへの自動格納機能の実装**
- 取得したMarkdownデータをChromaDBやPineconeなどのベクトルデータベースへ直接保存し、RAG（検索拡張生成）システムへ即座に組み込めるパイプラインを構築する。