# fetch_news 

from pathlib import Path
from datetime import date
import requests
import os

# Paths
TEMPLATE_PATH = Path("templates/daily-news-template.md")
OUTPUT_DIR = Path("vault/daily")

def get_news_from_api():
    api_key = os.getenv("NEWSDATA_API_KEY") or "pub_ef1790d6e67e436bbf66d10388deb1fc"
    url = "https://newsdata.io/api/1/latest"

    params = {
        "apikey": api_key,
        "q": "US news",
        "language": "en",
        "size": 5,
    }

    response = requests.get(url, params=params)
    data = response.json()

    news_items = []
    for article in data.get("results", []):
        news_items.append({
            "title": article.get("title", "No title"),
            "source": article.get("source_id", "Unknown"),
            "url": article.get("link", ""),
            "summary": article.get("description", "")
        })

    return news_items

def render_news_items(news):
    blocks = []
    for i, item in enumerate(news, start=1):
        blocks.append(
            f"## {i}. {item['title']}\n"
            f"- **Source:** {item['source']}\n"
            f"- **Link:** {item['url']}\n"
            f"- **Summary:** {item['summary']}\n"
        )
    return "\n".join(blocks)

def main():
    today = date.today().isoformat()
    news = get_news_from_api()

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    content = template.replace("{{date}}", today)
    content = content.replace("{{source}}", "newsdata.io")
    content = content.replace("{{news_items}}", render_news_items(news))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{today}.md"

    output_file.write_text(content, encoding="utf-8")
    print(f"✅ Daily news written to {output_file}")

if __name__ == "__main__":
    main()



