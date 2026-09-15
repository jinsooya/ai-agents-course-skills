---
name: analyzing-us-colleges
description: Analyze the US College data by comparing private and public colleges, analyze admission competitiveness, segment colleges with K-Means, predict graduation rate with RandomForest, and recommend strategies by college type. Use when the user asks for US college data analysis, private versus public comparison, acceptance rate analysis, graduation rate prediction, or college type classification.
---

# US College Data Analysis

Follow the 6 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Data loading premise

- The first column is the college name. Read it with `index_col=0` or keep it as a separate column; do not leave it as an unnamed column.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. Print the number of rows (colleges) and columns (variables).
2. Note that the first column is the college name (index); read it with index_col=0.
3. Print the data type and the number of missing values of each column.
4. Print descriptive statistics (mean, standard deviation, min, max) of the numeric variables.
5. Find and print the colleges whose Grad.Rate exceeds 100 (outliers).
6. Print the private/public distribution of the Private column (counts and shares).

Explain the results.

**Step 2: Compare private and public colleges** - Analyze the differences between private (Yes) and public (No) colleges.

1. Print a table comparing the private/public means of the following indicators:
   Outstate (tuition), Room.Board (room and board), Expend (instructional expenditure),
   Grad.Rate (graduation rate), S.F.Ratio (student-faculty ratio),
   PhD (share of faculty with a PhD), perc.alumni (alumni donation rate)
2. Visualize these four indicators as 2×2 box plots:
   Outstate, Grad.Rate, S.F.Ratio, perc.alumni
   (x-axis: Private, title: the indicator name)
3. Explain the three largest differences between private and public colleges.

**Step 3: Analyze admission competitiveness** - Analyze admission competitiveness.

1. Compute the acceptance rate (Accept/Apps) and the enrollment rate (Enroll/Accept) as new columns.
2. Print the 10 colleges with the highest and the 10 with the lowest acceptance rates (with names).
3. Compute the correlations between the acceptance rate and the following variables:
   Top10perc, Outstate, Expend, Grad.Rate, S.F.Ratio
4. Visualize 2×2 scatter plots with the acceptance rate on the y-axis:
   x-axis: Top10perc, Outstate, Expend, Grad.Rate
   point color: private (blue) / public (orange)
5. Interpret the admission competitiveness pattern.

**Step 4: Segment the colleges (K-Means)** - Classify the colleges into types with K-Means clustering.

1. Clustering features: Outstate, Room.Board, Expend, Grad.Rate,
   S.F.Ratio, PhD, perc.alumni, Top10perc
2. Standardize with StandardScaler.
3. Plot the elbow method chart to find the optimal k (2 to 8).
4. Run K-Means with k=4.
5. Visualize the clusters as a scatter plot after PCA (2 dimensions), colored by cluster.
6. Print a table of the mean of the main indicators per cluster.
7. Explain the characteristics of each cluster (for example elite private, large public).

**Step 5: Predict the graduation rate (RandomForest)** - Predict the graduation rate (Grad.Rate) with a RandomForest regression model.

1. Drop the outlier rows with Grad.Rate > 100.
2. Features: Apps, Accept, Enroll, Top10perc, Top25perc, F.Undergrad,
   Outstate, Room.Board, Books, Personal, PhD, Terminal,
   S.F.Ratio, perc.alumni, Expend
   Include Private encoded as 0/1.
3. Split into training and test data 8:2 (random_state=11).
4. Train a RandomForestRegressor (n_estimators=100, random_state=11).
5. Print the RMSE and R² score on the test set.
6. Plot the top 10 feature importances as a bar chart.
7. Draw a scatter plot of actual versus predicted values (with a diagonal reference line).
8. Interpret the factors with the largest effect on the graduation rate.

**Step 6: Recommend overall strategies** - Synthesize the analysis and write the following.

1. A summary of the findings:
   - two or three key differences between private and public colleges
   - the main factors affecting admission competitiveness
   - the characteristics of the four college types found with K-Means
   - the top 3 factors determining the graduation rate
2. Improvement strategies by college type (one or two per cluster):
   what should each cluster improve to raise its graduation rate or educational quality?
3. Two limitations of this analysis.
4. Write everything in the language of the request.

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
