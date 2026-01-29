# Web Content Scraper for LLM (Dockerized)

## 1. プロジェクト概要 (Overview)
Webサイトの情報を生成AI（LLM）に効率的に読み込ませるために開発した、**AI用Webスクレイピング自動化ツール**である。
指定したURLリストを読み込ませることで、HTMLからテキスト情報を自動抽出し、生成AIが解釈しやすいクリーンな形式で保存する。

### 解決した課題
* **Before:** Webサイトの情報をAIに入力する際、手動でのコピペ作業は非効率であり、HTMLタグや広告などのノイズが混入してAIの回答精度を下げる要因となっていた。
* **After:** URLリストを用意するだけで、AIのコンテキストウィンドウにそのまま渡せる高品質なテキストデータを自動収集・整形できるようになった。

---

## 2. 技術スタック (Tech Stack)
* **Language:** Python 3.x
* **Libraries:** [例: Requests, BeautifulSoup4, Pandas, Selenium]
* **Container:** Docker
* **Configuration:** python-dotenv (.env)

**Docker採用の理由:**
スクレイピング処理はOSやブラウザのバージョン依存によるエラーが発生しやすいため、Dockerで実行環境をコンテナ化し、**どのPCでも安定して動作する再現性**を担保した。

---

## 3. ディレクトリ構成
```text
.
├── Dockerfile
├── main.py             # スクレイピング実行スクリプト
├── urls.txt            # 読み込ませたいWebサイトのURLリスト
├── .env                
├── requirements.txt
└── data/raw/           # データの出力先
```

---

## 4. 設定
- urls.txtファイルにURLを入力
- id -uとid -gをターミナルで実行して、ユーザIDとグループIDを追加
- .envファイルにFirecrawlのAPIキー、ユーザID、グループIDを保存

###　.envファイル例
```text
API_KEY=your_key
FILE_NAME=output.md
UID=1000
GID=1000
```

---
## 5. 操作方法
- `docker compose up -d`
- `docker compose exec scraper bash`
- `python main.py --name ファイル名`