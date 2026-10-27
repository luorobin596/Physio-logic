# Initial validation report

Date: 2026-10-27. Package: 0.2.0. Specification: approved v0.3.

## What was actually performed

| Check | Result | Evidence / limits |
| --- | --- | --- |
| Required skill frontmatter | Passed | All three skills parsed as YAML and passed the bundled skill-creator quick_validate.py |
| Package structure | Passed | Exactly three active stage skills, seven approved table assets, three identity/version-aligned manifests |
| Original provenance | Passed | 12 source hashes verified; original PDF/Excel copies unchanged; nine PDF extraction snapshots preserve page labels |
| Local skill references | Passed | Every local resource resolves inside its own skill; duplicated contract/routing/pain guides match |
| Fixed table structure | Passed | Exact approved columns/base rows/order checked; Table 2.1 Stage/Irritability separate; system/structural extensions preserve base rows |
| E01 authored walkthrough | Structure passed | One symptom, two initial tables, staged stop; current agent authored/reviewed output |
| E03 authored walkthrough | Structure passed | Four symptoms, eight tables; no three-symptom cap or padding |
| E05 authored walkthrough | Structure passed | Both conflicting values retained, five-column 3.2, no final synthesis before request |
| PT-S01 complete reference | Structure passed | Seven ordered table assets, concise/full Impression aligned, traceable S1/O1/O2; current agent authored/reviewed output |
| E07 urgent-priority walkthrough | Manually inspected | Urgent assessment precedes routine knee tables; no formal clinical validation claim |
| Invalid-output controls | Passed | Missing Regions, missing Irritability, wrong timeline title, unapproved status, symptom-count mismatch were rejected; source locator accepted |

See structural-controls.json for exact negative-control outcomes. Authored outputs are reference walkthroughs: writing an expected output and validating it does not establish that a newly invoked model will reproduce it.

## Not performed / not claimed

- No blind or independent model forward test; no subagent evaluation.
- No actual installation, installed-plugin discovery or automatic skill-selection test.
- No Claude, Gemini CLI or Antigravity runtime test.
- No clinical effectiveness, therapist usability or complete disease/test-validity validation.
- The remaining 18-case suite is prepared for actual host runs; do not mark all 18 cases as executed. E01/E03/E05/E07 are manual references, plus PT-S01.
- Legacy case mapping is a source-format migration with explicit unknowns, not an independently verified original patient reassessment.

## Reproduce structural checks

From package root:

```sh
python3 scripts/validate_package.py
python3 scripts/validate_package.py --output evals/results/manual-e01.md --mode subjective-initial
python3 scripts/validate_package.py --output evals/results/manual-e03.md --mode subjective-initial --symptoms 4
python3 scripts/validate_package.py --output evals/results/manual-e05.md --mode objective
python3 scripts/validate_package.py --output evals/results/complete-case-output.md --mode complete
```

## Next host acceptance

Load/install by the host's supported route, verify all three skill names are available, then run cases.json using the rubric and record full outputs with host/version/model. Test staged multi-turn and explicit combined requests separately, including user language requests and data correction. Independent professional review and real therapist operation remain separate acceptance steps.
