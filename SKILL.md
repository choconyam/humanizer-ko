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
  version: "2.11.1-ko.5"
---

# humanizer-ko

Rewrite AI-like prose so it sounds like the writer. Keep the meaning, facts, and voice. Use this as an editing aid, not as a promise to bypass AI detectors.

The host has already loaded this file. Do not open `SKILL.md` again during the task.

## Non-negotiable constraints

1. Preserve every fact, number, unit, date, name, quote, citation, URL, identifier, and technical limitation.
2. Preserve tense, modality, and completion status. Do not turn *planned* into *completed*, *may* into *does*, a correlation into causation, a prototype into a product, or a preliminary result into a verified claim.
3. Do not invent support, examples, opinions, experiences, or specifics. Fiction is exempt because invention is the task.
4. Match the source's register and the user's writing sample. A supplied sample overrides general style preferences unless it conflicts with accuracy or the user's explicit request.
5. Keep code blocks, commands, paths, schema fields, link targets, product names, and established technical tokens unchanged unless the user asks to edit them.

## Load only the needed reference

Decide by the language of the requested output, not by isolated borrowed words.

- **Korean source or Korean output:** Read [the Korean editing guide](references/korean-editing.md) once and apply K1-K10.
- **Substantial English prose:** Read [the 35 English patterns](references/english-patterns.md) once.
- **Mixed prose:** Read each language guide only when that language forms a substantial prose span. English product names, code, identifiers, citations, and established technical terms inside Korean text do not trigger the English reference.
- **Unsettled specialist terminology:** Read [the domain terminology guide](references/domain-terminology.md) only when the task requires choosing or translating a field-specific term. Do not read it merely to preserve terms the source already uses consistently.

Do not read the same reference more than once in one task.

## Editing priorities

Rewrite the passage as a whole instead of replacing watched words one by one.

- Remove unsupported hype, sweeping importance claims, sales framing, vague attribution, and generic positive conclusions.
- Cut repetitive openings, forced groups, fake contrasts, canned transitions, filler, stacked hedges, and chatbot greetings or closings.
- Prefer concrete subjects and verbs, but keep a passive, formal term, repetition, or unusual rhythm when it serves the meaning or the writer's voice.
- Do not treat polished grammar, one transition, one dash, one formal word, or one formatting choice as proof of AI writing. Look for patterns in context.
- Add personality only when the genre and source voice call for it. Keep technical, legal, medical, scientific, financial, policy, and reference text precise.

## Mandatory Korean residue gate

Before returning Korean prose, search the draft for these expressions and close variants:

`혁신적인`, `획기적인`, `놀라운`, `뛰어난`, `고무적인`, `다양한`, `해당`, `성공적으로`, `효과적으로`, `중요한 시사점`, `무궁무진`, `새로운 패러다임`, `귀추가 주목`, `밝은 미래`, `~라고 해도 과언이 아니다`, `오늘은 ... 알아보겠습니다`, `오늘은 ... 말씀드리겠습니다`, `이번 발표에서는 ... 살펴보겠습니다`, `도움이 되셨기를 바랍니다`, `궁금한 점이 있으시면`, `좋은 질문입니다`, `물론입니다!`

Their presence in the source does not make the promotional framing a fact. Remove or rewrite each occurrence unless it is:

- inside a direct quote or proper name;
- an attributed or evidenced evaluation;
- a necessary field term with that exact meaning; or
- required by the user's requested marketing voice.

Keep the concrete claim underneath. Never invent details merely to replace a vague phrase.

## Output contract

- **Ordinary pasted text:** Return only the final rewrite. Do not announce the skill, explain that you will apply it, show analysis, or add a closing offer.
- **Audit, comparison, or explanation requested:** Show only the material needed for that request, followed by the final rewrite.
- **Named file:** Edit prose only, preserve non-prose structure, then give a short summary.
- **Embedded use:** Return only the finished text required by the parent task.

## Fast rewrite process

1. Record factual and stylistic constraints, including tense, uncertainty, and completion status.
2. Load only the reference selected above and rewrite around the passage's actual point.
3. Check that no claim or status changed. Run the applicable residue check.
4. Return the result under the output contract. Do not narrate these steps.

## Source

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The English reference preserves upstream Humanizer v2.11.1's 35 patterns. The Korean guide adds K1-K10 for Korean word order, subjects, particles, register, sentence endings, rhythm, and terminology.
