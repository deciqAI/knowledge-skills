---
name: ooda-loop
description: "Activate when: competitor outmaneuvers you despite worse resources; decisions take longer than the situation allows; team is losing a competition they should win; setting up crisis or incident response; someone says 'Boyd', 'decision cycle', 'get inside their loop', or 'tempo'. Do NOT activate when: situation is genuinely non-competitive and slow deliberation is right; speed was recently optimized at the expense of orientation quality."
---

# OODA Loop

## Overview

Colonel John Boyd (1927-1997) derived the OODA Loop from Korean War air-combat data: the F-86 Sabre achieved a ~10:1 kill ratio over the technically superior MiG-15 because better cockpit visibility and hydraulic controls let pilots cycle Observe → Orient → Decide → Act faster — the slower pilot was always reacting to obsolete information.

The strategic claim: **whichever side cycles faster wins** — but the bottleneck is almost always **Orient** (the synthesis step), not raw speed. A team that orients badly just produces wrong decisions faster.

Composes with [`metacognition`](../metacognition/SKILL.md) (Orient is where reasoning errors surface), [`feedback-loops`](../feedback-loops/SKILL.md) (OODA is a competitive feedback loop), [`first-principles`](../first-principles/SKILL.md) (orient from bedrock, not inherited belief), and [`momentum-and-form`](../momentum-and-form/SKILL.md) (cycle-time advantage builds momentum).

## When to Use

- Competitor outmaneuvers you despite your better resources, capital, or product
- Decisions take longer than the situation allows; losing a competition you should win
- Designing org structure where decision-speed is a competitive variable
- Crisis / incident response — OODA is the operational frame

**Not when:** genuinely non-competitive setting; your slowness is high-quality orientation worth keeping; speed was recently pushed at the expense of orient quality.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete competitive case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: the side cycling Observe-Orient-Decide-Act faster wins because the slower side reacts to obsolete info — but the bottleneck is usually *Orient*, not raw speed.
2. Check fit: non-competitive settings → not this lens.
3. Elicit the real situation: what competition or decision problem are you facing?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: map your loop, estimate the opponent's loop, find the bottleneck, test Orient quality.
> **[WAIT — do not advance until user responds]**
5. Close by naming the specific stage to accelerate and, if Orient, the exact mental-model fix they uncovered.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Map your loop.** For each stage (Observe / Orient / Decide / Act): what happens, who does it, how long does it take? Get actual time estimates.

**Step 2 — Estimate the opponent's loop.** Same analysis for the competitor. The *relative* cycle time is the strategic variable — if you take 2 weeks and they take 4 days, you are at a 3-4x disadvantage.

**Step 3 — Find the bottleneck.** Observe slow = data/instrumentation problem. Orient slow = synthesis/authority/framework problem (most common). Decide slow = political/sign-off problem. Act slow = capability problem. Speeding up non-bottleneck stages does nothing.

**Step 4 — Test Orient quality separately from Orient speed.** Ask: Do our frameworks fit this situation or are they inherited from past situations? Do we filter for confirmation? Are our mental models current? Broken Orient → faster cycling produces faster wrong decisions. Fix it first.

**Step 5 — Accelerate the bottleneck.** Observe: real-time data, lower-overhead channels. Orient: pre-built frameworks, red-team review, pre-committed decision criteria. Decide: clear decision rights, delegated authority. Act: capability redundancy, authority pushed to frontline.

**Step 6 — Get inside the opponent's loop.** Ship faster than they can respond → their moves target your last version, not current. In crisis, reach the next decision point before the public finishes processing the last.

## Output Template

```markdown
# OODA Loop Analysis: <situation>
- My loop: Observe <time> / Orient <time> / Decide <time> / Act <time> = <total>
- Opponent's loop (estimated): <total>
- Bottleneck: <stage + why>
- Orient quality: frameworks fit? mental models current? adversarial review?
- Acceleration plan: <stage to fix first + specific moves>
- Falsifier: <what outcome would tell me the diagnosis is wrong>
```

*→ Method in Action: [John Boyd and the F-86 vs MiG-15, Korean War 1950-1953](examples/john-boyd-f86-vs-mig15-korean-war-1950-1953.md)*

## Pack: OODA Patterns in Business

| Situation | Bottleneck | Acceleration move |
|---|---|---|
| Startup vs incumbent | Decide (sign-off politics) | Move while they deliberate |
| Cybersecurity incident | Observe (detecting attack) | Better SIEM / log retention |
| Product market response | Act (release cycle) | Shorter cadence, automated deploy |
| Crisis communications | Decide (sign-off chain) | Pre-approved templates, delegated authority |

## Applying It Well

- Map all four stages with actual time estimates before recommending acceleration.
- Measure decision *quality* after the fact — distinguish "fast + good" from "fast + wrong."
- Distinguish reversible from irreversible: reversible → bias toward action; irreversible → deliberation is worth it.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Speed is everything" | Cycle-time advantage requires orient quality. Speed without orient = faster wrong decisions. |
| [D] "We're deliberating, that's good" | Sometimes true. Sometimes the MiG pilot's rationalization. Test by measuring decision outcomes. |
| [D] Optimizing Observe and Act while ignoring Orient | The most common failure — better instrumentation doesn't help if synthesis is broken. |
| [D] "We're agile, we cycle fast" | True agility = fast orient + fast cycle. "Agile" with bad orientation = well-coordinated wrong moves. |
| [D] Treating OODA as a sequential checklist | It's a loop with continuous feedback. Observe and Orient never stop. |
| [D] Assuming the opponent has the same loop | Different opponents have different bottlenecks. Tailor acceleration to their specific weakness. |
| [D] "Boyd" cited without specific loop mapping | Rhetoric, not strategy. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Speed improvements without measuring decision quality
- Orient treated as overhead rather than the heavy step
- Competitor outmaneuvering you despite your better resources
- "Move fast and break things" applied to irreversible domains
- "We're agile" without specifying which loop stage actually accelerated

## Verification

- [ ] All 4 stages mapped with time estimates
- [ ] Opponent's loop estimated; relative advantage/disadvantage computed
- [ ] Bottleneck stage identified
- [ ] Orient quality assessed separately from orient speed
- [ ] Acceleration plan targets the actual bottleneck
- [ ] Reversibility of decisions considered

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/ooda-loop?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=ooda-loop** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
