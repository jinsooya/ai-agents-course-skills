---
name: analyzing-rfm
description: Run an RFM (Recency, Frequency, Monetary) analysis on transaction-level or customer-level data, segment the customers, and rank high-potential prospects. Use when the user asks for RFM analysis, customer segmentation, high-potential customers (candidates for conversion to Champions), Champions/Loyal/At Risk segments, or customer value scores.
---

# RFM Analysis

Follow the seven steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path, encoding, and column names from the user's request. If a column is not named in the request, inspect the data before using it.

**Step 1: Explore the data** - Load the data and print:
- The number of rows and columns. In transaction-level data a row is a transaction; in customer-level data a row is a customer.
- The data type of each column
- Columns with missing values and their counts
- Basic statistics (mean, min, max) of the main numeric columns
- The number of unique customers if a customer id column exists, and the min and max order date if an order date column exists

**Step 2: Build the RFM variables** - Build R, F, and M per customer in one of two ways depending on the data unit.
- Transaction-level data (one row per transaction): aggregate by the customer id column.
  + R (Recency): days between each customer's last order date and the maximum order date in the data. Convert the order date column to datetime first.
  + F (Frequency): number of unique orders per customer
  + M (Monetary): total sales per customer
- Customer-level data (one row per customer): add R, F, and M from the column combinations named in the request. For example, F is the sum of purchase-count columns and M is the sum of spending columns by product group.
- In both cases build a dataframe `rfm_df` with the customer identifiers and R, F, M; print basic statistics (mean, median, min, max) of each variable; and plot the distributions of R, F, and M as three histogram subplots.

**Step 3: Score R, F, and M** - Split each of R, F, and M into quintiles and assign scores from 1 to 5.
- R_score: smaller Recency is better, so the smallest group gets 5 and the largest gets 1
- F_score and M_score: larger is better, so the largest group gets 5 and the smallest gets 1
- Ties can stop `pandas.qcut()` from producing five bins, so apply `pandas.qcut(..., q=5, labels=[...])` to the ranks from `rank(method='first')` rather than to the raw values. This always yields five bins, so the fixed labels 1 to 5 can be assigned. Do not use `duplicates='drop'`: fewer than five bins would break the score thresholds in the segment rules.
- Add R_score, F_score, M_score and `RFM_total = R_score + F_score + M_score`; print the customer count per score and the top ten customers by RFM_total.

**Step 4: Segment the customers** - Read `references/segments.md` and classify the customers with those rules. Apply the rules in the listed order and assign the first matching segment.
- Add a Segment column.
- Print the customer count and share per segment, and the mean R, F, M per segment.
- Plot the customer count per segment as a bar chart.

**Step 5: Visualize** - Build the four charts below as a 2×2 subplot grid.
1. (top left) Mean M per segment - horizontal bar chart sorted from highest to lowest
2. (top right) Scatter plot of R_score versus F_score - color by M_score, point size proportional to M
3. (bottom left) Distribution of RFM_total - histogram
4. (bottom right) Mean M or mean income by the auxiliary variable named in the request - horizontal bar chart. Use mean M when the auxiliary variable is Region, and mean income when it is Income.

**Step 6: Rank high-potential prospects** - Apply the prospect criteria and the priority score formula in `references/segments.md`.
- The number of prospects and their share of all customers
- Details of the top twenty prospects by priority (customer identifiers, R, F, M, scores, segment, and the auxiliary variables named in the request)
- A comparison table of the average prospect profile against the average of all customers
- A pie chart of the prospects' purchase category mix. For transaction-level data join back to the raw data and sum sales by category; for customer-level data sum the spending columns by product group. If the data lacks category information or spending columns by product group, skip the chart and print why.

**Step 7: Interpret and propose marketing strategies** - Citing the printed figures from the previous steps, write:
1. A one- or two-sentence profile of each segment
2. Three marketing strategies to convert Potential Loyalists into Champions, each with a name, target customers, execution method, and expected effect
3. Two strategies to reactivate At Risk customers
4. A three-line summary of the key insights

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill.
- Every quantitative claim (customer counts, shares, averages) must trace back to a value printed in this run. Do not state a number that was not printed.
