---
name: reviewing-monthly-kiosk-sales
description: 릴코너(Reel Corner) 키오스크 대여 데이터의 월간 리뷰를 작성합니다. 사용자가 월간 리뷰, 월간 실적 보고서, 지난달 실적을 요청할 때 사용합니다.
---

# 월간 리뷰

**1단계: 대상 월** - 사용자가 지정한 월을 사용하세요. 지정하지 않으면 오늘 날짜 이전의
마지막 온전한 달을 사용하세요.

**2단계: 개요** - 해당 월과 전월의 총매출(`payment.amount`의 합)과 대여 건수
(`payment.rental_id`를 중복 없이 센 수)를 구하세요. 전월 대비 증감률은 `eval` 도구로 계산하세요.
각 달의 결제 기록이 있는 날의 수(`COUNT DISTINCT date(payment_date)`)도 세세요.
두 달의 기록 일수가 다르면, 증감률이 수요뿐 아니라 기록 범위의 차이도 반영한다는 점을 증감률 옆에 밝히세요.

**3단계: 세부 분석** - 해당 월의 언어별 매출, 장르별 매출, 배우별 매출 상위 5명을
각각 높은 순서대로 구하세요.

**4단계: 차트** - 언어별 매출로 `render_bar_chart`를 호출하여
`/output/revenue-by-language-<YYYY-MM>.png`로 저장하세요.

## 출력

사용자 요청의 언어로 `/output/monthly-review-<YYYY-MM>.md`를 작성하세요.
절 구성은 Overview, Revenue by Language, Revenue by Category, Top Actors, So what 순서입니다.
금액은 달러이며 소수점 둘째 자리와 천 단위 구분 기호를 사용하세요.
차트는 마크다운 이미지 링크로 넣으세요. Top Actors 절에는 배우별 매출이 서로 겹치므로
더하면 안 된다는 점을 밝히세요. So what 절에는 관리자가 실행할 수 있는 항목을 두세 개 작성하세요.
