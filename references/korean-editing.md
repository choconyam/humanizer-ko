# Korean editing guide

Use this guide only when the source is Korean or the user asks for Korean output.

The 35 upstream Humanizer patterns were written mainly for English. Preserve them for English and mixed-language work, but do not translate their grammar and punctuation rules mechanically. For Korean:

- Apply language-independent upstream patterns such as inflated claims, vague sourcing, sales language, forced structure, filler, fake objections, and chatbot residue.
- Apply an English-specific pattern only when it has a natural Korean equivalent or the edited span is English.
- Let K1-K10 below take priority for Korean word order, subjects, particles, register, sentence endings, rhythm, and terminology.
- In a mixed-language document, evaluate each span in its language while keeping facts, terminology, and document-level voice consistent.

## Preserve the source

- Keep every fact, number, unit, date, name, quote, citation, URL, identifier, and technical limitation.
- Do not turn a correlation into causation, a prototype into a finished product, or a preliminary result into a verified claim.
- Keep explicit uncertainty such as `가능성이 있습니다`, `검증이 필요합니다`, and `임상 성능을 의미하지 않습니다` when the source needs it.
- Do not add local examples, personal experience, or supporting evidence unless the user supplied them.

## K1. Keep one register and honorific level

Choose the register from the source and audience, then keep it consistent.

- Presentations, reports, hospital communication: plain `-습니다/-ㅂ니다` unless the user asks otherwise.
- Academic prose: consistent `-다` style when the source uses it.
- Emails and conversational writing: keep the writer's existing level of politeness.
- Do not mix `-다`, `-해요`, and `-합니다` endings without a real change in speaker or quoted material.
- Preserve honorifics, professional titles, and role names. Do not make patient-facing or senior-facing text more casual by accident.

## K2. Rebuild translation-like word order

Rewrite the clause instead of replacing one phrase mechanically.

- Repeated `이는 ...를 의미합니다` usually becomes a direct statement.
- Repeated `중요한 것은 ...라는 점입니다` usually becomes the point itself.
- Break chains built from `~에 대한`, `~를 통해`, `~와 관련하여`, `~에 기반하여`, and `~에 있어`.
- Rebuild long modifiers instead of preserving English clause order. Move the main claim forward or split a dense modifier into another sentence.
- Do not keep an English sentence boundary when Korean needs two sentences, or split Korean into fragments merely because the English source did.

Example:

> 이 결과는 모델의 일반화 가능성에 대한 중요한 시사점을 제공합니다.

> 이 결과만으로 모델이 다른 데이터에서도 잘 작동한다고 단정할 수는 없습니다.

## K3. Handle subjects, pronouns, and plurality naturally

- Avoid repeated `이것은`, `그것은`, and `그들은` when Korean can omit them or name the actual topic.
- Omit a subject only when the actor remains clear. Keep or restore it when patients, researchers, samples, models, or systems could be confused.
- Do not add `그의`, `그녀의`, `그들의`, or plural `들` mechanically from English.
- When two possible actors appear in one paragraph, repeat the relevant noun instead of relying on an ambiguous pronoun.
- Preserve a deliberate subject when it marks contrast, responsibility, or accountability.

## K4. Prefer verbs to noun stacks

Korean AI prose often stacks abstract nouns and then adds `진행하다`, `수행하다`, or `제공하다`.

- `검토를 진행하다` becomes `검토하다`.
- `개선의 필요성이 존재합니다` becomes `개선해야 합니다` when the source supports that strength.
- Reduce repeated `가능성`, `중요성`, `필요성`, `효율성`, `확장성`, and `연관성` by turning some into verbs or concrete statements.
- Keep the noun when it is a defined technical concept or changing it would alter the claim.

## K5. Cut Korean stock AI phrases

Watch for clusters, not single words. Remove the framing and keep the actual claim.

- `단순히 ...를 넘어`, `...에 그치지 않고`
- `혁신적인`, `획기적인`, `괄목할 만한`, `무궁무진한`
- `새로운 패러다임을 제시합니다`, `중요한 시사점을 제공합니다`
- `앞으로의 귀추가 주목됩니다`, `밝은 미래가 기대됩니다`
- `오늘날 빠르게 변화하는 환경에서`, `현대 사회에서 그 중요성이 커지고 있습니다`
- Repeated `첫째`, `둘째`, `셋째` when the ideas do not need a numbered structure

Do not delete a promotional or evaluative word inside a direct quote. Keep sourced judgments when the source clearly names who made them.

## K6. Use particles and connective endings for meaning

- Remove repeated sentence openers such as `또한`, `그리고`, `그러나`, and `한편` when the relationship is already clear.
- Break chains of `~하며`, `~하면서`, `~함으로써`, and `~하는 가운데` when they hide which event causes, contrasts with, or follows another.
- Keep a connector when it carries real logic such as cause, condition, concession, sequence, or contrast.
- Do not rotate particles or connective endings merely for variety. Change them only when the relationship between ideas changes.
- Avoid attaching every topic to `~은/는`; use the particle that matches the sentence's actual role and emphasis.

## K7. Use field-appropriate terminology

- For technical or specialist text, follow [the domain terminology guide](domain-terminology.md). Choose terms by field and audience, not by literal dictionary equivalence.
- Keep English terms when the field normally uses them, including `feature`, `label`, `baseline`, `validation`, `calibration`, `time-series`, and `prototype`.
- Keep the writer's established Korean or English term after first use. Do not cycle through synonyms to avoid repetition.
- Never translate code, model names, product names, API fields, file paths, commands, or citation keys.
- Preserve spacing and capitalization inside technical tokens. Change unit formatting only when the user asks for a style conversion.

## K8. Set Korean sentence boundaries and rhythm

- Split a sentence that carries several conditions, exceptions, actors, and conclusions. Keep related information together when splitting would hide the relationship.
- Merge clipped fragments that imitate English emphasis but sound abrupt in Korean.
- Formal Korean may repeat `-습니다` or `-다`. Vary sentence structure without mixing the chosen register just to avoid repeated endings.
- Let paragraph breaks follow changes in idea, speaker, time, or argument instead of a fixed paragraph length.
- Remove a closing sentence that merely repeats the paragraph's first sentence without adding evidence or a decision.

## K9. Write for speaking when needed

For presentation scripts, lectures, interviews, and video narration:

- Prefer sentences that can be spoken in one breath, but do not impose a fixed character limit.
- Put the main point before a long condition or list.
- Split dense parentheses and stacked modifiers into a following sentence.
- Keep slide numbers, figure references, and transition cues that help the presenter navigate.
- Remove report-like throat-clearing such as `이번 발표에서는 ...에 대해 살펴보도록 하겠습니다` when the next sentence can start with the topic.
- Read the result aloud mentally and fix tongue-twisting repetitions or abrupt register changes.

## K10. Handle high-stakes text carefully

For medical, legal, scientific, financial, or policy text:

- Preserve caution, scope, population, time range, comparison group, and validation status.
- Do not replace a precise term with a friendlier but broader word.
- Keep distinctions such as research use versus clinical use, association versus causation, and demonstration versus deployment.
- If naturalness conflicts with precision, keep the precise wording and simplify the surrounding sentence.

## Final Korean pass

Before returning the rewrite, check that:

1. The register and honorific level are consistent.
2. No fact, number, citation, technical token, or uncertainty marker changed.
3. English-specific rules were not imposed mechanically on Korean sentences.
4. Word order, subjects, pronouns, particles, and connective endings are natural and unambiguous.
5. Abstract noun stacks and Korean stock AI phrases are not repeated mechanically.
6. Specialist terms match the field and remain consistent.
7. Sentence boundaries fit Korean rhythm; spoken text is easy to say aloud.
8. High-stakes limits, scope, and uncertainty remain precise.
