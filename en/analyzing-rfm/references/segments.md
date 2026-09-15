# RFM Segment Rules and Prospect Criteria

## Segment classification rules

Apply the conditions in the listed order and assign the first segment that matches.

| Order | Segment | Condition |
|---|---|---|
| 1 | Champions | R_score >= 4 AND F_score >= 4 AND M_score >= 4 |
| 2 | Loyal Customers | F_score >= 4 AND M_score >= 4 |
| 3 | Potential Loyalist | R_score >= 4 AND F_score >= 2 AND M_score >= 2 |
| 4 | At Risk | R_score <= 2 AND F_score >= 3 AND M_score >= 3 |
| 5 | Hibernating | R_score <= 2 AND F_score <= 2 AND M_score <= 2 |
| 6 | Others | Every customer not matched above |

## High-potential prospect criteria

A customer is a prospect when either condition holds.

- Segment is 'Potential Loyalist' or 'Loyal Customers'
- RFM_total is 10 or higher and Segment is not 'Champions'

## Priority score

```
priority_score = R_score * 0.4 + F_score * 0.3 + M_score * 0.3
```

Recency carries the highest weight to focus on preventing churn. Rank prospects from the highest score down.
