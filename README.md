# daily-news -> obsidian pipeline project

**BACKGROUND/MOTIVATION**

This project is a first iteration of a simple automation pipeline that pulls the top five news articles from a news API and generates 
a daily Markdown note in my Obsidian vault containing article titles, links, and sources.

The pipeline runs hands-off via scheduled CI/CD (GitHub Actions), keeping me informed with the top 5 levant news items without 
having to manually check multiple sources. 

The goal is to stay meaninfully informed while reducing the noise and distractions of social media, news aggregators, and ads *sorry ads, much love*

## WHAT

- A simple automated pipline that pulls **top 5** news articles from a news publc API *so you don't have to*
- A simple daily ``Markdown`` note will get generated with the **top 5** news article and their title/links/sources
- The note will be dropped into my Obsidian vault
- Runs hands-off via (scheduled) CI/CD (Github Actions)

## ARCHETECTURE

```
┌──────────────┐
│ News API     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Python Script│
└──────┬───────┘
       ↓
┌──────────────┐
│ Obsidian     │
│ Daily Note   │ (.md file)
└──────┬───────┘
       ↓
┌──────────────┐
│ GitHub       │
│ Actions      │
└──────────────┘
```

## TECH
- Python (data fetching/processing)
- Markdown (note formatting)
- GitHub Actions (automation)
- News API (news source)
- Obsidian (for daily top 5 news generateion output)


## Future
- LLM summarization 
- Topic clustering
- Bias comparision (same story, different outlets)
- Weekly rollups 
- .. and more...

## STATUS
🚧 In Progress - stay tuned for updates!