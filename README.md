# daily-news-obsidian pipeline project

**Background/Motivation**

This project is a first iteration of a simple automation pipeline that pulls the top five news articles from a news API and generates 
a daily Markdown note in my Obsidian vault containing article titles, links, and sources.

The pipeline runs hands-off via scheduled CI/CD (GitHub Actions), keeping me informed with the top 5 levant news items without 
having to manually check multiple sources. 

The goal is to stay meaninfully informed while reducing the noise and distractions of social media, news aggregators, and ads *sorry ads, much love*

## What

- A simple automated pipline that pulls **top 5** news articles from a news publc API *so you don't have to*
- A simple daily ``Markdown`` note will get generated with the **top 5** news article and their title/links/sources
- The note will be dropped into my Obsidian vault
- Runs hands-off via (scheduled) CI/CD (Github Actions)

## Architecture

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


## Future
- LLM summarization 
- Topic clustering
- Bias comparision (same story, different outlets)
- Weekly rollups 
- .. and more...