---
name: predicting-spending-from-demographics
description: Marketing Campaign 고객 데이터로 인구통계 변수로부터 총소비금액(MntTotal)을 예측하는 랜덤 포레스트 회귀 모델을 학습하고 신규 고객의 소비금액을 예측합니다. 사용자가 소비금액 예측, 회귀 분석, 인구통계 기반 예측, 잠재 고가치 고객 조기 발굴을 요청할 때 사용합니다.
---

# 인구통계 기반 소비금액 예측 (회귀)

아래 7단계를 순서대로 수행합니다. 단계마다 `python_execute`로 코드를 실행하고 결과를 `print()`로 출력한 뒤, 그 출력에 근거해서만 설명합니다. 변수는 다음 단계에서 재사용할 수 있도록 전역 변수로 저장합니다. 단계를 통합하거나 생략하지 않습니다.

데이터 파일 경로와 인코딩은 사용자의 요청에 명시된 것을 따릅니다. 아래 컬럼 이름은 이 스킬이 전제하는 데이터셋의 컬럼이며, 요청에 다른 이름이 명시되면 그것을 따릅니다.

## 절차

**1단계: 데이터 탐색** - 데이터 파일을 읽어서 다음 항목을 분석하세요.

1. 전체 행(고객 수)과 열(변수 수) 개수
2. 인구통계 컬럼(Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome)의 기초 통계 및 고유값
   - 수치형: 평균, 중위수, 최솟값, 최댓값
   - 범주형: 고유값 목록과 각 값의 빈도
3. 소비 컬럼 6개(MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds) 합산 MntTotal의 기초 통계
4. Income 결측치 수, Marital_Status 이상값(YOLO, Absurd, Alone) 확인

결과는 표 형태로 보기 좋게 출력하고, 데이터 특이사항을 한국어로 요약하세요.

**2단계: 피처 엔지니어링** - 회귀 모델을 위한 피처 엔지니어링을 수행하세요.

1. 타겟 변수 생성: MntTotal = 6개 제품군 소비금액 합산
2. 나이 계산: Age = 2014 - Year_Birth
3. 이상치 제거:
   - Age > 80인 행 제거 (비현실적 출생연도)
   - Income > 200000인 행 제거 (극단적 이상치)
4. 결측치 처리: Income 결측치를 중위수로 대체
5. 범주형 변수 정리:
   - Marital_Status: Alone, YOLO, Absurd -> Single로 통합
   - Education: Basic -> 기초, Graduation -> 학사, Master -> 석사, PhD -> 박사, 2n Cycle -> 학사로 매핑
6. 원-핫 인코딩: Education, Marital_Status (drop_first=True)
7. 최종 피처 목록과 데이터 크기 출력

전처리 후 데이터 크기와 피처 목록을 출력하세요.

**3단계: 탐색적 분석** - 피처와 총소비금액(MntTotal)의 관계를 탐색적으로 분석하세요.

1. 소득(Income)과 MntTotal의 산점도 (색상: Education)
2. 나이(Age)와 MntTotal의 산점도
3. 자녀 수(Kidhome+Teenhome)별 MntTotal 박스플롯
4. 수치형 피처(Income, Age, Kidhome, Teenhome)와 MntTotal 간 피어슨 상관계수 출력

4개 차트를 2×2 서브플롯으로 구성하고, 각 관계에서 발견한 인사이트를 한국어로 설명하세요.

**4단계: 회귀 모델 학습** - RandomForest 회귀 모델을 학습하고 평가하세요.

1. 학습/테스트 분할: 80% 학습, 20% 테스트 (random_state=11)
2. 모델 학습: RandomForestRegressor(n_estimators=100, random_state=11)
3. 성능 평가 지표 출력
   - R² (결정계수): 학습셋 / 테스트셋
   - MAE (평균 절대 오차): 테스트셋
   - RMSE (평균 제곱근 오차): 테스트셋
4. Feature Importance 상위 10개를 내림차순으로 출력
5. Feature Importance 가로 막대그래프 시각화 (상위 10개, 한국어 레이블)

모델 성능과 중요 변수에 대한 해석을 한국어로 설명하세요.

**5단계: 모델 성능 시각화** - 모델 성능을 시각화하세요.

아래 4개 차트를 2×2 서브플롯으로 구성합니다.

1. (좌상) 실제값 vs 예측값 산점도 (x: 실제 MntTotal, y: 예측 MntTotal, 대각선 기준선 추가)
2. (우상) 잔차(residual = 실제값 - 예측값) 히스토그램 (정규분포 근접 여부 확인)
3. (좌하) Feature Importance 가로 막대그래프 (상위 10개)
4. (우하) 소득 구간별 실제 vs 예측 평균 소비금액 비교 막대그래프

**6단계: 소비금액 예측 및 활용** - 학습된 모델을 활용하여 소비금액을 예측하세요.

1. 가상 신규 고객 3명의 예상 소비금액 예측
   - 고객 A: Income=80000, Age=45, Education=박사, Marital_Status=Married, Kidhome=0, Teenhome=1
   - 고객 B: Income=30000, Age=35, Education=학사, Marital_Status=Single, Kidhome=1, Teenhome=0
   - 고객 C: Income=55000, Age=55, Education=석사, Marital_Status=Married, Kidhome=0, Teenhome=0
   - 3명의 예측 소비금액을 표로 출력
2. 전체 테스트셋에서 예측 소비금액 상위 20%를 잠재 고가치 고객으로 분류
   - 잠재 고가치 고객의 평균 Income, 평균 Age, Education 최빈값 출력
3. 결과를 RESULT_FOLDER / 'predicted_spending.csv'로 저장
   - 포함 컬럼: Income, Age, Education, Marital_Status, Kidhome, Teenhome, MntTotal_실제, MntTotal_예측

결과를 한국어로 요약하세요.

**7단계: AI 해석 및 마케팅 전략 제안** - 지금까지의 인구통계 기반 소비 예측 분석 결과를 종합하여 다음을 수행하세요.

1. 핵심 인사이트 요약 (3~4문장)
   - 소비금액 예측에 가장 중요한 인구통계 변수
   - 소득, 나이, 자녀 수와 소비금액의 관계
   - 모델 성능(R²)의 의미와 한계
2. 인구통계 유형별 소비 특성 (2~3개 유형)
   - 각 유형의 인구통계 프로파일과 예상 소비 패턴
3. 마케팅 활용 전략 제안 (3~5가지)
   - 신규 고객 온보딩: 인구통계로 기대 소비금액을 예측하여 VIP 후보 조기 발굴
   - 타겟 마케팅: 예측 소비금액 기준으로 마케팅 예산 배분
   - 각 전략은 구체적인 실행 방안 포함

결과는 마크다운 형식(##, ### 헤더, 표, 불릿 리스트 활용)으로 보기 좋게 작성하세요.

## 출력

- 차트는 `plotting-charts` 스킬의 규칙을 따릅니다.
- 모든 단계가 끝나면 `writing-analysis-report` 스킬의 규칙에 따라 보고서를 저장합니다. 마지막 단계의 해석과 제안은 보고서의 해석과 제안 절에 담습니다.
- 고객 수, 비율, 평균값, 모델 지표 같은 정량 주장은 모두 이번 실행에서 `print()`로 출력된 값에 연결되어야 합니다. 출력에 없는 수치는 제시하지 않습니다.
