---
name: cynefin
description: "Activate when: 'our best practices keep failing', 'experts disagree on the right answer', 'the old playbook isn't working', 'we're in crisis and don't know what to do first', 'best practice doesn't apply here', 'we need a different approach'. Do NOT activate when: situation is unambiguously routine (execution only); a specialized tool (OODA, expected value) already fits."
---

# Cynefin

## Overview

**Cynefin** (pronounced "kuh-NEV-in"; Welsh for "habitat") is a sense-making framework by Dave Snowden (IBM, 1999). Its claim: the right decision approach depends on which of five domains the situation falls into — **Clear** (obvious cause-effect, use SOP), **Complicated** (knowable with expertise, use analysis), **Complex** (emergent, probe first), **Chaotic** (absent cause-effect, act first), **Confused** (unknown domain, decompose first). The most common and costly error: treating Complex problems as Complicated.

Composes with [`ooda-loop`](../ooda-loop/SKILL.md), [`feedback-loops`](../feedback-loops/SKILL.md), [`antifragile`](../antifragile/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

- A familiar approach has stopped working and you can't articulate why
- Experts disagree on the right answer — a crisis unfolding where the previous playbook doesn't apply
- "Best practices from X" imported without checking if the domain matches
- A team is over-planning something emergent, or "let's get more data" when data won't come without action

**Not when:** domain is unambiguously Clear (execution only); small-stakes one-shot; specialized framework already fits.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** concrete case → run The Process. **Coach mode:** unfamiliar → guide step by step.
In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. Classify the situation (Clear/Complicated/Complex/Chaotic) and match decision method to domain.
2. Check fit: if unambiguously routine (Clear), skip framework.
3. Elicit their real case — decision, current method, cause-effect structure.
> **[WAIT — do not advance until user responds]**
4. Are cause-effect relationships obvious, knowable, emergent, or absent? Is current method matched?
> **[WAIT — do not advance until user responds]**
5. Close: named domain + matched decision method + boundary watch.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Describe:** `Decision/situation: | Current approach: | What worked/not: | Stakeholders:`

### Step 2: Diagnose the domain
```
Obvious to everyone? (Clear) | Knowable with expertise? (Complicated)
Only retrospective? (Complex) | Absent/in flux? (Chaotic) | Unknown? (Confused)
```
Diagnostics: 5 experts converge? (Yes → Complicated; No → Complex). Standard best practice works? (Yes → Clear/Complicated; No → Complex/Chaotic). Interventions predictable? (Yes → Clear/Complicated; No → Complex/Chaotic).

### Step 3: Match approach to domain
```
Clear: Sense→Categorize→Respond (SOP/automate) | Complicated: Sense→Analyze→Respond (experts)
Complex: Probe→Sense→Respond (safe-to-fail experiments, amplify wins)
Chaotic: Act→Sense→Respond (establish order, then re-classify) | Confused: decompose, classify each part
```

### Step 4: Check boundary movement + choose intervention
```
Domain shifted? (Complicated→Complex from disruption? Clear-Chaotic cliff approaching?)
Clear: deploy SOP; monitor. Complicated: experts; pick defensible alternative.
Complex: parallel safe-to-fail probes; amplify wins. Chaotic: decisive action; re-diagnose.
Boundary watch: shift signals | who monitors | re-diagnosis schedule
```

**Output template:**
```
Cynefin Diagnosis: <situation>
Domain: [Clear/Complicated/Complex/Chaotic/Confused] | Evidence: [cause-effect, expert agreement]
Method: [S-C-R / S-A-R / P-S-R / A-S-R] | Actions: | Mismatch cost (if any):
Boundary watch: [shift signals | monitoring owner | re-diagnosis schedule]
```

*→ Method in Action: [Snowden at IBM (1999) and the HBR Synthesis (2007)](examples/snowden-at-ibm-1999-and-the-hbr-synthesis-2007.md) · [Apollo 13 Mission Response (1970)](examples/apollo-13-1970-mission-response.md)*

## Pack: Cynefin Domain Patterns

| Domain | Examples | Method | Mistake |
|---|---|---|---|
| Clear | Routine compliance; manufacturing QC | S→Categorize→R; SOP | Over-analysis |
| Complicated | Engineering design; surgery; M&A | S→Analyze→R; experts | Analysis paralysis |
| Complex | Startup PMF; org culture; new market entry | Probe→S→R; safe-to-fail | Over-planning |
| Chaotic | Crisis first 24h; security breach | Act→S→R; decisive action | Deliberating |
| Confused | New market; leadership transition | Decompose; classify each | Defaulting to home domain |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We just need a better plan" | Often the issue is Complex — no plan works; probes and adaptation required. |
| [D] "Get me an expert" | Right for Complicated. Wrong for Complex: experts disagree because cause-effect is emergent. |
| [D] "Do what worked last time" | Right for Clear. Dangerous near Clear-Chaotic boundary — produces the cliff fall. |
| [D] "We need more data" | Often a deflection in Complex/Chaotic where data only emerges from probes/action. |
| [D] "The plan is right; execution is the problem" | Classic post-mortem rationalization when Complicated-domain plan failed on Complex-domain problem. |
| [D] "Best practices from industry X" | Only transfers if industry X has the same domain structure. Complex ≠ Complicated. |
| [D] "We need more analysis / more decisiveness" | Analysis: right for Complicated, wrong for Complex/Chaotic. Decisiveness: right for Chaotic, wrong for Complex. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Repeated failure always blamed on "execution" — "Best practices" imported without domain check
- Experts disagree on the right answer (Complex signal) — Crisis response dominated by analysis
- Complex situation managed with a single plan, not a probe portfolio
- Team waiting for clarity in a domain where clarity only comes from acting

## Verification

- [ ] Domain explicitly named with diagnostic evidence
- [ ] Decision method matched to domain (S-C-R / S-A-R / P-S-R / A-S-R)
- [ ] If current approach mismatches: mismatch cost named
- [ ] Boundary signals identified; re-diagnosis schedule set
- [ ] If Complex: ≥3 safe-to-fail probes designed
- [ ] If Chaotic: order-establishing action specified

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/cynefin** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
