# Guide for agents

This file explains how to change `humanizer-ko` without breaking its package or prompt.

## What this repo contains

`humanizer-ko` is an agent skill written in Markdown. `SKILL.md` is the prompt that agents read. The repo has no build step.

Keep the skill portable. Do not write instructions that limit it to one or two agent tools.

## Key files

- `SKILL.md` is the compact routing prompt and source of truth for behavior and metadata.
- `skills/humanizer-ko/SKILL.md` is the package copy used by Codex, Claude Desktop, and older plugin loaders. Keep it byte-for-byte identical to the root `SKILL.md`; do not edit it separately.
- The Korean K1-K10 checkpoints live in `SKILL.md` itself so they always load. `references/english-patterns.md` holds upstream's numbered English patterns, extracted by `scripts/sync-english-patterns.py`; do not edit it by hand. `references/korean-genres.md` handles genre and edit strength, `references/fidelity-review.md` handles meaning and token preservation, and `references/terminology/` routes specialist terminology by field. Their files under `skills/humanizer-ko/references/` are package mirrors and must match exactly.
- `README.md` is the maintained Korean documentation for installation, use, patterns, and version history. It is the repository's only README.
- `.upstream-version` records the upstream release that `references/english-patterns.md` follows.
- `NOTICE.md` records upstream attribution and the scope of the localization.
- `.claude-plugin/plugin.json` describes the Claude plugin.
- `.claude-plugin/marketplace.json` lets users add this repo as a Claude marketplace.
- `.codex-plugin/plugin.json` describes the Codex skills-only plugin.
- `scripts/check-rewrite.py` is the optional deterministic rewrite check that ships with the skill. It must stay dependency-free and safe to skip.
- `scripts/sync-english-patterns.py` rebuilds `references/english-patterns.md` from an upstream tag. It keeps pattern sections and drops upstream's own workflow, output, and source sections.
- `scripts/build-skill-zip.py` builds the symlink-free archive for Claude Desktop uploads.
- `scripts/validate-package.py` checks package files and shared values.
- `scripts/validate-localization.py` checks the Korean guide, attribution, tracked upstream release, and package mirror.

## Rules for changes

Keep `SKILL.md` and `README.md` in sync.

- **Patterns:** English patterns belong to upstream; change them only by running `scripts/sync-english-patterns.py`. Do not hard-code their count. K1-K10 live in `SKILL.md`; if you add, remove, or renumber one, update the README table, validator, and every reference.
- **Version:** This fork numbers its own releases as `ko-MAJOR.MINOR.PATCH`, independent of upstream. Bump it only when the fork changes. Keep the same version in `SKILL.md` under `metadata.version`, the first README version entry, `.claude-plugin/plugin.json`, and `.codex-plugin/plugin.json`. Do not add a top-level `version` field to the skill.
- **Compatibility:** Keep install and use instructions neutral across agents. Names such as Claude Code, OpenCode, and Codex are examples, not limits.
- **History:** Add a short README version note for any behavior change or non-obvious fix. Fold minor doc-only cleanups into the current version's note so the history stays complete instead of leaving them only in the commit log.
- **Prompt and checker:** Keep essential preservation principles in `SKILL.md` even when a script can detect violations. Put repeated detection logic in the optional `scripts/check-rewrite.py`; skipping it must not weaken the editing contract. Add instructions only when they change a useful decision.
- **Reference guides:** Keep every root reference and its plugin package mirror byte-for-byte identical.
- **Upstream sync:** Do not merge upstream branches or tags into this repo. Fetch the upstream tag and run `python3 scripts/sync-english-patterns.py --tag vX.Y.Z`; it updates the English reference and its mirror, `.upstream-version`, `LICENSE`, and the README badge. Push the upstream tag to `origin` too, because the validators read files from it.
- **Checks:** Before publishing, run `python3 scripts/validate-package.py`, `python3 scripts/validate-localization.py`, `python3 scripts/build-skill-zip.py /tmp/humanizer-ko-skill.zip`, `npx skills add . --list`, and `claude plugin validate .`.

Read only files needed for the requested change. During development, verify affected behavior; use the full package checks before publishing. Fix failures and recheck the affected parts, then stop when required checks pass and known issues are resolved. Do not launch benchmarks or repeat unrelated checks for a wording-only change.

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
