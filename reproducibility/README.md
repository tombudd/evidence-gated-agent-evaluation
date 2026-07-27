# EGEAS synthetic reproducibility package

This package accompanies:

> Tom Budd (2026), "Evidence-Gated Evaluation of Agentic AI Systems:
> A Bounded Framework for Testing Capability Without Expanding Authority."

Author website: https://tombudd.com

## Scope

The materials demonstrate deterministic gate semantics on synthetic metadata.
They do not evaluate a live model, agent, product, organization, or deployment.
They create no permission to connect tools, use credentials, process personal
data, communicate externally, or deploy any system.

## Contents

- `framework_schema.json`: closed JSON Schema for a minimal evaluation bundle.
- `synthetic_cases.json`: 18 valid and adversarial fixtures.
- `validate_bundle.py`: deterministic PASS, HOLD, FAIL, and INVALID_RUN gate.
- `test_validate_bundle.py`: regression tests.
- `validation_results.json`: generated result record.
- `MANIFEST.sha256`: byte-level file manifest generated after validation.

## Reproduce

Requires Python 3.11 or newer. The validator and tests use only the Python
standard library.

```bash
python validate_bundle.py
python -m unittest -q
```

Expected result:

```text
18/18 synthetic cases match their frozen expected gate.
5 tests pass.
```

## Interpretation

- `PASS`: the declared synthetic obligations are satisfied.
- `HOLD`: required evidence, approval, or exception resolution is incomplete.
- `FAIL`: a declared authority boundary is violated.
- `INVALID_RUN`: the evaluation bundle is malformed or unfrozen.

A PASS supports only the claim and environment named in the bundle. It does not
grant execution, deployment, or authority.

## License

The manuscript and documentation are licensed CC BY 4.0. The executable code
and JSON fixtures are licensed under the MIT License.
