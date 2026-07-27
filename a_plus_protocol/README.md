# EGEAS A+ Empirical Validation Program

**Author:** Tom Budd  
**Author website:** https://tombudd.com  
**Protocol:** EGEAS-A-PLUS-V1  
**Status:** `FREEZE_READY_NOT_EXECUTED`

This packet converts the research agenda in *Evidence-Gated Evaluation of
Agentic AI Systems* into a bounded confirmatory study. It does not report
experimental results and does not establish that EGEAS improves evaluation.

## Research question

Does an EGEAS evidence packet improve evaluators' ability to detect unsupported
capability claims and undeclared authority expansion, compared with an
outcome-only packet or a conventional evaluation packet?

## Current authority boundary

- Protocol design and synthetic fixture construction are authorized.
- Real credentials, private data, production systems, and consequential actions
  are prohibited.
- Human-participant recruitment and data collection are not authorized until an
  ethics or institutional-review determination is recorded.
- Live model or agent execution is not authorized by this packet.
- Publication, DOI registration, and public A+ claims remain separately gated.

## Study arms

1. `OUTCOME_ONLY`: final task outcome and claimed result.
2. `CONVENTIONAL`: outcome, rubric, summary log, and stated limitations.
3. `EGEAS`: conventional materials plus frozen identity, bounded claims,
   authority envelope, protocol digest, evidence ledger, provenance, approval
   evidence, full trajectory, and decision gate.

## Confirmatory targets

- Minimum 72 unique synthetic trajectories after a separately reviewed pilot.
- Three packet variants per trajectory.
- At least three independent ratings per packet.
- Primary endpoint: correct detection of critical unsupported claims or
  authority-boundary violations.
- Superiority threshold: at least 15 percentage points better sensitivity than
  `CONVENTIONAL`, with no more than a 5-point specificity loss.
- Reliability target: Gwet AC2 or Krippendorff alpha at least 0.80 for the
  primary categorical endpoint.

## Files

- `protocol.json`: machine-readable protocol state.
- `protocol.schema.json`: closed schema.
- `PREREGISTRATION.md`: hypotheses, estimands, exclusions, and stop rules.
- `STATISTICAL_ANALYSIS_PLAN.md`: confirmatory analysis rules.
- `TRAJECTORY_CODEBOOK.md`: frozen trajectory and defect taxonomy.
- `EXTERNAL_REVIEW_PACKET.md`: review scope and disposition process.
- `INDEPENDENCE_ATTESTATION.md`: reviewer identity and conflict declaration.

## Gate

`NEXT_REQUIRED_GATE = EGEAS_V1_PROTOCOL_INDEPENDENT_DESIGN_REVIEW_M0_1`

