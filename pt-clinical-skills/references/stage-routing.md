# Stage routing and continuity

Use the shared references at the plugin root and the assets or dedicated references within the skill being executed. Keep the complete plugin directory structure when installing or copying these skills; a skill folder alone omits required shared resources. Each stage can be used directly when its required case context is available, without running another stage first. Another skill's files are never required for a normal single-stage request.

## Default staged route

- Subjective entry: if no case history exists, ask for the main symptoms and useful history. With subjective data, generate Tables 1.1 and 1.2 for actual distinct symptoms, then STOP for a clear forward request.
- Subjective synthesis: on Next step, 下一步, 繼續 or another clear equivalent, generate 2.1 and 2.2, followed by the two named follow-up/verification lists; then request objective findings.
- Objective: when objective data arrive, generate 3.1 and 3.2, then STOP for a clear forward request.
- Final synthesis: on that request, generate Table 4 and full Impression, then offer a concise version or an appropriate alternative with a reason. Explicit version requests take precedence.

A clear forward request only advances the current stage. Do not invent missing objective findings when the next step requires them. Interrupt routine ordering for a potentially urgent issue.

## Complete-analysis request

When explicitly asked for a complete combined analysis, perform 1.1 → 1.2 → 2.1 → 2.2 → 3.1 → 3.2 → 4 → full Impression in order, with no intermediate confirmation stop. Use other installed stage skills when available and the host supports that; no subagents are required. If they are unavailable, complete the portion supported by this skill, state the missing stage capability and request/load the relevant stage skill rather than improvising its fixed schema or pretending the full request is complete.

Keep subjective preliminary hypotheses distinguishable from later objective updates. For multiple symptom blocks, preserve their IDs in summaries; do not assume there must be exactly three. Read only the resources needed for the next authorized stage.
