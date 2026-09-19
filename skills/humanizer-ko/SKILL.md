---
name: humanizer-ko
description: |
  Review or rewrite supplied Korean or English prose for AI-like phrasing,
  translation-like syntax, inflated claims, filler, or chatbot artifacts while
  preserving facts, meaning, and voice. Use for prose naturalization, including
  presentation scripts; not for unrelated code review or fact-checking alone.
license: MIT
metadata:
  version: "ko-1.1.0"
---

# humanizer-ko

Rewrite AI-like prose so it sounds like the writer. Keep the meaning, facts, and voice. Use this as an editing aid, not as a promise to bypass AI detectors.

Korean is this skill's primary target: the K1-K10 checkpoints below apply to any Korean source or output. The upstream English patterns live in a reference and load only when the text has substantial English prose.

Read this file fully if only its description is available. Reuse instructions already present in context and unchanged; reread only when content changed or is no longer available.

## Non-negotiable constraints

1. Preserve every fact, number, unit, date, name, quote, citation, URL, identifier, and technical limitation.
2. Preserve tense, modality, negation, scope, attribution, and completion status. Do not turn *planned* into *completed*, *may* into *does*, correlation into causation, a prototype into a product, or a preliminary result into a verified claim.
3. Preserve the source's viewpoint, evaluation, emotion, commitment, and degree of certainty. Lower unsupported intensity without deleting the underlying proposition or making the writer sound indifferent. This protects propositions, not decoration: when an unsupported evaluative modifier adds no claim the text needs, delete the modifier instead of swapping in a softer synonym.
4. Do not invent support, examples, opinions, experiences, or specifics. Adding a plausible domain detail the source does not state — an instrument, a mechanism, a failure mode, an achieved result or structure — is invention, not naturalness. Fiction is exempt because invention is the task.
5. Match the source's genre, register, and writing sample. A supplied sample overrides general style preferences unless it conflicts with accuracy or the user's explicit request.
6. Keep code blocks, commands, paths, schema fields, link targets, product names, approved copy, and established technical tokens unchanged unless the user asks to edit them. Keep their notation as written (`WS2` stays `WS2`, not `WS₂`), and do not swap a Korean transliteration for its English word or the reverse. Never reword text that may be claim or contract language. If a token looks like a typo, keep it and flag it instead of fixing it silently.

## Korean checkpoints K1-K10

Do not transfer English grammar, capitalization, dash, quote, or subject rules into Korean mechanically. Rebuild translation-like clauses as Korean sentences instead of swapping watched words. If the source says `센터는 다음 달 문을 열 예정입니다`, do not strengthen it to a completed or guaranteed event. Leave already-natural Korean unchanged unless coherence requires revision; never edit just to show the skill was used.

### K1. Keep one register and honorific level

- Match the source and audience, and keep overall politeness consistent. A conventional `안녕하세요` greeting with a `-합니다` body is natural; fix unexplained drift among `-다`, `-해요`, and `-합니다`.
- Preserve titles, role names, and respect for people, but do not honorify objects: `자료가 준비되셨습니다` → `자료가 준비됐습니다`.
- Formal repetition is acceptable when changing endings would make the text less precise.

### K2. Rebuild translation-like word order

- Strip repeated, empty frames such as `이는 ...를 의미합니다`, `~라는 점에서 의미가 있습니다`, and `~라고 할 수 있습니다`; state only the source-supported predicate. Keep real uncertainty or semantic explanation.
- Break chains built from `~에 대한`, `~를 통해`, `~와 관련하여`, `~에 기반하여`, and `~에 있어`.
- `의미를 가지다` often becomes `의미가 있다`; `문제가 존재하다` often becomes `문제가 있다`.
- 뜻과 문장 성분이 유지될 때만 번역투 서술어를 다듬는다: `회의를 갖다` → `회의를 열다`, `현장에서 필요로 하는` → `현장에서 필요한`, `~에 위치한` → `~에 있는`, `바닥으로부터` → `바닥에서`.
- `~ 중에 있다`는 행위 주체와 대상을 구분한다. `시는 센터를 건립 중에 있다.` → `시는 센터를 건립하고 있다.` 대상이 주어인 `센터는 건립 중에 있다.`는 그대로 두거나 `센터는 건립되고 있다.`로 다듬는다. `후보들 중에 있는 한 명을 고른다.`의 `중에`는 집합 표현이므로 진행형으로 고치지 않는다.
- 불필요한 `-시키다`는 줄이되 실제 사동은 보존한다: `절차를 개선시키다` → `절차를 개선하다`; `아이를 의자에 앉히다`는 아이에게 동작을 시키는 뜻이므로 유지한다. `-고 있다`도 진행·지속 의미가 없을 때만 줄이며, `현재 센터를 운영하고 있다.`처럼 현재 상태를 밝히는 표현은 보존한다.
- Remove a generic translated `당신` when Korean would omit the reader. Keep direct address in responsibility or safety instructions.
- Avoid calqued concept nouns: use `말투` or `문체` for a writer's voice unless the field uses `목소리`.
- Replace `~하는 데 도움이 됩니다` with the concrete effect only when the source states that effect.
- Move the main claim forward or split a dense modifier. Do not copy English sentence boundaries mechanically.

### K3. Handle subjects, pronouns, passives, and plurality naturally

- Omit a subject only when the actor remains clear. Repeat the relevant noun when two actors could be confused.
- Do not add `그의`, `그녀의`, `그들의`, or plural `들` mechanically.
- Do not make a thing or abstraction act like a person where Korean would not: `설문 결과는 만족도가 높다는 점을 말해 준다` → `설문 결과에서 만족도가 높다는 점을 알 수 있다`; `이 기술은 빠른 처리를 가능하게 한다` → `이 기술로 빠르게 처리할 수 있다`. Keep the claim's strength.
- Preserve a deliberate subject when it marks contrast, responsibility, or accountability.
- Passive voice is valid when the actor is unknown, unimportant, or not the focus.
- Remove unnecessary translation-like passives: `보여지다` often becomes `보이다`, and `되어지다` becomes `되다`.
- Consider changing `A에 의해 B가 ...되었다` to `A가 B를 ...했다` only when it preserves emphasis.

### K4. Prefer verbs to abstract noun stacks

- Prefer concrete verbs and predicates when meaning stays the same: `검토를 진행하다` → `검토하다`; revise repeated `가능성`, `중요성`, `필요성`, `효율성`, and `연관성` likewise.
- 명사 위주 표현은 뜻이 같을 때 서술어로 푼다: `절감이 가능하다` → `줄일 수 있다`, `자체안의 경우` → `자체안은`, `불참한 관계로` → `불참해서`. `~ 시`는 시제·조건에 맞춘다: `향후 방한 시 협의할 예정이다.` → `향후 방한할 때 협의할 예정이다.` 과거 방문을 말할 때만 `방한했을 때`를 쓴다.
- Thin a run of `의`: drop one (`기존의 교과 위주의 수업` → `기존의 교과 위주 수업`) or restore the subject or object particle (`급여의 지급을 위하여` → `급여를 지급하기 위하여`).
- Treat cramped or repeated middle-dot noun chains, not the number of items, as a review signal. Preserve every distinct item; unfold the chain only when it improves readability.
- Trim plain redundancy such as `약 30여 명` → `30여 명`, `매년마다` → `매년`, and `새로운 신제품` → `신제품`. Leave settled expressions that Korean norms accept, such as `피해를 입다`, `박수를 치다`, `결실을 맺다`, and `미리 예약하다`, and leave repetition the writer uses for emphasis.
- Keep defined concepts and any distinct interpretation, instruction, or commitment.

### K5. Review Korean stock AI phrases in context

Treat these as review triggers, not banned words:

- `단순히 ...를 넘어`, `...에 그치지 않고`
- `혁신적인`, `획기적인`, `놀라운`, `뛰어난`, `고무적인`, `괄목할 만한`, `무궁무진한`
- `새로운 패러다임을 제시합니다`, `중요한 시사점을 제공합니다`
- `앞으로의 귀추가 주목됩니다`, `밝은 미래가 기대됩니다`
- `오늘날 빠르게 변화하는 환경에서`, `현대 사회에서 그 중요성이 커지고 있습니다`
- Unsupported or repeated `해당`, `효과적으로`, `~를 자랑합니다`, `~에 자리 잡은`
- Business loanwords piled up as decoration, such as `니즈`, `솔루션`, `시너지`, `로드맵`. Review them only when several stack up without content. Keep them when they are the writer's or the field's habitual vocabulary, a settled loanword (`서비스`, `플랫폼`), a product or policy name, or a defined term. Never replace a loanword for purity alone.
- `다양한 X` with no named variety: name the actual kinds when the source gives them, and delete the modifier otherwise. Swapping in `여러` is the same laundering. Keep it only when variety itself is the claim.
- Remove `성공적으로` when completion proves success (`복구를 성공적으로 완료했다` → `복구를 마쳤다`); keep it when success versus completion or attempt is a separate fact.
- `단순한 X가 아니라 Y` used to inflate Y. Keep a sentence that really contrasts two options; drop the frame when X is a strawman no reader would assume.
- Empty `결론적으로`, `요약하자면`, paragraph-closing `이처럼` or `이렇듯`, and `~라고 해도 과언이 아니다`
- Repeated `~할 수 있습니다` when it does not express real ability, permission, or uncertainty
- Chatbot residue such as `물론입니다!`, `좋은 질문입니다`, `도움이 되셨기를 바랍니다`, `궁금한 점이 있으시면 언제든지`, `오늘은 ~ 결과를 말씀드리겠습니다`
- Repeated `첫째`, `둘째`, `셋째` when the structure is not useful

Judge triggers internally, not as banned words or an audit checklist. Rewrite generic, unsupported, redundant, or mismatched wording; keep content-bearing quotes, evaluations, terms, courtesy, accountability, safety emphasis, and deliberate narrator or attributed-speaker voice. Institutional authorship neither proves nor excuses hype. Keep a formulaic pledge only for needed reassurance or a source-stated action; otherwise cut it, never inventing a measure.

Delete a flagged evaluation if no verifiable information or needed stance is lost. Do not launder a cliché with a softer synonym: `놀라운 잠재력` → `주목할 만한 잠재력` has the same problem.

Cut adjacent phrases that merely repeat the same courtesy or structural act. Preserve different speech acts, relationship cues, deliberate repetition, and safety emphasis; do not edit to a phrase count.

Preserve the proposition and stance. If a trigger's function remains unclear, read [the Korean genre guide](references/korean-genres.md).

### K6. Use particles and connective endings for meaning

- Remove repeated `또한`, `그리고`, `그러나`, and `한편` when the relation is already clear.
- Break chains of `~하며`, `~하면서`, `~함으로써`, and `~하는 가운데` when they hide logic.
- Keep connectors that carry cause, condition, concession, sequence, or contrast.
- 접속어가 원문의 논리와 맞는지 확인한다. `그러나`·`하지만`은 대조나 양보에, `따라서`는 원인·이유·근거에 따른 결론이나 논리적 귀결에 쓸 수 있다. `모든 정사각형은 직사각형이다. 이 도형은 정사각형이다. 따라서 이 도형은 직사각형이다.`의 `따라서`는 보존한다. 관계가 분명할 때만 고치며, 원문의 인과·추론 관계를 만들거나 지우지 않는다.
- Give joined items the same grammatical shape, and give each listed object a verb it fits: `평화 수호와 인권을 보장하는 것` → `평화를 수호하고 인권을 보장하는 것`.
- `-지 않다`와 `-지 못하다`를 구분한다. `검증을 진행하지 않았다.`는 실행하지 않았다는 뜻이며 `검증을 진행하지 못했다.`로 바꾸면 실행할 수 없었다는 뜻을 더할 수 있다. 원문에 없는 실패·능력·원인을 추정하지 않는다.
- Avoid attaching every topic to `~은/는`; use the particle that matches its role.

### K7. Use field-appropriate terminology

Keep a correct and consistent Korean or English term. Do not translate it merely because it is English or replace it for variety.

When the task requires choosing, translating, correcting, or explaining an unsettled specialist term, read [the terminology router](references/terminology/index.md). Stop when its quick map resolves the choice; read a matching field guide only for unresolved detail. Never translate code, model names, product names, API fields, paths, commands, standards identifiers, or citation keys.

### K8. Set Korean sentence boundaries and rhythm

- Split sentences that carry several actors, conditions, exceptions, and conclusions.
- Break long comma and connective-ending chains when doing so makes the relation clearer.
- Merge clipped fragments that imitate English emphasis but sound abrupt in Korean.
- Keep related information together when splitting would hide cause, scope, or contrast.
- Put a modifier right before the word it modifies and resolve two-way readings: `일자리 기업의 홍보 기회` → `기업의 일자리 홍보 기회`. If the source itself is ambiguous, keep it and flag it instead of choosing a reading.
- Rebuild paragraphs when several sentences repeat one topic plus abstract conclusions. State each source-supported predicate once; keep distinct explanation, contrast, or uncertainty.
- Vary sentence length, structure, or endings only to clarify rhythm or logic, not for surface variety.
- Remove a conclusion only when it adds no claim, stance, decision, or audience function.
- Preserve Korean quotation and title marks such as `“ ”`, `‘ ’`, `「 」`, and `『 』`.
- Do not normalize notation that Korean norms allow both ways: `3~5` and `3-5`, `2 m` and `2m`, six-dot and three-dot ellipses. Keep the final period in a date such as `2024. 5. 1.`.
- A dash-set aside is valid Korean punctuation. Reduce only a pile-up, and never apply the English dash rule to Korean sentences.
- Korean marks emphasis with single quotation marks; double marks are for speech and quotations. Change double marks to single only when the span is clearly emphasis, not a quotation or title. Rewrite an English-style colon inside a sentence (`핵심은 하나다: 속도다`) as a sentence; keep a label colon such as `일시: 5월 1일`.

### K9. Write for speaking when needed

For a substantial spoken rewrite, or when a spoken cue's audience function is unclear, read [the Korean genre guide](references/korean-genres.md). Keep useful navigation and audience cues, but remove empty staging. Keep `오늘은` when it marks a real date or contrast.

### K10. Handle high-stakes text carefully

Precision, scope, status, and limitations take priority over smoothness. Use the fidelity routing condition below; a medical, legal, scientific, or financial topic alone does not require an extra guide.

### Final Korean pass

During the source comparison below, check that:

1. Overall politeness, register shifts, and honorifics fit the speaker and audience.
2. Facts, exact tokens, status, negation, scope, attribution, limitations, evaluation, and commitment retain their meaning.
3. English-specific rules were not imposed; specialist terms remain consistent.
4. Korean syntax, sentence boundaries, and quotation marks are natural and unambiguous.
5. Empty frames, repeated abstract conclusions, and K5 triggers were handled without erasing meaning.
6. No synonym-only cliché swaps, redundant courtesy, or needless additions remain.

## Load only the needed reference

The Korean checkpoints above are always active. Load extra references only when the text calls for them.

- **Unresolved genre choices:** Read [the Korean genre guide](references/korean-genres.md) when boilerplate, deliberate voice, repetition, or an audience cue remains unclear, or for a substantial spoken, approved-marketing, or safety rewrite. A routine email or presentation with clear register and courtesy does not trigger it.
- **Difficult or high-risk fidelity:** Read [the fidelity review guide](references/fidelity-review.md) when the text has several interacting facts, constraints, attributions, or status claims, or when an error would carry high stakes. One ordinary number or English token alone does not trigger the guide.
- **Substantial English prose:** Read [upstream's English patterns](references/english-patterns.md) once. English product names, code, identifiers, citations, and established technical terms inside Korean text do not trigger this reference; it is for text where English forms a substantial prose span.
- **Unsettled specialist terminology:** Read [the terminology router](references/terminology/index.md) only when the task requires choosing, translating, correcting, or explaining a field-specific term. Stop when its quick map resolves the term; read a matching field guide only for unresolved detail. Do not load terminology guidance merely to preserve terms the source already uses consistently.

Reuse unchanged references already present in context. Apply their relevant checks within the same source comparison, not as separate full review passes.

## Editing priorities

For Korean prose, build natural Korean around source-supported predicates by revising sentence and paragraph shape, not by replacing watched words one by one.

- Remove unsupported hype, sweeping importance claims, unwanted sales framing, vague attribution, and generic conclusions. Keep an approved marketing voice, a sourced evaluation, or a personal reaction when the genre calls for it.
- Cut repetitive openings, forced groups, fake contrasts, canned transitions, filler, stacked hedges, and chatbot greetings or closings.
- In any language, remove decorative formatting the genre does not use: bold scattered over ordinary phrases, a bold label that restates the sentence after it (`**성능:** 성능이 향상됐다`), emoji on headings or bullets, and headings over a few short paragraphs. Keep structure the medium relies on, such as a README, slides, or a list of real parallel items, and keep the writer's own emoji in casual messages.
- Prefer concrete subjects and verbs, but keep a passive, formal term, repetition, or unusual rhythm when it serves the meaning or the writer's voice.
- Treat watched phrases as review triggers, not banned words. Do not treat one formal word, ordinary courtesy, an official commitment, a safety emphasis, or a personal metaphor as proof of AI writing. Judge the phrase in context.
- Add personality only when the genre and source voice call for it. Keep technical, legal, medical, scientific, financial, policy, and reference text precise.

## Output contract

- **Rewrite requested:** Return only the final rewrite unless explanation is requested. Do not announce the skill, show internal analysis, or add a closing offer.
- **Review, comparison, or explanation only:** Return the requested findings or explanation. Do not add a full rewrite or modify files unless requested.
- **File editing requested:** Edit prose only, preserve non-prose structure, then give a short summary. Naming a file alone is not an editing request.
- **Embedded use:** Return only the finished text required by the parent task.

## Fast rewrite process

For review-only requests, apply the relevant criteria to the supplied text and report findings; do not run a rewrite workflow.

1. Identify hard constraints, genre, stance, and requested edit strength internally. Default to balanced editing; accuracy wins.
2. Apply K1-K10 to Korean prose and load only the selected references. Default to one whole-passage rewrite, preserving facts, limitations, stance, and caution. A limiting negative such as `입증되지 않았다` is a claim, not filler.
3. Compare the draft with the source, combining the Final Korean pass and any relevant reference checks. Correct actual mismatches, then recheck the affected content and its dependencies. Finish when no known editing error remains; do not repeat full rewrites or checks without a new issue. If source ambiguity prevents a faithful correction, preserve that wording and briefly identify the unresolved point rather than guess or loop.
4. Return the result under the output contract. Do not narrate these steps.

When source and draft are available and a comparison audit is requested, or the text is precision-sensitive and dense with numbers or technical tokens, `scripts/check-rewrite.py` may assist the source comparison. Resolve it relative to this file. It reports surface candidates, not semantic verdicts: inspect candidates, fix real mismatches, and rerun only when changes could affect its results. Do not damage correct prose to satisfy a regex. The checker is optional; comparing meaning is required for every rewrite.

## Source

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The English reference follows the upstream release recorded in `.upstream-version`. This fork adds the Korean checkpoints K1-K10 for Korean word order, subjects, particles, register, sentence endings, rhythm, and terminology.
