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
  version: "2.11.1-ko.6"
---

# humanizer-ko

Rewrite AI-like prose so it sounds like the writer. Keep the meaning, facts, and voice. Use this as an editing aid, not as a promise to bypass AI detectors.

The host has already loaded this file. Do not open `SKILL.md` again during the task.

## Non-negotiable constraints

1. Preserve every fact, number, unit, date, name, quote, citation, URL, identifier, and technical limitation.
2. Preserve tense, modality, negation, scope, attribution, and completion status. Do not turn *planned* into *completed*, *may* into *does*, correlation into causation, a prototype into a product, or a preliminary result into a verified claim.
3. Preserve the source's viewpoint, evaluation, emotion, commitment, and degree of certainty. Lower unsupported intensity without deleting the underlying proposition or making the writer sound indifferent.
4. Do not invent support, examples, opinions, experiences, or specifics. Fiction is exempt because invention is the task.
5. Match the source's genre, register, and writing sample. A supplied sample overrides general style preferences unless it conflicts with accuracy or the user's explicit request.
6. Keep code blocks, commands, paths, schema fields, link targets, product names, approved copy, and established technical tokens unchanged unless the user asks to edit them.

## Load only the needed reference

Decide by the language of the requested output, not by isolated borrowed words.

- **Korean source or Korean output:** Read [the Korean editing guide](references/korean-editing.md) once and apply K1-K10.
- **Genre-sensitive Korean prose:** Also read [the Korean genre guide](references/korean-genres.md) for email, notices, support text, presentations, personal writing, approved marketing copy, or safety instructions. Read it when a phrase may be either boilerplate or intentional voice.
- **Fact-dense or high-risk text:** Read [the fidelity review guide](references/fidelity-review.md) when the text contains factual claims, technical tokens, negation, limitations, status, attribution, or other wording that must survive the rewrite. A short casual passage without those constraints does not need it.
- **Substantial English prose:** Read [the 35 English patterns](references/english-patterns.md) once.
- **Mixed prose:** Read each language guide only when that language forms a substantial prose span. English product names, code, identifiers, citations, and established technical terms inside Korean text do not trigger the English reference.
- **Unsettled specialist terminology:** Read [the domain terminology guide](references/domain-terminology.md) only when the task requires choosing or translating a field-specific term. Do not read it merely to preserve terms the source already uses consistently.

Do not read the same reference more than once in one task.

## Editing priorities

Rewrite the passage as a whole instead of replacing watched words one by one.

- Remove unsupported hype, sweeping importance claims, unwanted sales framing, vague attribution, and generic conclusions. Keep an approved marketing voice, a sourced evaluation, or a personal reaction when the genre calls for it.
- Cut repetitive openings, forced groups, fake contrasts, canned transitions, filler, stacked hedges, and chatbot greetings or closings.
- Prefer concrete subjects and verbs, but keep a passive, formal term, repetition, or unusual rhythm when it serves the meaning or the writer's voice.
- Treat watched phrases as review triggers, not banned words. Do not treat one formal word, ordinary courtesy, an official commitment, a safety emphasis, or a personal metaphor as proof of AI writing. Judge the phrase in context.
- Add personality only when the genre and source voice call for it. Keep technical, legal, medical, scientific, financial, policy, and reference text precise.

## Context-aware Korean review gate

Before returning Korean prose, run the K5 review in the Korean guide. Rewrite an expression only when it is generic, unsupported, redundant, or mismatched to the genre. Keep it when it carries a quote, approved copy, evidence, attribution, technical meaning, ordinary courtesy, an official promise, safety emphasis, or deliberate personal voice.

Do not pass a phrase scan by deleting the sentence that contains it. Preserve the concrete claim and the writer's stance. A clean lexical scan is not more important than fidelity.

## Output contract

- **Ordinary pasted text:** Return only the final rewrite. Do not announce the skill, explain that you will apply it, show analysis, or add a closing offer.
- **Audit, comparison, or explanation requested:** Show only the material needed for that request, followed by the final rewrite.
- **Named file:** Edit prose only, preserve non-prose structure, then give a short summary.
- **Embedded use:** Return only the finished text required by the parent task.

## Fast rewrite process

1. Record hard constraints and the source's genre, stance, and intended edit strength. Use a balanced edit unless the user requests lighter or stronger intervention; accuracy always wins.
2. Load only the references selected above and rewrite the passage as a whole.
3. Compare the draft with the source. Check hard tokens, claims, status, limitations, stance, and justified K5 phrases.
4. Return the result under the output contract. Do not narrate these steps.

## Source

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The English reference preserves upstream Humanizer v2.11.1's 35 patterns. The Korean guide adds K1-K10 for Korean word order, subjects, particles, register, sentence endings, rhythm, and terminology.
