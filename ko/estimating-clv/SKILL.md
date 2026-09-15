---
name: estimating-clv
description: Superstore 거래 데이터로 고객 생애가치(CLV, Customer Lifetime Value)를 계산하고 Platinum·Gold·Silver·Bronze 등급으로 나누어 고가치 고객을 프로파일링합니다. 사용자가 CLV 추정, 고객 생애가치, 고객 등급 분류, 파레토 분석, 고가치 고객 유지 전략을 요청할 때 사용합니다.
---

# 고객 생애가치(CLV) 추정

아래 7단계를 순서대로 수행합니다. 단계마다 `python_execute`로 코드를 실행하고 결과를 `print()`로 출력한 뒤, 그 출력에 근거해서만 설명합니다. 변수는 다음 단계에서 재사용할 수 있도록 전역 변수로 저장합니다. 단계를 통합하거나 생략하지 않습니다.

데이터 파일 경로와 인코딩은 사용자의 요청에 명시된 것을 따릅니다. 아래 컬럼 이름은 이 스킬이 전제하는 데이터셋의 컬럼이며, 요청에 다른 이름이 명시되면 그것을 따릅니다.

## 절차

**1단계: 데이터 탐색** - 데이터 파일을 읽어서 다음 항목을 분석하세요. (인코딩은 요청을 따릅니다)
1. 전체 행(거래 건수)과 열(변수 수) 개수
2. 고유 고객 수 (Customer ID 기준)
3. 주문 기간 범위 (Order Date 최솟값, 최댓값)
4. 고객별 평균 거래 건수와 평균 총 구매금액
5. Sales 컬럼의 기초 통계량 (평균, 중앙값, 최솟값, 최댓값)

**2단계: 고객별 구매 이력 집계** - CLV 계산을 위한 고객별 구매 이력을 집계해 주시기 바랍니다.

Customer ID 기준으로 다음을 계산하세요.
1. 기본 집계:
   - first_order: 첫 주문일 (Order Date 최솟값)
   - last_order: 마지막 주문일 (Order Date 최댓값)
   - total_orders: 고유 주문 건수 (Order ID nunique)
   - total_sales: 총 구매금액 (Sales 합계)
2. Order Date를 날짜형으로 변환하여 계산하세요.
3. 집계 결과에 Customer Name, Segment도 포함하세요.
4. 집계 결과 상위 5행과 기초 통계량을 출력하세요.

**3단계: CLV 계산** - CLV 구성 요소를 계산하고 최종 CLV를 산출해 주시기 바랍니다.

1. CLV 구성 요소 계산:
   - lifespan_days: last_order - first_order (일수)
   - lifespan_years: lifespan_days / 365 (최솟값 1년으로 처리)
   - aov: total_sales / total_orders (평균 주문 금액)
   - purchase_freq: total_orders / lifespan_years (연간 구매 횟수)
2. CLV 계산:
   - clv = aov × purchase_freq × lifespan_years
3. CLV 기준 고객 등급 분류:
   - Platinum: 상위 10%
   - Gold: 상위 10~30%
   - Silver: 상위 30~60%
   - Bronze: 하위 40%
4. 등급별 고객 수, 평균 CLV, 평균 total_sales를 표로 출력하세요.

**4단계: CLV 분포 분석** - CLV 분포를 분석해 주시기 바랍니다.

1. 전체 CLV 기초 통계량 (평균, 중앙값, 표준편차, 최솟값, 최댓값)
2. 파레토 분석:
   - 상위 20% 고객이 전체 CLV 합계의 몇 %를 차지하는지 계산
3. CLV 등급별 총 CLV 기여도 (파이차트)
4. Segment(Consumer/Corporate/Home Office)별 평균 CLV 비교 (막대그래프)

**5단계: CLV 시각화** - CLV 분석 결과를 시각화합니다.

아래 4개의 차트를 2×2 서브플롯으로 구성합니다.
1. (좌상) CLV 분포 히스토그램 — 등급별 색상 구분
2. (우상) AOV vs 연간 구매 횟수 산점도 — 색상은 CLV 등급, 크기는 CLV 값에 비례
3. (좌하) 고객 유지 기간(lifespan_years) 분포 — 히스토그램
4. (우하) 등급별 평균 AOV와 평균 연간 구매 횟수 — 그룹 막대그래프

**6단계: 고가치 고객 프로파일링** - Platinum 등급 고객의 프로파일을 분석해 주세요.

1. Platinum 고객 수와 전체 대비 비율
2. Platinum vs 전체 평균 비교표:
   - 평균 CLV, 평균 AOV, 평균 연간 구매 횟수, 평균 유지 기간
3. Platinum 고객의 Segment 분포 (파이차트)
4. Platinum 고객의 지역(Region) 분포 (막대그래프)
5. CLV 상위 20명의 상세 정보 (Customer Name, Segment, Region, CLV, 등급) 출력

**7단계: AI 해석 및 마케팅 전략 제안** - 지금까지의 CLV 분석 결과를 종합하여 다음을 수행해 주시기 바랍니다.

1. CLV 등급별 특성 요약 (1~2문장씩)
   - 각 등급(Platinum/Gold/Silver/Bronze)의 핵심 특징 정리
2. Platinum 고객 유지를 위한 전략 2가지 제안
   - 전략명, 대상 고객, 실행 방법, 기대 효과 포함
3. Bronze → Silver 등급 상향을 위한 전략 2가지 제안
   - 이탈 방지와 구매 빈도 증가에 초점
4. 파레토 법칙 관점에서 마케팅 예산 배분 제안
   - 각 등급별 투자 비중 권고와 근거
5. 전체 CLV 분석의 핵심 인사이트를 3줄로 요약

모든 항목은 실제 데이터 수치를 근거로 인용하여 설명해 주시기 바랍니다.

## 출력

- 차트는 `plotting-charts` 스킬의 규칙을 따릅니다.
- 모든 단계가 끝나면 `writing-analysis-report` 스킬의 규칙에 따라 보고서를 저장합니다. 마지막 단계의 해석과 제안은 보고서의 해석과 제안 절에 담습니다.
- 고객 수, 비율, 평균값, 모델 지표 같은 정량 주장은 모두 이번 실행에서 `print()`로 출력된 값에 연결되어야 합니다. 출력에 없는 수치는 제시하지 않습니다.
