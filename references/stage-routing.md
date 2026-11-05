# Stage routing and continuity

Use the shared references at the plugin root and the assets or dedicated references within the skill being executed. Keep the complete plugin directory structure when installing or copying these skills; a skill folder alone omits required shared resources. Each stage can be used directly when its required case context is available, without running another stage first. Another skill's files are never required for a normal single-stage request.

## Default staged route

- History intake: use `history-intake` to organize and clarify history, apply the minimum-data checklist, classify symptoms with stable IDs and perform model-led red-flag follow-up. When ready, ask whether to proceed to subjective analysis unless that analysis was already requested. Retain unknowns and any explicitly agreed limited-analysis exception in the handoff.
- Subjective entry: briefly check available history or the intake handoff and proceed when sufficient; a full intake is not mandatory for every analysis request. Use history-intake for unresolved required information or symptom grouping, without repeating known information. For each symptom, consider adjacent tissues in Table 1.1 column 2, then remote tissue sources in column 3, then system/disease explanations in Table 1.2, following subjective-analysis Phase 1. Complete these three internal steps without additional confirmation stops, then STOP for a clear forward request before subjective synthesis.
- Subjective synthesis: on Next step, 下一步, 繼續 or another clear equivalent, generate one numbered Table 2.1 per Phase 1 symptom and one shared Table 2.2, followed by the two named follow-up/verification lists. Apply the clinical contract's user-hypothesis checkpoint: present the first six rows and timeline, ask for user hypotheses, and wait. Record supplied hypotheses or an explicit decline before requesting objective findings; do not generate a synthesis hypothesis on the user's behalf.
- Objective: when objective data arrive, generate one numbered 3.1 and 3.2 per symptom, preserving symptom IDs and the table-instance mapping, then STOP for a clear forward request.
- Final synthesis: on that request, generate Table 4 and full Impression, then offer a concise version or an appropriate alternative with a reason. Explicit version requests take precedence.

A clear forward request only advances the current stage. Do not invent missing objective findings when the next step requires them. Interrupt routine ordering for a potentially urgent issue.

Within subjective Phase 1, each symptom's Table 1.1 → Table 1.2 may be followed by selected system expansions before the next symptom block. These are optional detail within Step 3, not a new stage or permission to generate Table 2. Preserve each symptom ID and the existing stop before subjective synthesis.

## Complete-analysis request

When explicitly asked for a complete combined analysis, perform 1.1 → 1.2 → 2.1 → 2.2 → 3.1 → 3.2 → 4 → full Impression in order, without intermediate stage-continuation confirmations. The user-hypothesis checkpoint still applies after the symptom profiles and shared timeline: wait for user hypotheses or an explicit decline before continuing to the objective portion, unless already supplied for this analysis. Then resume the authorized combined analysis when the required data are available. history-intake's minimum-data requirement still applies; a complete-analysis request alone does not authorize a limited-data exception. Use other installed stage skills when available and the host supports that; no subagents are required. If they are unavailable, complete the portion supported by this skill, state the missing stage capability and request/load the relevant stage skill rather than improvising its fixed schema or pretending the full request is complete.

Keep subjective preliminary hypotheses distinguishable from later objective updates. For multiple symptom blocks, preserve their IDs in summaries; do not assume there must be exactly three. Read only the resources needed for the next authorized stage.
