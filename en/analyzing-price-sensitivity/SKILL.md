---
name: analyzing-price-sensitivity
description: Analyze price sensitivity in the Marketing Campaign customer data by computing the deal purchase ratio (DealRatio), classifying customers into Low, Medium, and High sensitivity segments, and relating sensitivity to customer characteristics and promotion strategies. Use when the user asks for price sensitivity, deal purchase ratio, discount-dependent customers, or promotion strategies.
---

# Price Sensitivity Analysis

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. Basic statistics (mean, median, min, max) of the four channel columns (NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases)
3. The distribution of NumDealsPurchases: customer counts and shares for 0, 1-2, 3-5, and 6 or more
4. The number of missing values in the Income column

Print the results as tidy tables and summarize the main characteristics in two or three sentences.

**Step 2: Compute the deal purchase ratio** - Compute the deal purchase ratio.

1. TotalPurchases = NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases
2. DealRatio = NumDealsPurchases / TotalPurchases
   - Set DealRatio = 0 when TotalPurchases is 0
3. Print basic statistics of DealRatio (mean, median, standard deviation, min, max)
4. Plot the DealRatio distribution as a histogram (x-axis: deal purchase ratio, y-axis: number of customers, 20 bins)
5. Customer counts by band: 0%, 1-20%, 21-40%, 41-60%, 61-80%, 81-100%

Explain the characteristics of the DealRatio distribution together with the results.

**Step 3: Classify price sensitivity segments** - Classify the price sensitivity segments.

1. Split DealRatio into three segments at the 33.3% and 66.7% quantiles
   - PriceSensitivity: Low (bottom third) / Medium (middle third) / High (top third)
2. Print the customer count and share per segment
3. Print basic statistics per segment
   - mean DealRatio, mean TotalPurchases, mean Income, mean total spending (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds)
4. Plot the customer count per segment as a bar chart

Explain the characteristics of the segmentation together with the results.

**Step 4: Price sensitivity by customer characteristics** - Analyze price sensitivity by customer characteristics.

Preprocessing:
- Compute Age from Year_Birth (reference year 2014)
- Bin Age into 39 and under, 40s (40-49), 50s (50-59), 60 and over (60+)
- Replace missing Income with the median

Analysis items:
1. Mean DealRatio by income group (25th-percentile cut points: Low / Mid-Low / Mid-High / High)
   - Check whether lower income means a higher DealRatio
2. Mean DealRatio by age group
3. Mean DealRatio by education level
4. Mean DealRatio by whether the customer has children (Kidhome + Teenhome > 0)
5. A scatter plot of Income versus DealRatio (x: Income, y: DealRatio, color: PriceSensitivity segment)

Print the results as tables and explain the insights about the relation between price sensitivity and customer characteristics.

**Step 5: Visualize price sensitivity** - Build a combined visualization of price sensitivity.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Bar chart of mean DealRatio by income group (value shown above each bar)
2. (top right) Bar chart comparing mean total spending by price sensitivity segment
3. (bottom left) Stacked bar chart of the price sensitivity segment distribution by age group (share within each age group)
4. (bottom right) Horizontal bar chart of mean DealRatio by education level (sorted from highest)

**Step 6: Profile price-sensitive customers** - Profile the price-sensitive customers.

1. A comparison table of the High versus Low segments
   - mean income, mean age, share (%) with children, most common education level
   - mean total purchases, mean total spending
   - mean spending on each of the six product groups
   - mean purchases per channel (web / catalog / store)
2. The ranking of product groups for High (price-sensitive) customers (which product groups attract the most deal purchases)
3. Save the result to RESULT_FOLDER / 'price_sensitivity_profile.csv'
   - columns: PriceSensitivity, DealRatio, TotalPurchases, Income, Age, Education, Marital_Status, total spending, the six product groups

Summarize the results.

**Step 7: Interpret and propose marketing strategies** - Synthesize the price sensitivity analysis and write the following.

1. Key characteristics of each segment (one or two sentences each)
   - High (price-sensitive): who they are and how to approach them
   - Medium: characteristics and management direction
   - Low (price-insensitive): who they are and how to leverage them
2. A two- or three-sentence summary of the relation between price sensitivity, income, and age
3. Promotion strategy proposals (three to five)
   - High segment: strategies that keep purchases while reducing discount dependence
   - Low segment: premium strategies that raise margins
   - Each with a specific target customer and execution plan

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
