---
name: writing-segment-threat-report
description: Use when planning threat searches per business segment of a multi-segment company, or when writing the per-segment competitor and threat reports and the consolidated threat analysis report.
---

# Competitive Threat Analysis by Business Segment

## Threat search plan structure
- Input: the company's disclosure analysis report (the /reports/ file named in the request)
- Group the issues that could threaten the company into 3-5 topics by business segment, and give each topic an English slug. Use only lowercase English letters and hyphens, and keep the slug a short English name of the segment. If the request gives slug examples, follow them.
- For each topic, write:
  + Target business segment
  + Main competitor candidates: list competitors named in the disclosure analysis report first; if none is named, write '검색으로 확인' (to be confirmed by search)
  + Threat issues: 2-3
  + Search queries: 2-3 (Korean or English)
  + Search purpose
- End with a 5-column table: topic / slug / main competitor candidates / search queries / search purpose.
- Keep the search plan short and concise. Do not add introductions, elaboration, or decorative sentences.
- Do not run web searches in this step.

## Research procedure
- Call the competitor-researcher subagent once per topic in the search plan with the task tool.
- When calling it, pass only the topic name, the search plan path, the company's disclosure analysis report path, and the save path /reports/06-threats/<slug>.md. Do not copy file contents into the call.
- The subagent runs web_search with that topic's queries from the search plan and saves the report in the 'Segment threat report structure' below.
- The main agent reads every saved file with read_file and consolidates them in the 'Consolidated threat report structure' below. If a topic is missing, call the same subagent once more to fill it in.

## Segment threat report structure (for the subagent)
- Title the file with the topic name.
1. Summary: the competitive landscape of the segment and its biggest threat in 3 lines
2. Main competitors: recent moves, investments, orders or contracts, and capacity changes of each competitor
3. Market and industry trends: changes in demand, prices, regulation, and supply chains
4. Potential threats to the company's segment
5. Response implications
6. List of references

End with a 4-column table: threat factor / threat level (상/중/하) / evidence / implication for the company.

## Consolidated threat report structure (for the main agent)
1. Executive Summary
2. Competitive landscape and threats per segment (repeat for each topic): main competitors, key threats, evidence
3. Threats common to several segments: trends that cut across segments (exchange rates, raw materials, regulation, supply chains, etc.)
4. Threat priorities
5. Response implications
6. List of references

Always include this table in the threat priorities (keep the Korean column names).

| 사업부문 | 주요 경쟁사 | 핵심 위협 요인 | 위협 수준(상/중/하) | 대응 우선순위 |
|---|---|---|---|---|

## Output rules
- Output language: Korean; format: Markdown
- Use only the input reports and web search results as sources. Mark evidence from an input report as (출처: /reports/<file name>) and evidence from the web as (출처: URL).
- The goal is not to summarize news but to identify threat factors with quantitative and qualitative evidence and implications.
- Use news articles, company IR materials and press releases, government and international organization materials, and industry research reports as evidence. Do not use user-edited sites such as Namuwiki or Wikipedia as evidence.
- Minimize duplicate sources, use sources that complement each other, and balance Korean and global sources where possible.

## Prohibited
- Stating facts without a source based on pretrained knowledge or guesses
- Quoting without a URL, or writing false or made-up URLs
- Consolidating from memory without reading the subagent files
