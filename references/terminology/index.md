# Korean terminology router

Read this file for a suspected literal mistranslation or to choose, translate, correct, or explain an unsettled specialist term. Keep known-correct terms; repetition alone does not establish correctness.

## Choose before translating

Prefer the user's explicit glossary or required style. Otherwise establish the concept from source definitions, then choose usage appropriate to the target field and audience using its standard, professional literature, protocol, or product documentation. A source definition establishes meaning, not proof that its Korean label is idiomatic. A translated vendor page alone does not establish common Korean usage.

Translate the concept, not individual words. Suspect a calque when the label misstates the concept, collides with another technical sense, or clashes with relevant field usage. Unfamiliarity and English origin alone are not reasons to replace it. Correct ordinary prose only when the concept and replacement are supported; keep the underlying facts, measurements, method, and limitations.

## Correct or expose uncertainty

- **개념과 대응어가 확인됨:** 분야에서 실제로 쓰는 한국어·음역·영어 표현으로 고친다. 올바른 기존 영어를 억지로 한국어로 바꾸지 않는다. 사용자 지정 용어집은 우선하며, 일반 본문에 같은 오역이 반복되어도 검토한다.
- **음차와 직역 구분:** 사용자가 해당 전환을 명시적으로 요청하지 않았다면 `드롭릿`을 `Droplet`으로 바꾸거나 그 반대로 바꾸지 않는다. 같은 개념의 음차↔영어 전환은 용어 교정이 아니며, 분야 용례나 아래 병기 형식을 이유로 이 제한을 우회하지 않는다. 단어별 직역어는 개념이 같아도 분야 용례와 어긋나는 근거가 있으면 K7로 다듬을 수 있다. 올바른 음차에는 확인 표시도 붙이지 않는다.
- **원어는 확인됐지만 한국어 용례가 불확실함:** 첫 등장에 `English term(한국어 설명·용어 확인 필요)`로 쓴다. 설명도 확신하기 어렵다면 `English term(원문: 기존 표현·용어 확인 필요)`로 원문과 제안을 구분한다. 다음 등장에서는 원어를 일관되게 쓰며, 검토 요청에는 필요한 변경 이유도 알린다.
- **원어나 개념도 불확실함:** 원문 표현을 보존하고 바로 뒤에 `[용어 확인 필요]`를 붙인다. 한국어 표현을 역번역해 영어를 만들어 내거나 뜻이 다른 전문용어를 추측하지 않는다. 문서 목적상 표시를 붙일 수 없으면 짧은 용어 메모에 남긴다.
- **보호 대상:** 코드, API·스키마 필드, 식별자, 제품명, 직접 인용, 승인 문구, 청구항·계약 문언, 명시적 사용자 용어집은 몰래 바꾸지 않는다. 문제가 의심되면 해당 부분 밖의 메모에서만 확인 대상으로 알린다.

When lookup is needed, check a directly relevant authority or practitioner source for the unresolved concept, comparing the English definition if necessary. Reuse that decision for repeated occurrences. If available evidence does not settle it, use the uncertainty form instead of browsing indefinitely. Do not load every field guide, browse all terms, or add bilingual expansions to already-settled wording.

## Quick context map

Use this map for common collisions. If it and the source settle the choice, stop here.

| English term | Context | Korean usage |
|---|---|---|
| `endpoint` | clinical trial / API | 평가변수 / 엔드포인트 |
| `claim` | patent / assertion / insurance | 청구항 / 주장 / 청구·보험금 청구 |
| `cell` | battery / biology | 셀·전지 / 세포 |
| `substrate` | materials / biochemistry | 기판 / 기질 |
| `feature` | machine learning / product UI | 특성·피처 / 기능 |
| `validation` | model or data / pharmaceutical GMP | 검증 / 밸리데이션 |
| `interest` | lending / ownership / relationship | 이자 / 지분 / 이해관계 |

## Load a field guide only for unresolved detail

Read a matching guide only when the quick map does not resolve the term or field-specific usage and status rules matter.

| Field | Read |
|---|---|
| Materials, chemistry, deposition, electronics, batteries | [science and materials](science-materials.md) |
| Software, APIs, data, AI, machine learning | [software and ML](software-ml.md) |
| Medicine, clinical research, biotechnology, pharmaceuticals | [medical and biotech](medical-biotech.md) |
| Law, regulation, compliance, public policy | [legal and policy](legal-policy.md) |
| Finance, accounting, investment, insurance | [finance and accounting](finance-accounting.md) |

Do not load every field guide for a cross-domain list already resolved by the map. Read more than one only when unresolved details genuinely require them. If no guide fits, keep the original term when uncertain.

## Shared safeguards

- Keep one concept under one term unless the source distinguishes meanings.
- Use `한국어 용어(English term)` at first mention only when it helps the audience or verification. Use the English-first uncertainty form above only when the exact original is known but the Korean equivalent is unsettled.
- Keep English when practitioners normally use it.
- Never translate API names, code symbols, model or product names, standards identifiers, paths, commands, or citation keys.
- Preserve status and scope; terminology cleanup must not strengthen a claim.
- Verify current, disputed, regulated, or high-stakes terminology against one relevant authority when lookup is available. Do not browse merely to preserve an established term.

Useful authorities include the National Institute of Korean Language norms (https://korean.go.kr/kornorms), the Standard Korean Language Dictionary (https://stdict.korean.go.kr), the TTA ICT terminology dictionary (https://terms.tta.or.kr), the National Law Information Center (https://www.law.go.kr), and the relevant Korean professional society.
