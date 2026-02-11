from pathlib import Path
from datetime import date
import os
import requests

# ---------------------------
# Paths 
# ---------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = REPO_ROOT / "templates" / "daily-news-template.md"
OUTPUT_DIR = REPO_ROOT / "daily"
TEMPLATE_PATH = VAULT_ROOT / "templates" / "daily-news-template.md"
OUTPUT_DIR = VAULT_ROOT / "daily"


# ---------------------------
# Template
# ---------------------------

TEMPLATE_CONTENT = """# Daily News - {{date}}

Source: {{source}}

---

{{news_items}}
"""

def ensure_template_exists() -> None:
    TEMPLATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not TEMPLATE_PATH.exists():
        TEMPLATE_PATH.write_text(TEMPLATE_CONTENT, encoding="utf-8")
        print(f"✅ Created template at {TEMPLATE_PATH}")

# ---------------------------
# Fetch
# ---------------------------

def get_news_from_api() -> list[dict[str, str]]:
    """
    Fetch top news from newsdata.io.
    Returns a list of dicts with keys: title, source, url, summary
    """
    api_key = os.getenv("NEWS_API_KEY")
    url = "https://newsdata.io/api/1/latest"
    params = {
        "apikey": api_key or "pub_ef1790d6e67e436bbf66d10388deb1fc",   
        "q": "US news",
        "language": "en",
        "size": 5,
    }

    news_items: list[dict[str, str]] = []

    try:
        if not api_key:
            raise RuntimeError("NEWS_API_KEY is not set (GitHub Secret / env var).")

        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        # newsdata.io uses "results"
        results = data.get("results", [])
        if not isinstance(results, list):
            results = []

        for article in results:
            if not isinstance(article, dict):
                continue
            news_items.append({
                "title": str(article.get("title") or "No title"),
                "source": str(article.get("source_id") or "Unknown"),
                "url": str(article.get("link") or ""),
                "summary": str(article.get("description") or "")
            })

    except Exception as e:
        print(f"⚠️ API request failed: {e}")

    # Fallback (never return empty)
    if not news_items:
        print("⚠️ Using mock data fallback")
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
            },
        ]

    return news_items


# ---------------------------
# Markdown
# ---------------------------

def render_news_items(news: list[dict[str, str]]) -> str:
    blocks: list[str] = []
    for i, item in enumerate(news, start=1):
        title = item.get("title", "No title")
        source = item.get("source", "Unknown")
        url = item.get("url", "")
        summary = item.get("summary", "")

        blocks.append(
            f"## {i}. {title}\n"
            f"- **Source:** {source}\n"
            f"- **Link:** {url}\n"
            f"- **Summary:** {summary}\n"
        )

    return "\n".join(blocks).strip() + "\n"


# ---------------------------
# Main
# ---------------------------

def main() -> None:
    ensure_template_exists()

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




