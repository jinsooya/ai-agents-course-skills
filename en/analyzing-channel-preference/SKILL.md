---
name: analyzing-channel-preference
description: Analyze purchase channel preference in the Marketing Campaign customer data: usage of the web, catalog, store, and deal channels, channel preference by customer characteristics, channel combination patterns, and high-value customers per channel. Use when the user asks for channel preference, purchase channel analysis, web conversion rate, multichannel customers, or channel optimization strategies.
---

# Channel Preference Analysis

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. Basic statistics (mean, median, min, max, standard deviation) of the five channel columns (NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth)
3. Whether the channel columns have missing values
4. The mean and median of total purchases (sum of the four channels)

Print the results as tidy tables and summarize the main characteristics in two or three sentences.

**Step 2: Purchase distribution by channel** - Analyze the purchase distribution by channel.

1. The mean number of purchases in the four channels (web, catalog, store, deals), sorted from highest
2. The share (%) of total purchases held by each channel, shown alongside
3. The share (%) of customers with zero purchases per channel (never used the channel)
4. Web conversion rate: NumWebPurchases / NumWebVisitsMonth (guard against division by zero)
   - Print the mean, median, and distribution of the conversion rate
5. A 2×2 subplot grid of histograms of purchase counts per channel

Explain the main characteristics of channel usage together with the results.

**Step 3: Channel preference by customer characteristics** - Analyze channel preference by customer characteristics.

Preprocessing:
- Compute Age from Year_Birth (reference year 2014)
- Bin Age into 39 and under, 40s (40-49), 50s (50-59), 60 and over (60+)
- TotalPurchases = NumWebPurchases + NumCatalogPurchases + NumStorePurchases + NumDealsPurchases
- PrimaryChannel: the channel used most among the four (ties go to the store channel)

Analysis items:
1. A table of mean purchases per channel by income group (25th-percentile cut points: Low / Mid-Low / Mid-High / High)
2. A table of mean purchases per channel by age group
3. Channel preference differences by whether the customer has children (Kidhome + Teenhome > 0)
4. The distribution of customers by primary channel (which channel is the primary channel for the most customers)

Print the results as tables and explain the key insights about channel preference differences by characteristic.

**Step 4: Channel combination patterns** - Analyze channel combination patterns.

1. The Pearson correlation matrix between channels (NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases)
2. A correlation heatmap (seaborn heatmap, annot=True, palette coolwarm)
3. The number of channels used (channels with purchases > 0 among the four) and its distribution
   - customer counts and shares from 0 channels (no purchases) to 4 channels (all channels)
4. The mean total purchases of multichannel customers (3 or more channels) compared with single-channel customers

Explain the insights about channel combination patterns together with the results.

**Step 5: Visualize channel preference** - Build a combined visualization of channel preference.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Horizontal bar chart of mean purchases by channel (sorted from highest, count shown at the end of each bar)
2. (top right) Pie chart of the purchase share by channel (percentage and channel name shown together)
3. (bottom left) Grouped bar chart of mean purchases by income group (Low / Mid-Low / Mid-High / High) × channel
4. (bottom right) Stacked bar chart of the primary channel distribution by age group (channel share within each age group)

**Step 6: Profile high-value customers per channel** - Profile the high-value customers of each channel.

1. For each channel (web, catalog, store, deals), classify the top 25% by purchases as that channel's high-value customers
2. A comparison table of the high-value customer profiles per channel
   - mean income, mean age, share (%) with children, most common education level
   - mean total purchases, mean total spending (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds)
3. A comparison focused on the differences between web high-value customers and store high-value customers
4. Save the result to RESULT_FOLDER / 'channel_highvalue_profile.csv'
   - columns: all channel purchase counts, Income, Age, Education, Marital_Status, total spending

Summarize the results.

**Step 7: Interpret and propose marketing strategies** - Synthesize the channel preference analysis and write the following.

1. Key characteristics of each channel (one or two sentences each)
   - Which customer segment mainly uses it
   - Its share of total purchases
   - Its strengths and weaknesses
2. Channel approach strategies by customer type (two or three types)
   - Recommended channel touchpoints by age, income, children, and other characteristics
3. Channel optimization strategy proposals (three to five)
   - Each with a specific target customer and channel combination
   - Include web conversion improvement, a multichannel strategy, and budget allocation by channel

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
