---
name: predicting-spending-from-demographics
description: Train a random forest regression model on the Marketing Campaign customer data to predict total spending (MntTotal) from demographic variables and predict spending for new customers. Use when the user asks for spending prediction, regression analysis, demographic-based prediction, or early identification of potential high-value customers.
---

# Demographic-Based Spending Prediction (Regression)

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. Basic statistics and unique values of the demographic columns (Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome)
   - numeric: mean, median, min, max
   - categorical: the list of unique values and their frequencies
3. Basic statistics of MntTotal, the sum of the six spending columns (MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds)
4. The number of missing Income values and the Marital_Status anomalies (YOLO, Absurd, Alone)

Print the results as tidy tables and summarize the notable characteristics of the data.

**Step 2: Feature engineering** - Engineer the features for the regression model.

1. Target: MntTotal = the sum of spending on the six product groups
2. Age = 2014 - Year_Birth
3. Outlier removal:
   - drop rows with Age > 80 (unrealistic birth years)
   - drop rows with Income > 200000 (extreme outliers)
4. Missing values: replace missing Income with the median
5. Categorical cleanup:
   - Marital_Status: merge Alone, YOLO, Absurd into Single
   - Education: map Basic -> 기초, Graduation -> 학사, Master -> 석사, PhD -> 박사, 2n Cycle -> 학사
6. One-hot encoding: Education, Marital_Status (drop_first=True)
7. Print the final feature list and the data size

Print the data size and the feature list after preprocessing.

**Step 3: Exploratory analysis** - Explore the relation between the features and total spending (MntTotal).

1. Scatter plot of Income versus MntTotal (color: Education)
2. Scatter plot of Age versus MntTotal
3. Box plot of MntTotal by number of children (Kidhome + Teenhome)
4. Pearson correlations between the numeric features (Income, Age, Kidhome, Teenhome) and MntTotal

Arrange the four charts as a 2×2 subplot grid and explain the insights from each relation.

**Step 4: Train the regression model** - Train and evaluate a RandomForest regression model.

1. Split into 80% training and 20% test (random_state=11)
2. Train a RandomForestRegressor (n_estimators=100, random_state=11)
3. Print the performance metrics
   - R² (coefficient of determination): training set / test set
   - MAE (mean absolute error): test set
   - RMSE (root mean squared error): test set
4. Print the top 10 feature importances in descending order
5. Plot the top 10 feature importances as a horizontal bar chart

Explain the model performance and the important variables.

**Step 5: Visualize the model performance** - Visualize the model performance.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Scatter plot of actual versus predicted values (x: actual MntTotal, y: predicted MntTotal, with a diagonal reference line)
2. (top right) Histogram of the residuals (residual = actual - predicted), to check closeness to a normal distribution
3. (bottom left) Horizontal bar chart of the top 10 feature importances
4. (bottom right) Bar chart comparing mean actual and predicted spending by income group

**Step 6: Predict spending and apply the model** - Use the trained model to predict spending.

1. Predict the expected spending of three hypothetical new customers
   - Customer A: Income=80000, Age=45, Education=박사, Marital_Status=Married, Kidhome=0, Teenhome=1
   - Customer B: Income=30000, Age=35, Education=학사, Marital_Status=Single, Kidhome=1, Teenhome=0
   - Customer C: Income=55000, Age=55, Education=석사, Marital_Status=Married, Kidhome=0, Teenhome=0
   - print the three predictions as a table
2. Classify the top 20% by predicted spending in the test set as potential high-value customers
   - print their mean Income, mean Age, and most common Education
3. Save the result to RESULT_FOLDER / 'predicted_spending.csv'
   - columns: Income, Age, Education, Marital_Status, Kidhome, Teenhome, MntTotal_실제, MntTotal_예측

Summarize the results.

**Step 7: Interpret and propose marketing strategies** - Synthesize the demographic-based spending prediction and write the following.

1. A summary of the key insights (three or four sentences)
   - the demographic variables that matter most for predicting spending
   - the relation of income, age, and number of children to spending
   - what the model performance (R²) means and its limits
2. Spending characteristics by demographic type (two or three types)
   - the demographic profile and the expected spending pattern of each type
3. Marketing application strategies (three to five)
   - new customer onboarding: predict expected spending from demographics to identify VIP candidates early
   - target marketing: allocate marketing budget by predicted spending
   - each with a concrete execution plan

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
