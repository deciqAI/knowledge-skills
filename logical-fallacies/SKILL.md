---
name: logical-fallacies
description: "Activate when: someone says 'this argument feels off but I can't explain why', 'is this a real argument or just rhetoric?', 'what's wrong with this reasoning?', an argument relies entirely on authority/emotion/popularity, or you're about to decide based on a single analogy. Do NOT activate when: the conclusion is already verifiable empirically (just check the data); casual conversation where rigor is socially expensive and stakes are low."
---

# Logical Fallacies

## Overview

A fallacy is an argument that looks like it works but doesn't. The test is not whether the conclusion is true — it's whether the *inference* from premises to conclusion is valid. This skill covers two layers: the **classical taxonomy** (Aristotle's 13, c. 350 BCE — verbal and structural errors) and the **modern cognitive map** (Tversky-Kahneman 1983 — errors competent reasoners commit automatically before any sophist arrives).

Composes with neighbors: [`critical-thinking`](../critical-thinking/SKILL.md) audits evidence quality and framing; [`first-principles`](../first-principles/SKILL.md) attacks premises; [`mece`](../mece/SKILL.md) catches decomposition errors that masquerade as false-dichotomy or composition fallacies.

## When to Use

- An argument feels persuasive but you cannot articulate why
- A claim is supported entirely by authority, popularity, emotion, or anecdote
- You're about to decide based on a single argument or analogy
- A debate is moving fast ("everyone knows Y") — speed is the sophist's friend
- You catch yourself reasoning emotionally ("this has to be true because…")
- You're weighing an AI hype or AI-adoption claim ("a lab CEO said it's near," "it passed the benchmark so it's intelligent," "doom vs. utopia")

**When NOT to use:** casual small talk with low stakes; conclusion is empirically verifiable (just check the data); you're tempted to name a fallacy to dismiss an opponent rather than find truth (that is itself the fallacy fallacy).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete argument → run The Process directly.
- **Coach mode:** user signals unfamiliarity or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: some arguments *sound* right but don't earn their conclusion — this is a checklist for finding that gap, including in your own thinking.
2. Check fit against When to Use / When NOT to use. If data can answer it, say so.
3. Elicit their real argument — ask for a concrete case (something someone said, an article they're suspicious of). > **[WAIT — do not advance until user responds]**
4. Walk through the Audit one pass per turn: pose the question, wait for their answer, surface what they missed. > **[WAIT — do not advance until user responds]**
5. Close by naming the one fallacy *they* found and what changes about the conclusion now that they've seen it. > **[WAIT — do not advance until user responds]**

## The Process

Run the **Fallacy Audit** in four passes — structure, language, cognition, rhetoric — then judge.

1. **State the argument cleanly.** Rewrite as premises → conclusion. If you cannot, first finding: it's an assertion dressed as an argument.
2. **Structural pass.** Begging the question, affirming the consequent, denying the antecedent, false cause (*post hoc*), hasty generalization, accident, complex question, ignoratio elenchi.
3. **Linguistic pass.** Equivocation (key term shifts meaning), amphiboly, composition/division (part↔whole), accent/figure of speech.
4. **Cognitive pass.** Conjunction fallacy (P(A∧B) > P(A) from representativeness), base-rate neglect, availability, anchoring — see [`anchoring`](../anchoring/SKILL.md).
5. **Rhetorical-trap pass.** Ad hominem, appeal to authority (exception: expert in own domain), appeal to popularity (weak prior only), appeal to emotion (evidence vs. substitute), false dichotomy, straw man, slippery slope, tu quoque.
6. **Judge the argument, not the moves.** A fallacy means the inference fails — not that the conclusion is false.
7. **Fallacy-fallacy check.** If you can't articulate *why this instance fails*, you have a dismissal, not a finding.
8. **Output:** for each fallacy — (a) which and where, (b) what the inference fails to establish, (c) what would actually support the conclusion.

### Output: the Fallacy Audit

```
Argument: Premise 1 / Premise 2 / Conclusion
Structural findings: <fallacy, which inference, why it fails>
Linguistic findings: <fallacy, which term, what shifts>
Cognitive findings: <fallacy, why intuition misfires>
Rhetorical-trap findings: <fallacy, what move replaced an argument>
Fallacy-fallacy check: <any dismissals dressed as findings?>
Verdict: argument <fails/partly/holds> | conclusion <still open — what evidence would settle it>
Repair: <what inference or evidence would actually support the claim>
```

*→ Method in Action: [Tversky & Kahneman's Linda Problem (1983)](examples/tversky-kahnemans-linda-problem-1983.md)*
*→ 2026 lens: [Four Fallacies in the AI Debate (2024–2026)](examples/ai-hype-discourse-fallacies-2024-2026.md)*

## Pack: Common Fallacy Patterns by Domain

- **Startup/business:** survivorship bias (hasty generalization on filtered data), appeal to authority ("Sequoia said X"), anecdote as evidence, false dichotomy ("raise now or die")
- **Policy/public debate:** undocumented slippery slope, straw man, ad hominem, appeal to consequences
- **Internal arguments (most expensive):** conjunction fallacy, confirmation bias, sunk cost, optimism bias — see [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) and [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md)
- **Statistical/data:** base-rate neglect, Texas sharpshooter (target drawn after the fact), cherry-picking, regression to mean confused with causation

## Applying It Well

Run the filter on your *own* arguments first. The ones that survive are worth more than the ones you flag in opponents. Fallacy-detection at speed is suspicious — it usually means surface pattern-matching, not an actual audit. Slow is good.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I named the fallacy, so I refuted the argument" | A fallacious argument doesn't make the conclusion false — it fails to *establish* it. Refuting an argument ≠ refuting a claim. |
| [D] "Citing an expert is appeal to authority" | Expert testimony in the expert's actual domain is legitimate evidence. The fallacy is treating a citation as *proof* or citing outside their domain. |
| [D] "Any analogy is a false analogy" | Reasoning by analogy is often valid. The fallacy is asserting similarity on the relevant dimensions without showing it. |
| [D] Spotting fallacies only in arguments you disagree with | If the filter has a personal valence, it is broken. Run it on your own most-loved arguments. |
| [D] "No formal fallacy → the argument is sound" | Formal fallacies are a small fraction. Most modern errors are informal. Run all four passes. |
| [D] "Knowing the conjunction fallacy means I won't commit it" | Tversky-Kahneman 1983 showed otherwise. Only the explicit check prevents the error. |
| [D] "I caught the fallacy quickly, so I'm good at this" | Speed signals surface pattern-matching, not an actual audit. Slow is good. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Fallacy label with no articulation of which inference step fails and why
- Audit found fallacies only in arguments the auditor already disagreed with
- Only the structural pass ran; linguistic, cognitive, or rhetorical skipped
- No distinction between "the argument fails" and "the conclusion is false"
- Output is a list of labels with no "what would actually support this claim" section

## Verification

- [ ] Argument rewritten as premises → conclusion (or flagged as not an argument)
- [ ] All four passes run: structural, linguistic, cognitive, rhetorical
- [ ] Each fallacy specifies exact location and exact failure
- [ ] Fallacy-fallacy check performed — no findings are dismissals dressed as fallacies
- [ ] Verdict separates "argument fails" from "conclusion is false"
- [ ] Output names what evidence would actually support the claim
- [ ] At least one cognitive fallacy (modern empirical category) considered
- [ ] Filter applied to arguments the auditor agrees with, not only opponents'

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/logical-fallacies** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
