---
name: writing-competitor-threat-report
description: Use when writing the web search plan for one competitor, or the threat analysis report on that competitor's recent moves and its potential threats to the group and its affiliates.
---

# Competitor Threat Analysis

## Search plan structure
- Input: the company analysis report and the competitor information file (the paths named in the request)
- For each of the 7 items below, write at least 3 search queries and the search purpose.
  1. Recent core business trends
  2. Main product/service/channel strategy
  3. Pricing policy and promotion changes
  4. Investment, partnerships, acquisitions, overseas expansion, and capacity expansion
  5. Market response, consumer response, and implications for results or share
  6. Potential threats to the group and its affiliates
  7. Response implications for the group and its affiliates
- End with a 3-column table: section / search queries / search purpose.
- Do not run web searches in this step.

## Research procedure
- Delegate the competitor research to the competitor-researcher subagent with the task tool.
- Pass only the competitor name, the search plan path, the competitor information file path, the company analysis report path, and the save path. Do not copy file contents into the call.
- The subagent researches with web_search following the search plan and saves the report in the structure below.
- The main agent reads the saved file with read_file and checks the sections and sources. If a section is missing, call the same subagent once more to complete it.

## Threat analysis report structure
1. Executive Summary
2. Recent core trends
3. Product/service/channel/distribution strategy
4. Pricing/promotion/brand strategy
5. Investment/partnership/production/overseas expansion
6. Potential threats to the group and its affiliates
7. Response implications for the group and its affiliates
8. References

End with a 4-column table: threat area / threat level (상/중/하) / evidence / implication for the company.

## Output rules
- Output language: Korean; format: Markdown
- Use only the input reports and web search results as sources.
- Give a clear source as (출처: URL) for every claim, figure, and case.
- Focus on identifying threat factors, their quantitative and qualitative evidence, and the implications, in detail.
- Minimize duplicate sources, use sources that complement each other, and balance Korean and global sources where possible.

## Prohibited
- Stating facts without a source, from pretrained knowledge or estimation
- Citations without a URL, or false or fictional URLs
- Researching companies that were not assigned
