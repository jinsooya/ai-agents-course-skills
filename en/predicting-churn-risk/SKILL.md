---
name: predicting-churn-risk
description: Build churn labels from Superstore transaction data, train a random forest classifier to predict churn risk, and propose retention strategies by risk tier. Use when the user asks for churn prediction, at-risk customers, churn, retention strategies, or training a classification model.
---

# Churn Risk Prediction (Classification)

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Procedure

**Step 1: Explore the data** - Load the data file and analyze the following. (Take the encoding from the request.)
1. The number of rows (transactions) and columns (variables)
2. The number of unique customers (by Customer ID)
3. The order period (min and max of Order Date)
4. The distribution of each customer's last purchase date as a histogram of days elapsed from the reference date (the maximum order date)
5. The distribution of customers by Segment (bar chart)

**Step 2: Build churn labels and engineer features** - Build the churn labels and engineer the features.

1. Reference date: the maximum Order Date in the dataset
2. Churn label:
   - compute each customer's last purchase date
   - recency_days = reference date - last purchase date (in days)
   - Churned = 1 (recency_days > 180, no purchase for six months or more), 0 (active)
3. Features (aggregated by Customer ID):
   - total_orders: number of unique orders
   - total_sales: total purchase amount
   - avg_order_value: total_sales / total_orders
   - lifespan_days: days from the first order to the last order
   - pct_furniture: share of Furniture purchases (by Sales)
   - pct_office_supplies: share of Office Supplies
   - pct_technology: share of Technology
   - segment_encoded: Segment label-encoded

4. Print the number and share of churned and active customers.

**Step 3: Train/test split and class imbalance handling** - Split the data and handle the class imbalance.

1. Separate the features (X) and the target (y = Churned)
2. Split into training (80%) and test (20%) with train_test_split (random_state=11, stratify=y)
3. Check the class distribution of the training data (churned versus active)
4. Oversample the training data with SMOTE (random_state=11)
5. Print the class distribution before and after SMOTE.

**Step 4: Train the model** - Predict churn with a random forest classifier.

1. Train a RandomForestClassifier (n_estimators=100, random_state=11)
2. Train on the SMOTE-balanced training data
3. Predict on the test data
4. Print all of the following metrics:
   - Accuracy, Precision, Recall, F1-Score, ROC-AUC Score
5. Explain why Recall matters most in churn prediction (compare the cost of missing a churner with the cost of flagging an active customer as a churner).

**Step 5: Visualize the model evaluation** - Visualize the model evaluation.

Build the four charts below as a 2×2 subplot grid.
1. (top left) Confusion matrix as a heatmap
2. (top right) ROC curve with the AUC value shown
3. (bottom left) Top 10 feature importances as a horizontal bar chart
4. (bottom right) Recency distribution of churned versus active customers as overlaid histograms

**Step 6: Select at-risk customers** - Select the at-risk customers and rank them.

1. Compute the churn probability (predict_proba) for all customers
2. Churn risk tiers:
   - High Risk: churn probability ≥ 0.7
   - Medium Risk: churn probability 0.4 to 0.7
   - Low Risk: churn probability < 0.4
3. Print a table with the customer count, share, and mean churn probability per tier
4. Print details of the top 20 High Risk customers (Customer Name, Segment, Region, recency_days, total_sales, churn probability)
5. Summarize the Segment distribution and the average purchase characteristics of High Risk customers.

**Step 7: Interpret and propose retention strategies** - Synthesize the churn risk prediction and write the following.

1. A model performance summary
   - assess the model's reliability with a focus on Recall and ROC-AUC
2. Interpret the top 3 features driving churn
   - explain how each feature relates to churn from a business perspective
3. Three retention strategies for High Risk customers
   - each with a name, target customer characteristics, execution method, and expected effect
   - grounded in the actual characteristics of High Risk customers (recency, total_sales, and so on)
4. Two preventive strategies for Medium Risk customers
5. A three-line summary of the key insights

Cite actual figures from the data for every item.

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
