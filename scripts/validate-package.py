#!/usr/bin/env python3
"""Check the humanizer-ko package files without external dependencies."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
ENGLISH_PATTERNS = (ROOT / "references" / "english-patterns.md").read_text(
    encoding="utf-8"
)
README = (ROOT / "README.md").read_text(encoding="utf-8")
AGENTS = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
OPENAI_AGENT = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
MARKETPLACE = json.loads(
    (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
)
PLUGIN_SKILL = ROOT / "skills" / "humanizer-ko" / "SKILL.md"
PLUGIN_ENGLISH_PATTERNS = (
    ROOT / "skills" / "humanizer-ko" / "references" / "english-patterns.md"
)


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must begin with YAML metadata",
).group(1)

for unsupported_field in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Remove unsupported YAML field: {unsupported_field[:-1]}")

skill_name = require_match(
    re.search(r"(?m)^name:\s*([^\s]+)\s*$", yaml_metadata),
    "Add name to SKILL.md",
).group(1)
if skill_name != "humanizer-ko":
    raise SystemExit("Use humanizer-ko as the skill ID")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', yaml_metadata),
    "Add metadata.version to SKILL.md",
).group(1)
readme_version = require_match(
    re.search(
        r"(?m)^- \*\*v?([0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?)\*\*",
        README,
    ),
    "Add a version entry to README.md",
).group(1)

package_versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(package_versions) != 1:
    raise SystemExit(
        f"Use one package version in all files: {sorted(package_versions)}"
    )

if PLUGIN_SKILL.is_symlink():
    plugin_skill_is_linked = PLUGIN_SKILL.resolve() == (ROOT / "SKILL.md").resolve()
else:
    index_entry = subprocess.run(
        ["git", "ls-files", "-s", "--", "skills/humanizer-ko/SKILL.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    plugin_skill_is_linked = (
        index_entry.returncode == 0
        and index_entry.stdout.startswith("120000 ")
        and PLUGIN_SKILL.read_text(encoding="utf-8").strip() == "../../SKILL.md"
    )

if PLUGIN.get("name") != "humanizer-ko":
    raise SystemExit("Use humanizer-ko as the Claude plugin ID")

marketplace_plugins = MARKETPLACE.get("plugins", [])
if (
    MARKETPLACE.get("name") != "humanizer-ko"
    or len(marketplace_plugins) != 1
    or marketplace_plugins[0].get("name") != "humanizer-ko"
):
    raise SystemExit("Use humanizer-ko as the Claude marketplace and entry ID")

if (
    'display_name: "humanizer-ko"' not in OPENAI_AGENT
    or "$humanizer-ko" not in OPENAI_AGENT
):
    raise SystemExit("Display humanizer-ko and invoke the skill as $humanizer-ko")

if not plugin_skill_is_linked:
    raise SystemExit("Link skills/humanizer-ko/SKILL.md to the root SKILL.md")

if ENGLISH_PATTERNS != PLUGIN_ENGLISH_PATTERNS.read_text(encoding="utf-8"):
    raise SystemExit("Keep both copies of english-patterns.md byte-for-byte identical")

if "](references/english-patterns.md)" not in SKILL:
    raise SystemExit("Link the English pattern reference from SKILL.md")

plain_language_rules = (
    "## Writing style",
    "Lead with the main point.",
    "Use common words and active voice.",
    "Keep sentences and paragraphs short.",
    "Use `must` for requirements.",
    "Keep the full technical meaning.",
)
missing_plain_language_rules = [
    rule for rule in plain_language_rules if rule not in AGENTS
]
if missing_plain_language_rules:
    raise SystemExit(
        "Add the missing Plain Language rules to AGENTS.md: "
        + ", ".join(missing_plain_language_rules)
    )

pattern_numbers = [
    int(number)
    for number in re.findall(r"(?m)^### ([0-9]+)\. ", ENGLISH_PATTERNS)
]
if pattern_numbers != list(range(1, 36)):
    raise SystemExit(
        f"Number english-patterns.md patterns from 1 through 35: {pattern_numbers}"
    )

if re.search(r"(?m)^### ([0-9]+)\. ", SKILL):
    raise SystemExit("Keep detailed English patterns out of the routing SKILL.md")

readme_numbers = {
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
}
if readme_numbers != set(range(1, 36)):
    raise SystemExit("List patterns 1 through 35 in the README table")

if len(SKILL.splitlines()) > 260:
    raise SystemExit("Keep SKILL.md (body with K1-K10) at 260 lines or fewer")

print(f"humanizer-ko package v{skill_version} is valid")
