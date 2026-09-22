---
name: predicting-campaign-response
description: Marketing Campaign 고객 데이터로 Response를 타겟으로 하는 랜덤 포레스트 분류 모델을 학습하여 캠페인 반응을 예측하고 타겟 고객을 선별합니다. 사용자가 캠페인 반응 예측, 지도학습 분류, SMOTE 클래스 불균형 처리, 랜덤 포레스트, 타겟 고객 선별을 요청할 때 사용합니다.
---

# 캠페인 반응 예측 (분류)

아래 7단계를 순서대로 수행합니다. 단계마다 `python_execute`로 코드를 실행하고 결과를 `print()`로 출력한 뒤, 그 출력에 근거해서만 설명합니다. 변수는 다음 단계에서 재사용할 수 있도록 전역 변수로 저장합니다. 단계를 통합하거나 생략하지 않습니다.

데이터 파일 경로와 인코딩은 사용자의 요청에 명시된 것을 따릅니다. 아래 컬럼 이름은 이 스킬이 전제하는 데이터셋의 컬럼이며, 요청에 다른 이름이 명시되면 그것을 따릅니다.

## 해석 전제

캠페인 관련 컬럼(`AcceptedCmp1`~`AcceptedCmp5`, `Response`)은 아래만 전제로 해석하고 서술합니다.
- `AcceptedCmp1`~`AcceptedCmp5`: 문서대로 1~5번째 캠페인에서 제안 수락 여부(1/0).
- `Response`: 문서대로 마지막 캠페인(the last campaign)에서 제안 수락 여부(1/0). 과거 1~5번 캠페인 지표와는 **별도 컬럼**으로 다룹니다. 이 스킬의 **예측 타깃**입니다.
- `Response`와 `AcceptedCmp5`를 **같은 사건, 같은 컬럼**으로 취급하지 않습니다. 데이터상으로도 두 컬럼은 다르게 나타나는 고객이 많습니다.
- 수락 비율은 컬럼마다 (값=1인 고객 수)/(전체 고객 수)로 계산했음을 밝히고, 일정, 오퍼 내용, 성패 원인 등은 추측하지 않습니다.
- 표와 막대그래프에서 번호형 5개와 `Response`를 **레이블, 색 등으로 시각적으로 구분**합니다.

## 절차

**1단계: 데이터 탐색** - 데이터 파일을 읽어서 다음을 수행하세요.

[변수 해석 — 노트북의 Step 1 참고 메모와 동일하게만 사용]
- AcceptedCmp1~AcceptedCmp5: 각각 1~5번째 캠페인에서 제안 수락 여부(1/0).
- Response: 문서상 the last campaign(마지막 캠페인)에서 제안 수락 여부(1/0). 본 실습의 예측 타깃. `AcceptedCmp5`와 동일 사건으로 보지 마세요.

1. 전체 행(고객 수)과 열(변수 수) 개수
2. 타깃 변수 Response의 분포(수락 및 거절 건수와 비율)
3. 결측치가 있는 컬럼과 개수
4. AcceptedCmp1~5와 Response 각 열에 대해 (값=1인 고객 수)/(전체 고객 수)를 표로 정리하고 막대그래프로 시각화하세요. `AcceptedCmp1`~`5`와 `Response`는 막대, 범례, 색에서 **구분**하세요. 해석은 위 규칙만 따르고, 수락률 차이의 원인을 데이터에 없는 내용으로 단정하지 마세요.

**2단계: 피처 엔지니어링 및 전처리** - 캠페인 반응 예측을 위한 피처 엔지니어링 및 전처리를 수행해 주시기 바랍니다.

1. 파생 변수 생성:
   - Age = 2026 - Year_Birth
   - TotalSpent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds
   - TotalPurchases = NumWebPurchases + NumCatalogPurchases + NumStorePurchases + NumDealsPurchases
   - TotalCampaigns = AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5
2. 전처리:
   - Income 결측치(24건)는 중앙값으로 대체
   - Education, Marital_Status는 Label Encoding 또는 One-Hot Encoding
   - Marital_Status 이상값('YOLO', 'Absurd', 'Alone')은 'Other'로 통합
   - Year_Birth 이상치(1900년 이전)는 제거
3. 최종 피처 목록과 타겟 변수(Response)를 확인하고 X, y로 분리하세요.

**3단계: 학습/테스트 분리 및 클래스 불균형 처리** - 학습/테스트 데이터 분리와 클래스 불균형 처리를 수행해 주시기 바랍니다.

1. train_test_split으로 학습(80%) / 테스트(20%) 분리 (random_state=11, stratify=y)
2. 학습 데이터의 클래스 분포 확인 (Response=0 vs 1 비율)
3. SMOTE로 학습 데이터 오버샘플링하여 클래스 균형 맞추기
   (imbalanced-learn 라이브러리 사용, random_state=11)
4. SMOTE 적용 전후 클래스 분포를 비교하여 출력하세요.

sklearn.model_selection.train_test_split과
imblearn.over_sampling.SMOTE를 사용하세요.

**4단계: 모델 학습** - 랜덤 포레스트(Random Forest) 분류 모델을 학습해 주시기 바랍니다.

1. RandomForestClassifier로 모델 학습 (n_estimators=100, random_state=11)
2. SMOTE 적용한 학습 데이터로 훈련
3. 테스트 데이터로 예측 수행
4. 다음 평가 지표를 모두 출력하세요.
   - Accuracy (정확도)
   - Precision (정밀도)
   - Recall (재현율)
   - F1-Score
   - ROC-AUC Score

sklearn.ensemble.RandomForestClassifier를 사용하고,
각 지표가 무엇을 의미하는지 한국어로 간단히 설명해 주세요.

**5단계: 모델 평가 시각화** - 모델 평가 결과를 시각화합니다.

아래 4개의 차트를 2×2 서브플롯으로 구성합니다.
1. (좌상) Confusion Matrix - 히트맵으로 시각화 (True/False Positive/Negative)
2. (우상) ROC Curve - AUC 값을 그래프에 표시
3. (좌하) 피처 중요도 상위 15개 - 가로 막대그래프
4. (우하) 예측 확률 분포 - Response=0 vs 1 고객의 예측 확률 히스토그램

**6단계: 캠페인 타겟 고객 선별** - 예측 모델을 활용하여 다음 캠페인 타겟 고객을 선별해 주세요.

1. 전체 고객(학습+테스트)에 대해 캠페인 반응 확률(predict_proba) 계산
2. 반응 확률 기준 상위 20%를 타겟 고객으로 선정
3. 다음 결과를 제시하세요:
   - 타겟 고객 수 및 전체 대비 비율
   - 타겟 고객 중 실제 반응자(Response=1) 비율 (Precision 개념)
   - 전체 반응자 중 타겟에 포함된 비율 (Recall 개념)
   - 타겟 고객의 평균 프로필(소득, 총소비, 나이)과 비타겟 고객 비교표
4. 반응 확률 상위 20명의 상세 정보를 출력하세요.

**7단계: AI 해석 및 마케팅 전략 제안** - 지금까지의 캠페인 반응 예측 분석 결과를 종합하여 다음을 수행해 주시기 바랍니다.

1. 모델 성능 요약
   - 주요 평가 지표(F1-Score, ROC-AUC) 수치를 근거로 모델 신뢰도 평가
2. 캠페인 반응에 가장 영향력 있는 피처 상위 5개 해석
   - 각 피처가 왜 중요한지 비즈니스 관점에서 설명
3. 타겟 고객을 대상으로 한 캠페인 전략 3가지 제안
   - 전략명, 대상 고객 특성, 실행 방법, 기대 효과 포함
4. 전체 분석의 핵심 인사이트를 3줄로 요약

모든 항목은 실제 데이터 수치를 근거로 인용하여 설명해 주시기 바랍니다.

## 출력

- 차트는 `plotting-charts` 스킬의 규칙을 따릅니다.
- 모든 단계가 끝나면 `writing-analysis-report` 스킬의 규칙에 따라 보고서를 저장합니다. 마지막 단계의 해석과 제안은 보고서의 해석과 제안 절에 담습니다.
- 고객 수, 비율, 평균값, 모델 지표 같은 정량 주장은 모두 이번 실행에서 `print()`로 출력된 값에 연결되어야 합니다. 출력에 없는 수치는 제시하지 않습니다.
