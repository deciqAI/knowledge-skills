# Method in Action: OKRs in an AI-Native Org (2024–2026)

> *Example for the [okr-goal-setting](../SKILL.md) skill.*

By 2024–2026, "add AI" had become the default objective for nearly every product team. The trap is structural: an objective like *"ship AI features"* or *"increase AI usage"* invites exactly the vanity and Goodhart metrics OKRs exist to prevent. This is a composite, illustrative case — a small, fast product team (roughly 8 engineers plus a PM and a designer) putting an AI assistant into an existing SaaS product — chosen to show how the six Process steps discipline AI bets. The numbers below are illustrative targets, not measured results.

The team's first-draft OKR was the common one:

- Objective: *"Make our product AI-first."*
- KR1: Ship the AI assistant to GA.
- KR2: Get 50% of users to try the assistant.
- KR3: Reach 1M AI messages/month.

Every one of these is a trap. "Ship to GA" is an activity. "Try the assistant" and "messages/month" are usage-of-a-feature metrics that go up whether or not the feature helps anyone — a chatbot that fails and makes users retry inflates message count. This is Goodhart's law ("when a measure becomes a target, it ceases to be a good measure") applied to AI: optimize AI usage and you can grow the number while destroying trust.

**Step 1 — Write the Objective.** Rewrite around the value the AI is supposed to create, not the AI itself. Objective: *"Users trust the assistant to finish real work for them."* Qualitative, aspirational, and it passes the test — if achieved, it objectively matters, because it is the difference between a demo and a product.

**Step 2 — Write 3-5 outcome KRs.** The move is to measure completed value and cost, never activity or raw usage:

- KR1 (task success): "≥60% of assistant sessions end in a task the user accepts without editing or retrying" — measured via accept/undo/retry telemetry, not a thumbs-up widget people ignore. This is the anti-vanity core: a session only counts if it produced accepted work.
- KR2 (retention): "Day-30 retention of assistant users rises from 22% to 38%" — retention is Goodhart-resistant because a gamed, unhelpful feature does not bring people back.
- KR3 (unit economics): "Cost-per-resolved-task falls from ~$0.40 to ≤$0.18" — an outcome KR that ties model/inference spend to delivered value, so "more usage" is only good if it is *cheaper* delivered value. (Approximate, illustrative figures.)
- KR4 (trust/quality guardrail): "Human-flagged incorrect answers stay ≤2% of sampled sessions" — a counter-metric so the team cannot buy KR1–KR3 by shipping a confident-but-wrong assistant.

Note what is absent: no "messages sent," no "features shipped," no "% who tried it." Contrast with the skill's pattern table — "Increase AI usage" is the 2020s cousin of "Launch new onboarding flow."

**Step 3 — Calibrate ambition.** 22%→38% retention and 60% clean task-success on a new AI surface are genuine stretches (roughly 50–70% likelihood, not near-certain). The ≤2% error guardrail is deliberately *not* a stretch — guardrails should be safe by design, because you do not want the team betting on the ceiling of harm.

**Step 4 — Cascade and align.** In a small fast team the cascade is short but the cross-team dependency is load-bearing: the assistant's cost-per-task (KR3) depends on the platform/infra team's inference and caching work, so that dependency must appear explicitly in *both* teams' OKRs. Without it, the AI team is scored on a number another team controls.

**Step 5 — Run the quarterly cycle.** AI features degrade and drift faster than classic software (model updates, prompt regressions, changing user behavior), so the mid-quarter check matters more than usual — a KR1 that was 0.6 at mid-quarter can quietly fall as usage broadens beyond early adopters.

**Step 6 — Score honestly.** The honest-scoring payoff is the same as in the classic cases: a stretched 0.6 on "accepted task completions" is worth far more than a sandbagged 1.0 on "messages sent." If the team had shipped the first-draft OKR, it could have hit 1M messages/month, declared victory, and still have built something users quietly abandoned — the exact failure OKRs are designed to make visible.

The mapped steps:
1. Write the Objective: value the AI delivers ("trusted to finish real work"), not the AI itself ("AI-first")
2. Write outcome KRs: accepted task completions, retention, cost-per-resolved-task, plus an error-rate guardrail — never "usage" or "shipped"
3. Calibrate: retention and task-success as real stretches; the safety guardrail deliberately not a stretch
4. Cascade: inference-cost KR shared explicitly with the infra team it depends on
5. Run the cycle: tighter mid-quarter checks because AI quality drifts
6. Score honestly: a stretched 0.6 on accepted work beats a sandbagged 1.0 on message volume

*Sources: Doerr, J. (2018). *Measure What Matters.* Portfolio (OKR outcome-vs-activity discipline). Goodhart, C. A. E. (1975), and Strathern, M. (1997), "'Improving ratings': audit in the British University system," *European Review* 5(3):305–321 — the canonical "when a measure becomes a target…" formulation. AI-metric and drift framing is the author's illustrative synthesis, not a cited measured result.*
