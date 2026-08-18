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

## Authoritative Korean references

Use these references to verify spelling, spacing, punctuation, loanword transcription, and standard terms when the user's glossary and the source document do not settle the choice. The order of preference above still applies: a user glossary or an established source-document term wins over a dictionary entry.

- Korean orthography, spacing, punctuation, and loanword rules: the National Institute of Korean Language norms (한국어 어문 규범), https://korean.go.kr/kornorms
- Standard word forms and meanings: the Standard Korean Language Dictionary (표준국어대사전), https://stdict.korean.go.kr
- New and specialist words collected from real usage: Urimalsaem (우리말샘), https://opendict.korean.go.kr
- Information and communications technology terms: the TTA ICT terminology dictionary (정보통신용어사전), https://terms.tta.or.kr
- Korean statutes and legal terms: the National Law Information Center (국가법령정보센터), https://www.law.go.kr
- Medical terms: the terminology published by the Korean Medical Association and the relevant specialty societies (대한의사협회·대한의학회 의학용어집)

These are lookup aids, not sources of new facts. Look terms up one page at a time through the agent's approved browsing tools, as a person would. Do not bulk-download, crawl, or scrape these sites, and do not call their APIs without the registration and terms those APIs require. Do not copy definitions into the rewrite, and do not let a dictionary form override a term the field or the governing document actually uses.

## Final terminology check

Before returning the rewrite, check that:

1. Each specialist term matches its field and document type.
2. One concept uses one stable term unless the source distinguishes them.
3. Korean translation did not broaden, narrow, or change the technical claim.
4. Official terms, protected tokens, abbreviations, and bilingual definitions remain intact.
5. Any unresolved ambiguity is visible to the user rather than hidden behind a confident guess.
