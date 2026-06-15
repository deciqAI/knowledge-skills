---
name: first-principles
description: "Activate when: user says 'from first principles,' 'from scratch,' 'why do we even believe this,' 'tear this apart,' or 'the conventional answer seems wrong'; a decision is justified mainly by 'that's how it's done' or 'best practice says'; the conventional answer is expensive or hard to reverse and the user wants to pressure-test it. Do NOT activate when: the decision is routine and reversible (which linter, which date library) where convention is cheap and fine; the user has asked to just ship the conventional answer at speed."
---

# First Principles

## Overview

Most reasoning is reasoning by analogy: *X resembles Y, so do what Y does.* It is fast, usually right, and silently inherits every assumption baked into Y — including the wrong and expensive ones. First-principles reasoning strips a problem to statements that **cannot be reduced any further** — physical law, mathematical identity, a definition, or a cited empirical fact — and rebuilds the answer using only those.

This is one of three composable motions in the deciqAI collection: **first-principles** decomposes *downward* to bedrock; [occams-razor](../occams-razor/SKILL.md) chooses *sideways* among competing accounts you could build on top of bedrock; [second-order-thinking](../second-order-thinking/SKILL.md) traces *forward* through time and consequence. Compose: reduce to find the foundations (here), pick the simplest hypothesis that fits the evidence (occams), then trace where that pick actually leads (second-order).

## When to Use

**Use when:** decision is justified mainly by "that's how it's done" or authority; conventional answer is expensive/hard to reverse (pricing, architecture, business model); structuring a knowledge artifact from irreducible elements; user says "from first principles," "from scratch," "why do we believe this," "tear this apart."

**Skip when:** routine reversible decision where convention is cheap (which linter) — tearing down is theater; facts aren't gathered yet; user asked for speed and the conventional answer.

## Coaching Novices (Adaptive Front Door)

Before running the Teardown, read the user. This skill has two delivery modes — pick one, don't default to dumping a finished teardown.

- **Engine mode (do-it-for-me):** the user brought a concrete claim/decision and wants it analyzed → run the full First-Principles Teardown directly and concisely.
- **Coach mode (teach-me):** the user gave no concrete claim, or signals unfamiliarity → guide, don't analyze at them.

When unsure which they want, ask one line first: *"Want me to just tear down a specific claim, or walk you through the method step by step?"*

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output that step's question and nothing more.

In coach mode:

1. **One-line what-it-is.** Say what first-principles thinking buys them, in plain words (≤2 sentences, no jargon): most answers are inherited — *"that's how it's done."* This strips a claim down to what can't be reduced further and rebuilds using only that, so the assumptions you absorbed without noticing get caught.
2. **Check fit.** Match their situation against *When to Use* / *When NOT to use*. If it doesn't fit, say so and point elsewhere.
3. **Elicit their real claim.** If they have no concrete case, ask for one. Never run the teardown on a hypothetical when a real decision is available.

> **[WAIT — do not advance until user responds]**

4. **One step at a time.** Walk the Process one step per turn: surface assumptions *with* them, tag each together, interrogate the inherited ones one by one — wait for their input before advancing.

> **[WAIT — do not advance until user responds]**

5. **Close by naming the payoff.** End with the one inherited assumption *they* demolished — or the bedrock reason convention turned out to be right — so they remember the move, not just the answer.

> **[WAIT — do not advance until user responds]**

Then enter The Process below at the depth the chosen mode calls for.

## The Process

Run the **First-Principles Teardown** (7 steps → one artifact). Do not skip the tagging step — it is where analogy gets caught.

1. **State the claim** in one sentence.
2. **Surface every assumption** — be exhaustive and uncharitable.
3. **Tag each:** `BEDROCK` (irreducible or citable) vs `INHERITED` (convention/analogy/authority/untested).
4. **Interrogate every `INHERITED`:** necessarily true, or just usually/elsewhere/authority-said? → mark `DEMOLISHED` or promote to `BEDROCK`.
5. **Stop correctly:** reduce until irreducible/cited — no further. Reducing past bedrock is performance, not rigor.
6. **Reconstruct from bedrock only** — if the rebuild needs a demolished belief, the teardown isn't done.
7. **Diff against convention** — state what changed and why. "Nothing changed — convention was right" is a valid result.

**Output template:** `Claim / Assumptions (tagged) / Bedrock / Reconstruction / What changes / Confidence & open questions`

*→ Method in Action: [Wright Brothers and the Lift Tables (1901)](examples/wright-brothers-1901.md)*

## Bedrock Packs

"What counts as bedrock" is domain-specific. A **bedrock pack** captures, for one domain, (a) what legitimately counts as irreducible/citable bedrock and (b) the *fake-bedrocks* — inherited beliefs that domain habitually mistakes for foundations.

Packs are the contribution surface of this skill. Two ship with it:

- [`bedrock-packs/business-unit-economics.md`](bedrock-packs/business-unit-economics.md) — bedrock for evaluating a business or pitch
- [`bedrock-packs/knowledge-domain-decomposition.md`](bedrock-packs/knowledge-domain-decomposition.md) — bedrock for structuring a knowledge artifact before writing it

Adding or sharpening a pack is the easiest way to contribute — one self-contained file. See the contribution template at the repo root.

*→ Sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

The ways people fake first-principles thinking. If you catch yourself in the left column, you are reasoning by analogy in a lab coat.

**Note — [D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I reasoned from first principles" — but actually reasoned *X is like Y, so do what Y does* | That is analogy. Name the analogy explicitly and tear *it* down. Analogy in disguise is the single most common failure. |
| [D] Stopping at a convenient "axiom" ("customers want X," "the market expects Y") | A claim about the world is not bedrock unless it is irreducible or cited. "Customers want X" is an untested inherited belief until you have the data. Apply the regress test. |
| [D] Treating an expert / best-practice / competitor as bedrock | Authority is a *pointer* to evidence, not evidence. Cite the underlying fact, not the name attached to it. |
| [D] Confusing "hard to question" with "fundamental" | Cost, habit, and emotional weight make an assumption *sticky*, not *true*. Sunk cost is not a first principle. |
| [D] Reducing forever ("but what is value, really?") | The regress terminates (Post. An. I.3). Reducing past the indemonstrable or the citable is analysis paralysis dressed as depth. Stop at bedrock. |
| [D] Reconstructing with a smuggled assumption | If the rebuild quietly reuses a belief you marked DEMOLISHED, the teardown failed silently. Re-audit the reconstruction against surviving bedrock only. |
| [D] "The conventional answer is obviously wrong" before doing the teardown | First principles often *confirm* convention — convention encodes a lot of correct derivation. The output is the bedrock reason, not a contrarian reflex. |
| [D] Treating the **first level** of decomposition as bedrock | You broke "rocket cost" into "materials + labor + overhead" — but each decomposes further. The regress is rarely one hop; keep going until the next step would actually be performance. |
| [D] Mistaking a **citable number** for bedrock | A market price is bedrock for someone *trading*; for someone *building*, it decomposes into supply, demand, transport, regulation. Cite the number, then ask how it was generated and whether the generating conditions hold for you. |
| *To add [O] entries: paste a real failure instance here after each production use* | *Description of what happened* |

## Red Flags

- A `BEDROCK` item with no justification and no citation — it is an `INHERITED` belief wearing a badge
- No empirical claim in the whole teardown carries a number or source
- The reconstruction silently reuses a `DEMOLISHED` assumption
- "Obviously," "everyone knows," "industry standard," or a competitor's name used as a terminator
- More than ~7 surviving bedrock facts — you probably didn't reduce, or the scope is too big to tear down in one pass
- "What changes" is empty or hand-waved — you either skipped the diff or didn't actually reduce
- The teardown took thirty seconds — surfacing assumptions exhaustively is slow; speed here means you skipped step 2

## Verification

- [ ] The claim is stated in one sentence
- [ ] Every assumption was surfaced and tagged `BEDROCK` or `INHERITED` (none left untagged)
- [ ] Every `BEDROCK` item is irreducible or carries a source/number
- [ ] Every `INHERITED` item was interrogated, not just listed, and ended `DEMOLISHED` or promoted with evidence
- [ ] The regress terminated at the indemonstrable/citable — not arbitrarily, not infinitely
- [ ] The reconstruction uses only surviving bedrock — no smuggled beliefs
- [ ] "What changes" is explicit, even when the answer is "convention was right, here's why"

---

*Part of **deciqAI Knowledge Skills** — open-source thinking skills that make rigor executable for AI agents. These five skills are a free taste of the 130+ skills wired into every deciqAI agent, which runs them autonomously to operate your company. **Try it free → https://www.deciqai.com/skills?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=first-principles** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
