# Guide for agents

This file explains how to change `humanizer-ko` without breaking its package or prompt.

## What this repo contains

`humanizer-ko` is an agent skill written in Markdown. `SKILL.md` is the prompt that agents read. The repo has no build step.

Keep the skill portable. Do not write instructions that limit it to one or two agent tools.

## Key files

- `SKILL.md` is the compact routing prompt and source of truth for behavior and metadata.
- `skills/humanizer-ko/SKILL.md` links to the root skill for Claude Desktop and older plugin loaders. Do not replace the link with a copy or edit it as a separate file.
- `references/english-patterns.md` preserves upstream's numbered 1-35 patterns and examples. `references/korean-editing.md` contains compact K1-K10 guidance. `references/korean-genres.md` handles genre and edit strength, `references/fidelity-review.md` handles meaning and token preservation, and `references/terminology/` routes specialist terminology by field. Their files under `skills/humanizer-ko/references/` are package mirrors and must match exactly.
- `README.md` is the maintained Korean documentation for installation, use, patterns, and version history. It is the repository's only README.
- `.upstream-version` records the upstream release already merged into this fork.
- `NOTICE.md` records upstream attribution and the scope of the localization.
- `.claude-plugin/plugin.json` describes the Claude plugin.
- `.claude-plugin/marketplace.json` lets users add this repo as a Claude marketplace.
- `scripts/check-rewrite.py` is the optional deterministic rewrite check that ships with the skill. It must stay dependency-free and safe to skip.
- `scripts/build-skill-zip.py` builds the symlink-free archive for Claude Desktop uploads.
- `scripts/validate-package.py` checks package files and shared values.
- `scripts/validate-localization.py` checks the Korean guide, attribution, tracked upstream release, and package mirror.

## Rules for changes

Keep `SKILL.md` and `README.md` in sync.

- **Patterns:** Keep the 35 English patterns in `references/english-patterns.md` and K1-K10 in `references/korean-editing.md`. If you add, remove, or renumber one, update the README table, heading, validator, and every reference.
- **Version:** Keep the same version in `SKILL.md` under `metadata.version`, the first README version entry, and `.claude-plugin/plugin.json`. Do not add a top-level `version` field to the skill.
- **Compatibility:** Keep install and use instructions neutral across agents. Names such as Claude Code, OpenCode, and Codex are examples, not limits.
- **History:** Add a short README version note for any behavior change or non-obvious fix. Fold minor doc-only cleanups into the current version's note so the history stays complete instead of leaving them only in the commit log.
- **Reference guides:** Keep every root reference and its plugin package mirror byte-for-byte identical.
- **Upstream sync:** Update `.upstream-version` only after the corresponding upstream tag is merged. Port upstream pattern changes to `references/english-patterns.md` and keep the upstream `LICENSE` unchanged.
- **Checks:** Before publishing, run `python3 scripts/validate-package.py`, `python3 scripts/validate-localization.py`, `python3 scripts/build-skill-zip.py /tmp/humanizer-ko-skill.zip`, `npx skills add . --list`, and `claude plugin validate .`.

## Writing style

Use Plain Language in code comments, prompts, documentation, descriptions, validation messages, and progress reports.

- Lead with the main point.
- Use common words and active voice.
- Keep sentences and paragraphs short.
- Use one term for the same item.
- Use `must` for requirements.
- Use headings, lists, and tables when they help the reader.
- Remove repeated or unnecessary words.
- Limit acronyms and explain technical terms.
- Avoid double negatives.
- Keep exact identifiers, commands, paths, schema fields, quotations, watched phrases, and behavior-bearing examples.
- Keep the full technical meaning.

## Editing the skill

- Keep the YAML metadata valid.
- Treat the prompt below the metadata as the product.
- Prefer a short, clear instruction over another exception or repeated explanation.
