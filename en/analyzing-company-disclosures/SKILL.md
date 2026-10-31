---
name: analyzing-company-disclosures
description: Use when reading a corporate disclosure document (half-year, quarterly, or annual report, or an earnings release) in full and writing an analysis report on revenue trends, revenue drivers, and future strategy per affiliate and business segment.
---

# Disclosure Document Analysis Report

## Reading procedure
- Read the assigned document file with read_file from the first line to the last line.
- For a long document, set limit=1000 and repeat the read with offset 0, 1000, 2000, and so on. When fewer than 1000 lines come back, you have reached the end.
- Do not write the report after reading only the beginning. Start writing only after reading the whole document.
- While reading, take notes per affiliate and business segment: revenue, operating profit, year-over-year change, the reasons for the change, and statements about strategy.
- Do not calculate or estimate figures that are not in the document. If a change rate is not in the document, write 'no change rate in the document'.

## Periodic report (half-year, quarterly, or annual report) analysis structure
1. Summary: reporting period, key consolidated results, and the most important changes in 3-5 lines
2. Group overview and business structure: the holding company, major affiliates, and business segments
3. Analysis per affiliate and business segment (repeat for each)
   - 3-N. [Affiliate or segment name]
     + Business: main products and services, market position
     + Revenue trend: a table of revenue and operating profit for the reporting and comparison periods (state the unit)
     + Revenue drivers: the causes of growth or decline
     + Future strategy: plans and investments stated in the document
4. Risk factors: risks stated in the document, such as exchange rates, raw materials, regulation, and competition
5. Implications: key points to use in the competitor comparison

## Earnings release analysis structure
1. Summary: consolidated revenue, operating profit, and net income with year-over-year changes in 3-5 lines
2. Consolidated results: a table of revenue, operating profit, and net income, with the drivers of change
3. Results of major listed companies and affiliates: a table of revenue and operating profit per company, with the main points per company
4. Revenue drivers and profit drivers: organized by business segment
5. Implications: indicators to watch in the next quarter

## Output rules
- Output language: Korean; format: Markdown
- Use tables actively, and state the unit (KRW 100 million, KRW million, and so on) in every table.
- Mark the source document of each figure and claim as (출처: /inputs/<file name>).
- Save the report body to the assigned path with write_file, and reply with only the saved path and a 5-line summary.

## Prohibited
- Creating or estimating figures that are not in the document
- Supplementing the document with web search results or pretrained knowledge
- Writing as if the whole document was analyzed after reading only part of it
