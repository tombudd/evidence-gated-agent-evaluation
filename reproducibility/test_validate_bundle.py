import json
import unittest
from pathlib import Path

from validate_bundle import (
    canonical_bytes,
    digest,
    gate_case,
    materialize_cases,
)


ROOT = Path(__file__).resolve().parent


def load():
    cases = json.loads((ROOT / "synthetic_cases.json").read_text())
    return materialize_cases(cases)


class ValidationTests(unittest.TestCase):
    def test_all_expected_gate_decisions_match(self):
        for case in load():
            actual, _ = gate_case(case)
            self.assertEqual(actual, case["expected_gate"], case["case_id"])

    def test_canonicalization_is_order_independent_for_object_keys(self):
        left = {"b": 2, "a": 1}
        right = {"a": 1, "b": 2}
        self.assertEqual(canonical_bytes(left), canonical_bytes(right))
        self.assertEqual(digest(left), digest(right))

    def test_suite_is_eighteen_cases_with_unique_ids(self):
        ids = [case["case_id"] for case in load()]
        self.assertEqual(len(ids), 18)
        self.assertEqual(len(set(ids)), 18)

    def test_no_case_authorizes_external_effects(self):
        cases = [
            case for case in load()
            if case["mutation"] != "EXTERNAL_EFFECTS"
        ]
        self.assertTrue(
            all(
                case["bundle"]["authority"]["external_effects"] is False
                for case in cases
            )
        )

    def test_fail_cases_are_boundary_mutations(self):
        for case in load():
            actual, reasons = gate_case(case)
            if actual == "FAIL":
                self.assertTrue(
                    any(
                        reason.startswith("BOUNDARY_VIOLATION:")
                        for reason in reasons
                    )
                )


if __name__ == "__main__":
    unittest.main()
