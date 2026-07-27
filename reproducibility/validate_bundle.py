#!/usr/bin/env python3
"""Deterministic synthetic validator for the EGEAS methods preprint.

This program performs no network, model, tool, credential, or external-system
access. It validates the supplied synthetic fixtures only.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

FAIL_CLOSED_MUTATIONS = {
    "WILDCARD_RESOURCE",
    "NETWORK_ENABLED",
    "CREDENTIALS_PRESENT",
    "REAL_PERSON_DATA",
    "EXTERNAL_EFFECTS",
    "UNKNOWN_OPERATION",
}

TOP_KEYS = {"bundle_version", "system", "claims", "authority", "protocol", "evidence"}
SYSTEM_KEYS = {"system_id", "version", "artifact_digest"}
CLAIM_KEYS = {"claim_id", "statement", "metric", "threshold", "exclusions"}
AUTHORITY_KEYS = {
    "resources",
    "operations",
    "network",
    "credentials",
    "real_person_data",
    "external_effects",
    "approval_required",
}
PROTOCOL_KEYS = {
    "protocol_id",
    "frozen",
    "fixtures_digest",
    "scorer_digest",
    "expected_cases",
}
EVIDENCE_KEYS = {
    "raw_results_present",
    "environment_manifest_present",
    "exceptions",
    "independent_review",
}
OPERATIONS = {
    "READ_SYNTHETIC_FIXTURE",
    "DRAFT_SYNTHETIC_OUTPUT",
    "PROPOSE_SYNTHETIC_ACTION",
    "SIMULATE_SYNTHETIC_DECISION",
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def set_path(target: Any, dotted_path: str, value: Any) -> None:
    parts = dotted_path.split(".")
    node = target
    for part in parts[:-1]:
        node = node[int(part)] if isinstance(node, list) else node[part]
    final = parts[-1]
    if isinstance(node, list):
        node[int(final)] = value
    else:
        node[final] = value


def remove_path(target: Any, dotted_path: str) -> None:
    parts = dotted_path.split(".")
    node = target
    for part in parts[:-1]:
        node = node[int(part)] if isinstance(node, list) else node[part]
    final = parts[-1]
    if isinstance(node, list):
        del node[int(final)]
    else:
        del node[final]


def materialize_cases(raw_cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    materialized: list[dict[str, Any]] = []
    for raw in raw_cases:
        case = copy.deepcopy(raw)
        if "base_case" in case:
            base_id = case["base_case"]
            if base_id not in by_id:
                raise ValueError(f"Unknown base case: {base_id}")
            bundle = copy.deepcopy(by_id[base_id]["bundle"])
            for path, value in case.get("patch", {}).items():
                set_path(bundle, path, value)
            for path in case.get("remove", []):
                remove_path(bundle, path)
            case["bundle"] = bundle
        by_id[case["case_id"]] = case
        materialized.append(case)
    return materialized


def closed_object_errors(
    value: Any, required_keys: set[str], label: str
) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    missing = required_keys - set(value)
    unknown = set(value) - required_keys
    return [
        *[f"{label} missing required field {key}" for key in sorted(missing)],
        *[f"{label} contains unknown field {key}" for key in sorted(unknown)],
    ]


def schema_errors(bundle: Any) -> list[str]:
    errors = closed_object_errors(bundle, TOP_KEYS, "bundle")
    if errors:
        return errors
    if bundle["bundle_version"] != "1.0":
        errors.append("bundle_version must equal 1.0")

    errors.extend(closed_object_errors(bundle["system"], SYSTEM_KEYS, "system"))
    if not errors:
        system = bundle["system"]
        if not isinstance(system["system_id"], str) or len(system["system_id"]) < 3:
            errors.append("system_id must be a bounded string")
        for field in ("artifact_digest",):
            value = system[field]
            if (
                not isinstance(value, str)
                or not value.startswith("sha256:")
                or len(value) != 71
                or any(ch not in "0123456789abcdef" for ch in value[7:])
            ):
                errors.append(f"{field} must be a lowercase SHA-256 digest")

    claims = bundle["claims"]
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty array")
    else:
        for index, claim in enumerate(claims):
            errors.extend(
                closed_object_errors(claim, CLAIM_KEYS, f"claims[{index}]")
            )
            if isinstance(claim, dict) and CLAIM_KEYS <= set(claim):
                if len(claim["statement"]) < 10:
                    errors.append(f"claims[{index}].statement is too short")
                if not isinstance(claim["exclusions"], list):
                    errors.append(f"claims[{index}].exclusions must be an array")

    errors.extend(
        closed_object_errors(bundle["authority"], AUTHORITY_KEYS, "authority")
    )
    if isinstance(bundle["authority"], dict) and AUTHORITY_KEYS <= set(bundle["authority"]):
        authority = bundle["authority"]
        if not isinstance(authority["resources"], list) or not authority["resources"]:
            errors.append("authority.resources must be a non-empty array")
        elif any("*" in resource for resource in authority["resources"]):
            errors.append("authority.resources cannot contain wildcards")
        if (
            not isinstance(authority["operations"], list)
            or not authority["operations"]
            or any(operation not in OPERATIONS for operation in authority["operations"])
        ):
            errors.append("authority.operations contains an undeclared operation")
        if authority["network"] != "DISABLED":
            errors.append("authority.network must be DISABLED")
        if authority["credentials"] != "NONE":
            errors.append("authority.credentials must be NONE")
        if authority["real_person_data"] is not False:
            errors.append("authority.real_person_data must be false")
        if authority["external_effects"] is not False:
            errors.append("authority.external_effects must be false")

    errors.extend(
        closed_object_errors(bundle["protocol"], PROTOCOL_KEYS, "protocol")
    )
    if isinstance(bundle["protocol"], dict) and PROTOCOL_KEYS <= set(bundle["protocol"]):
        protocol = bundle["protocol"]
        if protocol["frozen"] is not True:
            errors.append("protocol.frozen must be true")
        for field in ("fixtures_digest", "scorer_digest"):
            value = protocol[field]
            if (
                not isinstance(value, str)
                or not value.startswith("sha256:")
                or len(value) != 71
                or any(ch not in "0123456789abcdef" for ch in value[7:])
            ):
                errors.append(f"protocol.{field} must be a lowercase SHA-256 digest")

    errors.extend(
        closed_object_errors(bundle["evidence"], EVIDENCE_KEYS, "evidence")
    )
    return errors


def gate_case(case: dict[str, Any]) -> tuple[str, list[str]]:
    bundle = case["bundle"]
    validation_errors = schema_errors(bundle)
    mutation = case["mutation"]

    if mutation in FAIL_CLOSED_MUTATIONS:
        reasons = [f"BOUNDARY_VIOLATION:{mutation}"]
        if validation_errors:
            reasons.extend(f"SCHEMA:{error}" for error in validation_errors)
        return "FAIL", reasons

    if validation_errors:
        return "INVALID_RUN", [f"SCHEMA:{error}" for error in validation_errors]

    evidence = bundle["evidence"]
    if not evidence["raw_results_present"]:
        return "HOLD", ["MISSING_RAW_RESULTS"]
    if not evidence["environment_manifest_present"]:
        return "HOLD", ["MISSING_ENVIRONMENT_MANIFEST"]
    if evidence["exceptions"]:
        return "HOLD", ["UNRESOLVED_EXCEPTION"]
    if bundle["authority"]["approval_required"]:
        return "HOLD", ["APPROVAL_EVIDENCE_REQUIRED"]
    return "PASS", ["ALL_DECLARED_OBLIGATIONS_SATISFIED"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default="synthetic_cases.json")
    parser.add_argument("--schema", default="framework_schema.json")
    parser.add_argument("--output", default="validation_results.json")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    cases_path = root / args.cases
    schema_path = root / args.schema
    output_path = root / args.output

    raw_cases = json.loads(cases_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    cases = materialize_cases(raw_cases)

    results = []
    for case in cases:
        actual, reasons = gate_case(case)
        results.append(
            {
                "case_id": case["case_id"],
                "expected_gate": case["expected_gate"],
                "actual_gate": actual,
                "matched": actual == case["expected_gate"],
                "reasons": reasons,
                "bundle_digest": digest(case["bundle"]),
            }
        )

    result = {
        "suite": "EGEAS_SYNTHETIC_SUITE_V1",
        "suite_digest": digest(raw_cases),
        "schema_digest": digest(schema),
        "case_count": len(results),
        "matched_count": sum(item["matched"] for item in results),
        "all_matched": all(item["matched"] for item in results),
        "authority_delta": "NONE",
        "external_effects": False,
        "results": results,
    }
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["all_matched"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
