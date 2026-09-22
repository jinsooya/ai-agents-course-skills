---
name: selecting-and-analyzing-segments
description: Use when selecting target market and customer segment candidates, or when writing the segment analysis report that studies each segment and selects the final target segment.
---

# Segment Candidate Selection and Segment Analysis Report

## Candidate output format
Write each segment in the format below.

**Segment N: [segment name]**
- Definition: one sentence describing who this customer group is
- Demographics: age range, gender, occupation or role, income level, company size, and any other applicable items
- Market: the industry, market category, and geographic scope this customer group belongs to, as concretely as possible
- Rationale: why this company can target this segment

Output rules
- Output language: the language of the request, format: Markdown
- Output only the candidate list (no analysis process or commentary)
- Make demographics and market as concrete as the company information allows

Prohibited
- Selecting duplicate or near-duplicate segments
- Selecting segments unrelated to the company information
- Writing speculative numbers without a source

## Segment analysis report structure
Research procedure
- First plan the research per segment with write_todos, then research sequentially according to the plan.
- For each segment, focus on the items below.
  + The size, growth rate, and trends of the market the segment belongs to
  + The main needs, pain points, and purchase behavior of the customer group
  + The competitive landscape of the market and its major players
- Exclude duplicate or similar content and keep complementary information.
- Keep every source URL internally for use in the report.
- Once collection is complete, stop searching and start writing the report immediately.

Report structure
1. Executive Summary: three to five lines of key insights across all segments
2. Detailed analysis per segment (repeat for each segment)
   - 2-N. [segment name]
     + Market status: market size, growth rate, main trends
     + Customer characteristics: key needs, pain points, purchase behavior
     + Competitive landscape: major competitors and their positioning in the market
     + Feasibility assessment: fit with the company situation and the campaign requirements
3. Final target segment selection
   - Selected segment(s): the segment(s) to target (more than one allowed)
   - Rationale: why these segments were chosen, based on the analysis above
   - Excluded segments and reasons: the segments not selected and why
   - Campaign direction: a proposed campaign approach based on the selected target

Output rules
- Output language: the language of the request, format: Markdown
- Write the report in prose (minimize bullet lists)
- Cite a source for every claim and analysis in the form (source: URL)
- Save only the final report to the file (do not output the research process)

Prohibited
- Asserting facts from prior knowledge or guesswork without a source
- Citations without a URL, or fabricated or fictional URLs
- Citing the same article more than once
- Starting the report without searching
