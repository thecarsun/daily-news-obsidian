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
- The note will automatically drop into my Obsidian vault 
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
Completed my first iteration of the pipeline! 
It successfully pulls the top 5 news articles and generates a daily Markdown note in my Obsidian vault.

## FEW TWEAKS TO NOTE
- At first, I had Obsidian's intended vault where the daily news markdown file that would generate seperate from the Github repo 
- To streamline the process and make it as efficient as possible, I decided to move the Obsidian vault into the Github repo
- After that, I created the GitHub action to run the worklow on a schedule and it successfully generated the daily news markdown file in the Obsidian vault within the repo
- There are other ways to do this such as using (Windows Task Scheduler, Cron Jobs, etc.) but I wanted to use GitHub Actions to keep it simple and cloud-based
- I also wanted to use GitHub Actions to keep the code and workflow in one place, making it easier to manage and update as needed

## MOOD
Happy 😁

**If you like this project and want to see more, please let me know and feel free to reach out with any feedback/questions/suggestions**
