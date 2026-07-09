# Method in Action: Sorting 2024–2026 AI Decisions by Domain

> *Example for the [cynefin](../SKILL.md) skill.*

By 2024–2026, many organizations building with AI had moved past "should we use AI?" into a harder question: *which* AI decisions can be run like engineering, which must be run like exploration, and which are outright fires. Cynefin's core warning — that the costliest error is treating a Complex problem as a Complicated one — maps almost exactly onto the mistakes teams made when they applied the same delivery playbook to a known API integration, to an autonomous agent, and to a live incident. This example walks one organization's AI portfolio through the skill's Process.

**Step 1 — Describe.**

- **Decision/situation:** A product org wants to ship three AI capabilities: (a) integrate a well-documented large language model API for text summarization, (b) build an "agentic" workflow where an LLM plans and calls tools autonomously across multi-step tasks, and (c) respond when that agent misbehaves in production.
- **Current approach:** One delivery process for all three — scope it, estimate it, assign experts, ship on a roadmap date.
- **What worked / not:** The integration shipped cleanly. The agentic workflow blew past estimates and behaved differently every time it was tested. Nobody had a plan for the production incident.
- **Stakeholders:** Engineering, product, an ML/platform team, security/trust-and-safety, affected end users, executives allocating AI capex.

**Step 2 — Diagnose the domain.** Run each capability through the diagnostic questions (5 experts converge? standard best practice works? interventions predictable?).

- **(a) The known model integration — Complicated.** Cause-effect is knowable with expertise. Calling a documented API, handling rate limits and token budgets, adding retries and evals, caching, and streaming responses are all engineering problems with defensible right answers. Five competent engineers would broadly converge on the design. Best practice transfers. Interventions are predictable. This is not Clear (it takes genuine expertise, not an SOP), but it is knowable.
- **(b) Agentic reliability and emergent behavior — Complex.** Here cause-effect is only visible in retrospect. An autonomous agent that plans, uses tools, and chains model calls exhibits behavior that emerges from the interaction of the model, the prompt, the tools, and the live environment — small changes to a prompt or a model version can shift outcomes unpredictably, and the same input can produce different trajectories. Experts genuinely *disagree* on the right architecture because the terrain is new and shifting. Standard software estimation fails. This is the classic Complex signal — and treating it as Complicated (just scope it, assign an expert, commit a date) is the exact mistake Cynefin flags as most costly.
- **(c) A production incident — Chaotic.** When the deployed agent starts taking a harmful or runaway action against real users — leaking data, looping expensive tool calls, or emitting unsafe output at scale — cause-effect is in flux and every second of deliberation compounds harm. There is no time to analyze first.

**Step 3 — Match approach to domain.**

- **(a) Complicated → Sense–Analyze–Respond.** Put experienced engineers on it, evaluate a few defensible design alternatives (sync vs. streaming, which eval harness, prompt vs. fine-tune), pick one, and ship on a plan. Analysis is the right move; the only failure mode here is *analysis paralysis* — over-deliberating a solved-shape problem.
- **(b) Complex → Probe–Sense–Respond.** Do **not** commit to one grand agent design on a roadmap date. Instead run a portfolio of **safe-to-fail probes**: constrain the agent's tool permissions, run it in a sandbox or shadow mode against real traffic without acting, add human-in-the-loop checkpoints, cap spend and action counts, and measure against evals. Sense which probes hold, **amplify** what works, and kill what fails. The output is not a prediction; it is a set of experiments cheap enough to be wrong. Publicly available 2024–2026 agent-building guidance from major AI labs converged on exactly this posture — start narrow, add autonomy incrementally, keep humans in the loop, and constrain the action space — which is Probe–Sense–Respond by another name.
- **(c) Chaotic → Act–Sense–Respond.** Establish order first: trip the kill switch, revoke the agent's tool credentials, roll back to the previous model or disable the feature, and cut off the blast radius. Only once the bleeding stops do you re-classify — the post-incident investigation into *why* is then a Complicated (root-cause analysis) or Complex (emergent-behavior) problem, not a Chaotic one.

**Step 4 — Check boundary movement + choose intervention.**

- **Complicated → Complex under disruption.** The dangerous boundary is that a capability that *looks* Complicated can be Complex underneath. A model-version upgrade, a new tool added to the agent, or a shift in user behavior can move a "solved" integration back into emergent territory. The boundary watch: version-pinning and eval regressions as **shift signals**, the ML/platform team as the **monitoring owner**, and re-diagnosis on every model or tool change.
- **The Clear–Chaotic cliff.** A seductive error in this period is treating a maturing AI feature as *Clear* — "it worked in the demo, automate it and walk away." Complacent over-automation of an emergent system is precisely the fall off the Clear–Chaotic cliff: it looks routine right up until it produces a production incident. Keeping the feature classified as Complex (with probes, monitoring, and human oversight) rather than prematurely Clear is what prevents the cliff.
- **Mismatch cost, named.** Running the agentic workflow (Complex) through the integration's process (Complicated) is what produced the blown estimates and the unhandled incident — the plan was "right" for a domain the problem did not live in. The observable symptom was the recurring "the plan was fine, execution was the problem" post-mortem, which Cynefin identifies as the tell of a Complicated-domain plan failing on a Complex-domain problem.

**Output template, filled.**

```
Cynefin Diagnosis: Enterprise AI portfolio, 2024–2026
Domain: Complicated (known model integration) | Complex (agentic reliability) | Chaotic (production incident)
Evidence: (a) experts converge, best practice transfers, interventions predictable
          (b) experts disagree, behavior emergent/retrospective, estimation fails
          (c) cause-effect in flux, harm compounds with delay
Method: (a) S-A-R  (b) P-S-R  (c) A-S-R
Actions: (a) expert design + evals, ship on plan
         (b) sandbox/shadow, constrained permissions, human-in-loop, capped spend, amplify winning probes
         (c) kill switch, revoke credentials, roll back, contain, then re-diagnose
Mismatch cost: running (b) as (a) → blown timelines + unhandled incident (the "execution" post-mortem)
Boundary watch: model/tool version changes = shift signals | ML-platform team monitors | re-diagnose each release
```

**The lesson.** The AI decisions of 2024–2026 were not one problem to be managed with one methodology; they spanned three Cynefin domains that each demand a *different* decision method. Teams that treated agent-building as ordinary feature engineering paid the classic Complex-as-Complicated tax, while teams that ran constrained, safe-to-fail probes — and kept a kill switch ready for the Chaotic case — matched approach to domain. Domains are phases, not labels: as models and tools change, yesterday's Complicated integration can slide back into Complex, so the discipline is to keep asking "which domain is this decision in *now?*"

*Sources: Snowden, D. J., & Boone, M. E. (2007). "A Leader's Framework for Decision Making." Harvard Business Review, 85(11), 68–76 (Cynefin domains and the Complex-vs-Complicated error). Kurtz, C. F., & Snowden, D. J. (2003). "The new dynamics of strategy." IBM Systems Journal, 42(3), 462–483. Anthropic (2024–2025), "Building effective agents" and related public agent-engineering guidance (start simple, add autonomy incrementally, keep humans in the loop, constrain the action space). General characterizations of large-language-model and agent behavior — non-determinism, sensitivity to prompt/model changes, and emergent multi-step behavior — reflect widely documented, publicly reported properties as of early 2026.*
