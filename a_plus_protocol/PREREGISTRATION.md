# EGEAS-A-PLUS-V1 Preregistration Candidate

**Author:** Tom Budd  
**Website:** https://tombudd.com  
**State:** `FREEZE_READY_NOT_PREREGISTERED`

## Hypotheses

### Primary hypothesis

Evaluators receiving `EGEAS` packets will identify critical unsupported claims
or undeclared authority-boundary violations more accurately than evaluators
receiving `CONVENTIONAL` packets.

### Confirmatory success rule

The primary claim may pass only when all conditions hold:

1. estimated sensitivity improvement is at least 15 percentage points;
2. the two-sided 95% confidence interval excludes zero;
3. specificity loss is no greater than 5 percentage points;
4. the reliability estimate is at least 0.80;
5. no critical protocol, blinding, custody, or contamination failure occurred.

### Secondary hypotheses

- EGEAS improves evidence-to-claim traceability judgments.
- EGEAS improves identification of missing approval and provenance.
- EGEAS reduces overconfident PASS decisions.
- EGEAS does not impose disproportionate review time.

Secondary outcomes are exploratory unless separately adjusted for multiplicity.

## Experimental unit

The underlying unit is one frozen synthetic agent trajectory. Each trajectory
has one sealed answer key and three presentation variants. A reviewer must not
see more than one variant of the same underlying trajectory.

## Randomization

Packet arm and packet order will be assigned from a committed random seed by a
custodian who did not author the trajectory. Assignment will be balanced across
defect family, consequence class, and nominal task outcome.

## Blinding

Reviewers will not receive the study hypothesis, framework labels, answer keys,
or alternate packet variants. Packet formatting will be normalized to reduce
obvious condition identification.

## Pilot and power

A blind pilot will estimate prevalence, reviewer variance, trajectory variance,
missingness, and review-time dispersion. Confirmatory sample size will be
selected by simulation before unblinding and may not fall below 72 trajectories.

## Exclusions

Exclusions are permitted only for:

- duplicate or corrupted packets;
- failed randomization or custody;
- reviewer conflict discovered before unblinding;
- incomplete response as defined before execution;
- protocol-defined comprehension failure.

Outcome-dependent exclusions are prohibited.

## Stop and invalidation rules

Stop or invalidate for:

- answer-key exposure;
- author access to blinded reviewer outcomes;
- protocol modification after outcome inspection;
- reviewer identity or conflict uncertainty;
- missing raw trajectory or assignment receipt;
- live external effects, credentials, or real-person data;
- material divergence between preregistration and executed analysis.

## Maximum permitted conclusion

A successful result supports only that EGEAS improved specified reviewer
decisions within the frozen synthetic study. It does not establish general
alignment, system safety, regulatory compliance, or deployment readiness.

