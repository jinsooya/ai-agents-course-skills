# RFM 세그먼트 규칙과 잠재 우수고객 기준

## 세그먼트 분류 규칙

아래 조건을 제시된 순서대로 적용하고, 먼저 일치하는 세그먼트를 부여합니다.

| 순서 | 세그먼트 | 조건 |
|---|---|---|
| 1 | Champions | R_score >= 4 AND F_score >= 4 AND M_score >= 4 |
| 2 | Loyal Customers | F_score >= 4 AND M_score >= 4 |
| 3 | Potential Loyalist | R_score >= 4 AND F_score >= 2 AND M_score >= 2 |
| 4 | At Risk | R_score <= 2 AND F_score >= 3 AND M_score >= 3 |
| 5 | Hibernating | R_score <= 2 AND F_score <= 2 AND M_score <= 2 |
| 6 | Others | 위 조건에 해당하지 않는 나머지 고객 |

## 잠재 우수고객 선정 기준

다음 중 하나를 만족하는 고객을 잠재 우수고객으로 선정합니다.

- Segment가 'Potential Loyalist' 또는 'Loyal Customers'인 고객
- RFM_total이 10 이상이면서 Segment가 'Champions'가 아닌 고객

## 우선순위 점수

```
priority_score = R_score * 0.4 + F_score * 0.3 + M_score * 0.3
```

최근 구매에 더 높은 가중치를 부여하여 이탈 방지에 중점을 둡니다. 점수가 높은 고객부터 우선순위를 부여합니다.
