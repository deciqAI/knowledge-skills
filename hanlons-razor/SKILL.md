---
name: hanlons-razor
description: "Activate when: someone feels a colleague/partner/company did something on purpose to hurt them; a team believes another side is acting in bad faith; someone is about to escalate based on assumed malicious intent; a pattern of bad outcomes is being labeled a coordinated attack. Do NOT activate when: concrete documented evidence of malice already exists; the cost of being wrong about non-malice is catastrophic (e.g., safety-critical or abusive-relationship context). More: deciqai.com/s/hanlons-razor"
---

# Hanlon's Razor

## Overview

Before assuming someone hurt you on purpose, construct the version where they made a mistake — and see how much evidence it explains. The razor is a Bayesian *prior*, not a proof; override it when concrete evidence of malice arrives. Human attribution systematically over-weights intent (fundamental attribution error); most hostile-seeming acts are incompetence, miscommunication, or asymmetric information.

Composes with [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md), [`abductive-reasoning`](../abductive-reasoning/SKILL.md), [`occams-razor`](../occams-razor/SKILL.md), [`critical-thinking`](../critical-thinking/SKILL.md).

## When to Use

- You feel an emotional pull toward "they did this on purpose"
- You're about to escalate on the assumption of malice
- A pattern of bad outcomes is being framed as a coordinated attack
- A team is in conflict and each side believes the other is acting in bad faith
- An AI model's harmful/biased output or a competitor's surprising AI move is being read as deliberate malice rather than an emergent bug, honest error, or ordinary self-interested competition

**Not when:** concrete evidence of malicious intent exists; cost of being wrong is catastrophic; power imbalance makes "they probably didn't mean it" an abuse-enabling stance.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before believing someone did it on purpose, construct the mistake version — see how much evidence it covers.
2. Check fit: concrete malice evidence / catastrophic cost of being wrong → not this lens.
3. Elicit the specific incident — what exactly happened?
> **[WAIT — do not advance until user responds]**
4. Work through The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close: name the clarifying-conversation move + the override signal to watch for.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Describe the action and harm** (factual, not interpretive)
```
- What was done: <specific, factual>
- Harm to me: <concrete>
- Gut attribution: <what your instinct is saying>
```
**Step 2 — Construct the non-malice explanation**
```
- Bad information they had: / Didn't realize: / Optimizing for: / Under pressure from:
- Coverage: <% of observed behavior this explains>
```
**Step 3 — Name what malice would additionally require**
```
- Info they'd need: / Motivation at your expense: / Harm predictable from their position?
```
**Step 4 — Choose starting posture** · **Step 5 — Set override signal** · **Step 6 — Hold prior until evidence changes it**
```
- Prior: <mistake / malice> · Starting posture: · First move: · Override trigger:
```

## Output Template
```
# Hanlon's Razor Analysis: <incident>
Mistake explanation + coverage % | Malice extra assumptions | Prior | Override signal | First action
```

*→ Method in Action: [Hanlon's Submission 1980; Heinlein's 1941 Articulation](examples/hanlons-submission-1980-heinleins-1941-articulation.md)*

*→ 2026 lens: [AI Incidents — Incompetence & Emergent Error as a Prior Over Malice (2024–2026)](examples/ai-incidents-malice-vs-emergent-error-2024-2026.md)*

## Pack: Common Patterns

| Situation | Default malice | Likely incompetence |
|---|---|---|
| Colleague sends harsh email | "They're undermining me" | Tired, didn't notice tone |
| Manager ignores your work | "They don't value me" | Overloaded, missed the update |
| Customer complains publicly | "Trying to extort us" | Real issue, tried other channels |
| Investor passes after diligence | "Were never serious" | Portfolio rebalancing |
| Co-founder makes unilateral decision | "Cutting me out" | Time pressure, assumed approval |

## Applying It Well

- Mistake-prior conversations produce information; malice-prior conversations produce defensiveness — even when malice later turns out true.
- The malice attribution feels viscerally correct in real-time; almost always overconfident in retrospect.
- Scales from individual to institutional: most "broken culture" is coordination failure, not coordinated malice.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Apply razor then ignore mounting evidence of malice | It's a prior, not a permanent ban on updating. |
| [D] Use razor to avoid hard conversations | It recommends a *clarifying* conversation, not silence. |
| [D] Apply razor across power asymmetries | Boss-harming-subordinate: power shifts the calculus. |
| [D] Invoke razor on yourself to dodge accountability | "Didn't mean to" doesn't undo the harm. |
| [D] Stop investigating once incompetence is identified | Incompetence-caused harm still requires response. |
| [D] Use razor to gaslight someone who was genuinely harmed | Attribution ≠ override of their lived experience. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Razor invoked by the actor, not the receiver
- "Incompetence" explanation conveniently absolves a powerful party
- Pattern of "incompetence" always harming the same direction
- Razor used to silence a victim's report or applied repeatedly without updating priors

## Verification

- [ ] Action and harm stated factually (not interpretively)
- [ ] Specific incompetence explanation constructed and coverage assessed
- [ ] Additional assumptions required for malice named
- [ ] Clarifying-conversation posture chosen (not accusation)
- [ ] Override signals specified; power asymmetry considered

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/hanlons-razor** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/hanlons-razor.json*
