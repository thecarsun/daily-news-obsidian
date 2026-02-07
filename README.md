# daily-news -> obsidian pipeline project

**BACKGROUND/MOTIVATION**

This project is a first iteration of a simple automation pipeline that pulls the top five news articles from a news API and generates 
a daily Markdown note in my Obsidian vault containing article titles, links, and sources.

The pipeline runs hands-off via scheduled CI/CD (GitHub Actions), keeping me informed with the top 5 relevant news items without 
having to manually check multiple sources. 

The goal is to stay meaningfully informed while reducing the noise and distractions of social media, news aggregators, and ads (*sorry ads, much love*)

## WHAT

- A simple automated pipline that pulls **top 5** news articles from a news API *so you don't have to*
- A simple daily ``Markdown`` note will get generated with the **top 5** news article and their title/links/sources
- The generated daily-news note will automatically drop into my Obsidian vault 
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
- News API (news source) - I've used [NEWSDATA.IO](https://newsdata.io/) for this project, there are many other news APIs available that could be used as well.
- Obsidian (for daily top 5 news generateion output)


## FUTURE
- LLM summarization 
- Topic clustering
- Bias comparision (same story, different outlets)
- Weekly rollups 
- .. and more... 

## RETROSPECTIVE/LEARNINGS
- Obsidian Vault and GitHub Repo: 
  - In the beginning of this project, the Obsidian vault where the daily top 5 news markdown file would be generated to was in its own path. 
  - Thinking of automation and efficiency in the process, I updated the path of the intended Obsidian vault to be within the Github repo where my Pyton script and GitHub action workflow are locatd.
  
- Github Action/Task schedule flows:
  - There are more than 1 way to get an automated scheduled task running to achieve my goal of generating a daily top 5 news markdown file. 
  - Actions such as Windows Task Scheduler could have been used to run the Python script on a schedule.
  - Thinking about this project and efficiency, I opted for GitHub Actions for a few reasons:
    - It allows me to keep all my code and automation in one place (GitHub repo).
    - It's cloud based, so it runs even when my local machine is off (one less dependency).
    - It's easy to set up and manage with a simple YAML configuration file.
    - It provides built-in logging and monitoring for the scheduled tasks.

## STATUS
- Succssfully completed and achieved the goal and purpose of this project!

## MOOD
Happy 😁

*If you like this project and want to see more, please let me know! Feel free to reach out with any feedback/questions/suggestions. Thank you* 
