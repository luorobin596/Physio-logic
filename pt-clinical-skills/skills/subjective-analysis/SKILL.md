---
name: subjective-analysis
description: Analyze physical therapy subjective history using fixed symptom tables, a history timeline and preliminary clinical hypotheses. Use for symptom/history analysis or the subjective stage of a complete assessment; not for literature appraisal.
---

# Subjective analysis

Read [clinical contract](references/clinical-contract.md) and [stage routing](references/stage-routing.md) when starting this workflow. Runtime outputs default to English. This skill owns Tables 1.1, 1.2, 2.1 and 2.2; Table 2 is preliminary subjective synthesis, not an objectively confirmed final Impression.

## First subjective step

1. Identify the available history, actual distinct symptoms, functional goals, dates and missing information. Do not fabricate a case if no data were supplied.
2. Read [Table 1.1](assets/table-1-1.md) and [Table 1.2](assets/table-1-2.md). Replace authoring placeholders with supported content or explicit unknowns. Repeat each for the actual symptom count, with stable IDs; one symptom yields one pair, four symptoms four pairs. Never pad or truncate to three.
3. Keep Table 1.1's 13 base tissue rows in order. For Table 1.2 preserve its three columns and six base system rows; append other case-relevant systems/disease categories when useful, clearly named and not confused with kinetic-chain terminology. Candidate structures require a basis and uncertainty, not proof of injury at the pain site.
4. Add the clinical contract's Red Flags, Yellow Flags and Reasoning Rationale and Limitations sections. Stop and invite a clear forward request before Table 2, unless a complete combined analysis was explicitly requested.

## Subjective synthesis step

1. Read [pain-mechanism guide](references/pain-mechanisms.md) when interpreting mechanisms; consult [discussion catalog](references/pain-discussion-catalog.md) only when relevant, with its evidence limits.
2. Fill [Table 2.1](assets/table-2-1.md). Preserve Item/Content and all rows, including SEPARATE Symptoms Stage and Irritability. Stage describes reported duration/course; irritability considers provocation, response and settling. Do not infer either from the other or solely from a pain score. Contributing factors remains open to all case-supported factors.
3. Fill [Table 2.2](assets/table-2-2.md) using only reported events/times, preserving the exact History timeline-S title. Do not invent earlier history or a fixed number of events.
4. Outside the tables, include exactly these two named lists, with as many material items as needed rather than a fixed quota:
   - Suggested Follow-Up Questions & Recommended Additional Information
   - Next Steps in Clinical Reasoning (How to Confirm or Refute the Hypothesis)
5. Include the three clinical-contract sections, avoiding duplicate evidence. Identify which questions/tests could change a hypothesis. End by requesting objective findings; do not generate Tables 3 or 4 from missing data.

## Complete input

Use the same resources and table order without the internal subjective stop when the user explicitly requests one combined analysis. Follow stage routing for the objective and Impression portions; do not silently omit them or invent their templates. Keep assumptions distinct from provided facts and identify limitations when only partial data exist.
