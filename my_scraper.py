from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
file_name = os.getenv("FILE_NAME")

app = FirecrawlApp(api_key)

# 1. 特定の複数URLを個別に取得する場合
urls = [
    "https://realunivlog.com/articles/reality-portfolio-example-make-method",
    "https://d3n6by1l4doufg.cloudfront.net/portfolio.html",
    "https://engineerbegin.com/engineer-portfolio-guide/",
    "https://tech-go.jp/it-engineer/portfolio",
    "https://rookie.levtech.jp/guide/detail/60005/",
]

scraped_data = []
for url in urls:
    # Markdown形式で抽出
    result = app.scrape(url, formats=["markdown"])
    scraped_data.append(result.markdown)

"""
# 2. 特定ドメインを再帰的に取得（Crawl）する場合
# 指定したURLからリンクを辿り、サイト全体をMarkdown化します
crawl_result = app.crawl_url(
    'https://www.kaggle.com/competitions/example',
    params={
        'limit': 10, # 取得ページ数の制限
        'scrapeOptions': {'formats': ['markdown']}
    },
)
"""

# 取得したデータをファイルに保存し、Geminiのコンテキストとして利用
with open(file_name, "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(scraped_data))
