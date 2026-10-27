# PT Clinical Skills

A skill-only plugin for physical therapists to analyze subjective history, compare objective evidence and produce a clinical Impression. Version **0.2.0**, based on the approved specification v0.3 (2026-10-27).

## Start here

| Skill | Output |
| --- | --- |
| [subjective-analysis](skills/subjective-analysis/SKILL.md) | Tables 1.1/1.2 per actual symptom, then preliminary hypotheses and timeline in 2.1/2.2 |
| [objective-analysis](skills/objective-analysis/SKILL.md) | Structural/system evidence tables 3.1/3.2, support/opposition and missing information |
| [impression](skills/impression/SKILL.md) | Concise Table 4 and full Impression; optional versions on request |

Provide de-identified assessment data and ask for the relevant stage. Example:

> Analyze my subjective physical therapy assessment using the fixed tables. Identify missing information and preliminary hypotheses without inventing results.

For a complete case:

> Analyze the complete assessment in one combined flow through full Impression, using subjective-analysis, objective-analysis and impression in that order.

All runtime output defaults to English. An explicit request may change narrative/filled-cell language; approved table titles and headers stay English. Staged operation accepts Next step, 下一步, 繼續 or another clear forward request. Complete-analysis requests bypass intermediate stops. The initial subjective tables precede preliminary synthesis; objective tables precede the final synthesis.

## What stays fixed and what can vary

Seven Markdown table assets implement six original table groups (Table 2 has two sub-tables). Headers, base rows and order are fixed. Symptom count follows the supplied case, not a three-symptom quota. System rows and Table 3.1 categories may be extended while retaining base rows. Symptoms Stage and Irritability are separate. Contributing factors remains open to all case-supported factors.

Approved support labels: ★★★ Strong, ★★ Moderate, ★ Low, − Currently not supported, ✕ Ruled-out, ⚠ Conflicting evidence, ? Unable to determine / Pending assessment. Each needs its case rationale; these are not numerical probabilities or research grades. Unknown findings are never negative by default.

The workflow ends at Impression and related clarification/assessment questions. It does not provide unrequested treatment plans or exercise dosage. Source examples are not default patient findings.

## Shared references and installation

Keep the complete `pt-clinical-skills/` plugin directory when installing or copying this package. Copying only `skills/<name>/` omits required shared references; standalone per-skill copies are not supported by this source layout. A future per-skill distribution must bundle the shared resources and rewrite its links before installation.

```text
pt-clinical-skills/
├── references/                      # Shared across stages
│   ├── clinical-contract.md
│   ├── stage-routing.md
│   ├── pain-mechanisms.md
│   └── pain-discussion-catalog.md
└── skills/
    ├── subjective-analysis/          # SKILL.md + local assets/
    ├── objective-analysis/           # SKILL.md + local assets/
    └── impression/                   # SKILL.md + local assets/
        └── references/
            └── template-selection.md
```

All three skills link to the shared [clinical contract](references/clinical-contract.md), [stage routing](references/stage-routing.md) and [pain-mechanism guide](references/pain-mechanisms.md). The [historical discussion catalog](references/pain-discussion-catalog.md) is available when relevant; subjective synthesis links to it explicitly. Store cross-stage guidance once in root `references/`; keep guidance specific to one skill in that skill's `references/`. Output templates remain in each skill's `assets/`.

## Try a reviewable example

Read [synthetic complete input](evals/inputs/complete-case.md) alongside the [complete reference output](evals/results/complete-case-output.md). The output is an authored same-agent walkthrough, not an independently measured model result. [Legacy case mapping](examples/legacy-case-mapped.md) illustrates the source's three/five-column migration and provenance limitations.

## Validate locally

From this package directory:

```sh
python3 scripts/validate_package.py
python3 scripts/validate_package.py --output evals/results/complete-case-output.md --mode complete
```

The validator uses Python's standard library and checks package identity, source hashes, skill links, shared and skill-specific resource links, table headers/base rows and selected output invariants. It does not prove clinical correctness, actual skill discovery, or model behavior. [Behavioral cases](evals/cases.md), [rubric](evals/rubric.md) and [recorded results](evals/results/validation-report.md) specify the remaining review.

## Platforms

The shared skills use Markdown and have no server/API runtime dependency. [Platform guidance](docs/platforms/usage.md) distinguishes portable/Codex packaging, Claude Code and Gemini/Antigravity skill loading. No plugin has been installed or published by this implementation. Cross-platform host behavior remains to be verified.

## Source and development records

- [Source archive](sources/README.md): 12 read-only originals and nine page-tagged extraction snapshots.
- [Source manifest](sources/manifest.json): hashes for local provenance checks.
- [Template mapping](docs/migration/template-map.md): approved changes to each original table.
- [Approved specification](docs/specs/clinical-reasoning-rebuild.md) and [decision handoff](docs/migration/decision-audit.md).
- sources/legacy-scaffold/ holds the old three generic scaffold skills, outside the active skills directory.

Professional references include explicitly unverified material; consult the local guides and linked original sources before making disease-specific claims. This package has not undergone independent clinical validation or therapist usability testing. LICENSE retains existing rights; redistribution permissions for source materials remain to be confirmed before public release.
