#!/usr/bin/env python3
"""Deterministic rewrite check for humanizer-ko.

Usage: python check-rewrite.py SOURCE_FILE REWRITE_FILE

Compares a rewrite against its source without calling a model:

- fact errors: numbers, quoted spans, or technical tokens from the source
  that are missing from the rewrite
- review items: stock phrases from the K guides that remain in the rewrite
- length ratio between rewrite and source

Exit codes: 0 = clean, 1 = review items only, 2 = fact errors.
This check is optional. The skill works without it.
"""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

# Stock-phrase patterns documented in references/korean-editing.md (K2, K3, K5).
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


def extract_numbers(text: str) -> set[str]:
    return {
        match.replace(",", "")
        for match in re.findall(r"\d+(?:[.,]\d+)*", text)
    }


def extract_quotes(text: str) -> set[str]:
    spans: set[str] = set()
    for opener, closer in QUOTE_PAIRS:
        pattern = re.escape(opener) + r"([^" + re.escape(opener + closer) + r"]{1,500})" + re.escape(closer)
        for span in re.findall(pattern, text):
            span = span.strip()
            if span:
                spans.add(span)
    return spans


def extract_latin_tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[A-Za-z][A-Za-z0-9_.\-/]*[A-Za-z0-9]", text)
        if len(token) >= 2
    }


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    source = Path(sys.argv[1]).read_text(encoding="utf-8-sig")
    rewrite = Path(sys.argv[2]).read_text(encoding="utf-8-sig")

    fact_errors: list[str] = []
    rewrite_numbers = extract_numbers(rewrite)
    for number in sorted(extract_numbers(source)):
        if number not in rewrite_numbers:
            fact_errors.append(f"missing number: {number}")
    for span in sorted(extract_quotes(source)):
        if span not in rewrite:
            fact_errors.append(f"missing quoted span: {span}")
    source_tokens = extract_latin_tokens(source)
    rewrite_tokens = extract_latin_tokens(rewrite)
    for token in sorted(source_tokens):
        if token not in rewrite_tokens:
            fact_errors.append(f"missing technical token: {token}")
    # Inventions are fact errors too: tokens or numbers that appear only in the rewrite.
    for token in sorted(rewrite_tokens - source_tokens):
        fact_errors.append(f"added technical token: {token}")
    source_numbers = extract_numbers(source)
    for number in sorted(rewrite_numbers - source_numbers):
        fact_errors.append(f"added number: {number}")

    reviews: list[str] = []
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

    if fact_errors:
        print(f"fact errors: {len(fact_errors)}")
        for item in fact_errors:
            print(f"  - {item}")
    else:
        print("facts: OK")

    if reviews:
        print(f"review items: {len(reviews)}")
        for item in reviews:
            print(f"  - {item}")
    else:
        print("residue: none")

    if fact_errors:
        return 2
    if reviews:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
