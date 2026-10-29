# Software and ML terminology

Use this guide for software, APIs, data work, AI, and machine learning. Follow the project glossary, codebase, product documentation, and intended technical audience.

## Context-sensitive terms

| Term | Context | Likely Korean usage |
|---|---|---|
| `feature` | product or UI | 기능 |
| `feature` | machine learning | 특성 or 피처, following the project glossary |
| `validation` | model or data work | 검증; keep `validation` when the project does |
| `endpoint` | API | 엔드포인트 |
| `label` | machine learning | 레이블, 라벨, or `label` according to the project |
| `baseline` | experiment or benchmark | 베이스라인 or `baseline` according to the project |
| `calibration` | model probabilities | 보정 or 캘리브레이션 according to field usage |
| `time window` | time-series input, aggregation, or observation | keep `time window` or established 윈도우 wording; use 입력 구간·집계 구간·관측 구간 only when that role is explicit, not as interchangeable translations |
| `context window` | LLM token context capacity | 컨텍스트 윈도우; do not confuse it with a time-series input interval |
| `production`, `staging` | deployment environment | keep the established environment names |

## Literal translations need context

`window`가 들어간 용어를 모두 `창`이나 `입력 구간`으로 바꾸지 않는다. 문서의 용어집과 개념을 먼저 확인한다. `time window`, `sliding window`, `context window`, `process window`는 같은 개념이 아니다. 입력 길이를 이동하는 방식이 원문에 없으면 `슬라이딩 윈도우`라고 구체화하지 않는다.

- **고칠 수 있는 경우:** 사용자 용어집이 `time window = 입력 윈도우`라고 지정했다면 `과거 24개 관측값을 시간 창(time window)으로 묶어 입력한다.` → `과거 24개 관측값을 입력 윈도우(time window)로 묶어 입력한다.` 관측값 개수와 역할은 그대로 둔다.
- **용례가 안 정해진 경우:** 원어 `time window`는 확인됐고 최근 24개 관측값을 입력한다는 설명만 있다면 `time window(입력 구간·용어 확인 필요)`처럼 개념 설명과 미확정 용어임을 함께 드러낼 수 있다. 이것을 표준 번역어라고 단정하지 않는다.
- **유지할 경우:** 프로젝트가 `시간 창`을 정의해 사용하도록 지정했거나, 원문 인용이 `시간 창`이라고 썼다면 보존한다. 생소하다는 이유만으로 금칙어로 삼지 않는다.

Usage checks: [Google Cloud's Korean glossary](https://docs.cloud.google.com/docs/generative-ai/glossary?hl=ko#context-window) uses `컨텍스트 윈도우`. The [Korean Institute of ITS 2023 proceedings](https://kits.or.kr/file/2023/ITS_2023b_1.pdf#page=319), “대조학습 기반 운전자 행동 변화 탐지,” uses both `윈도우` and `시간 창`; that is evidence of occurrence, not a universal preferred term. Check the audience's usage rather than treating any one translation as mandatory.

Keep exact code-facing material unchanged: API paths such as `/v2/predict`, field names, commands, package names, model IDs, filenames, and schema keys. Preserve internal spacing and punctuation in technical tokens such as `F1 score`.

Do not turn prototype, validation, staging, release candidate, or experimental status into production deployment.
