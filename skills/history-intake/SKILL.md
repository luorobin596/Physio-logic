---
name: history-intake
description: Organize and clarify physical therapy history, collect missing interview information and check readiness for subjective analysis. Use when the user wants help completing history or when required history is missing before analysis.
---

# History - intake

## Overview

Help the user clarify and supplement the history already collected. Preserve their descriptions, identify missing information and determine whether the history is sufficient to begin subjective analysis.

## When to Use

Use for history collection, clarification or readiness review. Reuse supplied facts and prior intake work; a completed intake is not a mandatory prerequisite when the user directly requests analysis with sufficient data.

## Workflow

### Scope Check and Data Collection

1. **Required references:** Read [clinical contract](../../references/clinical-contract.md) and [stage routing](../../references/stage-routing.md) when starting this workflow.
   - This skill prepares history for analysis; do not generate candidate-source tables or preliminary clinical hypotheses during intake.

2. **Data inventory:** Identify the available history, actual distinct symptoms, functional goals, dates and missing information.
3. **Symptom classification:** Apply the symptom-splitting rules below. Classify each distinct symptom with a stable ID, its reported location/distribution and symptom description; preserve these in the handoff and subsequent analysis.
   - If no case history exists, ask for the main symptoms and useful history before assessing readiness; do not fabricate a case.
   - Use supplied information without asking for it again.

4. **Requested scope:** Preserve whether the user requested intake only, subjective analysis or a complete combined analysis so the handoff follows their intent.

#### Symptom-Splitting Rules

- **Descriptive scope:** Use symptoms that can be independently described and tracked as the unit of classification. Organize the patient's descriptions without judging symptom sources or establishing hypotheses; leave those judgments to subjective analysis. Do not split symptoms by a presumed diagnosis.
- **Separate locations:** Assign separate IDs when symptoms in different locations can occur or change independently.
- **Different qualities:** At the same location, split different symptom qualities when their timing, provoking conditions or course differ. If they always occur together, initially retain them as multiple descriptors of one symptom.
- **Continuous distribution:** Initially retain a continuously extending symptom pattern as one symptom's distribution, such as symptoms extending from the buttock to the calf. Do not automatically create an item for every region.
- **Bilateral symptoms:** Split sides when they can vary independently. If timing and quality are the same, initially allow a combined item while preserving side-specific differences.
- **Unclear relationship:** Ask whether symptoms occur together and whether they can change independently before deciding how to group them; do not guess.
- **Separate context:** Record functional limitations and existing diagnoses separately rather than automatically treating them as symptom items.
- **Grouping meaning:** Combining descriptions into one symptom item is a recording decision, not a conclusion that they share one cause.

#### Minimum-Data Checklist

- **Intake inventory:** Inventory the seven items below from supplied information before subjective analysis.
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
- Collect outstanding recommended information before preliminary subjective synthesis where possible, retaining explicit limitations if it remains unavailable.

- **Missing required data:** If the threshold is not met, continue intake and ask one concise, grouped set of questions for missing required information, using existing answers without asking again.
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

#### Intake Output

Present the following four parts in order, using supplied facts, explicit unknowns and stable symptom IDs:

1. **Background summary:** Summarize age, relevant history, injury/surgery and medications.
2. **Symptom list:** For each ID, include the original description, location/distribution, character, onset/course and aggravating/relieving conditions. Explain grouping or splitting where needed so the user can correct the classification.
3. **Inventory and questions:** Present the minimum-data checklist with Available, Partial or Not provided status and ask only for missing information. List model-led red-flag questions separately from the minimum-data questions.
4. **Continuation status:** State whether intake remains open or the history is ready for subjective analysis.
   - Continue intake when required information is missing or a grouping relationship needs clarification, and request the relevant answers.
   - When required data are sufficient and symptom grouping is unambiguous, ask whether the user wants to proceed to subjective analysis. If they already requested subjective or complete combined analysis, continue within that authorized scope without asking again.
   - Preserve the explicitly agreed limited-analysis exception and urgent-concern priority defined above.

### Handoff

Preserve the case scope, dates/data version, stable symptom IDs, source-labeled history, grouping decisions, checklist status, contradictions, unknowns and screening answers or outstanding questions under the clinical contract. State any agreed limited-analysis exception and the next authorized action. Carry recommended information still missing into subjective synthesis; do not mark it complete merely because analysis can begin.

## Verification

- [ ] Symptoms are grouped from patient descriptions rather than source hypotheses; independent variation, continuous distributions, side differences and unresolved grouping questions follow the symptom-splitting rules.
- [ ] The four intake output parts are presented in order; red-flag questions remain separate from minimum-data gaps.
- [ ] The seven-item checklist uses supplied facts; all five required items are available for the case and each symptom, or the remaining gaps and explicitly agreed limited-analysis exception remain visible.
- [ ] Relevant unanswered red-flag questions were actively identified and asked; initial omission was not treated as a failed intake item or a negative screen, and urgent cues took priority.
- [ ] Previously supplied information was reused, and facts, unknowns and contradictions remain source-labeled without generating clinical source hypotheses.
- [ ] The continuation offer respects the user's existing request and the handoff preserves symptom IDs, outstanding information and screening status.
