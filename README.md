# Webサイトのスクレイピング自動化

## 方法
1. urlsにURLをコピペする
2. .envのFILE_NAMEにファイル名を指定
3. イメージを作成: `docker build -t scraper .`
4. ターミナルで実行: `docker run --env-file .env -v $(pwd):/app -it scraper`