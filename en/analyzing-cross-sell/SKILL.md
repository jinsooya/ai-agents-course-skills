---
name: analyzing-cross-sell
description: Analyze cross-sell opportunities in the Marketing Campaign customer data by combining product group correlations and co-purchase rates into cross-sell scores, then select cross-sell pairs and target customers. Use when the user asks for cross-sell analysis, product group combinations, bundle marketing, or co-purchase patterns.
---

# Cross-Sell Analysis

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. Basic statistics (mean, median, min, max) of the six product group columns (MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds)
3. The number and share of customers with zero spending in each product group (never purchased)
4. The mean and median of total spending (MntTotal = sum of the six)

Print the results as tidy tables and summarize the main characteristics in two or three sentences.

**Step 2: Purchase patterns by product group** - Analyze purchase patterns by product group.

1. Create a purchase flag column per product group (1 if spending > 0, else 0)
   - column names: BuyWines, BuyFruits, BuyMeat, BuyFish, BuySweet, BuyGold
2. Print the distribution of the number of product groups purchased per customer (0 to 6)
3. Print the top 5 most frequently purchased product group combinations (for example wine + meat, wine + gold)
4. Plot the purchase rate per product group as a horizontal bar chart (sorted from highest)

Explain the main characteristics of the purchase patterns together with the results.

**Step 3: Correlations between product groups** - Analyze the correlations between product groups.

1. The Pearson correlation matrix of spending on the six product groups
2. A correlation heatmap (seaborn heatmap, annot=True, palette YlOrRd)
3. The top 5 pairs by correlation (highest cross-sell potential first)
4. Co-purchase rate: the share of customers who purchased both product groups (> 0)
   - compute it for all 15 pairs of the six product groups
   - print the top 5 pairs by co-purchase rate

Explain the insights from a cross-sell perspective together with the results.

**Step 4: Discover cross-sell pairs** - Discover cross-sell opportunity pairs.

1. Cross-sell score
   - for each of the 15 pairs: cross-sell score = correlation × co-purchase rate
   - print the top 5 pairs by cross-sell score, descending (with correlation, co-purchase rate, and score)
2. Select the key cross-sell pairs: the top 3 by cross-sell score
   - draw a scatter plot for each pair (x: spending on product A, y: spending on product B)
   - arrange the three scatter plots as a 1×3 subplot grid
3. Identify cross-sell targets: customers who buy product A but not product B
   - print the target count and share for the highest-scoring pair

Explain the rationale for the cross-sell strategy together with the results.

**Step 5: Visualize cross-sell** - Build a combined visualization of cross-sell opportunities.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Correlation heatmap between product groups (annot=True)
2. (top right) Horizontal bar chart of the top 10 pairs by cross-sell score
3. (bottom left) Bar chart of the customer distribution by number of product groups purchased (0 to 6)
4. (bottom right) Bar chart of the mean number of product groups purchased by income group (check whether higher income buys more variety)

**Step 6: Select cross-sell target customers** - Select and profile the cross-sell target customers.

1. Based on the top pair by cross-sell score (for example wine → meat):
   - targets: customers in the top 50% of spending on product A with zero spending on product B
   - print the target count and its share of all customers
2. Print the target profile
   - mean Income, mean age (from Year_Birth, reference year 2014), share (%) with children
   - the main purchase channel (the largest of NumWebPurchases, NumCatalogPurchases, NumStorePurchases)
   - mean total spending (MntTotal)
3. Print the top 20 targets by total spending, descending
4. Save the result to RESULT_FOLDER / 'cross_sell_targets.csv'
   - columns: Income, age, total spending, spending on the six product groups, purchases per channel

Summarize the results.

**Step 7: Interpret and propose marketing strategies** - Synthesize the cross-sell analysis and write the following.

1. A summary of the key cross-sell pairs (one or two sentences for each of the top 3)
   - Why these two products are bought together
   - The characteristics of the target customers
2. A two- or three-sentence profile of the cross-sell target customers
3. Bundle marketing strategy proposals (three to five)
   - Each with a specific product combination, target customer, and execution channel
   - For example: e-mail a meat coupon to wine buyers, place the products next to each other in stores

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
