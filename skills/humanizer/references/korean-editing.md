# Korean editing guide

Use this guide only when the source is Korean or the user asks for Korean output. Apply it with the shared Humanizer patterns in `SKILL.md`.

## Preserve the source

- Keep every fact, number, unit, date, name, quote, citation, URL, identifier, and technical limitation.
- Do not turn a correlation into causation, a prototype into a finished product, or a preliminary result into a verified claim.
- Keep explicit uncertainty such as `가능성이 있습니다`, `검증이 필요합니다`, and `임상 성능을 의미하지 않습니다` when the source needs it.
- Do not add local examples, personal experience, or supporting evidence unless the user supplied them.

## Keep one register

Choose the register from the source and audience, then keep it consistent.

- Presentations, reports, hospital communication: plain `-습니다/-ㅂ니다` unless the user asks otherwise.
- Academic prose: consistent `-다` style when the source uses it.
- Emails and conversational writing: keep the writer's existing level of politeness.
- Do not mix `-다`, `-해요`, and `-합니다` endings without a real change in speaker or quoted material.
- Preserve honorifics, professional titles, and role names. Do not make patient-facing or senior-facing text more casual by accident.

## Remove translation-like structure

Rewrite the clause instead of replacing one phrase mechanically.

- Repeated `이는 ...를 의미합니다` usually becomes a direct statement.
- Repeated `중요한 것은 ...라는 점입니다` usually becomes the point itself.
- Break chains built from `~에 대한`, `~를 통해`, `~와 관련하여`, `~에 기반하여`, and `~에 있어`.
- Avoid English-style dummy subjects such as repeated `이것은` or `그것은` when Korean can omit them naturally.
- Keep a subject when removing it would make the actor, patient, sample, or system ambiguous.

Example:

> 이 결과는 모델의 일반화 가능성에 대한 중요한 시사점을 제공합니다.

> 이 결과만으로 모델이 다른 데이터에서도 잘 작동한다고 단정할 수는 없습니다.

## Prefer verbs to noun stacks

Korean AI prose often stacks abstract nouns and then adds `진행하다`, `수행하다`, or `제공하다`.

- `검토를 진행하다` becomes `검토하다`.
- `개선의 필요성이 존재합니다` becomes `개선해야 합니다` when the source supports that strength.
- Reduce repeated `가능성`, `중요성`, `필요성`, `효율성`, `확장성`, and `연관성` by turning some into verbs or concrete statements.
- Keep the noun when it is a defined technical concept or changing it would alter the claim.

## Cut Korean stock AI phrases

Watch for clusters, not single words. Remove the framing and keep the actual claim.

- `단순히 ...를 넘어`, `...에 그치지 않고`
- `혁신적인`, `획기적인`, `괄목할 만한`, `무궁무진한`
- `새로운 패러다임을 제시합니다`, `중요한 시사점을 제공합니다`
- `앞으로의 귀추가 주목됩니다`, `밝은 미래가 기대됩니다`
- `오늘날 빠르게 변화하는 환경에서`, `현대 사회에서 그 중요성이 커지고 있습니다`
- Repeated `첫째`, `둘째`, `셋째` when the ideas do not need a numbered structure

Do not delete a promotional or evaluative word inside a direct quote. Keep sourced judgments when the source clearly names who made them.

## Keep natural terminology

- Keep English terms when the field normally uses them, including `feature`, `label`, `baseline`, `validation`, `calibration`, `time-series`, and `prototype`.
- Keep the writer's established Korean or English term after first use. Do not cycle through synonyms to avoid repetition.
- Never translate code, model names, product names, API fields, file paths, commands, or citation keys.
- Preserve spacing and capitalization inside technical tokens. Change unit formatting only when the user asks for a style conversion.

## Write for speaking when needed

For presentation scripts, lectures, interviews, and video narration:

- Prefer sentences that can be spoken in one breath, but do not impose a fixed character limit.
- Put the main point before a long condition or list.
- Split dense parentheses and stacked modifiers into a following sentence.
- Keep slide numbers, figure references, and transition cues that help the presenter navigate.
- Remove report-like throat-clearing such as `이번 발표에서는 ...에 대해 살펴보도록 하겠습니다` when the next sentence can start with the topic.
- Read the result aloud mentally and fix tongue-twisting repetitions or abrupt register changes.

## Handle high-stakes text carefully

For medical, legal, scientific, financial, or policy text:

- Preserve caution, scope, population, time range, comparison group, and validation status.
- Do not replace a precise term with a friendlier but broader word.
- Keep distinctions such as research use versus clinical use, association versus causation, and demonstration versus deployment.
- If naturalness conflicts with precision, keep the precise wording and simplify the surrounding sentence.

## Final Korean pass

Before returning the rewrite, check that:

1. The register and honorific level are consistent.
2. No fact, number, citation, technical token, or uncertainty marker changed.
3. Subjects are omitted only where the actor remains clear.
4. Translation-like connectors and abstract noun stacks are not repeated mechanically.
5. Spoken text is easy to say aloud, and written text still fits its audience.
