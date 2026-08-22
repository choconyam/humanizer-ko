# Fidelity review

Read this guide when a rewrite contains facts, technical tokens, negation, attribution, limitations, status, or other wording whose loss would matter. It separates exact preservation from semantic preservation so a style cleanup does not become a content edit.

## Build a compact source map

Before rewriting, identify three kinds of constraints. Keep the map internal unless the user asks for an audit.

| Constraint | What to preserve | How to check |
|---|---|---|
| Exact surface | Names, numbers, units, dates, URLs, paths, commands, identifiers, citations, direct quotes, approved slogans, code and schema fields | Compare the source and draft directly |
| Semantic claim | Negation, modality, tense, scope, attribution, causality, comparison, status, uncertainty, limitations and responsibilities | Compare each proposition, not one regex or word |
| Voice and stance | Evaluation, emotion, commitment, criticism, expectation and degree of confidence | Confirm that the writer still takes the same position with similar strength |

Do not treat every ordinary phrase as an exact token. Korean particles, honorifics, spacing around prose, and natural word order may change without changing the protected item.

## Preserve exact material

- Keep technical tokens internally unchanged: `F1 score`, `SEC-219`, `/v2/predict`, `USD/KRW`, `OD 6+`, model names, product names and standards identifiers.
- A Korean particle may follow a token when grammar requires it. `F1 score는 0.84` still contains the token `F1 score`; do not change it to `F1-score` merely for style.
- Keep direct quotations and approved slogans verbatim unless the user explicitly asks to edit them.
- Keep URLs, commands, paths, link targets, citation keys and code untouched. Do not localize their spelling or punctuation.
- Keep numbers with their units and comparison basis. Do not round, normalize, or convert units unless requested.

## Preserve semantic constraints

Check meaning rather than requiring one surface form.

- `문을 열 예정입니다` and `개관할 예정입니다` can carry the same planned status.
- `권고할 수 없습니다` and `권고할 수는 없습니다` can carry the same negation.
- `사용할 수 없습니다` and `사용하실 수 없습니다` can carry the same prohibition with different honorific marking.

These variations are acceptable only when scope and force stay the same. Watch for small words that do change meaning: `만`, `도`, `약`, `최대`, `최소`, `이상`, `이하`, `아직`, `직접`, `일부`, `모든`, and negative expressions.

Preserve the type of proposition as well as its topic. Do not turn an observation into a recommendation, an evaluation into a requirement, an aspiration into a promise, a possibility into a plan, or a commitment into a prediction. For example, `솔직한 대화가 방향을 잡는 데 도움이 된다` must not become `솔직한 대화가 필요하다` unless the source makes that recommendation.

For each factual paragraph, verify:

1. Who did or will do the action.
2. What happened, is planned, is allowed, or is prohibited.
3. When and under what conditions it applies.
4. Whether the source states evidence, possibility, expectation, correlation, or causation.
5. Which limitations, exceptions, unresolved points, and approval states remain.

## Preserve stance without preserving empty intensity

An evaluative phrase is not always a hard fact, but the writer's position is still part of the meaning.

> 이번 결과는 시장 기회가 무궁무진하다는 점을 보여줍니다.

If the evidence does not support `무궁무진`, lower the intensity while keeping the positive assessment, for example `회사는 이번 결과에서 추가 시장 기회를 기대하고 있습니다`. Do not delete the assessment solely to remove the watched word. Keep attribution when the source supplies it; do not invent attribution when it does not.

In personal writing, preserve first-person reactions and deliberate imagery. In reports, preserve conclusions and recommendations at their original confidence level. In notices, preserve commitments. In approved marketing copy, preserve the authorized promise and tone within the stated limits.

## Avoid over-compression

Shorter is not automatically more faithful or more natural.

- Do not reduce a paragraph to data points if its purpose also includes interpretation, instruction, reassurance, criticism, or personal voice.
- Remove a sentence only when it is genuinely redundant and carries no distinct stance, condition, or audience function.
- When a watched phrase contains a real proposition, rewrite the proposition instead of dropping the sentence.
- Do not add a new concluding inference merely because the rewrite feels abrupt.

## Final fidelity gate

Before returning the draft, compare it with the source in this order:

1. Exact tokens and quoted material.
2. Facts, status, negation, scope, attribution and limitations.
3. Evaluation, emotion, commitment and degree of certainty.
4. Genre and audience function.

If naturalness conflicts with any protected meaning, keep the meaning and simplify the surrounding prose instead.
