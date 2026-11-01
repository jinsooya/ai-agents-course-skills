---
name: planning-competitive-scenarios
description: Use when writing a future-dated business newspaper article, the competitor's strategy plan, the company's counter-strategy plan, or the strategy war game from the company and competitor reports.
---

# Competitive Scenario Analysis

## Common rules
- Write only after reading all input reports with read_file. Use web_search only when the input needs to be supplemented.
- Mark the source of every factual statement as `(출처: /reports/<file name>)` or `(출처: URL)`.
- Separate future outlooks and assumptions from facts, and label them as '가정' (assumption) or '시나리오' (scenario).
- Output language: Korean; format: Markdown

## Business newspaper article structure
- Perspective: a business journalist
- A front-page business newspaper article that explains, from the future year named in the request, how the competition between the company and the competitor turned out
1. Headline and subheadline
2. Lead: the outcome in 2-3 sentences
3. Body
   - Industry change
   - Competitive strategy
   - Factors of winning and losing
   - Market impact
4. Last line of the article: '이 기사는 분석 보고서를 바탕으로 작성한 가상 시나리오 기사입니다.'

## Competitor strategy plan structure
- Perspective: the competitor's head of corporate strategy
- Input: the company analysis report and the competitor threat analysis report
- Present a 3-year strategy. If the company has many business segments and affiliates, consider the synergies among them and name the key competing affiliates and segments.
1. Core growth axes
2. Channel/distribution strategy
3. Pricing/promotion strategy
4. Investment/partnership/production expansion

## Company counter-strategy plan structure
- Perspective: the company role named in the request
- Input: the company analysis report and the competitor strategy plan
- Write the company's detailed 3-year counter-strategy against the competitor.
1. Defensive strategy
2. Offensive strategy
3. Brand/channel strategy
4. Pricing/promotion strategy
5. Investment priorities
6. Execution risks

## Strategy war game structure
- Perspective: the facilitator of a 'strategy war game' in an MBA strategy class
- Input: the competitor strategy plan and the company counter-strategy plan
- Cover each of these three scenarios.
  1. The competitor strongly leads the market
  2. The company and the competitor compete in balance
  3. A third player enters and changes the game
- For each scenario, include:
  1. Three predicted next moves of the competitor
  2. Three predicted counter-moves of the company
  3. The key variables that decide the contest
  4. A judgment on who is more likely to have the advantage
  5. Three class discussion questions
- Include at least one table per scenario.
- Use actionable strategic language rather than vague expressions. Keep it engaging but not light, from a business strategy perspective.

## Prohibited
- Stating figures without a source as facts
- Mixing assumptions with facts
- Writing from memory without reading the input reports
