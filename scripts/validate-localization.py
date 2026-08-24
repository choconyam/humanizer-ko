#!/usr/bin/env python3
"""Check the Korean localization and its upstream provenance."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
NOTICE = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
GUIDE_NAMES = (
    "korean-editing.md",
    "korean-genres.md",
    "fidelity-review.md",
    "terminology/index.md",
    "terminology/science-materials.md",
    "terminology/software-ml.md",
    "terminology/medical-biotech.md",
    "terminology/legal-policy.md",
    "terminology/finance-accounting.md",
)
DIRECT_SKILL_GUIDES = {
    "korean-editing.md",
    "korean-genres.md",
    "fidelity-review.md",
    "terminology/index.md",
}
TRACKED_VERSION = (ROOT / ".upstream-version").read_text(encoding="utf-8").strip()


def fail(message: str) -> None:
    raise SystemExit(message)


if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", TRACKED_VERSION):
    fail(".upstream-version must contain one stable upstream tag such as v2.11.1")

tag_check = subprocess.run(
    ["git", "cat-file", "-e", f"{TRACKED_VERSION}^{{commit}}"],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=False,
)
if tag_check.returncode:
    fail(f"Fetch the tracked upstream tag before validating: {TRACKED_VERSION}")

guide_texts: list[str] = []
guide_text_by_name: dict[str, str] = {}
for guide_name in GUIDE_NAMES:
    guide = ROOT / "references" / guide_name
    plugin_guide = ROOT / "skills" / "humanizer-ko" / "references" / guide_name
    if not guide.is_file() or not plugin_guide.is_file():
        fail(f"Add {guide_name} to the root skill and plugin package")

    guide_text = guide.read_text(encoding="utf-8")
    if guide_text != plugin_guide.read_text(encoding="utf-8"):
        fail(f"Keep both copies of {guide_name} byte-for-byte identical")

    if not re.search(r"[가-힣]", guide_text):
        fail(f"{guide_name} must contain real Korean examples")

    if guide_name in DIRECT_SKILL_GUIDES and f"](references/{guide_name})" not in SKILL:
        fail(f"Link {guide_name} from SKILL.md")

    guide_texts.append(guide_text)
    guide_text_by_name[guide_name] = guide_text

terminology_index = guide_text_by_name["terminology/index.md"]
for guide_name in GUIDE_NAMES:
    if guide_name.startswith("terminology/") and guide_name != "terminology/index.md":
        if f"]({Path(guide_name).name})" not in terminology_index:
            fail(f"Link {guide_name} from the terminology router")

if (ROOT / "references" / "domain-terminology.md").exists():
    fail("Remove the legacy domain-terminology.md after splitting field guides")

korean_point_numbers = [
    int(number)
    for number in re.findall(
        r"(?m)^## K([0-9]+)\. ", guide_text_by_name["korean-editing.md"]
    )
]
if korean_point_numbers != list(range(1, 11)):
    fail(f"Number Korean checkpoints from K1 through K10: {korean_point_numbers}")

korean_coverage_terms = (
    "보여지다",
    "되어지다",
    "~하는 데 도움이 됩니다",
    "도움이 되셨기를 바랍니다",
    "센터는 다음 달 문을 열 예정입니다",
    "놀라운",
    "고무적인",
    "오늘은 ~ 결과를 말씀드리겠습니다",
    "~할 수 있습니다",
    "「 」",
    "『 』",
)
missing_korean_coverage = [
    term
    for term in korean_coverage_terms
    if term not in guide_text_by_name["korean-editing.md"]
]
if missing_korean_coverage:
    fail(
        "Cover Korean passives, literal translations, chatbot residue, and quotes: "
        + ", ".join(missing_korean_coverage)
    )

skill_routing_rules = (
    "Load only the needed reference",
    "K1-K10",
    "references/english-patterns.md",
    "substantial prose span",
    "Do not read the same reference more than once",
    "Context-aware Korean review gate",
    "references/korean-genres.md",
    "references/fidelity-review.md",
    "references/terminology/index.md",
    "matching field guide",
    "Preserve tense, modality, negation, scope, attribution, and completion status",
    "Return only the final rewrite",
    "Do not open `SKILL.md` again",
)
if any(rule not in SKILL for rule in skill_routing_rules):
    fail("SKILL.md must route references, preserve status, and return concise output")

if (
    "blader/humanizer" not in NOTICE
    or "Copyright (c) 2025 Siqi Chen" not in NOTICE
    or "K1-K10" not in NOTICE
):
    fail("NOTICE.md must preserve attribution and identify the Korean checkpoints")

if ".upstream-version" not in README:
    fail("README.md must identify .upstream-version as the source of truth")

if not re.search(r"[가-힣]", README):
    fail("README.md must contain Korean text")

if "blader/humanizer" not in README or "비공식" not in README:
    fail("README.md must identify the upstream project and unofficial fork status")

if "choconyam/humanizer-ko" not in README or "$humanizer-ko" not in README:
    fail("README.md must use the humanizer-ko repository and skill ID")

korean_readme_numbers = {
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
}
if korean_readme_numbers != set(range(1, 36)):
    fail("README.md must list patterns 1 through 35")

readme_korean_points = {
    int(number) for number in re.findall(r"(?m)^\| K([0-9]+) \|", README)
}
if readme_korean_points != set(range(1, 11)):
    fail("README.md must list Korean checkpoints K1 through K10")

if TRACKED_VERSION.removeprefix("v") not in README:
    fail("README.md must mention the tracked upstream release")

license_at_tag = subprocess.run(
    ["git", "show", f"{TRACKED_VERSION}:LICENSE"],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=False,
)
if license_at_tag.returncode:
    fail(f"Could not read LICENSE from {TRACKED_VERSION}")

current_license = (ROOT / "LICENSE").read_text(encoding="utf-8").replace("\r\n", "\n")
if current_license != license_at_tag.stdout.replace("\r\n", "\n"):
    fail("Keep LICENSE identical to the tracked upstream release")

public_text = "\n".join((SKILL, README, NOTICE, *guide_texts))
if re.search(r"(?i)[a-z]:\\users\\", public_text):
    fail("Remove personal Windows paths before publishing")

print(f"Korean localization based on {TRACKED_VERSION} is valid")
