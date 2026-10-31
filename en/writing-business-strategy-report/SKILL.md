---
name: writing-business-strategy-report
description: Use when consolidating the disclosure, news, and competitive threat analyses into the company's business analysis and strategy report, or when writing image plans and image prompts for the visuals of that report.
---

# Business Analysis and Strategy Report

## Procedure
- Input: the disclosure analysis report, the earnings call analysis report, the news analysis report, and the threat analysis report (the paths named in the request)
- Read every input report with read_file and integrate their key content. Avoid unnecessary repetition, and build a logical flow that shows business insight.
- Use web_search only for content that the input reports do not support well enough.
- Length: at least 1500 words

## Report structure
1. Executive Summary
2. Business portfolio overview: the business segments and the role of each
3. Financial results and sales drivers
   - Table of company-wide results for the reporting period and the comparison period
   - Table of sales, operating profit, and share per segment
   - Sales drivers and profit change factors per segment
4. Recent key issues: based on the news analysis report
5. Competitive landscape and potential threats: summary of the threat priorities in the threat analysis report
6. Future business strategy and growth drivers: strategy, investment, and shareholder returns per segment
7. Conclusion and strategic recommendations: at least 3 actionable recommendations
8. References

## Image plan structure
- Input: the business analysis and strategy report
- Write at least 3 plans for visuals to insert in the report. Each plan has:
  1. Title: in the form '### 기획안 N: <title>'
  2. Placement: which section of the report it goes into
  3. Message: the single message the image conveys
  4. Visual concept: color, composition, mood, style
  5. Image prompt: one English prompt in a code block under '**Image prompt**'
- Prompt rules
  + Use a restrained style that suits an executive report.
  + Do not add excessive text or numeric elements that lower image quality. State that the image contains no text, numbers, charts, graphs, or data screens.
  + State that real company logos, trademarks, and product designs must not be reproduced.

## Output rules
- Output language: Korean; format: Markdown (only the image prompts are in English)
- Use tables actively, and state the unit (억원, 백만원, etc.) in every table.
- Use only the input reports and web search results as sources. Mark evidence from an input report as (출처: /reports/<file name>) and evidence from the web as (출처: URL).

## Prohibited
- Relying on pretrained knowledge or assumptions
- Making up or estimating content
- Adding figures that are not in the input reports without a source
