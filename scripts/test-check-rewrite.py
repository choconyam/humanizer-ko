#!/usr/bin/env python3
"""Focused regressions for the optional rewrite checker."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts" / "check-rewrite.py"
SPEC = importlib.util.spec_from_file_location("check_rewrite", CHECKER_PATH)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class CheckerTests(unittest.TestCase):
    def run_checker(self, source: str, rewrite: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            source_path = Path(directory) / "source.txt"
            rewrite_path = Path(directory) / "rewrite.txt"
            source_path.write_text(source, encoding="utf-8")
            rewrite_path.write_text(rewrite, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source_path), str(rewrite_path)],
                capture_output=True,
                check=False,
                encoding="utf-8",
                text=True,
            )

    def test_ordinary_english_paraphrase_is_not_a_technical_token_failure(self) -> None:
        result = self.run_checker(
            "This system performs a careful rewrite.",
            "This tool makes the prose read naturally.",
        )
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("protected items: no deterministic changes found", result.stdout)
        self.assertNotIn("source-only identifier", result.stdout)

    def test_sign_and_unit_changes_need_source_review(self) -> None:
        for source, rewrite in (("증가율은 +5%다.", "증가율은 -5다."), ("온도는 5℃다.", "온도는 5℉다.")):
            with self.subTest(source=source, rewrite=rewrite):
                result = self.run_checker(source, rewrite)
                self.assertEqual(result.returncode, 2, result.stdout)
                self.assertIn("source-only numeric item", result.stdout)
                self.assertIn("rewrite-only numeric item", result.stdout)

    def test_counts_detect_one_lost_occurrence(self) -> None:
        source = CHECKER.extract_numbers("수율은 5%였고 오차도 5%였다.")
        rewrite = CHECKER.extract_numbers("수율은 5%였다.")
        self.assertEqual(source - rewrite, Counter({"5%": 1}))

    def test_range_date_and_exponent_controls_are_stable(self) -> None:
        source = CHECKER.extract_numbers("범위 5-10%, 날짜 2024/1/2, 값 1e-5와 10^-3.")
        rewrite = CHECKER.extract_numbers("범위 5–10%, 날짜 2024-01-02, 값 1e-5와 10^-3.")
        expected = Counter({"5": 1, "10%": 1, "2024-01-02": 1, "1e-5": 1, "10^-3": 1})
        self.assertEqual(source, expected)
        self.assertEqual(rewrite, expected)

    def test_uncertain_mixed_language_words_are_advisory(self) -> None:
        result = self.run_checker("model을 검토했다.", "approach를 검토했다.")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("Latin wording changed (advisory", result.stdout)
        self.assertNotIn("protected-item changes:", result.stdout)

    def test_code_url_path_and_identifiers_remain_protected(self) -> None:
        source = "`foo()` API GPT-5 WS₂ https://example.com/a scripts/check.py"
        rewrite = "`bar()` API GPT-4 WS₂ https://example.com/b scripts/check.py"
        result = self.run_checker(source, rewrite)
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("source-only backtick span: foo()", result.stdout)
        self.assertIn("source-only URL: https://example.com/a", result.stdout)
        self.assertIn("source-only identifier: GPT-5", result.stdout)

    def test_backtick_content_keeps_significant_punctuation(self) -> None:
        result = self.run_checker("Use `x;` here.", "Use `x` here.")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("source-only backtick span: x;", result.stdout)

    def test_clean_output_does_not_claim_semantic_proof(self) -> None:
        result = self.run_checker("문장을 고친다.", "문장을 고친다.")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("facts: OK", result.stdout)
        self.assertIn("cannot prove factual or semantic fidelity", result.stdout)


if __name__ == "__main__":
    unittest.main()
