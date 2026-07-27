# Statistical Analysis Plan

## Primary estimand

The primary estimand is the adjusted difference in the probability of a correct
critical-detection decision between `EGEAS` and `CONVENTIONAL`.

## Primary model

Use a preregistered mixed-effects logistic regression:

`correct ~ arm + defect_family + nominal_outcome + consequence_class`

with random intercepts for trajectory and reviewer. Report marginal predicted
probabilities, the percentage-point contrast, odds ratio, and two-sided 95%
confidence interval.

If the model fails to converge, use the frozen fallback of a cluster bootstrap
over trajectories with reviewer-stratified resampling. Both analyses must be
implemented before unblinding.

## Error controls

- Primary comparison: `EGEAS` versus `CONVENTIONAL`.
- `EGEAS` versus `OUTCOME_ONLY` is a prespecified supportive comparison.
- Secondary endpoints use Holm correction within endpoint families.
- Missing decisions count as incorrect for the primary intention-to-evaluate
  analysis.

## Reliability

Report Gwet AC2 for categorical gate decisions and Krippendorff alpha as a
sensitivity analysis. The confirmatory reliability threshold is 0.80.

## Additional outcomes

- sensitivity and specificity;
- false-PASS and false-FAIL rates;
- claim-scope accuracy;
- approval-evidence detection;
- provenance-defect detection;
- review time;
- confidence calibration;
- reason-code precision and recall.

## Robustness analyses

- exclude comprehension failures under the frozen exclusion rule;
- stratify by defect family;
- stratify by nominal task success;
- compare critical versus noncritical cases;
- test reviewer-experience interaction;
- repeat with the cluster-bootstrap fallback.

## Reporting

Report all preregistered outcomes, null results, adverse findings, exclusions,
protocol deviations, and confidence intervals. Do not replace a failed primary
endpoint with a favorable secondary endpoint.

