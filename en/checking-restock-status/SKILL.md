---
name: checking-restock-status
description: Check which Northwind products need restocking. Use when the user asks which products need restocking, which products are low on stock, or asks about inventory levels.
---

# Restock Check

**Step 1: Below reorder level** - List products where `UnitsInStock < ReorderLevel`
and `Discontinued = 0`. Include the product name, the supplier, the units in stock,
and the reorder level.

**Step 2: Demand** - For those products only, get the quantity sold in the 90
days up to the latest OrderDate in the database. Do not use today's date. A product that is low on stock but rarely sold
is not urgent.

**Step 3: Priority** - Rank the products by demand, not by how low the stock is.

## Output

A short table with product, supplier, units in stock, reorder level, and recent
demand, sorted by priority. Add one line naming the single most urgent product
and why.
