---
name: reviewing-monthly-kiosk-sales
description: Write the monthly review of the Reel Corner kiosk rental data. Use when the user asks for a monthly review, a monthly business report, or how last month went.
---

# Monthly Review

**Step 1: Month** - Use the month the user names. Otherwise use the last complete
calendar month before today's date.

**Step 2: Overview** - Get total revenue (`SUM` of `payment.amount`) and the number of
rentals (`COUNT DISTINCT payment.rental_id`) for the month and for the month before.
Compute the month-over-month change in percent with the `eval` tool.
Also count the days that have payments in each month (`COUNT DISTINCT date(payment_date)`).
If the two months have different numbers of days with data, say so next to the change,
because the change then reflects data coverage as well as demand.

**Step 3: Breakdowns** - Get revenue by film language, revenue by category, and the
top 5 actors by revenue for the month, each sorted high to low.

**Step 4: Chart** - Call `render_bar_chart` with the revenue by language and save it
as `/output/revenue-by-language-<YYYY-MM>.png`.

## Output

Write `/output/monthly-review-<YYYY-MM>.md` in the language of the user's request with
these sections in order: Overview, Revenue by Language, Revenue by Category,
Top Actors, So what. Keep these section headings in English exactly as written, even
when the rest of the report is in another language. Amounts are in USD with two
decimals and thousands separators.
Embed the chart with a Markdown image link. Under Top Actors, state that actor
revenues overlap and must not be added up. The So what section has two or three
bullets a manager can act on.
