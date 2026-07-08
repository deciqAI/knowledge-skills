---
name: narrative-fallacy
description: "Activate when: user is reading a business case study or founder biography and drawing lessons; a post-mortem produced a neat single root cause; someone says 'the story is too clean' or 'that explanation is too convenient'; a pundit explains a market or political event confidently after it happened; user is building a strategy based on what worked at another company.
  Do NOT activate when: the causal structure is genuinely well-understood (physics, well-tested medical interventions) and the narrative reflects that; the user needs a narrative for communication purposes and already knows it is a compression."
---

# Narrative Fallacy

## Overview

The **narrative fallacy** is the tendency to construct retrospective causal stories that make past events seem inevitable — even when those events were largely random or contingent. Named by Nassim Taleb (*The Black Swan*, 2007, ch. 6); grounded in Kahneman's "illusion of understanding" (*Thinking, Fast and Slow*, 2011, ch. 19). Three structural drivers: causal hunger (brains auto-infer causation from sequence), retrospective selection (only survivors are visible), coherence comfort (tidy stories feel true).

Composes with [`hindsight-bias`](../hindsight-bias/SKILL.md), [`survivorship-bias`](../survivorship-bias/SKILL.md), [`black-swan`](../black-swan/SKILL.md), [`first-principles`](../first-principles/SKILL.md), and [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md).

## When to Use

- You're reading a business case study or founder biography and drawing lessons
- A post-mortem produces a satisfyingly neat single root cause
- A pundit explains a market or political event with one dominant narrative — after it happened
- You're constructing a strategy based on what worked at another company
- Someone says "the story is too neat," "after-the-fact rationalization," or "post-hoc explanation"

**Not when:** causal structure is genuinely well-understood (physics, tested medicine); the narrative is a hypothesis to test; storytelling is the medium and you already treat it as a compression.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific compelling narrative → run The Process directly.
- **Coach mode:** user is new or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: when a story explains the past with neat causal clarity, suspect the narrative fallacy — minds construct causal sequences automatically, even from random events.
2. Check fit: physical sciences have genuine causal understanding; most business / political / historical narratives don't.
3. Elicit: what's the story? What causes does it identify? What outcome does it explain?
> **[WAIT — do not advance until user responds]**
4. Probe: what does the narrative strip out (non-survivors, contingencies, unknowns at the time)? Would the narrative survive if the outcome had been different?
> **[WAIT — do not advance until user responds]**
5. Close: reframe the narrative as a compressed retrospective + name the operational implication if lessons were about to be drawn.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify the narrative:** story / outcome explained / causes identified / implied lesson.
**Step 2 — Test selection bias:** how many comparable attempts didn't produce this outcome? Would the same narrative-construction method explain their failure equally well? If yes, the narratives are post-hoc, not causal.
**Step 3 — Reconstruct pre-event uncertainty:** what did contemporaneous documents actually say? What were the plausible alternative outcomes? How much of the "obvious cause" was visible in advance?
**Step 4 — Test counterfactuals:** if the identified cause had been absent, would the outcome still have occurred? What chance events could plausibly have changed it?
**Step 5 — Probabilistic re-expression:** replace "X happened because Y" with "X happened; Y likely contributed; here's the evidence; here's what we don't know; here's my confidence."
**Step 6 — Document lessons cautiously:** what is the actual transferable insight (vs. narrative-coloration)? What's the evidence base across cases beyond the focal one?

## Output: Narrative-Fallacy Audit

```markdown
# Narrative-Fallacy Audit: <narrative>
Narrative: story / outcome / identified causes / implied lesson
Selection bias: comparable non-survivors and their narratives
Pre-event uncertainty: contemporaneous predictions / alternative outcomes
Counterfactual test: if cause Y absent → outcome? If cause Z instead → outcome?
Probabilistic reformulation: "X happened; Y likely contributed; [evidence]; [what we don't know]"
Operational lesson (revised): transferable insight / evidence base / confidence
```

*→ Method in Action: [Taleb's 9/11 Example + Business-History Critique](examples/talebs-911-example-business-history-critique.md)*

## Pack: Application Patterns

| Domain | What the narrative strips out | Operational risk |
|---|---|---|
| Founder biography | 1000s with same vision who failed; specific luck moments | Imitating X's behaviors expecting Y outcome |
| Business case study | Comparable companies with same strategy that failed | Adopting strategy as recipe |
| Investment thesis | Sector noise; counterexamples; trend exhaustion | Concentrated position on narrative |
| Engineering post-mortem | Multiple contributing factors; latent vulnerabilities | "We fixed root cause; we're safe" |
| Market crash / macro event | Multiple factors; mass psychology | Single-cause policy prescription |

## Applying It Well

Recognize when you are receiving a narrative. Identify what it strips out. Demand counterfactual reasoning. Express your own narratives probabilistically. Use stories for communication; preserve uncertainty for decision-making.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The pattern is clear; we have to learn from it" | The pattern is clear *in this narrative*. Most "clear patterns" don't survive modest base-rate testing across cases. |
| [D] "If we don't learn from history, we'll repeat it" | Many "history lessons" are narrative-fallacy products that misfire in different conditions. |
| [D] "I've personally experienced this; it's not just a story" | Personal experience is one data point. The fallacy operates on personal histories equally. |
| [D] "The expert wrote a whole book on it" | Many widely-cited business books show enormous regression to mean of their case studies post-publication. |
| [D] "We need a story to communicate" | Use the story for communication; preserve analytical caveats for decision-making. |
| [D] "Counterfactual reasoning is academic" | It is precisely the disciplined version of "acting on what happened" — it separates causal from contingent. |
| [D] "I have a strong gut on this" | The gut produces narratives automatically. Strong-gut causal feelings are System 1 output, not insight. |
| [D] "Without the narrative, we don't know what to do" | Base rates, first-principles reasoning, and structured analysis can guide decisions without a clean causal story. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- A complex outcome explained by a single dominant cause
- Narrative does not engage with comparable cases that produced different outcomes
- The past sounds obvious / inevitable in retrospect
- A clean recipe-like lesson is the output
- Narrator had motivated framing (founder, profiting investor, commentator needing an explanation)

## Verification

- [ ] Narrative identified as a narrative, not as fact
- [ ] Selection bias checked (what happened to comparable non-survivors?)
- [ ] Pre-event uncertainty reconstructed
- [ ] Counterfactual reasoning applied
- [ ] Narrative re-expressed in probabilistic / uncertain terms
- [ ] Operational lessons documented with calibrated confidence
- [ ] At least one alternative interpretation considered

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/narrative-fallacy?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=narrative-fallacy** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
