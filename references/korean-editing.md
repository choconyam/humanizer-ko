# Korean editing guide

Use this guide for Korean source text or Korean output. Keep upstream's language-independent checks, but do not transfer English grammar, capitalization, dash, quote, or subject rules mechanically.

For an ordinary Korean rewrite:

1. Preserve facts, status, limitations, stance, and intended voice.
2. Rebuild translation-like clauses as Korean sentences instead of swapping watched words.
3. Run the context-aware K5 review before returning the text.

If the source says `센터는 다음 달 문을 열 예정입니다`, do not strengthen it to a completed or guaranteed event.

## K1. Keep one register and honorific level

- Choose the register from the source and audience, then keep it consistent.
- Preserve honorifics, titles, role names, and the relationship between writer and reader.
- Do not mix `-다`, `-해요`, and `-합니다` without a real change in speaker or quoted material.
- Formal repetition is acceptable when changing endings would make the text less precise.

## K2. Rebuild translation-like word order

- Replace repeated `이는 ...를 의미합니다` with the concrete statement when the source supports it.
- Break chains built from `~에 대한`, `~를 통해`, `~와 관련하여`, `~에 기반하여`, and `~에 있어`.
- `의미를 가지다` often becomes `의미가 있다`; `문제가 존재하다` often becomes `문제가 있다`.
- Remove a generic translated `당신` when Korean would omit the reader. Keep direct address in responsibility or safety instructions.
- Watch concept nouns calqued from English, such as `목소리` used for a writer's voice. Prefer the established Korean word (`말투`, `문체`) unless the field's standard term really is the loan.
- Replace `~하는 데 도움이 됩니다` with the concrete effect only when the source states that effect.
- Move the main claim forward or split a dense modifier. Do not copy English sentence boundaries mechanically.

## K3. Handle subjects, pronouns, passives, and plurality naturally

- Omit a subject only when the actor remains clear. Repeat the relevant noun when two actors could be confused.
- Do not add `그의`, `그녀의`, `그들의`, or plural `들` mechanically.
- Preserve a deliberate subject when it marks contrast, responsibility, or accountability.
- Passive voice is valid when the actor is unknown, unimportant, or not the focus.
- Remove unnecessary translation-like passives: `보여지다` often becomes `보이다`, and `되어지다` becomes `되다`.
- Consider changing `A에 의해 B가 ...되었다` to `A가 B를 ...했다` only when it preserves emphasis.

## K4. Prefer verbs to abstract noun stacks

- `검토를 진행하다` usually becomes `검토하다`.
- Turn repeated `가능성`, `중요성`, `필요성`, `효율성`, and `연관성` into concrete predicates when meaning stays the same.
- A repeated middle-dot chain that joins three or more nouns (`사실·수치·인용` style) signals a noun stack. Keep it where the genre expects it — official notices, headlines, technical specifications — and otherwise trim the list or unfold it into a sentence.
- Keep a noun when it is a defined concept or when changing it would strengthen the claim.
- Do not shorten a sentence by deleting its interpretation, instruction, or commitment.

## K5. Review Korean stock AI phrases in context

Treat these as review triggers, not banned words:

- `단순히 ...를 넘어`, `...에 그치지 않고`
- `혁신적인`, `획기적인`, `놀라운`, `뛰어난`, `고무적인`, `괄목할 만한`, `무궁무진한`
- `새로운 패러다임을 제시합니다`, `중요한 시사점을 제공합니다`
- `앞으로의 귀추가 주목됩니다`, `밝은 미래가 기대됩니다`
- `오늘날 빠르게 변화하는 환경에서`, `현대 사회에서 그 중요성이 커지고 있습니다`
- Unsupported or repeated `해당`, `효과적으로`, `~를 자랑합니다`, `~에 자리 잡은`
- `다양한 X` with no named variety: name the actual kinds when the source gives them, and delete the modifier otherwise. Swapping in `여러` is the same laundering. Keep it only when variety itself is the claim.
- `성공적으로` before a completion verb is redundant: `복구를 성공적으로 완료했다` becomes `복구를 마쳤다`.
- `단순한 X가 아니라 Y` used to inflate Y. Keep a sentence that really contrasts two options; drop the frame when X is a strawman no reader would assume.
- Empty `결론적으로`, `요약하자면`, paragraph-closing `이처럼` or `이렇듯`, and `~라고 해도 과언이 아니다`
- Repeated `~할 수 있습니다` when it does not express real ability, permission, or uncertainty
- Chatbot residue such as `물론입니다!`, `좋은 질문입니다`, `도움이 되셨기를 바랍니다`, `궁금한 점이 있으시면 언제든지`, `오늘은 ~ 결과를 말씀드리겠습니다`
- Repeated `첫째`, `둘째`, `셋째` when the structure is not useful

Rewrite a trigger only when it is generic, unsupported, redundant, or wrong for the genre. Keep it when it is a direct quote, proper name, supported or attributed evaluation, field term, approved copy, ordinary courtesy, an official commitment that names a concrete action, safety emphasis, or deliberate personal voice grounded in the writer's own first-person experience. To keep a trigger, name which of these reasons applies; if none fits, rewrite it. Formulaic resolve or vision closings — `확고한 의지`, `더 나은 ~를 만들어가겠습니다` with no concrete measure — are decoration, not commitments: state the action or end on the last fact.

Apply a deletion test before rewording a flagged evaluation: if removing it costs no verifiable information and no stance the writer needs, delete it instead of softening it. `놀라운 잠재력` → `주목할 만한 잠재력` and `귀중한 인사이트` → `의미 있는 단서` launder the cliché rather than fix it.

One function, one expression. When several phrases perform the same social or structural function — thanks, apology, softened request, greeting, closing, transition — keep the single expression the relationship and genre require and cut the rest. A polite email usually needs one act of thanks, not three.

Do not delete the sentence to pass the scan. Preserve the proposition and stance, and do not replace one stock phrase with another vague metaphor or a softer synonym. Read [the Korean genre guide](korean-genres.md) when the phrase's function depends on genre.

## K6. Use particles and connective endings for meaning

- Remove repeated `또한`, `그리고`, `그러나`, and `한편` when the relation is already clear.
- Break chains of `~하며`, `~하면서`, `~함으로써`, and `~하는 가운데` when they hide logic.
- Keep connectors that carry cause, condition, concession, sequence, or contrast.
- Do not rotate particles or endings merely for variety.
- Avoid attaching every topic to `~은/는`; use the particle that matches its role.

## K7. Use field-appropriate terminology

Keep a correct and consistent Korean or English term. Do not translate it merely because it is English or replace it for variety.

When the task requires choosing, translating, correcting, or explaining an unsettled specialist term, read [the terminology router](terminology/index.md). Stop when its quick map resolves the choice; read a matching field file only for unresolved detail. Never translate code, model names, product names, API fields, paths, commands, standards identifiers, or citation keys.

## K8. Set Korean sentence boundaries and rhythm

- Split sentences that carry several actors, conditions, exceptions, and conclusions.
- Break long comma and connective-ending chains when doing so makes the relation clearer.
- Merge clipped fragments that imitate English emphasis but sound abrupt in Korean.
- Keep related information together when splitting would hide cause, scope, or contrast.
- Let paragraph breaks follow changes in idea, speaker, time, or argument.
- Remove a conclusion only when it adds no claim, stance, decision, or audience function.
- Preserve Korean quotation and title marks such as `“ ”`, `‘ ’`, `「 」`, and `『 』`.

## K9. Write for speaking when needed

For presentations, lectures, interviews, and narration, read [the Korean genre guide](korean-genres.md). Keep useful navigation and audience cues, but remove empty staging. Keep `오늘은` when it marks a real date or contrast.

## K10. Handle high-stakes text carefully

For medical, legal, scientific, financial, policy, safety, compliance, tax, accounting, or other high-risk text, read [the fidelity review guide](fidelity-review.md). Precision, scope, status, and limitations take priority over smoothness.

## Final Korean pass

Check that:

1. Register and honorific level are consistent.
2. Facts, exact tokens, status, negation, scope, attribution, limitations, evaluation, and commitment retain their meaning.
3. English-specific rules were not imposed mechanically.
4. Word order, subjects, passives, particles, and connective endings are natural and unambiguous.
5. Every remaining K5 trigger has a clear reason.
6. Specialist terms remain correct and consistent.
7. Sentence boundaries and quotation marks fit Korean usage.
8. No flagged phrase was replaced with a softer synonym, no courtesy function appears twice, and the rewrite is not longer than the source without a reason.
