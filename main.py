import os
import argparse
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

parser = argparse.ArgumentParser(description="Firecrawl Web Scraper")
parser.add_argument(
    "-n",
    "--name",
    type=str,
    default=os.getenv("FILE_NAME", "output.md"),
)

args = parser.parse_args()

file_name = args.name

save_dir = "data/raw"
os.makedirs(save_dir, exist_ok=True)
file_path = os.path.join(save_dir, file_name)

app = FirecrawlApp(api_key)

try:
    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

except FileNotFoundError:
    print("エラー: urls.txt が見つかりません")
    urls = []

if not urls:
    print("処理対象のURLがありません。終了します。")
    exit()

print(f"{len(urls)} 件のURLを処理します...")

scraped_data = []
for url in urls:
    # Markdown形式で抽出
    result = app.scrape(url, formats=["markdown"])
    scraped_data.append(result.markdown)


# 取得したデータをファイルに保存し、Geminiのコンテキストとして利用
if scraped_data:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(scraped_data))

    print(f"完了: {file_path} に保存しました。")
else:
    print("保存するデータがありませんでした。")
