---
name: detecting-outliers
description: Detect missing values, categorical anomalies, and numeric outliers (IQR, Z-score) in the Marketing Campaign customer data, save a cleaned dataset, and write a preprocessing checklist. Use when the user asks for outlier detection, missing value handling, data cleaning, data quality checks, or a preprocessing guide.
---

# Outlier Detection and Data Cleaning

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following.

1. The number of rows (customers) and columns (variables)
2. The data type of each column
3. Basic statistics (mean, median, min, max) of all numeric columns
4. The columns with missing values and their counts

Print the results as tidy tables and point out the columns suspected of containing outliers.

**Step 2: Detect missing values** - Detect missing values and compare handling methods.

1. Find every column with missing values and print the count and share (%)
2. Compare three methods for the 24 missing Income values
   - method 1: drop the rows -> check the change in data size
   - method 2: replace with the mean -> compare the mean before and after
   - method 3: replace with the median -> compare the median before and after
3. Plot the Income distribution as a histogram (after dropping missing values)
4. Recommend the most appropriate method with reasons.

Explain the results.

**Step 3: Detect categorical anomalies** - Detect anomalies in the categorical columns.

1. Print the unique values and frequencies of all categorical (object) columns
   - columns: Marital_Status, Education, Country
2. Detect the Marital_Status anomalies
   - normal values: Single, Married, Together, Divorced, Widow
   - anomalies: YOLO, Absurd, Alone → count each
3. Compare handling methods
   - method 1: drop the rows
   - method 2: replace with the closest normal value (Alone -> Single, YOLO/Absurd -> drop)
4. Plot the frequency of Marital_Status values as a bar chart with the anomalies highlighted

Infer the likely cause of each anomaly and explain the handling method.

**Step 4: Detect numeric outliers** - Detect numeric outliers.

1. Income outliers
   - IQR method: values below Q1 - 1.5×IQR or above Q3 + 1.5×IQR
   - Z-score method: values with |z| > 3
   - print the number of outliers found by each method and the Income values
   - check where the value 666,666 falls
2. Year_Birth outliers
   - detect birth years before 1900 (unrealistic ages) → print how many and which years
   - check customers aged 90 or older as of 2014
3. Outliers in the spending columns (MntWines, MntMeatProducts)
   - count the outliers in each column with the IQR method
4. Box plots of Income and Year_Birth (with outliers shown as points)

Explain the characteristics of the outliers found.

**Step 5: Visualize the outliers** - Build a combined visualization of the outliers.

Build the four charts below as a 2×2 subplot grid.

1. (top left) Income box plot plus strip plot (outliers as points, the 666,666 value marked with an arrow)
2. (top right) Year_Birth histogram (outliers before 1900 highlighted in red)
3. (bottom left) Scatter plot of Income versus MntTotal (Income outliers highlighted in red)
4. (bottom right) Marital_Status frequency bar chart (the anomalies YOLO / Absurd / Alone in a different color)

**Step 6: Clean the data** - Handle the outliers and build a cleaned dataset.

Proceed in this order.

1. Missing values: Income -> replace with the median
2. Categorical anomalies:
   - Marital_Status: Alone -> Single; YOLO, Absurd -> drop the rows
3. Numeric outliers:
   - Year_Birth: birth years before 1900 -> drop the rows
   - Income: above 600,000 -> drop the rows
4. Print a before/after comparison table
   - row count, Income mean/median, minimum Year_Birth, the list of Marital_Status values
5. Save the cleaned data to RESULT_FOLDER / 'marketing_data_clean.csv'

Explain how many rows each step removed or replaced.

**Step 7: Interpret and write the preprocessing guide** - Synthesize the outlier detection and handling and write the following.

1. A summary of the outliers found (one or two sentences per type)
   - missing values: where, how many, and why they may have arisen
   - categorical anomalies: which values appeared and how they were handled
   - numeric outliers: which values appeared and how they were handled
2. A summary of the change in data quality before and after cleaning
   - change in data size, change in key statistics
3. A practical preprocessing checklist (five to seven items)
   - the items to check whenever new data arrives
   - each with a concrete way to check it

Write the result in Markdown (##, ### headers, tables, bullet lists).

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
