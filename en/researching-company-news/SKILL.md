---
name: researching-company-news
description: Use when planning news searches per affiliate and business segment from the disclosure analyses, or when consolidating the per-topic news files collected by subagents into the news analysis report.
---

# Company News Research

## Search plan structure
- Input: the disclosure analysis reports (the /reports/ files named in the request)
- Group the affiliates and business segments into 4-6 research topics, and give each topic an English slug (e.g., cj-cheiljedang, cj-logistics, cj-oliveyoung, cj-enm, holding-and-others).
- For each topic, write:
  + Key issues: 2-3 changes found in the disclosure analysis reports
  + Search queries: 2-3 (Korean or English)
  + Search purpose
- End with a 4-column table: topic / slug / search queries / search purpose.
- Keep the search plan short and concise. No introduction, elaboration, or decoration.
- Do not run web searches in this step.

## News collection procedure
- Call the news-researcher subagent once per topic in the search plan with the task tool.
- Pass only the topic name, the search plan path, and the save path /reports/04-news/<slug>.md. Do not copy the search plan text into the call.
- The subagent collects at least 3 recent news articles per topic and saves them in the article summary format below.

## Article summary format (for the subagent)
- Use the topic name as the file title.
- For each article, write:
  + Title, outlet, publication date, URL
  + One paragraph (6 or more sentences) summarizing it from a business perspective: what happened and what it means for results and strategy
- Avoid duplicate articles and repeated content; select articles that complement each other.

## News analysis report structure (for the main agent)
- Write it after reading all the saved per-topic files with read_file.
1. Summary: key recent issues in 3-5 lines
2. Key news per topic (repeat for each topic): key issues, article summaries, and the link to the disclosures
3. Group-wide common issues: trends that span several affiliates
4. References: article titles and URLs

## Output rules
- Output language: Korean; format: Markdown
- Use only web search results as sources, and keep at least one URL for every article.

## Prohibited
- Citations without a URL, or false or fictional URLs
- Making up article content from pretrained knowledge
- Consolidating from memory without reading the subagent files
