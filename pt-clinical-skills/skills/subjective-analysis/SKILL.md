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

1. **Required references:** Read [clinical contract](../../references/clinical-contract.md) and [stage routing](../../references/stage-routing.md) when starting this workflow.
   - This skill owns Tables 1.1, 1.2, 2.1 and 2.2; Table 2 is preliminary subjective synthesis, not an objectively confirmed final Impression.

2. **Data inventory:** Identify the available history, actual distinct symptoms, functional goals, dates and missing information.
3. **Symptom classification:** Classify each distinct symptom with a stable ID, its reported location/distribution and symptom description; preserve these across all three Phase 1 steps.
   - If no case history exists, ask for the main symptoms and useful history before generating tables; do not fabricate a case.
   - Use supplied information without asking for it again.

4. **Analysis mode:** Determine whether the request is staged or explicitly asks for a complete combined analysis; follow the corresponding route below.

#### Minimum-Data Checklist

- **Intake inventory:** Inventory the seven items below from supplied information before Phase 1.
- **Completion status:** Check an item only when Available; otherwise leave it unchecked and label it Partial or Not provided.
- Add a brief source-labeled summary.
- Only Available counts toward completion; do not count inferred information.
- Explicitly reported absence is information, whereas an omitted history is not.
- These are workflow intake criteria, not a validated clinical score.

- [ ] **1. Background and relevant history:** Age or age range; known diseases, relevant injury/surgery and medication overview, including explicitly reported absence where applicable.
- [ ] **2. Symptom location and distribution:** Reported location, side where applicable, extent and whether symptoms extend elsewhere.
- [ ] **3. Symptom character:** The patient's description, such as pain, tingling, burning, stiffness or perceived weakness; preserve their wording.
- [ ] **4. Onset and course:** Approximate onset, sudden/gradual presentation, any reported initiating event or absence of a known event, and improving/worsening/stable course.
- [ ] **5. Symptom behavior:** Constant/intermittent pattern and aggravating/relieving activities, postures or contexts; an explicit report of no recognized pattern is acceptable.
- [ ] **6. Functional impact and goals:** Affected daily/work/valued activities and what the person wants to improve.
- [ ] **7. Intensity and episode details:** Intensity or tolerability, frequency, episode duration and recovery/settling time where applicable.

- **Required items:** Items 1–5 are required: item 1 is case-wide and items 2–5 must be checked separately for each symptom; items 6–7 are recommended additions.

- The normal entry threshold is at least 5 of 7 Available items, with all five required items Available.
- Apply items 2–5 separately to each symptom; one well-described symptom must not conceal another symptom's missing information.
- Report per-symptom gaps rather than a misleading case-wide pass.
- Optional items cannot compensate for missing required items.
- Collect outstanding recommended information before Phase 2 where possible, retaining explicit limitations if it remains unavailable.

- **Missing required data:** If the threshold is not met, stay in Phase 0 and ask one concise, grouped set of questions for missing required information, using existing answers without asking again.
  - Do not generate candidate-source tables yet.
- **Limited-analysis exception:** If the user cannot supply a required item, retain the unknown, explain the specific limitation and ask whether they want a limited preliminary analysis.
  - Proceed under that exception only after explicit agreement, keeping the limitation visible rather than marking the intake complete.
- A complete-analysis request bypasses routine stage-confirmation stops, not this missing-data requirement.

#### Model-Led Red-Flag Follow-Up

- Red-flag screening is an active follow-up responsibility of the model, not information the user must supply in the initial submission or a point toward a minimum-data completion score.
- **Targeted screening:** Review the available symptoms and history, identify relevant unanswered screening questions under the clinical contract, and ask specific questions rather than asking the user to identify their own red flags.
- Use existing answers without repeating questions and tailor follow-up to the presentation rather than requiring a universal checklist.

- Distinguish reported answers, unanswered questions and potentially urgent cues.
- Missing or unanswered screening information remains unknown, not a negative screen.
- **Urgent concerns:** Address potentially urgent cues immediately under the clinical contract; do not wait for routine data collection or table completion.
- Continue relevant follow-up as new information emerges.

### Phase 1: Symptom-Source Exploration

- For each symptom classified in Phase 0, perform Steps 1–3 in order.
- **Symptom templates:** Read [Table 1.1](assets/table-1-1.md) and [Table 1.2](assets/table-1-2.md); replace authoring placeholders with candidate explanations or explicit unknowns.
- Repeat each table for the actual symptom count, with stable IDs; one symptom yields one pair, four symptoms four pairs.
- Never pad or truncate to three.
- These are three reasoning steps within Phase 1, without additional confirmation stops between them.

#### Step 1: Adjacent Tissue Candidates — Table 1.1, Column 2

1. **Symptom location:** Start at the reported symptom location.
2. **Adjacent sources:** In Adjacent possible sources, enumerate nearby tissues that could plausibly generate that symptom.
3. **Tissue coverage:** Review all 13 tissue categories in their original order and cover applicable categories as fully as the symptom location and available history allow.
4. **Candidate rationale:** Name specific anatomical candidates where possible and explain their anatomical/symptom-pattern basis; these are possibilities to examine, not evidence that an injury exists there.

   - Retain every base row.
   - When a category is inapplicable to this symptom/location, enter Not applicable with a brief reason.
   - When applicability or a candidate cannot be determined because information is missing, use an explicit unknown rather than Not applicable.
   - Do not fill rows merely to achieve a candidate count.

#### Step 2: Remote Tissue Candidates — Table 1.1, Column 3

1. **Remote sources:** In Possible sources of referred pain from remote regions, enumerate tissues outside the reported symptom location that could produce symptoms there.
2. **Referral references:** Consider relevant trigger-point referral maps, facet-joint referred-pain patterns, visceral referral, remote neural sources and vascular sources as candidate-generating references.
   - These examples are non-exhaustive; use symptom type and distribution to decide relevance, and distinguish referred pain from neural or vascular symptom pathways rather than calling every remote mechanism referred pain.

3. **Source mapping:** Name the remote structure and location, place it in the appropriate tissue row, and state the proposed connection to the reported symptom, its basis and uncertainty.
4. **Joint classification:** Describe joint candidates at the tissue level where justified; do not force a multi-tissue joint explanation into an unreliable single-row mapping.
5. **Source verification:** Check sources when needed under the clinical contract; a map or pattern match generates a hypothesis and does not establish causation.
   - Apply the same Not applicable versus unknown distinction as Step 1.
   - Keep the completed Table 1.1's three columns and 13 base tissue rows in order.

#### Step 3: System and Disease Candidates — Table 1.2

1. **Systems and diseases:** Broaden from the tissue/source candidates in Steps 1–2 to systems, integrated functions and disease categories that could explain or contribute to the symptom.
   - Do not merely repeat the adjacent and remote tissue lists.
   - Preserve Table 1.2's three columns and six base system rows; append other case-relevant systems or disease categories as needed.
   - The categories are open-ended, not limited to the base rows.

2. **System rationale:** For each relevant row, identify the possible system-level explanation or disease category, the case/anatomical basis for considering it, relevant structures or pathways, and affected regions.
   - Disease entries need not have an upstream/downstream chain: use Not applicable with a reason where that column does not fit, and keep missing information explicitly unknown.
   - Distinguish hypotheses from established diagnoses and avoid listing unrelated diseases solely for completeness.

- Retain Kinetic chain as an existing template row pending further discussion of its role.
- Do not treat it as a synonym for systemic disease or force every system/disease explanation into a kinetic-chain model.

3. **Required sections:** After Steps 1–3, add the clinical contract's Red Flags, Yellow Flags and Reasoning Rationale and Limitations sections.
- Address potentially urgent concerns immediately rather than waiting to finish the steps.
- **Subjective stop:** Stop and invite a clear forward request before Table 2, unless a complete combined analysis was explicitly requested.

### Phase 2: Preliminary Hypotheses and History Timeline

1. **Mechanism guidance:** Read [pain-mechanism guide](../../references/pain-mechanisms.md) when interpreting mechanisms; consult [discussion catalog](../../references/pain-discussion-catalog.md) only when relevant, with its evidence limits.
2. **Preliminary hypotheses:** Fill [Table 2.1](assets/table-2-1.md).
   - Preserve Item/Content and all rows, including SEPARATE Symptoms Stage and Irritability.
   - Stage describes reported duration/course; irritability considers provocation, response and settling.
   - Do not infer either from the other or solely from a pain score.
   - Contributing factors remains open to all case-supported factors.
3. **History timeline:** Fill [Table 2.2](assets/table-2-2.md) using only reported events/times, preserving the exact History timeline-S title.
   - Do not invent earlier history or a fixed number of events.
4. **Follow-up lists:** Outside the tables, include exactly these two named lists, with as many material items as needed rather than a fixed quota:
   - Suggested Follow-Up Questions & Recommended Additional Information
   - Next Steps in Clinical Reasoning (How to Confirm or Refute the Hypothesis)
5. **Required sections:** Include the three clinical-contract sections, avoiding duplicate evidence.
6. **Hypothesis verification:** Identify which questions/tests could change a hypothesis.
7. **Objective handoff:** End by requesting objective findings; do not generate Tables 3 or 4 from missing data.

### Phase 3: Handoff or Complete-Analysis Continuation

- **Stage continuity:** For a staged handoff, preserve the clinical contract's case scope, data version, symptom IDs, source-labeled findings, hypotheses, unknowns and completed tables.
  - State that objective findings are needed next.

- Use the same resources and table order without the internal subjective stop when the user explicitly requests one combined analysis.
- Follow stage routing for the objective and Impression portions; do not silently omit them or invent their templates.
- Keep assumptions distinct from provided facts and identify limitations when only partial data exist.

## Verification

Before delivering the current stage, confirm:

- [ ] The seven-item intake checklist uses supplied facts; all five required items are available for the case and each symptom before Phase 1, or an explicit limited-analysis exception and its remaining gaps are recorded.
- [ ] Relevant unanswered red-flag questions were actively identified and asked from the available case context; initial omission was not treated as a failed intake item or a negative screen.
- [ ] When produced, Tables 1.1 and 1.2 match the actual symptom count and retain stable symptom IDs, base rows and columns.
- [ ] Table 1.1 considers all 13 categories in sequence: adjacent candidates in column 2, then remote candidates in column 3, with a basis and uncertainty for each candidate.
- [ ] Not applicable has a reason and denotes inapplicability; missing information remains unknown rather than inapplicable or negative.
- [ ] Table 1.2 broadens to system/disease explanations with case relevance, permits additional categories and does not reduce every explanation to a kinetic chain.
- [ ] If subjective synthesis is authorized, Tables 2.1 and 2.2 retain all required items and the exact timeline title; Stage and Irritability have separate bases.
- [ ] When produced, the timeline contains only reported events/times; unknowns and current inferences are distinct from supplied facts.
- [ ] When produced, subjective synthesis includes both named follow-up/verification lists, with material items rather than a fixed quota.
- [ ] The current table group includes Red Flags, Yellow Flags and Reasoning Rationale and Limitations as required by the clinical contract.
- [ ] The response respects the current staged stop or explicit complete-analysis request and identifies outstanding data and the next action.
