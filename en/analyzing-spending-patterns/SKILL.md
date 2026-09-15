---
name: analyzing-spending-patterns
description: Analyze spending patterns in the Marketing Campaign customer data, covering spending distribution by product group, spending by customer characteristics, correlations between product groups, and a profile of high spenders. Use when the user asks for spending pattern analysis, spending by product group, high spenders, or spending comparisons by income, age, or education.
---

# Spending Pattern Analysis

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. Basic statistics (mean, median, min, max, standard deviation) of the six spending columns (MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds)
3. Whether the six spending columns have missing values
4. The mean and median of total spending (sum of the six columns)

Print the results as tidy tables and summarize the main characteristics in two or three sentences.

**Step 2: Spending distribution by product group** - Analyze the spending distribution by product group.

1. The mean spending of the six product groups (wine, fruit, meat, fish, sweets, gold products), sorted from highest to lowest
2. The share (%) of total spending held by each product group, shown alongside
3. The share (%) of customers with zero spending per product group (zero spending = non-buyers)
4. Visualize the spending distribution
   - A 2×3 subplot grid of histograms per product group (each subplot titled with the product group name)
   - x-axis: spending, y-axis: number of customers

Explain the main characteristics of the spending patterns together with the results.

**Step 3: Spending patterns by customer characteristics** - Analyze spending patterns by customer characteristics.

Preprocessing:
- Compute Age from Year_Birth (reference year 2014)
- Bin Age into 20s (20-29), 30s (30-39), 40s (40-49), 50s (50-59), 60 and over (60+)
- Create a total spending column (MntTotal) as the sum of the six product groups

Analysis items:
1. Mean total spending by income group (four groups at the 25th-percentile cut points: Low / Mid-Low / Mid-High / High)
2. Mean total spending by age group
3. Mean total spending by education level (Education column)
4. Mean total spending by whether the customer has children (Kidhome + Teenhome > 0)

Print the results as tables and explain the key insights about spending differences by characteristic.

**Step 4: Spending pattern correlations** - Analyze the correlations between spending patterns.

1. The Pearson correlation matrix of the six product group columns
2. A correlation heatmap (seaborn heatmap, annot=True, palette coolwarm)
3. Product group pairs with a correlation of 0.5 or higher, sorted from highest (pairs with cross-sell potential)
4. One scatter plot for the most correlated pair (x-axis: spending on one product group, y-axis: spending on the other)

Explain the insights from a cross-sell perspective together with the results.

**Step 5: Visualize spending patterns** - Build a combined visualization of the spending patterns.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Horizontal bar chart of mean spending by product group (sorted from highest, amount shown at the end of each bar)
2. (top right) Pie chart of the spending share by product group (percentage and product group name shown together)
3. (bottom left) Stacked bar chart of mean spending by income group (Low / Mid-Low / Mid-High / High) × product group
4. (bottom right) Box plot of total spending by age group

**Step 6: Profile high spenders** - Profile the high spenders.

1. Classify the top 20% by total spending (MntTotal) as high spenders (HighSpender=True)
2. A comparison table of high spenders versus other customers
   - mean income, mean age, share (%) with children, most common education level
   - mean spending on each of the six product groups
3. The ranking of product groups preferred by high spenders (1st to 6th)
4. The top 20 high spenders sorted by total spending, descending
   - columns: Income, Age, Education, Marital_Status, MntTotal, the six product groups
5. Save the full list of high spenders to RESULT_FOLDER / 'high_spender_profile.csv'

Summarize the results.

**Step 7: Interpret and propose marketing strategies** - Synthesize the spending pattern analysis and write the following.

1. Key characteristics of each product group (one or two sentences each)
   - Which customer segment mainly buys it
   - Its share of total spending
   - Its cross-sell potential
2. Spending patterns by customer type (two or three types)
   - The customer types with the most distinctive spending patterns and their characteristics
3. Marketing strategy proposals (three to five)
   - Each with a specific target customer and product group combination

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
