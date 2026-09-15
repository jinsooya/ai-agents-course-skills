---
name: comparing-campaign-effectiveness
description: Compare campaign effectiveness in the Marketing Campaign customer data: acceptance rate per campaign, acceptance patterns, response rates by customer characteristics, and a profile of customers who accepted multiple campaigns. Use when the user asks for campaign effectiveness comparison, campaign acceptance rates, campaign response analysis, or future campaign strategies.
---

# Campaign Effectiveness Comparison

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Interpretation premises

Interpret and describe the campaign columns (`AcceptedCmp1` to `AcceptedCmp5`, `Response`) only under the premises below.
- `AcceptedCmp1` to `AcceptedCmp5`: as documented, whether the customer accepted the offer in campaigns 1 to 5 (1/0).
- `Response`: as documented, whether the customer accepted the offer in the last campaign (1/0). Treat it as a **separate column** from the five earlier campaigns.
- Never treat `Response` and `AcceptedCmp5` as the **same event or the same column**; many customers differ between the two.
- State that the acceptance rate of each column is (customers with value 1) / (all customers), and do not speculate about schedules, offer contents, or reasons for success or failure.
- In tables and bar charts, **visually distinguish** the five numbered columns from `Response` with labels and colors.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. The unique values (0/1) of the six campaign columns (AcceptedCmp1 to AcceptedCmp5, Response)
3. Whether the campaign columns have missing values
4. The number and share of customers who accepted at least one campaign
5. The number and share of customers who never accepted a campaign

Print the results as tables and summarize the overall campaign response in two or three sentences.

**Step 2: Acceptance rate per campaign** - Analyze the acceptance rate per campaign.

1. The number of accepting customers and the acceptance rate (%) for each of the six columns (AcceptedCmp1 to AcceptedCmp5, Response)
2. A table sorted from the highest acceptance rate
3. A bar chart of the acceptance rate per campaign
   - x-axis: campaign name, y-axis: acceptance rate (%), value shown above each bar
   - highlight the highest and lowest columns in different colors; distinguish AcceptedCmp1 to 5 from Response in the legend and colors
4. Summarize the high and low columns from the table and chart, without treating `Response` and `AcceptedCmp5` as the same campaign and without asserting schedules, offers, or reasons for success that the data does not contain.

Explain the acceptance rate pattern together with the results.

**Step 3: Campaign acceptance patterns** - Analyze the campaign acceptance patterns.

1. The distribution of the total number of campaigns accepted per customer (0 to 6)
2. A correlation heatmap between campaigns
   - Pearson correlation between the six campaign columns
   - seaborn heatmap, annot=True, palette Blues
3. The top 3 campaign pairs most often accepted together
   - the number and share of customers who accepted both
4. A bar chart of customer counts by number of campaigns accepted (0 / 1 / 2 / 3 or more)

Explain the insights about acceptance patterns together with the results.

**Step 4: Campaign response by customer characteristics** - Analyze the campaign response rate by customer characteristics.

Preprocessing:
- Compute Age from Year_Birth (reference year 2014)
- Bin Age into 39 and under, 40s (40-49), 50s (50-59), 60 and over (60+)
- TotalAccepted = AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5 + Response (sum of 0/1 columns; Response is a separate column from the five earlier campaigns, so interpret the sum as a sum of different indicators)
- AnyAccepted = TotalAccepted > 0 (accepted at least once)

Analysis items:
1. The AnyAccepted rate by income group (25th-percentile cut points: Low / Mid-Low / Mid-High / High)
2. The AnyAccepted rate by age group
3. The AnyAccepted rate by education level
4. The AnyAccepted rate by whether the customer has children (Kidhome + Teenhome > 0)

Print the results as tables and explain the insights about the relation between campaign response and customer characteristics.

**Step 5: Visualize campaign effectiveness** - Build a combined visualization of campaign effectiveness.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Bar chart of the acceptance rate per campaign (sorted from highest, value shown above each bar)
2. (top right) Grouped bar chart comparing campaign response rates by income group (income group × responded / did not respond)
3. (bottom left) Box plot of the number of campaigns accepted by age group
4. (bottom right) Correlation heatmap between campaigns (annot=True, palette Blues)

**Step 6: Profile multi-campaign acceptors** - Profile the customers who accepted multiple campaigns.

1. Classify customers into three groups by the number of campaigns accepted
   - no response: TotalAccepted = 0
   - low response: TotalAccepted = 1
   - high response: TotalAccepted >= 2
2. A comparison table of the three groups
   - customer count, share (%)
   - mean Income, mean age, share (%) with children
   - mean total spending (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds)
   - main purchase channels (mean NumWebPurchases, NumCatalogPurchases, NumStorePurchases)
3. The top 20 high-response customers (TotalAccepted >= 2) sorted by total accepted, descending
4. Save the result to RESULT_FOLDER / 'campaign_response_profile.csv'
   - columns: TotalAccepted, response group, Income, Age, Education, total spending, the six campaign columns

Summarize the results.

**Step 7: Interpret and propose campaign strategies** - Synthesize the campaign effectiveness comparison and write the following.

1. A one-sentence performance summary of each campaign
   - acceptance rate level and which customer segment mainly responded
2. A two- or three-sentence profile of the responding customers
   - common characteristics of high-response customers
   - key differences from non-responding customers
3. Future campaign strategy proposals (three to five)
   - target selection criteria to raise the acceptance rate
   - an improvement direction for campaign 2 (the lowest acceptance rate)
   - ideas based on the high response to the last campaign (`Response`), stating the limits and the additional data needed rather than asserting causes or success factors from the data
   - an ambassador or referral program built on high-response customers

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
