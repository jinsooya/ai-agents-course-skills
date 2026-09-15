---
name: predicting-campaign-response
description: Train a random forest classifier on the Marketing Campaign customer data with Response as the target to predict campaign response and select target customers. Use when the user asks for campaign response prediction, supervised classification, SMOTE class-imbalance handling, random forest, or target customer selection.
---

# Campaign Response Prediction (Classification)

Follow the 7 steps below in order. In every step, run the code with `python_execute`, show results with `print()`, and describe only what that output shows. Keep variables global so the next step can reuse them. Do not merge or skip steps.

Take the data file path and encoding from the user's request. The column names below are those of the dataset this skill assumes; if the request names different columns, follow the request.

## Interpretation premises

Interpret and describe the campaign columns (`AcceptedCmp1` to `AcceptedCmp5`, `Response`) only under the premises below.
- `AcceptedCmp1` to `AcceptedCmp5`: as documented, whether the customer accepted the offer in campaigns 1 to 5 (1/0).
- `Response`: as documented, whether the customer accepted the offer in the last campaign (1/0). Treat it as a **separate column** from the five earlier campaigns. It is the **prediction target** of this skill.
- Never treat `Response` and `AcceptedCmp5` as the **same event or the same column**; many customers differ between the two.
- State that the acceptance rate of each column is (customers with value 1) / (all customers), and do not speculate about schedules, offer contents, or reasons for success or failure.
- In tables and bar charts, **visually distinguish** the five numbered columns from `Response` with labels and colors.

## Procedure

**Step 1: Explore the data** - Load the data file and do the following.

[Variable interpretation, exactly as in the notebook's Step 1 note]
- AcceptedCmp1 to AcceptedCmp5: whether the offer was accepted in campaigns 1 to 5 (1/0).
- Response: whether the offer was accepted in the last campaign as documented (1/0). The prediction target of this skill. Do not treat it as the same event as `AcceptedCmp5`.

1. The number of rows (customers) and columns (variables)
2. The distribution of the target Response (accepted and declined counts and shares)
3. Columns with missing values and their counts
4. For each of AcceptedCmp1 to 5 and Response, tabulate (customers with value 1) / (all customers) and plot it as a bar chart. **Distinguish** `AcceptedCmp1` to `5` from `Response` in the bars, legend, and colors. Interpret only under the rules above and do not assert reasons for rate differences that the data does not contain.

**Step 2: Feature engineering and preprocessing** - Do the feature engineering and preprocessing for campaign response prediction.

1. Derived variables:
   - Age = 2026 - Year_Birth
   - TotalSpent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds
   - TotalPurchases = NumWebPurchases + NumCatalogPurchases + NumStorePurchases + NumDealsPurchases
   - TotalCampaigns = AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5
2. Preprocessing:
   - Replace the 24 missing Income values with the median
   - Label-encode or one-hot-encode Education and Marital_Status
   - Merge the Marital_Status anomalies ('YOLO', 'Absurd', 'Alone') into 'Other'
   - Drop Year_Birth outliers (before 1900)
3. Confirm the final feature list and the target (Response), then split into X and y.

**Step 3: Train/test split and class imbalance handling** - Split the data and handle the class imbalance.

1. Split into training (80%) and test (20%) with train_test_split (random_state=11, stratify=y)
2. Check the class distribution of the training data (Response=0 versus 1)
3. Oversample the training data with SMOTE to balance the classes (imbalanced-learn, random_state=11)
4. Print the class distribution before and after SMOTE.

Use sklearn.model_selection.train_test_split and imblearn.over_sampling.SMOTE.

**Step 4: Train the model** - Train a random forest classifier.

1. Train a RandomForestClassifier (n_estimators=100, random_state=11)
2. Train on the SMOTE-balanced training data
3. Predict on the test data
4. Print all of the following metrics:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - ROC-AUC Score

Use sklearn.ensemble.RandomForestClassifier and briefly explain what each metric means.

**Step 5: Visualize the model evaluation** - Visualize the model evaluation.

Build the four charts below as a 2×2 subplot grid.
1. (top left) Confusion matrix as a heatmap (true/false positives and negatives)
2. (top right) ROC curve with the AUC value shown on the chart
3. (bottom left) Top 15 feature importances as a horizontal bar chart
4. (bottom right) Predicted probability distribution: histograms of predicted probabilities for Response=0 versus 1

**Step 6: Select campaign target customers** - Use the model to select the targets for the next campaign.

1. Compute the campaign response probability (predict_proba) for all customers (training + test)
2. Select the top 20% by response probability as targets
3. Present the following:
   - the number of targets and their share of all customers
   - the share of actual responders (Response=1) among the targets (precision concept)
   - the share of all responders included in the targets (recall concept)
   - a comparison table of the average target profile (income, total spending, age) versus non-targets
4. Print details of the top 20 customers by response probability.

**Step 7: Interpret and propose marketing strategies** - Synthesize the campaign response prediction and write the following.

1. A model performance summary
   - assess the model's reliability from the key metrics (F1-Score, ROC-AUC)
2. Interpret the top 5 features driving campaign response
   - explain why each feature matters from a business perspective
3. Three campaign strategies for the target customers
   - each with a name, target customer characteristics, execution method, and expected effect
4. A three-line summary of the key insights

Cite actual figures from the data for every item.

## Output

- Follow the `plotting-charts` skill for every chart.
- After all steps, save the report according to the `writing-analysis-report` skill. Put the final step's interpretation and recommendations in the report's interpretation and recommendation sections.
- Every quantitative claim (customer counts, shares, averages, model metrics) must trace back to a value printed in this run. Do not state a number that was not printed.
