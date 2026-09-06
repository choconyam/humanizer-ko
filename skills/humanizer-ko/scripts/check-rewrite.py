#!/usr/bin/env python3
"""Deterministic rewrite check for humanizer-ko.

Usage: python check-rewrite.py SOURCE_FILE REWRITE_FILE

Compares a rewrite against its source without calling a model:

- protected-item changes: numbers with signs or common units, quoted spans,
  code, URLs, paths, and high-confidence identifiers
- review items: uncertain Latin wording changes and stock phrases from the K guides
- length ratio between rewrite and source

Exit codes: 0 = no candidates, 1 = advisory review items only,
2 = protected-item changes that need source review.
This optional surface check cannot prove factual or semantic fidelity.
"""

from __future__ import annotations

import io
import re
import sys
from collections import Counter
from pathlib import Path

# Stock-phrase patterns documented in SKILL.md (K2, K3, K5).
RESIDUE_PATTERNS = (
    (r"되어[지진질졌짐]", "K3 double passive"),
    (r"보여[지진질졌짐]", "K3 double passive"),
    (r"에 있어", "K2 translation-like"),
    (r"결론적으로", "K5 empty closer"),
    (r"요약하자면", "K5 empty closer"),
    (r"과언이 아니", "K5 stock phrase"),
    (r"귀추가 주목", "K5 stock phrase"),
    (r"밝은 미래", "K5 stock phrase"),
    (r"빠르게 변화하는", "K5 stock phrase"),
    (r"새로운 패러다임", "K5 stock phrase"),
    (r"중요한 시사점", "K5 stock phrase"),
    (r"단순히 .{0,12}를 넘어", "K5 stock phrase"),
    (r"에 그치지 않고", "K5 stock phrase"),
    (r"도움이 되셨기를", "K5 chatbot residue"),
    (r"물론입니다", "K5 chatbot residue"),
    (r"좋은 질문", "K5 chatbot residue"),
    (r"궁금한 점이 있으시면 언제든지", "K5 chatbot residue"),
)

# Repetition thresholds for phrases that are normal once but a tell in bulk.
REPEAT_PATTERNS = (
    (r"할 수 있습니다|할 수 있다", 3, "K5 repeated ability hedge"),
    (r"다양한", 2, "K5 repeated 다양한"),
)

QUOTE_PAIRS = (("“", "”"), ("‘", "’"), ("\"", "\""), ("「", "」"), ("『", "』"))

PROTECTED_SPAN_PATTERNS = (
    ("backtick span", re.compile(r"`+([^`\n]+?)`+"), 1),
    ("URL", re.compile(r"\b(?:https?://|www\.)[^\s<>()]+"), 0),
    (
        "path",
        re.compile(
            r"(?<![A-Za-z0-9_])(?:"
            r"(?:[A-Za-z]:\\|/|\.\.?[/\\])(?:[A-Za-z0-9_.-]+[/\\])*[A-Za-z0-9_.-]+"
            r")"
        ),
        0,
    ),
)
LATIN_TOKEN_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z][A-Za-z0-9₀-₉_.\-/\\]*[A-Za-z0-9₀-₉]"
)

NUMBER_CORE = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?"
COMMON_UNIT = (
    r"(?:%|‰|℃|℉|°[CFK]|GHz|MHz|kHz|Hz|MPa|kPa|Pa|mmol|mol|"
    r"km|cm|mm|nm|kg|mg|mL|µL|μL|ms|µs|μs|ns|kW|mW|mV|mA|dB|rpm|fps|"
    r"g|L|m|s|h|K|V|A|W|J|M)"
)
NUMBER_PATTERN = re.compile(
    rf"""
    (?<![A-Za-z0-9_.])
    (?:
        (?P<date>\d{{4}}[-/.]\d{{1,2}}[-/.]\d{{1,2}})
      |
        (?P<sign>[+−-]?)(?P<currency>[$€£¥₩]?)
        (?P<number>{NUMBER_CORE})
        (?P<exponent>(?:[eE]|\^)[+−-]?\d+)?
        (?P<unit>\s*{COMMON_UNIT})?
    )
    (?![A-Za-z0-9_])
    """,
    re.VERBOSE,
)


def _is_protected_identifier(token: str) -> bool:
    letters = re.findall(r"[A-Za-z]", token)
    return bool(
        re.search(r"[0-9₀-₉]", token)
        or re.search(r"[_.\\/]", token)
        or sum(letter.isupper() for letter in letters) >= 2
        or re.search(r"[a-z][A-Z]", token)
    )


def extract_latin_items(text: str) -> tuple[Counter[tuple[str, str]], Counter[str], str]:
    """Return protected items, uncertain words, and text with protected spans masked."""
    protected: Counter[tuple[str, str]] = Counter()
    masked = list(text)
    for label, pattern, value_group in PROTECTED_SPAN_PATTERNS:
        current = "".join(masked)
        for match in pattern.finditer(current):
            value = match.group(value_group)
            if label != "backtick span":
                value = value.rstrip(".,;:!?")
            if value:
                protected[(label, value)] += 1
            masked[match.start() : match.end()] = " " * (match.end() - match.start())

    uncertain: Counter[str] = Counter()
    current = "".join(masked)
    for match in LATIN_TOKEN_PATTERN.finditer(current):
        token = match.group()
        if _is_protected_identifier(token):
            protected[("identifier", token)] += 1
            masked[match.start() : match.end()] = " " * len(token)
        else:
            uncertain[token.casefold()] += 1
    return protected, uncertain, "".join(masked)


def extract_numbers(text: str) -> Counter[str]:
    _, _, text = extract_latin_items(text)
    numbers: Counter[str] = Counter()
    for match in NUMBER_PATTERN.finditer(text):
        if match.group("date"):
            year, month, day = re.split(r"[-/.]", match.group("date"))
            numbers[f"{year}-{int(month):02d}-{int(day):02d}"] += 1
            continue
        sign = match.group("sign").replace("−", "-")
        currency = match.group("currency")
        number = match.group("number").replace(",", "")
        exponent = re.sub(r"\s+", "", match.group("exponent") or "").replace("−", "-").lower()
        unit = re.sub(r"\s+", "", match.group("unit") or "")
        numbers[f"{sign}{currency}{number}{exponent}{unit}"] += 1
    return numbers


def extract_quotes(text: str) -> Counter[str]:
    spans: Counter[str] = Counter()
    for opener, closer in QUOTE_PAIRS:
        pattern = re.escape(opener) + r"([^" + re.escape(opener + closer) + r"]{1,500})" + re.escape(closer)
        for span in re.findall(pattern, text):
            span = span.strip()
            if span:
                spans[span] += 1
    return spans


def _describe_counter(counter: Counter[str], limit: int = 6) -> str:
    values = []
    for value, count in sorted(counter.items())[:limit]:
        values.append(f"{value} ({count})" if count > 1 else value)
    remaining = len(counter) - limit
    if remaining > 0:
        values.append(f"and {remaining} more")
    return ", ".join(values)


def _append_changes(
    changes: list[str], source: Counter[str], rewrite: Counter[str], label: str
) -> None:
    for value, count in sorted((source - rewrite).items()):
        suffix = f" ({count} occurrences)" if count > 1 else ""
        changes.append(f"source-only {label}: {value}{suffix}")
    for value, count in sorted((rewrite - source).items()):
        suffix = f" ({count} occurrences)" if count > 1 else ""
        changes.append(f"rewrite-only {label}: {value}{suffix}")


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    source = Path(sys.argv[1]).read_text(encoding="utf-8-sig")
    rewrite = Path(sys.argv[2]).read_text(encoding="utf-8-sig")

    protected_changes: list[str] = []
    source_tokens, source_words, _ = extract_latin_items(source)
    rewrite_tokens, rewrite_words, _ = extract_latin_items(rewrite)
    _append_changes(protected_changes, extract_numbers(source), extract_numbers(rewrite), "numeric item")
    _append_changes(protected_changes, extract_quotes(source), extract_quotes(rewrite), "quoted span")
    for (label, value), count in sorted((source_tokens - rewrite_tokens).items()):
        suffix = f" ({count} occurrences)" if count > 1 else ""
        protected_changes.append(f"source-only {label}: {value}{suffix}")
    for (label, value), count in sorted((rewrite_tokens - source_tokens).items()):
        suffix = f" ({count} occurrences)" if count > 1 else ""
        protected_changes.append(f"rewrite-only {label}: {value}{suffix}")

    reviews: list[str] = []
    source_word_changes = source_words - rewrite_words
    rewrite_word_changes = rewrite_words - source_words
    if re.search(r"[가-힣]", source + rewrite) and (source_word_changes or rewrite_word_changes):
        parts = []
        if source_word_changes:
            parts.append(f"source-only {_describe_counter(source_word_changes)}")
        if rewrite_word_changes:
            parts.append(f"rewrite-only {_describe_counter(rewrite_word_changes)}")
        reviews.append(
            "Latin wording changed (advisory; review only terms that carry meaning): " + "; ".join(parts)
        )
    for pattern, label in RESIDUE_PATTERNS:
        for match in dict.fromkeys(re.findall(pattern, rewrite)):
            reviews.append(f"{label}: {match}")
    for pattern, threshold, label in REPEAT_PATTERNS:
        count = len(re.findall(pattern, rewrite))
        if count >= threshold:
            reviews.append(f"{label}: {count} occurrences")

    # Negative qualifiers are claims; a sharp drop suggests limits were cut.
    negation = r"않|없|아니|미정|보류"
    source_negations = len(re.findall(negation, source))
    rewrite_negations = len(re.findall(negation, rewrite))
    if source_negations >= 3 and rewrite_negations * 2 < source_negations:
        reviews.append(
            f"negation drop: source {source_negations} -> rewrite {rewrite_negations}; check limiting claims"
        )

    src_len = len(source.strip())
    out_len = len(rewrite.strip())
    ratio = out_len / src_len if src_len else 0.0
    print(f"length: source {src_len} chars, rewrite {out_len} chars, ratio {ratio:.2f}")
    if ratio > 1.0:
        print("length note: rewrite is longer than the source; justify each addition or cut it")
    if 0 < ratio < 0.5:
        print("length note: rewrite lost more than half the source; check for deleted claims")

    if protected_changes:
        print(f"protected-item changes: {len(protected_changes)} (source review required)")
        for item in protected_changes:
            print(f"  - {item}")
    else:
        print("protected items: no deterministic changes found")

    if reviews:
        print(f"review items: {len(reviews)}")
        for item in reviews:
            print(f"  - {item}")
    else:
        print("residue: none")
    print(
        "semantic note: this surface check cannot prove factual or semantic fidelity; "
        "compare claims, stance, and context with the source"
    )

    if protected_changes:
        return 2
    if reviews:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
