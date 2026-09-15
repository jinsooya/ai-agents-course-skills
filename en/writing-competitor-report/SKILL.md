---
name: writing-competitor-report
description: Use when selecting competitors within the target segment and writing the consolidated competitor research report from the per-company files that the subagents produced.
---

# Competitor Research Report

## Research procedure
- First plan the competitor selection and research with write_todos, then proceed sequentially according to the plan.
- Step 1: explore competitor candidates and select three to five by relevance to the target segment.
- Step 2: for each selected company, call the competitor-researcher subagent once with the task tool.
  Pass the company name and the save path /reports/03-competitors/<company-name-english-slug>.md.
  The subagent researches the items below and saves them to the file.
  + Company overview: founding background, size, business areas
  + Main products or services: core offerings, pricing policy, key features
  + Market positioning: brand message, target customers, positioning strategy
  + Marketing and promotion: main channels, campaign examples, content strategy
  + Recent developments: new launches, partnerships, investments, mergers and acquisitions, and other major news
- Step 3: read every per-company file with read_file, exclude duplicate or similar content, and consolidate the complementary information.
- Once collection is complete, stop searching and start writing the report immediately.

## Report structure
1. Executive Summary: three to five lines on the competitive landscape and key implications
2. Competitor selection rationale: the list of selected competitors and why each was chosen
3. Detailed research per competitor (repeat for each competitor)
   - 3-N. [company name]
     + Company overview: founding background, size, business areas
     + Main products or services: core offerings, pricing policy, key features
     + Market positioning: brand message, target customers, positioning strategy
     + Marketing and promotion: main channels, campaign examples, content strategy
     + Recent developments: new launches, partnerships, investments and acquisitions, and other major news
4. Competitive landscape summary: commonalities and differences between competitors and the pattern of competition in the market

## Output rules
- Output language: the language of the request, format: Markdown
- Write the report in prose (minimize bullet lists)
- Cite a source for every claim and analysis in the form (source: URL)
- Save only the final report to the file (do not output the research process)

## Prohibited
- Asserting facts from prior knowledge or guesswork without a source
- Citations without a URL, or fabricated or fictional URLs
- Citing the same article more than once
- Writing the report from memory without reading the subagent files
