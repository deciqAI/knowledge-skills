---
name: timing-action-matrix
description: "Activate when: a major decision is imminent and the team hasn't explicitly checked whether NOW is the right time; a correct strategy keeps hitting unexpected resistance; a post-mortem asks why something failed despite being the right call; planning a product launch or market entry. Do NOT activate when: timing is fixed by a hard deadline with no real choice about when to act; the decision is low-stakes and reversible."
---

# Timing-Action Matrix

## Overview

Most frameworks ask: "Is this the right action?" Timing is an *independent variable* of equal weight — a brilliant action at the wrong time fails because of timing, not the action. The 2×2:

```
                  Right Timing      Wrong Timing
Right Action  →   成功 Success       抵制 Resistance
Wrong Action  →   犯错 Mistake        灾难 Disaster
```

The 抵制 quadrant is the most dangerous: correct actions against wrong conditions exhaust energy, then teams wrongly conclude the action was bad. Timing is partly controllable — wait, engineer conditions, or redesign the action.

**Compose with:** [ooda-loop] (timing = Observe + Orient phases); [second-order-thinking] (surfaces WHY timing is wrong); [batna-zopa] (sequence offers around timing).

## When to Use

- Major decision imminent; team confident in action but timing not explicitly assessed
- A previously correct action met unexpected resistance — retrospective quadrant diagnosis
- Policy, product launch, or market entry planning — requires both action and timing design
- Post-mortem: action error, timing error, or both?

**When NOT to use:** Timing fixed by hard deadline; reversible low-stakes decisions; no genuine choice about when to act.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete case → run The Process directly. **Coach mode:** unfamiliar or no case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: "Four zones — success (right action, right time), resistance (right action, wrong time), mistake (wrong action, right time), disaster (wrong action, wrong time)."
2. Check fit: "Have you ever done everything right but gotten nowhere? That's resistance — correct action, wrong timing."
3. Elicit their real case: ask them to state the action in one sentence and list three conditions that must be true for it to succeed.
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input — assess action quality independently, then timing, then map the quadrant.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight: "Resistance tells you about timing — not necessarily about strategy. That distinction is operationally critical."
> **[WAIT — do not advance until user responds]**

## The Process

**Gate:** Steps 1 and 2 must be completed independently — do not let timing uncertainty contaminate action assessment, or action confidence inflate timing assessment.

**Step 1 — State the action.** One specific sentence with scope and timeline.
**Step 2 — Assess action quality independently.** If conditions were perfectly favorable, would this action succeed? → Right / Wrong / Uncertain. If Uncertain, resolve before proceeding.
**Step 3 — Assess timing independently.** Name specific environmental conditions required for success. Check each Present / Absent / Partial. Stop-rule: if timing reduces to "it feels right," return here.
**Step 4 — Map to the 2×2.** Combine both assessments into one quadrant: 成功 / 抵制 / 犯错 / 灾难.
**Step 5 — Respond by quadrant.** 成功: commit fully. 抵制: do NOT conclude action is wrong — set a timing trigger ("act when [condition] is met"). 犯错: redesign urgently before window closes. 灾难: stop.

### Output Template

```
Decision: ___  Date: ___
Action (one sentence): ___
Action Quality: [ ] Right  [ ] Wrong  [ ] Uncertain
Timing conditions: (1)___ [Y/N/P]  (2)___ [Y/N/P]  (3)___ [Y/N/P]
Quadrant: [ ] 成功  [ ] 抵制 trigger:___  [ ] 犯错 redesign:___  [ ] 灾难
Next Action: ___  Owner: ___  By: ___
```

*→ Method in Action: [D-Day Timing Decision (June 1944)](examples/d-day-timing-decision-june-1944.md)*

## Timing Packs

**Regulatory/Policy:** check what regulatory conditions must be present (timing) vs. product design (action quality separately).
**Market Entry:** customer awareness of problem, competitive context, distribution infrastructure, purchasing authority — all checkable.
**Negotiation/Partnership:** make the offer when the counterparty has felt the pain. Combine with [batna-zopa].

*→ Primary sources: [references/sources.md](references/sources.md)*

## Applying It Well

1. Run assessments in sequence, not simultaneously — simultaneous collapses to gut feel.
2. 抵制 is most recoverable — assets intact, strategy sound; wait or change conditions.
3. Timing conditions must be checkable against reality. If a condition can't be verified, it's a hope.
4. 犯错 is urgent — timing window is open but action is wrong. Fix before the window closes.
5. Timing can be engineered: "act when 3 enterprise LOIs are signed" is a designed trigger, not a passive wait.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Rationalization | Why It Fails |
|-----------------|--------------|
| [D] "We've been waiting — it's time to act." | Duration is not a timing condition. Check whether specific conditions are present. |
| [D] "The timing is never perfect — just go." | Collapses 抵制 and 成功 into one, hiding the cost of wrong-timing execution. |
| [D] "Our competitors are doing it, so timing must be right." | Competitors may be in 犯错. Their timing choice doesn't validate yours. |
| [D] "We already committed resources, so we have to go." | Sunk cost. Prior commitment doesn't change the quadrant; proceeding in 灾难 compounds loss. |
| [D] "Our analysis says action is right — therefore timing is right." | Conflates two independent assessments. One correct does not imply the other correct. |
| [D] "We can't afford to wait — first-mover advantage." | Moving first in 抵制 produces first-mover disadvantage: you educate the market; others capture returns. |
| [D] "If not now, when?" | Urgency masquerading as a timing assessment. Answer: "When condition X is met." |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Timing discussion is "it feels like the right time" with no named checkable conditions
- Last two similar actions in this domain met unexpected resistance — possible systematic timing blindness
- Post-mortem blames "execution" without distinguishing 抵制 (right action, wrong time) from 犯错 (wrong action)
- Decision meeting spends 90% on "what to do," 5% on "when" — timing systematically under-analyzed

## Verification

- [ ] Action in one specific sentence with scope and timeline
- [ ] Action quality assessed independently, as if timing were perfect
- [ ] Timing assessed against ≥3 named conditions, each checked present/absent/partial
- [ ] Both assessments combined into one explicit quadrant
- [ ] 抵制: timing trigger named; 犯错: redesign timeline set before window closes
- [ ] Stop-rule verified: timing does not reduce to "it feels right"

---
*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/timing-action-matrix** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
