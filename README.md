# PT Clinical Skills

A skill-only plugin for physical therapists to collect and clarify history, analyze subjective history, compare objective evidence and produce a clinical Impression. Version **0.2.0**, based on the approved specification v0.3 (2026-10-27).

## Start here

| Skill | Output |
| --- | --- |
| [history-intake](skills/history-intake/SKILL.md) | History clarification, symptom grouping, missing-data follow-up and readiness for subjective analysis |
| [subjective-analysis](skills/subjective-analysis/SKILL.md) | Tables 1.1/1.2 per actual symptom, then preliminary hypotheses and timeline in 2.1/2.2 |
| [objective-analysis](skills/objective-analysis/SKILL.md) | Structural/system evidence tables 3.1/3.2, support/opposition and missing information |
| [impression](skills/impression/SKILL.md) | Concise Table 4 and full Impression; optional versions on request |

Provide de-identified assessment data and ask for the relevant stage. Use **history-intake** to organize an unfinished history and collect missing information. Once the required history is sufficient, it offers to continue to subjective analysis. Direct analysis requests use a lightweight entry check and reuse existing history; they do not require a separate intake run. Missing required information is clarified before analysis, unless a limited preliminary analysis is explicitly agreed after its limitations are explained.

Subjective analysis example:

> Analyze my subjective physical therapy assessment using the fixed tables. Identify missing information and preliminary hypotheses without inventing results.

For a complete case:

> Analyze the complete assessment in one combined flow through full Impression, using subjective-analysis, objective-analysis and impression in that order.

All runtime output defaults to English. An explicit request may change narrative/filled-cell language; approved table titles and headers stay English. Staged operation accepts Next step, 下一步, 繼續 or another clear forward request. Complete-analysis requests bypass intermediate stops. The initial subjective tables precede preliminary synthesis; objective tables precede the final synthesis.

## What stays fixed and what can vary

Seven Markdown table assets implement six original table groups (Table 2 has two sub-tables). Headers, base rows and order are fixed. Symptom count follows the supplied case, not a three-symptom quota. System rows and Table 3.1 categories may be extended while retaining base rows. Symptoms Stage and Irritability are separate. Contributing factors remains open to all case-supported factors.

Approved support labels: ★★★ Strong, ★★ Moderate, ★ Low, − Currently not supported, ✕ Ruled-out, ⚠ Conflicting evidence, ? Unable to determine / Pending assessment. Each needs its case rationale; these are not numerical probabilities or research grades. Unknown findings are never negative by default.

The workflow ends at Impression and related clarification/assessment questions. It does not provide unrequested treatment plans or exercise dosage. Source examples are not default patient findings.

## Shared references and installation

The repository root is the plugin directory. Keep the complete repository when installing or copying this package, including the hidden `.codex-plugin/` and `.claude-plugin/` directories. Copying only `skills/<name>/` omits required shared references; standalone per-skill copies are not supported by this source layout. A future per-skill distribution must bundle the shared resources and rewrite its links before installation.

```text
Physio-logic/                        # Repository and plugin root
├── README.md
├── plugin.json
├── .codex-plugin/
├── .claude-plugin/
├── references/                      # Shared across stages
│   ├── clinical-contract.md
│   ├── stage-routing.md
│   ├── pain-mechanisms.md
│   ├── kinetic-chain-analysis.md
│   └── pain-discussion-catalog.md
└── skills/
    ├── history-intake/               # SKILL.md
    ├── subjective-analysis/          # SKILL.md + local assets/
    ├── objective-analysis/           # SKILL.md + local assets/
    └── impression/                   # SKILL.md + local assets/
        └── references/
            └── template-selection.md
```

All four skills link to the shared [clinical contract](references/clinical-contract.md) and [stage routing](references/stage-routing.md). The three analysis skills also use the [pain-mechanism guide](references/pain-mechanisms.md). The [historical discussion catalog](references/pain-discussion-catalog.md) is available when relevant; subjective synthesis links to it explicitly. Store cross-stage guidance once in root `references/`; keep guidance specific to one skill in that skill's `references/`. Output templates remain in each skill's `assets/`.

For relevant functional or sporting tasks, the three analysis skills use the shared [kinetic-chain guide](references/kinetic-chain-analysis.md): subjective analysis explores candidate regional contributions, objective analysis evaluates supplied movement and examination findings, and Impression integrates the supported explanation. The guide covers task phases, anatomical movement demands, clinically observable sequence and Kinetic Control concepts without requiring instrumented peak-velocity or energy measurements.

## Try a reviewable example

Read [synthetic complete input](evals/inputs/complete-case.md) alongside the [historical complete reference output](evals/results/complete-case-output.md). The output is an authored same-agent walkthrough using the previous Table 1.2 contract, not an independently measured model result or a current-format validation fixture. [Legacy case mapping](examples/legacy-case-mapped.md) illustrates the source's three/five-column migration and provenance limitations.

Current subjective Table 1.2 uses System / Category, Explanation & Basis and Structures & Relationships, including relevant anatomical regions. Its Myofascial / Fascial system label is broader than the historical label. Selected system expansions may follow each symptom's table using the subjective skill's heading and content rules; they are optional detail within Phase 1. Existing system references retain their reasoning frameworks, and objective Table 3.2 retains its five-column contract.

## Validate locally

From the repository root:

```sh
python3 scripts/validate_package.py
python3 -B -m unittest discover -s scripts -p 'test_*.py'
```

The validator uses Python's standard library and checks package identity, source hashes, skill links, shared and skill-specific resource links, table headers/base rows and selected output invariants. Full package validation requires the source files and sources/manifest.json. To validate a current-format output, add `--output path/to/output.md --mode subjective-initial --symptoms 1` with the appropriate mode/count. The unit checks exercise current structural output behavior using synthetic fixtures; they do not replace source-integrity checks. Neither check proves clinical correctness, actual skill discovery, or model behavior. [Behavioral cases](evals/cases.md), [rubric](evals/rubric.md) and [recorded results](evals/results/validation-report.md) specify the remaining review.

## Platforms

The shared skills use Markdown and have no server/API runtime dependency. [Platform guidance](docs/platforms/usage.md) distinguishes portable/Codex packaging, Claude Code and Gemini/Antigravity skill loading. No plugin has been installed or published by this implementation. Cross-platform host behavior remains to be verified.

## Source and development records

- [Source archive](sources/README.md): 12 read-only originals and nine page-tagged extraction snapshots.
- [Source manifest](sources/manifest.json): hashes for local provenance checks.
- [Template mapping](docs/migration/template-map.md): approved changes to each original table.
- [Approved specification](docs/specs/clinical-reasoning-rebuild.md) and [decision handoff](docs/migration/decision-audit.md).
- sources/legacy-scaffold/ holds the old three generic scaffold skills, outside the active skills directory.

Professional references include explicitly unverified material; consult the local guides and linked original sources before making disease-specific claims. This package has not undergone independent clinical validation or therapist usability testing. LICENSE retains existing rights; redistribution permissions for source materials remain to be confirmed before public release.
