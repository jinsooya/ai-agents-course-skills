---
name: estimating-clv
description: Estimate customer lifetime value (CLV) from Superstore transaction data, assign Platinum, Gold, Silver, and Bronze tiers, and profile high-value customers. Use when the user asks for CLV estimation, customer lifetime value, customer tiering, Pareto analysis, or retention strategies for high-value customers.
---

# Customer Lifetime Value (CLV) Estimation

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following. (Take the encoding from the request.)
1. The number of rows (transactions) and columns (variables)
2. The number of unique customers (by Customer ID)
3. The order period (min and max of Order Date)
4. The average number of transactions and the average total purchase amount per customer
5. Basic statistics of the Sales column (mean, median, min, max)

**Step 2: Aggregate purchase history per customer** - Aggregate each customer's purchase history for the CLV calculation.

Compute the following by Customer ID.
1. Basic aggregates:
   - first_order: first order date (min of Order Date)
   - last_order: last order date (max of Order Date)
   - total_orders: number of unique orders (nunique of Order ID)
   - total_sales: total purchase amount (sum of Sales)
2. Convert Order Date to datetime before computing.
3. Include Customer Name and Segment in the result.
4. Print the first five rows and basic statistics of the result.

**Step 3: Compute CLV** - Compute the CLV components and the final CLV.

1. CLV components:
   - lifespan_days: last_order - first_order (in days)
   - lifespan_years: lifespan_days / 365 (floor at 1 year)
   - aov: total_sales / total_orders (average order value)
   - purchase_freq: total_orders / lifespan_years (purchases per year)
2. CLV:
   - clv = aov × purchase_freq × lifespan_years
3. Customer tiers by CLV:
   - Platinum: top 10%
   - Gold: top 10% to 30%
   - Silver: top 30% to 60%
   - Bronze: bottom 40%
4. Print a table with the customer count, mean CLV, and mean total_sales per tier.

**Step 4: Analyze the CLV distribution** - Analyze the distribution of CLV.

1. Basic statistics of CLV (mean, median, standard deviation, min, max)
2. Pareto analysis:
   - The share of total CLV held by the top 20% of customers
3. Total CLV contribution by tier (pie chart)
4. Mean CLV by Segment (Consumer / Corporate / Home Office) (bar chart)

**Step 5: Visualize CLV** - Visualize the CLV analysis.

Build the four charts below as a 2×2 subplot grid.
1. (top left) CLV distribution histogram, colored by tier
2. (top right) Scatter plot of AOV versus purchases per year, colored by tier, point size proportional to CLV
3. (bottom left) Distribution of customer lifespan (lifespan_years) as a histogram
4. (bottom right) Mean AOV and mean purchases per year by tier as a grouped bar chart

**Step 6: Profile high-value customers** - Profile the Platinum-tier customers.

1. The number of Platinum customers and their share of all customers
2. A comparison table of Platinum versus the overall average:
   - mean CLV, mean AOV, mean purchases per year, mean lifespan
3. The Segment distribution of Platinum customers (pie chart)
4. The Region distribution of Platinum customers (bar chart)
5. Details of the top 20 customers by CLV (Customer Name, Segment, Region, CLV, tier)

**Step 7: Interpret and propose marketing strategies** - Synthesize the CLV analysis and write the following.

1. A one- or two-sentence profile of each tier (Platinum / Gold / Silver / Bronze)
2. Two strategies to retain Platinum customers, each with a name, target customers, execution method, and expected effect
3. Two strategies to move Bronze customers up to Silver, focused on preventing churn and increasing purchase frequency
4. A marketing budget allocation proposal from the Pareto perspective, with the recommended investment share per tier and its rationale
5. A three-line summary of the key insights

Cite actual figures from the data for every item.

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
