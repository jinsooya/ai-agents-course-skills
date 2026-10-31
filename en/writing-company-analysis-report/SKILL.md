---
name: writing-company-analysis-report
description: Use when consolidating the disclosure and news analyses into the company analysis report, with a separate section (industry keywords, threat focus, comparison lens) prepared for the competitor comparison.
---

# Company Analysis Report

## Procedure
- Input: the disclosure analysis reports, the news analysis report, and the competitor information file (the paths named in the request)
- Read all input files with read_file and integrate the key content of each. Avoid unnecessary repetition.
- For the industry keywords, threat focus, and comparison lens in the competitor information file, look in the input reports first, and use web_search only when they are not enough.
- Length: at least 2000 words

## Report structure
1. Executive Summary
2. Group overview and business portfolio
3. Status per affiliate and business segment: results tables and revenue drivers
4. Key recent issues: based on the news analysis report
5. Future business strategy
6. Analysis for the competitor comparison (name the competitor in the heading)
   - 6-1. The company's position on the industry keywords
   - 6-2. The company's exposure from the threat focus perspective
   - 6-3. The company's strengths and weaknesses per comparison lens
7. Implications
8. References

## Output rules
- Output language: Korean; format: Markdown
- Use tables actively.
- Use only the input reports and web search results as sources. Mark evidence from an input report as (출처: /reports/<file name>) and evidence from the web as (출처: URL).

## Prohibited
- Relying on pretrained knowledge or assumptions
- Making up or estimating content
- Adding figures that are not in the input reports without a source
