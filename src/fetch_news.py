# fetch_news 

from pathlib import Path
from datetime import date

from pathlib import Path
from datetime import date

# Paths
TEMPLATE_PATH = Path("templates/daily-news-template.md")
OUTPUT_DIR = Path("vault/daily")

def get_mock_news():
    return [
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
        {
            "title": "New battery tech shows promise",
            "source": "IEEE Spectrum",
            "url": "https://example.com/battery-tech",
            "summary": "Solid-state batteries move closer to mass production."
        },
        {
            "title": "Regulators eye AI governance",
            "source": "Reuters",
            "url": "https://example.com/ai-regulation",
            "summary": "Governments propose new frameworks for AI oversight."
        },
        {
            "title": "Remote work enters new phase",
            "source": "Harvard Business Review",
            "url": "https://example.com/remote-work",
            "summary": "Hybrid work models stabilize across industries."
        },
    ]

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
    news = get_mock_news()

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    content = template.replace("{{date}}", today)
    content = content.replace("{{source}}", "mock-news")
    content = content.replace("{{news_items}}", render_news_items(news))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{today}.md"

    output_file.write_text(content, encoding="utf-8")
    print(f"✅ Daily news written to {output_file}")

if __name__ == "__main__":
    main()


