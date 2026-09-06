---
name: humanizer-ko
description: |
  Rewrite Korean or English text that sounds AI-generated while keeping the
  writer's facts, meaning, and voice. Use when humanizing prose, polishing Korean
  presentation scripts, or reviewing text for inflated claims, translation-like
  phrasing, stock AI words, filler, and chatbot artifacts. Based on Wikipedia's
  "Signs of AI writing."
license: MIT
metadata:
  version: "2.11.1-ko.12"
---

# humanizer-ko

Rewrite AI-like prose so it sounds like the writer. Keep the meaning, facts, and voice. Use this as an editing aid, not as a promise to bypass AI detectors.

Korean is this skill's primary target: the K1-K10 checkpoints below apply to any Korean source or output. The upstream English patterns live in a reference and load only when the text has substantial English prose.

The host has already loaded this file. Do not open `SKILL.md` again during the task.

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
- Remove a generic translated `당신` when Korean would omit the reader. Keep direct address in responsibility or safety instructions.
- Avoid calqued concept nouns: use `말투` or `문체` for a writer's voice unless the field uses `목소리`.
- Replace `~하는 데 도움이 됩니다` with the concrete effect only when the source states that effect.
- Move the main claim forward or split a dense modifier. Do not copy English sentence boundaries mechanically.

### K3. Handle subjects, pronouns, passives, and plurality naturally

- Omit a subject only when the actor remains clear. Repeat the relevant noun when two actors could be confused.
- Do not add `그의`, `그녀의`, `그들의`, or plural `들` mechanically.
- Preserve a deliberate subject when it marks contrast, responsibility, or accountability.
- Passive voice is valid when the actor is unknown, unimportant, or not the focus.
- Remove unnecessary translation-like passives: `보여지다` often becomes `보이다`, and `되어지다` becomes `되다`.
- Consider changing `A에 의해 B가 ...되었다` to `A가 B를 ...했다` only when it preserves emphasis.

### K4. Prefer verbs to abstract noun stacks

- Prefer concrete verbs and predicates when meaning stays the same: `검토를 진행하다` → `검토하다`; revise repeated `가능성`, `중요성`, `필요성`, `효율성`, and `연관성` likewise.
- Treat cramped or repeated middle-dot noun chains, not the number of items, as a review signal. Preserve every distinct item; unfold the chain only when it improves readability.
- Keep defined concepts and any distinct interpretation, instruction, or commitment.

### K5. Review Korean stock AI phrases in context

Treat these as review triggers, not banned words:

- `단순히 ...를 넘어`, `...에 그치지 않고`
- `혁신적인`, `획기적인`, `놀라운`, `뛰어난`, `고무적인`, `괄목할 만한`, `무궁무진한`
- `새로운 패러다임을 제시합니다`, `중요한 시사점을 제공합니다`
- `앞으로의 귀추가 주목됩니다`, `밝은 미래가 기대됩니다`
- `오늘날 빠르게 변화하는 환경에서`, `현대 사회에서 그 중요성이 커지고 있습니다`
- Unsupported or repeated `해당`, `효과적으로`, `~를 자랑합니다`, `~에 자리 잡은`
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
- Keep `-지 않다` distinct from `-지 못하다`: `진행하지 않았다` ≠ `진행하지 못했다`. Do not turn nonoccurrence into failure or infer inability or cause.
- Avoid attaching every topic to `~은/는`; use the particle that matches its role.

### K7. Use field-appropriate terminology

Keep a correct and consistent Korean or English term. Do not translate it merely because it is English or replace it for variety.

When the task requires choosing, translating, correcting, or explaining an unsettled specialist term, read [the terminology router](references/terminology/index.md). Stop when its quick map resolves the choice; read a matching field guide only for unresolved detail. Never translate code, model names, product names, API fields, paths, commands, standards identifiers, or citation keys.

### K8. Set Korean sentence boundaries and rhythm

- Split sentences that carry several actors, conditions, exceptions, and conclusions.
- Break long comma and connective-ending chains when doing so makes the relation clearer.
- Merge clipped fragments that imitate English emphasis but sound abrupt in Korean.
- Keep related information together when splitting would hide cause, scope, or contrast.
- Rebuild paragraphs when several sentences repeat one topic plus abstract conclusions. State each source-supported predicate once; keep distinct explanation, contrast, or uncertainty.
- Vary sentence length, structure, or endings only to clarify rhythm or logic, not for surface variety.
- Remove a conclusion only when it adds no claim, stance, decision, or audience function.
- Preserve Korean quotation and title marks such as `“ ”`, `‘ ’`, `「 」`, and `『 』`.

### K9. Write for speaking when needed

For a substantial spoken rewrite, or when a spoken cue's audience function is unclear, read [the Korean genre guide](references/korean-genres.md). Keep useful navigation and audience cues, but remove empty staging. Keep `오늘은` when it marks a real date or contrast.

### K10. Handle high-stakes text carefully

For medical, legal, scientific, financial, policy, safety, compliance, tax, accounting, or other high-risk text, read [the fidelity review guide](references/fidelity-review.md). Precision, scope, status, and limitations take priority over smoothness.

### Final Korean pass

Check that:

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
- **Substantial English prose:** Read [upstream's 35 English patterns](references/english-patterns.md) once. English product names, code, identifiers, citations, and established technical terms inside Korean text do not trigger this reference; it is for text where English forms a substantial prose span.
- **Unsettled specialist terminology:** Read [the terminology router](references/terminology/index.md) only when the task requires choosing, translating, correcting, or explaining a field-specific term. Stop when its quick map resolves the term; read a matching field guide only for unresolved detail. Do not load terminology guidance merely to preserve terms the source already uses consistently.

Do not read the same reference more than once in one task.

## Editing priorities

For Korean prose, build natural Korean around source-supported predicates by revising sentence and paragraph shape, not by replacing watched words one by one.

- Remove unsupported hype, sweeping importance claims, unwanted sales framing, vague attribution, and generic conclusions. Keep an approved marketing voice, a sourced evaluation, or a personal reaction when the genre calls for it.
- Cut repetitive openings, forced groups, fake contrasts, canned transitions, filler, stacked hedges, and chatbot greetings or closings.
- Prefer concrete subjects and verbs, but keep a passive, formal term, repetition, or unusual rhythm when it serves the meaning or the writer's voice.
- Treat watched phrases as review triggers, not banned words. Do not treat one formal word, ordinary courtesy, an official commitment, a safety emphasis, or a personal metaphor as proof of AI writing. Judge the phrase in context.
- Add personality only when the genre and source voice call for it. Keep technical, legal, medical, scientific, financial, policy, and reference text precise.

## Context-aware Korean review gate

Use K5 and the Final Korean pass as one gate; do not sacrifice meaning or natural prose to a lexical scan.

## Output contract

- **Ordinary pasted text:** Return only the final rewrite. Do not announce the skill, explain that you will apply it, show analysis, or add a closing offer.
- **Audit, comparison, or explanation requested:** Show only the material needed for that request, followed by the final rewrite.
- **Named file:** Edit prose only, preserve non-prose structure, then give a short summary.
- **Embedded use:** Return only the finished text required by the parent task.

## Fast rewrite process

1. Internally record hard constraints and the source's genre, stance, and intended edit strength. Use a balanced edit unless the user requests lighter or stronger intervention; accuracy always wins.
2. Apply K1-K10 to Korean text, load only the references selected above, and rewrite the passage once as a whole. Remove filler and duplicated courtesy, transitions, or emphasis during that rewrite, but keep facts, limitations, stance, and required caution. A limiting negative such as `입증되지 않았다` is a claim, not filler.
3. Compare the final draft with the source once. Check hard tokens, claims, status, negation, scope, attribution, limitations, stance, and justified K5 phrases. If the user requests an audit or the text is precision-sensitive and dense with numbers or technical tokens, the optional checker may help: resolve `scripts/check-rewrite.py` relative to this `SKILL.md` and run it on the source and final draft. Its output lists surface-level candidates, not factual or semantic verdicts. Inspect every candidate against the source, fix real mismatches, and rerun once if the draft changed. Do not dismiss a real mismatch, but do not damage correct prose merely to satisfy a regex. Semantic comparison is always required. Skip the checker silently otherwise.
4. Return the result under the output contract. Do not narrate these steps.

## Source

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The English reference preserves upstream Humanizer v2.11.1's 35 patterns. This fork adds the Korean checkpoints K1-K10 for Korean word order, subjects, particles, register, sentence endings, rhythm, and terminology.
