# ai-agents-course-skills

강의 실습에서 Deep Agents가 사용하는 스킬(skill) 라이브러리입니다. 스킬은 에이전트가 특정 작업을 수행하는 절차를 담은 재사용 가능한 작업 지침이며, 각 스킬은 `SKILL.md`를 가진 폴더 하나로 구성됩니다.

- 작성 규칙: <https://github.com/jinsooya/skills>
- 언어: 한국어 스킬은 `ko/`, 영어 스킬은 `en/` 아래에 같은 이름으로 배치합니다.

## 폴더 구조

```
ai-agents-course-skills/          # 로컬 폴더 이름은 달라도 된다
├── README.md
├── scripts/check_parity.py     # ko와 en의 스킬 목록과 이름 규칙을 검사한다
├── ko/                         # 한국어 스킬
│   ├── analyzing-rfm/
│   │   ├── SKILL.md
│   │   └── references/segments.md
│   ├── writing-analysis-report/
│   │   ├── SKILL.md
│   │   └── references/report-template.md
│   ├── plotting-charts/SKILL.md
│   ├── generating-monthly-sales-report/SKILL.md
│   └── checking-restock-status/SKILL.md
└── en/                         # 영어 스킬 (ko와 같은 구조)
```

## 스킬 목록

| 스킬 | 용도 | 사용하는 노트북 | ko | en |
|---|---|---|---|---|
| `analyzing-rfm` | 거래 또는 고객 데이터로 RFM 분석을 수행하고 잠재 우수고객을 도출한다 | 13-02-1, 13-02-2 | O | O |
| `writing-analysis-report` | 분석 결과를 `/report.md` 보고서로 정리한다 | 13 계열 공통 | O | O |
| `plotting-charts` | pyplot으로 차트를 작성하고 결과 폴더에 저장한다 | 13 계열 공통 | O | O |
| `generating-monthly-sales-report` | Northwind 월간 매출 보고서를 작성한다 | 10-1-09 | O | O |
| `checking-restock-status` | Northwind 재고 보충 대상을 점검한다 | 10-1-09 | O | O |

> Exercise와 Lab의 답에 해당하는 스킬은 이 공개 저장소에 올리지 않습니다. 예를 들어 `10-1-09s`의 휴면 고객 스킬과 보고서 양식을 참조 파일로 분리한 월간 보고서 스킬은 여기에 없습니다.

## 노트북에서 사용하는 방법

노트북은 필요한 스킬만 선택하여 로컬 `skills/` 폴더에 내려받고, 에이전트에는 항상 `skills=['/skills']`를 전달합니다.

```python
LANG = 'ko'                                                    # 'ko' 또는 'en'
SKILLS = ['analyzing-rfm', 'writing-analysis-report', 'plotting-charts']
REPO = 'https://raw.githubusercontent.com/jinsooya/ai-agents-course-skills/main'

import urllib.request
from pathlib import Path
for name in SKILLS:
    files = urllib.request.urlopen(f'{REPO}/{LANG}/{name}/manifest.txt').read().decode().split()
    for rel in files:
        dst = Path('skills') / name / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(f'{REPO}/{LANG}/{name}/{rel}', dst)
```

각 스킬 폴더의 `manifest.txt`는 그 스킬이 포함하는 파일의 상대 경로 목록입니다. 참조 파일이 있는 스킬은 이 목록으로 함께 내려받습니다.

```python
agent = create_deep_agent(
    model=model,
    tools=[...],
    backend=backend,       # 노트북 폴더를 가상 루트로 연결한다
    skills=['/skills'],    # 내려받은 스킬 폴더
    system_prompt=INSTRUCTION
)
```

## 작성 규칙 요약

- 폴더 이름과 `SKILL.md`의 `name`은 같아야 하며, 소문자와 숫자와 하이픈만 사용합니다. 동명사(verb + -ing) 형태를 권장합니다.
- `description`에는 스킬이 무엇을 하는지와 언제 사용하는지를 함께 적고, 에이전트가 요청과 대조할 수 있는 키워드를 포함합니다.
- 본문은 500줄 이내로 유지하고, 긴 참조 자료는 `references/`로 분리합니다. 참조 파일은 `SKILL.md`에서 한 단계 깊이까지만 허용합니다.
- 한국어 스킬을 먼저 작성하고 영어 스킬을 번역본으로 작성합니다. 두 언어의 스킬 목록은 항상 같아야 합니다.

## 검사

```bash
python scripts/check_parity.py
```

`ko`와 `en`의 스킬 목록이 같은지, 각 `SKILL.md`의 `name`이 폴더 이름과 같은지, `manifest.txt`가 실제 파일과 일치하는지 검사합니다.
