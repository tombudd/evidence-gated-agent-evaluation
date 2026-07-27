# Evidence-Gated Evaluation of Agentic AI Systems

**Author:** Tom Budd  
**Website:** https://tombudd.com  
**Paper:** https://tombudd.com/evidence-gated-evaluation-agentic-ai-systems  
**Status:** Public release candidate, independent review pending, no DOI

This repository contains the manuscript, deterministic synthetic demonstration,
reproducibility materials, and the freeze-ready protocol for the next empirical
validation stage of Evidence-Gated Evaluation of Agentic Systems (EGEAS).

EGEAS separates capability evidence from authority. A successful evaluation
supports only the predeclared claim within the tested environment and does not
authorize deployment, external action, or a broader safety claim.

## Repository map

- `manuscript/`: source, Word manuscript, and rendered PDF.
- `reproducibility/`: closed schema, 18 synthetic cases, deterministic gate,
  tests, and frozen results.
- `a_plus_protocol/`: preregistration candidate, statistical analysis plan,
  trajectory codebook, and independent-review materials.
- `INDEPENDENT_REVIEW_FORM.md`: manuscript review form.
- `REVIEW_REQUEST.md`: bounded technical-review invitation and instructions.
- `CONTRIBUTING.md`: contribution, review, and disclosure policy.
- `CITATION.cff`: repository and manuscript citation metadata.
- `LICENSE.md`: license boundary for code and research materials.
- `PUBLICATION_STATUS_AND_RELEASE_CHECKLIST.md`: controlling release state.

## Reproduce the current demonstration

```bash
cd reproducibility
python3 validate_bundle.py
python3 -m unittest -v test_validate_bundle.py
```

Expected result:

- 18 of 18 frozen case decisions match.
- Five regression tests pass.
- No model calls or external effects occur.

## Validate the A+ protocol candidate

```bash
cd a_plus_protocol
python3 -m unittest -v test_protocol.py
```

## Claim boundary

This repository does not establish that any AI system is safe, aligned,
compliant, secure, conscious, or ready for deployment. The empirical A+ study
has not been executed, independently reproduced, or independently validated.

## Citation

Citation metadata is available in `CITATION.cff`. A DOI will be added only
after the exact reviewed release is archived.

## Independent review and replication

Technical criticism and clean-room replication reports are welcome. Start with
`REVIEW_REQUEST.md`, use the appropriate GitHub issue form, and disclose any
relevant conflicts. A review is not treated as an endorsement. Review status
changes only when the evidence and disposition are public.
