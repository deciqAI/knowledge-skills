---
name: fundamental-attribution-error
description: "Activate when: someone says 'they're just like that,' an employee is being blamed for underperformance without examining their situation, a post-mortem is focusing on who screwed up, customer churn is being written off as 'not the right fit,' or someone asks 'why did they do that?' with a character-based answer. Do NOT activate when: the behavior forms a documented pattern across many genuinely different situations (dispositional inference is warranted); situational analysis is being used as a shield to excuse behavior that warrants accountability."
---

# Fundamental Attribution Error

## Overview

The **fundamental attribution error (FAE)** is the systematic tendency to over-weight character factors and under-weight situational factors when explaining others' behavior — while reversing this for your own behavior (actor-observer asymmetry). Coined by Lee Ross (1977), grounded in Jones & Harris's 1967 Castro study. The bias is automatic (System 1); situational correction requires deliberate effort (System 2).

Composes with [`hanlons-razor`](../hanlons-razor/SKILL.md), [`survivorship-bias`](../survivorship-bias/SKILL.md), [`critical-thinking`](../critical-thinking/SKILL.md), [`dual-system-thinking`](../dual-system-thinking/SKILL.md), [`narrative-fallacy`](../narrative-fallacy/SKILL.md).

## When to Use

- Diagnosing why an employee is underperforming
- Analyzing customer churn
- Conducting post-mortems on outages, accidents, or failures
- Mediating interpersonal conflict
- Designing products and observing user behavior
- Performance reviews, evaluations, competitor behavior analysis
- Someone says "fundamental attribution error," "actor-observer," or "what situation made this rational"

**Not when:** behavior shows a documented pattern across many distinct situations; situational framing is being used to avoid accountability.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific judgment to test for FAE → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before concluding someone behaved a certain way because of who they are, ask what situation would make the behavior rational — that's the FAE counter-move.
2. Check fit: if the same person behaves the same way across many *distinct* situations, dispositional inference is stronger. Single-situation explanations are FAE-prone.
3. Elicit the specific judgment. Who's the person? What's the behavior? What explanation is being offered?
> **[WAIT — do not advance until user responds]**
4. One question at a time: is the explanation dispositional? What's the situational alternative? If I were in that situation, would I have behaved differently?
> **[WAIT — do not advance until user responds]**
5. Close: balanced analysis with both dispositional and situational factors + which is doing the explanatory work.
> **[WAIT — do not advance until user responds]**

## The Process

**1. State the judgment** — person, behavior, current explanation, decision dependent on it.

**2. Categorize** — dispositional (character/ability) vs. situational (context/constraints/incentives). If purely dispositional, FAE is likely.

**3. Generate situational alternative** — what situation would make this behavior rational? What would I do there? What does a situated expert think?

**4. Actor-observer test** — if I did this, what would I attribute it to? If situational for me, why dispositional for them? Name the asymmetry.

**5. Synthesize** — estimate dispositional vs. situational % contribution; identify what intervention each implies; compare cost and probability of success.

**6. Decide with calibrated attribution** — document the mix, set a re-evaluation point (e.g., 90 days after situational changes); if behavior persists, dispositional inference gains credibility.

## Output: FAE Audit

```
FAE Audit: <person/behavior>
Judgment: Person / Behavior / Current explanation / Decision
Explanation: Dispositional: / Situational:
Situational alternative: What situation would make this rational / What I would do / Expert view
Actor-observer test: If I did this I'd attribute to: / Asymmetry revealed:
Balanced: Dispositional (%) / Situational (%) / Intervention implications
Decision: Decision / Justification / Re-evaluation point
```

*→ Method in Action: [Jones-Harris 1967 Castro Study + Ross 1977 Synthesis + Modern Applications](examples/jones-harris-1967-castro-study-ross-1977-synthesis-modern-applications.md)*

## Pack: FAE Application Patterns

| Domain | Common FAE attribution | Situational alternative |
|---|---|---|
| Employee underperformance | "Lacks drive / skill" | Resource constraints, unclear expectations, role-fit |
| Customer churn | "Wasn't really a good fit" | Onboarding gaps, support failures, product-fit issues we caused |
| Outage / mistake | "X person made a bad call" | System design encouraged the error; time pressure |
| User abandoning product | "They didn't understand it" | UX is confusing; constraints we don't see |

## Applying It Well

FAE is automatic (System 1); correction is effortful (System 2). Build situational analysis into processes structurally — rubrics, blameless post-mortems, structured customer interviews. Use actor-observer asymmetry as a real-time diagnostic. Balanced attribution (both factors) produces better interventions than pure dispositional or pure situational reasoning.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I know them; this is who they are" | The most-knowing observers still commit FAE. Knowledge doesn't immunize. |
| [D] "I've seen them do this many times" | Often "many times" is the same situation recurring — not cross-situational evidence. |
| [D] "I just have good intuition for people" | Intuition for people is heavily FAE-laden. Trust calibrated track record, not intuition. |
| [D] "Situational factors are excuses" | Sometimes. Often they're the actual causes. The question is which is which. |
| [D] "If situation were the issue, others would behave the same" | Often they do — you're already explaining them situationally and this person dispositionally (asymmetry). |
| [D] "We need to hold people accountable" | Yes — but for what they can control. Accountability for situational factors is unfair and ineffective. |
| [D] "I was in that situation and I behaved differently" | Were you actually in the same situation? Salience differences often differ between actors. |
| [D] "The pattern is too clear to be situational" | Then specify the pattern across multiple *distinct* situations. Often it's one situation observed many times. |
| [D] "Asking 'what situation made this rational' lets bad behavior off the hook" | No. It helps diagnose accurately so the response is calibrated. |
| [D] "I'm not biased; I'm just being honest" | The bias-blind-spot is real (Pronin et al. 2002). Self-perception of unbias correlates poorly with measured bias. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Explanation is dispositional with no situational analysis
- "They are X" rather than "they did X because Y"
- Same behavior explained dispositionally for others, situationally for self
- Firing/coaching decision made without examining situational factors
- Post-mortem is blame-driven; churn attributed to customer character without examining product/onboarding

## Verification

- [ ] Dispositional explanation explicitly stated; situational alternative generated
- [ ] Actor-observer asymmetry checked
- [ ] Balanced explanation (both factors) considered; interventions weighed
- [ ] If dispositional: pattern verified across multiple *distinct* situations
- [ ] Re-evaluation point scheduled

---
*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/fundamental-attribution-error?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=fundamental-attribution-error** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
