---
name: generating-monthly-sales-report
description: Write a monthly Northwind sales report. Use when the user asks for a monthly sales report or a summary of one month of Northwind sales.
---

# Monthly Sales Report

Follow these steps in order. Run one query per step and keep each result small.

**Step 1: Total** - Get total revenue and order count for the month. Compute revenue as `UnitPrice * Quantity * (1 - Discount)`.
Filter with `strftime('%Y-%m', o.OrderDate) = '<YYYY-MM>'`.

**Step 2: Comparison** - Get the total revenue for the previous month with the same formula and compute the change as a percentage.

**Step 3: Categories** - Get revenue by category for the month, sorted high to low.
Report the top five and the share of total revenue for each.

**Step 4: Customers** - Get the top five customers by revenue for the month.
Include the company name and the country.


## Output

Write the report as Markdown with this structure.

```
# Northwind Monthly Sales Report - <YYYY-MM>

## Summary
One or two sentences: total revenue, order count, and change from the previous month.

## Revenue by Category
A table with category, revenue, and share.

## Top Customers
A table with company, country, and revenue.

## Notes
Any anomalies or exceptions that require further review.
```

Round every amount to two decimals and use thousands separators.
Never state a number that did not come from a query result.
