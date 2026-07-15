---
name: nudge-theory
description: "Activate when: user says 'nudge,' 'default,' 'opt-in vs opt-out,' 'choice architecture,' or 'why do people know they should but don't?'; user has a behavior gap between intent and action; user is designing product onboarding, policy enrollment, or public health interventions and wants to change behavior without mandates or incentives.
  Do NOT activate when: the gap is informational (people genuinely don't know what to do — education precedes nudging); the designer's goal is to serve their own interests rather than the chooser's (that is a dark pattern, not a nudge)."
---

# Nudge Theory

## Overview

People procrastinate on retirement savings, skip vaccine appointments, and leave privacy settings on dangerous defaults — not from ignorance, but because the choice environment works against them. Nudge theory (Thaler & Sunstein) treats *choice architecture* — defaults, framing, social norms, friction — as the decisive variable. A nudge alters behavior in a predictable way without forbidding options or changing economic incentives; it must be easy and cheap to avoid. The foundational result: switching 401(k) enrollment from opt-in to opt-out raised participation from ~49% to ~86% — a 37-point lift from changing only the default.

Composition: use [status-quo-bias](../status-quo-bias/SKILL.md) before nudge design to know where inertia points; use [probabilistic-thinking](../probabilistic-thinking/SKILL.md) to estimate effect size; use [second-order-thinking](../second-order-thinking/SKILL.md) to catch downstream consequences (e.g., a low default rate that anchors people).

## When to Use

Apply when: (1) intent-action gap exists; (2) mandates or financial incentives are infeasible or unacceptable; (3) the choice environment can be redesigned; (4) you are setting defaults, opt-in/opt-out flows, or model-selection and data-sharing settings in an AI-native product where choice architecture steers millions of users amid rapid AI adoption and AI-native competition.

**When NOT to use:** gap is informational (educate first); deep values at stake; expert deliberate decision-makers (System 2); no defensible claim one outcome is better for the chooser.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete behavior gap → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: a nudge is any small change to the environment — a default, a framing tweak, a social comparison — that steers people toward a better choice without forcing or paying them.
2. Check fit against When to Use / When NOT to use. If the gap is informational, redirect to communication design.
3. Elicit their real behavior gap. "We want users to engage more" is not a case; "63% never complete their first savings transfer despite signing up" is.
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time — diagnose each EAST barrier before prescribing a mechanism.
> **[WAIT — do not advance until user responds]**
5. Close by naming the one nudge change most likely to close the gap, and the metric that would prove it worked.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **EAST Nudge Design**. Behavior first, barrier second, mechanism third, test fourth.

**Stop-rule:** If you cannot name a specific, observable, measurable target behavior, stop. "Improve engagement" is not a target behavior.

1. **Define the target behavior precisely.** Exact action, population, and baseline rate.
2. **Diagnose the barrier (EAST).** E — Easy (friction/complexity/defaults); A — Attractive (salience/framing/loss aversion); S — Social (missing norm info); T — Timely (wrong trigger moment).
3. **Match barrier to mechanism.** Easy → default redesign, friction removal; Attractive → loss framing, salience; Social → descriptive norm message; Timely → implementation-intention prompt or event trigger.
4. **Design the nudge.** Specify exact wording, default state, timing, visual. Check: (a) free choice preserved? (b) transparent — would disclosing it collapse the effect? (c) serves the chooser, not the designer?
5. **Design the test.** Randomized control: define primary metric, minimum detectable effect, sample size, resolution date.
6. **Plan for scale and decay.** Define monitoring cadence and re-evaluation trigger.

### Output: EAST Nudge Design

```
Target Behavior: <exact action | population | baseline rate | measurement>
Barrier Diagnosis: E:<Y/N> A:<Y/N> S:<Y/N> T:<Y/N> → Primary barrier: <>
Nudge Mechanism: <chosen> — Rationale: <why it addresses primary barrier>
Intervention: <exact change in wording/default/timing/visual> | all options preserved | Transparency: <Y/N> | Serves chooser: <Y/N>
Test: Control vs Treatment | Metric: <> | MDE: <> | n: <> | Resolution: <>
Scale/Decay: Monitoring cadence: <> | Re-evaluation trigger: <>
```

*→ Method in Action: [401(k) Automatic Enrollment and the Pension Protection Act (2006)](examples/401k-automatic-enrollment-and-the-pension-protection-act-2006.md)*
*→ 2026 lens: [Choice Architecture in AI Products (2023–2026)](examples/choice-architecture-in-ai-products-2023-2026.md)*

## EAST Packs

- **Retirement/financial:** Easy + Timely barriers dominate; default redesign + implementation-intention at onboarding.
- **Public health:** social norm messages + implementation-intention prompts; risk = messaging a norm that isn't locally true (backfires).
- **Product/UX:** Easy barrier primary; ethical risk highest — defaults serving revenue over user = dark pattern.
- **Organizational HR:** Timely underdeveloped; leverage onboarding and promotion moments.

## Applying It Well

- Diagnose barrier before choosing mechanism — mechanism-first is the most common error.
- The default is the most powerful lever; audit every default and ask whose interests it serves.
- Nudge effects decay — build monitoring in from day one.
- Ethical test: a legitimate nudge still works when disclosed, because it helps people do what they already want.
- Validate social norm content against the actual target population before messaging it.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We changed the messaging and nothing moved." | Messaging is the weakest lever. Without changing the default or friction, a new headline rarely shifts behavior. |
| [D] "Our users are rational — defaults don't affect them." | Madrian & Shea documented a 37-point enrollment gap among professional employees. |
| [D] "We nudge toward what's best for them, so ethics are fine." | The test is not the designer's belief — it is whether the outcome is genuinely better and the choice freely reversible. |
| [D] "A 5% lift is small — nudges are overhyped." | 5% of 10M users = 500K behaviors. Evaluate effect size against cost and population size. |
| [D] "We added a social norm but nothing changed." | Social norm nudges require the stated norm to be locally true. Verify before messaging. |
| [D] "We ran the test two weeks and got null." | Nudge effects need sufficient dwell time or seasonal context. Mistimed tests produce false nulls. |
| [D] "Our default is neutral." | No default is neutral — every default favors some outcome. Ask whose interests it serves. |
| [D] "We A/B tested one message and called it a nudge experiment." | That is a copy test. A nudge experiment tests a structural intervention with adequate statistical power. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "Nudge" removes or obscures an option — that is a mandate or dark pattern
- No specific, observable target behavior named
- Ethical check skipped — no one asks whose interests the nudge serves
- Test has no control condition or pre-registered primary metric
- Social norm is aspirational, not verified against the actual population
- Default redesigned but exit path made deliberately difficult — that is manipulation
- Effect size evaluated without base population or implementation cost

## Verification

- [ ] Target behavior specific, observable, with baseline rate
- [ ] EAST barrier diagnosed before mechanism chosen
- [ ] Mechanism directly addresses the primary barrier
- [ ] All options remain available and reachable
- [ ] Transparency test passed (disclosing wouldn't collapse the effect)
- [ ] Serves-the-chooser test passed
- [ ] Randomized test with pre-registered metric and adequate sample size
- [ ] Post-launch monitoring and decay-detection trigger defined

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/nudge-theory** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
