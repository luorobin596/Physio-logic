---
name: subjective-analysis
description: Analyze physical therapy subjective history using fixed symptom tables, a history timeline and preliminary clinical hypotheses. Use for symptom/history analysis or the subjective stage of a complete assessment.
---

# Subjective analysis

## Overview

Analyze reported symptoms and history in two steps: symptom-source exploration, then preliminary subjective synthesis. Keep these hypotheses distinct from objectively confirmed conclusions.

## When to Use

Use for symptom/history analysis, subjective synthesis, or the subjective portion of an explicitly requested complete assessment. Resume from the current stage when a handoff is available.

## Workflow

### Phase 0: Scope Check and Data Collection

Read [clinical contract](../../references/clinical-contract.md) and [stage routing](../../references/stage-routing.md) when starting this workflow. This skill owns Tables 1.1, 1.2, 2.1 and 2.2; Table 2 is preliminary subjective synthesis, not an objectively confirmed final Impression.

Identify the available history, actual distinct symptoms, functional goals, dates and missing information. If no case history exists, ask for the main symptoms and useful history before generating tables; do not fabricate a case. Use supplied information without asking for it again.

Determine whether the request is staged or explicitly asks for a complete combined analysis; follow the corresponding route below.

### Phase 1: Symptom-Source Exploration

1. Read [Table 1.1](assets/table-1-1.md) and [Table 1.2](assets/table-1-2.md). Replace authoring placeholders with supported content or explicit unknowns. Repeat each for the actual symptom count, with stable IDs; one symptom yields one pair, four symptoms four pairs. Never pad or truncate to three.
2. Keep Table 1.1's 13 base tissue rows in order. For Table 1.2 preserve its three columns and six base system rows; append other case-relevant systems/disease categories when useful, clearly named and not confused with kinetic-chain terminology. Candidate structures require a basis and uncertainty, not proof of injury at the pain site.
3. Add the clinical contract's Red Flags, Yellow Flags and Reasoning Rationale and Limitations sections. Stop and invite a clear forward request before Table 2, unless a complete combined analysis was explicitly requested.

### Phase 2: Preliminary Hypotheses and History Timeline

1. Read [pain-mechanism guide](../../references/pain-mechanisms.md) when interpreting mechanisms; consult [discussion catalog](../../references/pain-discussion-catalog.md) only when relevant, with its evidence limits.
2. Fill [Table 2.1](assets/table-2-1.md). Preserve Item/Content and all rows, including SEPARATE Symptoms Stage and Irritability. Stage describes reported duration/course; irritability considers provocation, response and settling. Do not infer either from the other or solely from a pain score. Contributing factors remains open to all case-supported factors.
3. Fill [Table 2.2](assets/table-2-2.md) using only reported events/times, preserving the exact History timeline-S title. Do not invent earlier history or a fixed number of events.
4. Outside the tables, include exactly these two named lists, with as many material items as needed rather than a fixed quota:
   - Suggested Follow-Up Questions & Recommended Additional Information
   - Next Steps in Clinical Reasoning (How to Confirm or Refute the Hypothesis)
5. Include the three clinical-contract sections, avoiding duplicate evidence. Identify which questions/tests could change a hypothesis. End by requesting objective findings; do not generate Tables 3 or 4 from missing data.

### Phase 3: Handoff or Complete-Analysis Continuation

For a staged handoff, preserve the clinical contract's case scope, data version, symptom IDs, source-labeled findings, hypotheses, unknowns and completed tables. State that objective findings are needed next.

Use the same resources and table order without the internal subjective stop when the user explicitly requests one combined analysis. Follow stage routing for the objective and Impression portions; do not silently omit them or invent their templates. Keep assumptions distinct from provided facts and identify limitations when only partial data exist.

## Verification

Before delivering the current stage, confirm:

- [ ] When produced, Tables 1.1 and 1.2 match the actual symptom count and retain stable symptom IDs, base rows and columns.
- [ ] If subjective synthesis is authorized, Tables 2.1 and 2.2 retain all required items and the exact timeline title; Stage and Irritability have separate bases.
- [ ] When produced, the timeline contains only reported events/times; unknowns and current inferences are distinct from supplied facts.
- [ ] When produced, subjective synthesis includes both named follow-up/verification lists, with material items rather than a fixed quota.
- [ ] The current table group includes Red Flags, Yellow Flags and Reasoning Rationale and Limitations as required by the clinical contract.
- [ ] The response respects the current staged stop or explicit complete-analysis request and identifies outstanding data and the next action.
