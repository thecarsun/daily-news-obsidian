# fetch_news 

from pathlib import Path
from datetime import date
import re
import requests
import os

# Paths
TEMPLATE_PATH = Path("templates/daily-news-template.md")
OUTPUT_DIR = Path("vault/daily")

def get_news_from_api():
    import requests 

    api_key = os.getenv("NEWSDATA_API_KEY") or "pub_ef1790d6e67e436bbf66d10388deb1fc"
    url = "https://newsdata.io/api/1/latest"
    params = {
        "apikey": api_key,
        "q": "US news",
        "language": "en",
        "size": 5,
    }
    
    news_items = []
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
    except Exception as e:
        print(f"⚠️ API request failed: {e}")
        results = []

    for article in results:
        if not isinstance(article, dict):
            continue
        news_items.append({
            "title": article.get("title", "No title"),
            "source": article.get("source_id", "Unknown"),
            "url": article.get("link", ""),
            "summary": article.get("description", "")
        })

    if not news_items:
        print("⚠️ No news items found in API response.")
        news_items = [
            {
                "title": "No news available",
                "source": "N/A",
                "url": "",
                "summary": "The news API did not return any articles."
            },
            {
                "title": "API Error",
                "source": "N/A",
                "url": "",
                "summary": "There was an issue fetching news from the API."
            }
        ]
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

    if not TEMPLATE_PATH.exists():
        print(f"⚠️ Template file not found: {TEMPLATE_PATH}")
        return

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



