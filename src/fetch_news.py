# fetch_news 

from pathlib import Path
from datetime import date
import requests
import os

# ---------------------------
# Paths
# ---------------------------

VAULT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = REPO_ROOT / "templates" / "daily-news-template.md"
OUTPUT_DIR =REPO_ROOT / "daily"


# ---------------------------
# Template
# ---------------------------

TEMPLATE_CONTENT = """# Daily News - {{date}}

Source: {{source}}

---

{{news_items}}
"""

TEMPLATE_PATH.parent.mkdir(parents=True, exist_ok=True)
if not TEMPLATE_PATH.exists():
    TEMPLATE_PATH.write_text(TEMPLATE_CONTENT, encoding="utf-8")
    print(f"✅ Created template at {TEMPLATE_PATH}")

# ---------------------------
# Fetch
# ---------------------------

def get_news_from_api():
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

    # fallback if API fails or returns empty
    if not news_items:
        print("⚠️ No news returned from API, using mock data")
        news_items = [
            {
                "title": "AI accelerates drug discovery",
                "source": "Nature",
                "url": "https://example.com/ai-drug-discovery",
                "summary": "Researchers report faster compound screening using AI models."
            },
            {
                "title": "Cloud costs continue to rise",
                "source": "TechCrunch",
                "url": "https://example.com/cloud-costs",
                "summary": "Enterprises reassess cloud strategies amid rising costs."
            }
        ]

    return news_items  # ✅ must return a list

# ---------------------------
# Markdown
# ---------------------------

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

# ---------------------------
# Main
# ---------------------------

def main():
    today = date.today().isoformat()
    news = get_news_from_api()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = (
        template
        .replace("{{date}}", today)
        .replace("{{source}}", "newsdata.io")
        .replace("{{news_items}}", render_news_items(news))
    )

    output_file = OUTPUT_DIR / f"{today}.md"
    output_file.write_text(content, encoding="utf-8")
    print(f"✅ Daily news written to {output_file}")

if __name__ == "__main__":
    main()




