---
name: predicting-churn-risk
description: Superstore 거래 데이터로 이탈 레이블을 만들고 랜덤 포레스트 분류 모델로 고객 이탈 위험을 예측하여 위험 등급별 리텐션 전략을 제안합니다. 사용자가 이탈 예측, 이탈 위험 고객, churn, 리텐션 전략, 분류 모델 학습을 요청할 때 사용합니다.
---

# 고객 이탈 위험 예측 (분류)

아래 7단계를 순서대로 수행합니다. 단계마다 `python_execute`로 코드를 실행하고 결과를 `print()`로 출력한 뒤, 그 출력에 근거해서만 설명합니다. 변수는 다음 단계에서 재사용할 수 있도록 전역 변수로 저장합니다. 단계를 통합하거나 생략하지 않습니다.

데이터 파일 경로와 인코딩은 사용자의 요청에 명시된 것을 따릅니다. 아래 컬럼 이름은 이 스킬이 전제하는 데이터셋의 컬럼이며, 요청에 다른 이름이 명시되면 그것을 따릅니다.

## 절차

**1단계: 데이터 탐색** - 데이터 파일을 읽어서 다음 항목을 분석하세요. (인코딩은 요청을 따릅니다)
1. 전체 행(거래 건수)과 열(변수 수) 개수
2. 고유 고객 수 (Customer ID 기준)
3. 주문 기간 범위 (Order Date 최솟값, 최댓값)
4. 고객별 마지막 구매일 분포 — 기준일(최대 주문일)로부터 경과일 히스토그램
5. Segment별 고객 수 분포 (막대그래프)

**2단계: 이탈 레이블 생성 및 피처 엔지니어링** - 이탈 레이블 생성과 피처 엔지니어링을 수행해 주시기 바랍니다.

1. 기준일 설정: 데이터셋 내 최대 Order Date
2. 이탈 레이블 생성:
   - 고객별 마지막 구매일 계산
   - recency_days = 기준일 - 마지막 구매일 (일수)
   - Churned = 1 (recency_days > 180, 6개월 이상 미구매), 0 (활성)
3. 피처 생성 (Customer ID 기준 집계):
   - total_orders: 고유 주문 건수
   - total_sales: 총 구매금액
   - avg_order_value: total_sales / total_orders
   - lifespan_days: 첫 주문일 ~ 마지막 주문일 기간
   - pct_furniture: Furniture 카테고리 구매 비중 (Sales 기준)
   - pct_office_supplies: Office Supplies 비중
   - pct_technology: Technology 비중
   - segment_encoded: Segment를 Label Encoding

4. 이탈 고객 수와 활성 고객 수 및 비율을 출력하세요.

**3단계: 학습/테스트 분리 및 클래스 불균형 처리** - 학습/테스트 데이터 분리와 클래스 불균형 처리를 수행해 주시기 바랍니다.

1. 피처(X)와 타겟(y=Churned) 분리
2. train_test_split으로 학습(80%) / 테스트(20%) 분리
   (random_state=11, stratify=y)
3. 학습 데이터의 클래스 분포 확인 (이탈 vs 활성 비율)
4. SMOTE로 학습 데이터 오버샘플링 (random_state=11)
5. SMOTE 적용 전후 클래스 분포를 비교하여 출력하세요.

**4단계: 모델 학습** - 랜덤 포레스트(Random Forest) 분류 모델로 이탈을 예측해 주시기 바랍니다.

1. RandomForestClassifier 학습 (n_estimators=100, random_state=11)
2. SMOTE 적용 학습 데이터로 훈련
3. 테스트 데이터로 예측 수행
4. 다음 평가 지표를 모두 출력하세요:
   - Accuracy, Precision, Recall, F1-Score, ROC-AUC Score
5. 이탈 예측에서 Recall이 특히 중요한 이유를 한국어로 설명해 주세요.
   (이탈 고객을 놓치는 것 vs 정상 고객을 이탈로 잘못 분류하는 것의 비용 비교)

**5단계: 모델 평가 시각화** - 모델 평가 결과를 시각화합니다.

아래 4개의 차트를 2×2 서브플롯으로 구성합니다.
1. (좌상) Confusion Matrix — 히트맵
2. (우상) ROC Curve — AUC 값 표시
3. (좌하) 피처 중요도 상위 10개 — 가로 막대그래프
4. (우하) 이탈 고객 vs 활성 고객의 Recency 분포 비교 — 오버레이 히스토그램

**6단계: 이탈 위험 고객 선별** - 이탈 위험 고객을 선별하고 우선순위를 매겨 주세요.

1. 전체 고객에 대해 이탈 확률(predict_proba) 계산
2. 이탈 위험 등급 분류:
   - High Risk: 이탈 확률 ≥ 0.7
   - Medium Risk: 이탈 확률 0.4~0.7
   - Low Risk: 이탈 확률 < 0.4
3. 등급별 고객 수, 비율, 평균 이탈 확률을 표로 출력
4. High Risk 고객 상위 20명 상세 정보 출력
   (Customer Name, Segment, Region, recency_days, total_sales, 이탈 확률)
5. High Risk 고객의 Segment 분포와 평균 구매 특성을 요약하세요.

**7단계: AI 해석 및 리텐션 전략 제안** - 지금까지의 이탈 위험 예측 분석 결과를 종합하여 다음을 수행해 주시기 바랍니다.

1. 모델 성능 요약
   - Recall과 ROC-AUC를 중심으로 모델 신뢰도 평가
2. 이탈에 가장 영향력 있는 피처 상위 3개 해석
   - 각 피처가 이탈과 어떤 관계인지 비즈니스 관점에서 설명
3. High Risk 고객 리텐션 전략 3가지 제안
   - 전략명, 대상 고객 특성, 실행 방법, 기대 효과 포함
   - 실제 High Risk 고객의 특성(recency, total_sales 등)을 근거로 제안
4. Medium Risk 고객을 위한 예방적 접근 전략 2가지
5. 전체 이탈 예측 분석의 핵심 인사이트를 3줄로 요약

모든 항목은 실제 데이터 수치를 근거로 인용하여 설명해 주시기 바랍니다.

## 출력

- 차트는 `plotting-charts` 스킬의 규칙을 따릅니다.
- 모든 단계가 끝나면 `writing-analysis-report` 스킬의 규칙에 따라 보고서를 저장합니다. 마지막 단계의 해석과 제안은 보고서의 해석과 제안 절에 담습니다.
- 고객 수, 비율, 평균값, 모델 지표 같은 정량 주장은 모두 이번 실행에서 `print()`로 출력된 값에 연결되어야 합니다. 출력에 없는 수치는 제시하지 않습니다.
