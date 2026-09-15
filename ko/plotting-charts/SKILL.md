---
name: plotting-charts
description: python_execute 도구 안에서 matplotlib pyplot과 seaborn으로 차트를 작성하고 결과 폴더에 PNG로 자동 저장되게 합니다. 사용자가 시각화, 차트, 그래프, 히스토그램, 산점도, 막대그래프, 파이차트, 서브플롯을 요청할 때 사용합니다.
---

# 차트 작성

`python_execute` 도구는 `pyplot.show()`가 호출될 때 현재 figure를 결과 폴더에 PNG로 자동 저장하고 노트북에 표시합니다. 아래 규칙은 자동 저장이 누락되지 않도록 하기 위한 규칙입니다.

## 규칙

1. `from matplotlib import pyplot`으로 불러온 `pyplot`으로 그립니다. `pyplot.subplots()`, `pyplot.plot()` 등을 사용하고, alias(`plt`)는 사용하지 않습니다.
2. seaborn은 `pyplot`이 만든 figure와 axes 위에서 사용합니다. `ax=` 전달인자로 axes를 지정합니다.
3. 차트를 완성하면 마지막에 `pyplot.show()`를 호출합니다.
4. `matplotlib.figure.Figure`를 단독으로 만들어 그리지 않습니다. 자동 저장과 노트북 표시가 누락됩니다.
5. `savefig()`는 호출하지 않아도 됩니다. 도구가 저장합니다. 직접 저장해야 하면 `RESULT_FOLDER / '<파일명>.png'` 경로만 사용합니다.
6. `pyplot.close('all')`을 호출하지 않습니다. 호출하면 자동 저장이 누락됩니다.
7. 차트의 제목, 축 라벨, 범례, 주석은 영어로 작성합니다. 한글 폰트가 없는 환경에서도 정상적으로 표시되도록 하기 위한 것이며, 분석 결과의 해석과 설명은 한국어로 작성합니다.
8. 여러 차트를 한 번에 그릴 때는 서브플롯으로 구성하고 `pyplot.tight_layout()`을 호출합니다. 2×2 구성이면 `figsize=(14, 10)` 정도를 사용합니다.
9. 막대그래프는 값이 큰 순서로 정렬하고, 산점도에서 색상으로 구분하는 변수는 colorbar나 범례로 표시합니다.

## 출력

차트를 그린 뒤에는 무엇을 그렸는지 1~2문장으로 설명하고, 차트에서 읽을 수 있는 수치는 반드시 코드로 계산해 `print()`한 값을 인용합니다.
