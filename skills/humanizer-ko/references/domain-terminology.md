# Korean domain terminology

Use this guide when Korean text contains professional, academic, technical, legal, medical, financial, scientific, or industry-specific terms. Its purpose is to prevent awkward literal translations and false synonym changes.

## Choose the term from its context

Identify the field, subfield, document type, and audience before translating a term. The same English word can require different Korean terms in different settings.

Use this order of preference:

1. The user's glossary, organization style guide, or explicit wording choice.
2. A term already defined and used consistently in the source document.
3. The official Korean term used by the relevant regulator, standards body, professional society, product documentation, or named reference.
4. The term Korean practitioners commonly use in that field.
5. The original English term when no Korean equivalent is stable or a translation would be misleading.

Do not replace an organization's official term merely because another translation sounds smoother. When the terminology is current, unfamiliar, disputed, or high-stakes, verify it against an authoritative domain source if source lookup is available. Do not guess a Korean equivalent from the English spelling alone.

## Handle ambiguity explicitly

- Use `한국어 용어(English term)` at first mention when the audience is mixed, the Korean term may be ambiguous, or later source checking matters.
- Keep a common English loanword when professionals use it more naturally than a translated form.
- If two Korean terms are both established, follow the source, audience, and governing document instead of mixing them for variety.
- If a reliable choice cannot be made, keep the original term and briefly flag the ambiguity. Do not silently invent a translation.
- Preserve abbreviations after defining them once. Do not translate API names, code symbols, model names, standards identifiers, or citation keys.

## Context changes the translation

The examples below show why domain context matters. They are examples, not a fixed glossary.

| English term | Context | Likely Korean usage |
|---|---|---|
| `feature` | product or UI | 기능 |
| `feature` | machine learning | 특성 or 피처, following the project glossary |
| `validation` | machine learning | 검증 |
| `validation` | pharmaceutical or GMP work | 밸리데이션 |
| `endpoint` | API | 엔드포인트 |
| `endpoint` | clinical trial | 평가변수, following the protocol or regulator wording |
| `subject` | grammar | 주어 |
| `subject` | clinical research | 임상시험 대상자 or 연구대상자, following the governing document |
| `substrate` | electronics or materials | 기판 |
| `substrate` | biochemistry | 기질 |
| `claim` | patent | 청구항 |
| `claim` | insurance | 청구 or 보험금 청구 |
| `claim` | academic argument | 주장 |

## Final terminology check

Before returning the rewrite, check that:

1. Each specialist term matches its field and document type.
2. One concept uses one stable term unless the source distinguishes them.
3. Korean translation did not broaden, narrow, or change the technical claim.
4. Official terms, protected tokens, abbreviations, and bilingual definitions remain intact.
5. Any unresolved ambiguity is visible to the user rather than hidden behind a confident guess.
