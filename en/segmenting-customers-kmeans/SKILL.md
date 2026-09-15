---
name: segmenting-customers-kmeans
description: Segment customers in the Marketing Campaign data with K-Means clustering on standardized spending, channel, income, and Recency features, then name each cluster and derive marketing strategies. Use when the user asks for customer segmentation, K-Means clustering, unsupervised learning, cluster profiling, or the optimal number of clusters (elbow, silhouette).
---

# K-Means Customer Segmentation

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.
1. The number of rows (customers) and columns (variables)
2. Basic statistics of the main clustering columns (six spending columns, four purchase channels, Income, Recency)
3. Columns with missing values and their counts
4. The distribution of Income (histogram)

**Step 2: Select and preprocess features** - Select and preprocess the features for clustering.

1. Select these 12 features.
   - spending: MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds
   - purchase channels: NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumDealsPurchases
   - customer attributes: Income, Recency

2. Preprocessing:
   - replace the 24 missing Income values with the median
   - standardize with StandardScaler (mean 0, standard deviation 1)

3. After preprocessing, print the mean and standard deviation of each feature.

**Step 3: Determine the optimal number of clusters** - Determine the optimal number of clusters (K).

1. Run K-Means for K from 2 to 10
2. Compute the inertia (WCSS) and the silhouette score for each K
3. Visualize the results as two subplots:
   - (left) inertia by K, the elbow method (the bend marks the optimal K)
   - (right) silhouette score by K (higher is better)
4. Recommend the optimal K and explain why.

Use sklearn.cluster.KMeans and sklearn.metrics.silhouette_score with random_state=11 for reproducibility.

**Step 4: Run K-Means clustering** - Run K-Means clustering with the optimal K chosen above.

1. Run K-Means with the optimal K (random_state=11)
2. Add a Cluster column (integers starting at 0) to the original dataframe
3. Present the customer count and share per cluster as a table
4. Present the mean of each feature per cluster on the original scale (before standardization, for easier interpretation)

**Step 5: Visualize the clusters** - Visualize the clustering result.

Build the four charts below as a 2×2 subplot grid.
1. (top left) Mean total spending per cluster (sum of the six spending categories) as a horizontal bar chart
2. (top right) Scatter plot after reducing to two dimensions with PCA, colored by cluster
3. (bottom left) Mean Income per cluster as a horizontal bar chart
4. (bottom right) Purchase channel mix per cluster as a stacked horizontal bar chart

**Step 6: Profile the clusters** - Analyze each cluster and give it a customer type name.

1. Compute the following per cluster.
   - mean total spending (sum of the six categories), Income, Recency
   - preferred purchase channel (the highest of the four channels)
   - campaign acceptance rate (sum of AcceptedCmp1 to 5 and Response / 6)
2. Based on the analysis, name each cluster's customer type. For example: 'high-income loyal customers', 'price-sensitive customers', 'new or potential customers'.
3. Add the cluster type names as a Cluster_Name column.
4. Print a summary table of cluster characteristics.

**Step 7: Interpret and propose marketing strategies** - Synthesize the customer segmentation and write the following.

1. A one- or two-sentence profile of each cluster, covering spending level, income, preferred channel, and campaign response
2. Marketing strategies tailored to each cluster (two per cluster), each with a name, target customers, execution method, and expected effect
3. The cluster that deserves the most attention from a business priority perspective, and why
4. A three-line summary of the key insights

Cite actual figures from the data for every item.

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
