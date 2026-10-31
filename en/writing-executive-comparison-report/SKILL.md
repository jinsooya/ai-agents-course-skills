---
name: writing-executive-comparison-report
description: Use when writing the executive competitor comparison report (one competitor or several) from the company and competitor reports, or the image plans and image prompts for the visuals of that report.
---

# Executive Competitor Comparison Report

## Common rules
- Read all input reports with read_file and integrate their key content. Avoid unnecessary repetition, and build a logical flow that shows business insight.
- Center the report on comparison, threat prioritization, and response implications for the company.
- Use tables actively.
- Use web_search only when the input needs to be supplemented.

## Single-competitor comparison report structure
Length: at least 2000 words
1. Executive Summary
2. Key trends of the company
3. Key trends and threat types of the competitor
4. Threat priorities for the company
5. Short-term actions
6. Mid- to long-term strategy
7. 5-line summary for executives
8. References

## Multi-competitor comparison report structure
Length: at least 3000 words
1. Executive Summary
2. Key trends of the group
3. Comparison of key trends per competitor
4. Comparison of threat types per competitor
5. Threat priorities for the group and its affiliates
6. Short-term actions
7. Mid- to long-term strategy
8. 5-line summary for executives
9. References

Always include these three tables (keep the Korean column names).

Table 1
| 경쟁사 | 핵심 사업 축 | 최근 핵심 동향 | 본사 영향 영역 | 위협 수준(상/중/하) | 대응 우선순위 |
|---|---|---|---|---|---|

Table 2
| 경쟁사 | 가격 위협 | 채널 위협 | 브랜드 위협 | 제품/서비스 위협 | 플랫폼/IP 위협 | 해외확장 위협 |
|---|---|---|---|---|---|---|

Table 3
| 우선순위 | 대응 과제 | 목적 | 관련 경쟁사 | 기대 효과 |
|---|---|---|---|---|

- The competitors differ in industry, so do not compare them by one yardstick; compare their strategic impact from the company's perspective.
- End by naming the 1-2 competitors to watch most closely now.

## Image plan structure
- Input: the competitor comparison report
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
- Use only the input reports and web search results as sources. Mark evidence from an input report as (출처: /reports/<file name>) and evidence from the web as (출처: URL).

## Prohibited
- Relying on pretrained knowledge or assumptions
- Making up or estimating content
- Adding competitors or figures that are not in the input reports without a source
