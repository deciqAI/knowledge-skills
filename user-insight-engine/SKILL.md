---
name: user-insight-engine
description: "Activate when: user says 'why aren't users doing X despite saying they would', or 'our survey scores are high but churn is high', or 'we shipped a feature that tested well but nobody uses it', or 'we have conflicting signals from research', or 'I can see the drop-off point but don't know why'.
  Do NOT activate when: the product has no real users yet (use lean-startup / jobs-to-be-done instead); or the purchase is a multi-stakeholder B2B enterprise deal (use principal-agent / signaling-games instead)."
---

# User Insight Engine

## Overview

User research produces data. The Engine produces *insight* — the causal link between an observable behavior and the deep-layer driver that causes it. Three layers: **Surface** (what users say), **Behavioral** (what users do), **Deep** (why — cognitive and social drivers). Four Deep Layer drivers: **Loss Aversion**, **Social Proof**, **Cognitive Load**, **Trust Cost**.

Cross-skill: use **after `jobs-to-be-done`** to map interview output onto drivers; **before `feedback-loops`** to avoid optimizing for the wrong behavior; **alongside `confirmation-bias`** as a meta-check; **alongside `loss-aversion-prospect-theory`** when Loss Aversion is primary.

## When to Use

**Trigger:** Surveys show satisfaction but behavioral data shows churn; a change that tested well failed in production; "why aren't users doing X?" where X is available and users expressed willingness; identical segments behaving differently; consistent drop-off that UX friction can't explain; low onboarding completion despite users rating it "easy"; feature adoption plateaued despite awareness.

**When NOT to use:** Zero behavioral data (don't attempt Deep Layer analysis); pre-launch no users (use `lean-startup` + `jobs-to-be-done`); B2B enterprise >12-month cycles (use `principal-agent` + `signaling-games`).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete behavior gap + behavioral data → run The Process directly.
- **Coach mode:** new to synthesis or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: The Engine finds the *why* behind a behavior gap by layering what users say, what they do, and what actually drives them — then names the one lever to pull.
2. Check fit: confirm they have behavioral data and a specific user action to understand. If pre-launch or enterprise buying committee, redirect.
3. Ask: "What specific user action are you trying to understand? State it as an observed behavior, not an outcome."
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time using their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the driver uncovered and the one intervention to test.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Behavior Gap:** "[User segment] is [doing/not doing] [specific action] at [workflow point], despite [Surface Layer evidence they intend to / are capable of doing it]."

**Step 2 — Three-Layer Synthesis:** Collect Surface (surveys, interviews, tickets), Behavioral (clickstream, funnels, session recordings, cohort retention), Deep (ethnographic observation, JTBD interviews, diary studies, driver-isolating A/B). **Stop-rule:** no Deep Layer evidence = analysis incomplete; do not proceed to interventions.

**Step 3 — Map to Driver:** High trial-to-abandonment → Trust Cost / Cognitive Load. Low feature adoption despite awareness → Cognitive Load / Social Proof. Sudden drop-off after initial engagement → Social Proof / Trust Cost. Feature used in unintended order → Cognitive Load.

**Step 4 — Intervention:** Loss Aversion → reframe as prevention. Social Proof → surface specific peer group norm. Cognitive Load → reduce simultaneous decisions. Trust Cost → make first action reversible. Prioritize by: driver magnitude, testability, implementation cost.

### Output: Insight Engine Report Card

```
USER INSIGHT ENGINE — REPORT CARD
Product / Feature: ___  Date: ___  Owner: ___
BEHAVIOR GAP: [segment] is [doing/not doing] [action] at [point], despite [Surface evidence].
SURFACE LAYER: ___  BEHAVIORAL LAYER: ___
Surface-Behavioral conflict: [ Yes / No ]  If yes: ___
DEEP LAYER: Method: [ Ethnographic / JTBD / Diary / A/B ]  Finding: ___
STOP-RULE: [ ] At least one Deep Layer piece collected — if unchecked, stop.
PRIMARY DRIVER: [ Loss Aversion / Social Proof / Cognitive Load / Trust Cost ]
Evidence: ___  Secondary driver: ___
INTERVENTION: Driver: ___  Change: ___  Test design: ___  Metric (behavioral): ___
```

*→ Method in Action: [Taylor's Behavioral Observation at Bethlehem Steel (1898–1901)](examples/taylors-behavioral-observation-at-bethlehem-steel-1898-1901.md)*

## Domain Packs

- **Consumer Mobile:** Daily opens, never reach core action → Cognitive Load / Trust Cost. Session recordings + diary study. Fix: progressive onboarding; explicit reversibility.
- **Enterprise SaaS:** Adoption <20% despite awareness → Social Proof / Trust Cost. Internal champion mapping. Fix: role-specific peer adoption data; sandbox/undo mode.
- **Healthcare / FinTech:** Drop-off at identity or financial commitment → Trust Cost. JTBD "switch" interviews. Fix: social proof from completers; staged commitment.

## Applying It Well

- Surface–Behavioral conflict is your most reliable signal — train your research process to find it, not average it away.
- Treat each driver as a hypothesis: Deep Layer evidence confirms or disconfirms. No evidence = structured guess.
- Segment before synthesizing — the same Surface-Layer segment can have different Deep Layer drivers across contexts.
- Loss Aversion frames require validation against Deep Layer evidence before deploying in copy.
- Social Proof specificity matters: peer-group-specific stats outperform generic "other users" claims.
- Cognitive Load accumulates: map the entire decision sequence, not just the final action.
- Trust Cost is highest at first action — front-load risk reduction.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|-----------|---------|
| [D] "80% said the feature is useful." | Stated utility is Surface Layer. 80% say useful + 20% use it = the conflict is the finding. |
| [D] "We watched 10 sessions — they completed without difficulty." | Lab sessions are Surface Layer in disguise. Real-environment observation is Deep Layer. |
| [D] "A/B test showed 5% lift in clicks." | Click lift is Behavioral Layer on one metric — doesn't confirm driver identification. |
| [D] "Users said onboarding is confusing — redesign it." | Cognitive Load, Trust Cost, and Social Proof all produce confusion; they require different fixes. |
| [D] "100,000 users — aggregate data is reliable." | Scale makes Behavioral statistically reliable; it says nothing about Deep Layer causes. |
| [D] "Power users love the feature." | Power users have resolved Trust Cost and formed habits — they're past the barriers you're trying to understand. |
| [D] "We've been doing user research for years." | Institutional knowledge accumulates Surface patterns; Deep Layer drivers shift as the user base scales. |
| [D] "Drop-off is at Step 3 — simplify Step 3." | Trust Cost established at Step 1 may only manifest as abandonment at Step 3. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Behavioral and survey data presented together without checking for Surface–Behavioral conflicts
- "User research" = interviews only; no behavioral layer
- No Deep Layer evidence ever collected for this behavior
- Interventions designed before a driver has been identified
- Segments defined by demographics or plan tier, not behavioral pattern
- Churn interviews take "why did you leave?" answers at face value

## Verification

- [ ] Behavior gap stated as specific observable action at specific workflow point
- [ ] Surface–Behavioral conflict explicitly checked; documented if present
- [ ] At least one Deep Layer evidence piece collected — if not, stop-rule triggers
- [ ] Each behavioral anomaly traced to at least one driver, with evidence
- [ ] Intervention targets the identified driver specifically (not general UX improvement)
- [ ] Intervention is a testable experiment that isolates the driver
- [ ] Success metric is behavioral, not attitudinal
- [ ] Segments checked for driver heterogeneity before pooling

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/user-insight-engine?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=user-insight-engine** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
