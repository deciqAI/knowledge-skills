---
name: hindsight-bias
description: "Activate when: someone says 'I knew it all along' or 'we should have seen it coming'; a post-mortem is blaming someone for not predicting an outcome; a team is reviewing a past decision and the outcome is coloring the judgment; a decision-maker is being evaluated on what happened rather than what was knowable at the time.
  Do NOT activate when: contemporaneous pre-decision records exist and match current memory (bias is bounded); the goal is explicitly pattern-recognition from outcomes rather than evaluating the original decision-maker."
---

# Hindsight Bias

## Overview

**Hindsight bias** — the "I knew it all along" effect — is the tendency, *after* learning an outcome, to misremember your prior judgment as having been closer to that outcome than it actually was. Fischhoff (1975) demonstrated three distinct components: **memory distortion** ("I said it would happen"), **inevitability** ("it had to happen"), and **foreseeability** ("anyone should have seen it"). Each requires a different countermeasure; the structural fix for all three is pre-commitment documentation.

Composes with [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md), [`premortem`](../premortem/SKILL.md), [`confirmation-bias`](../confirmation-bias/SKILL.md), and [`survivorship-bias`](../survivorship-bias/SKILL.md).

## When to Use

- A post-mortem is becoming an exercise in blame for an "obviously foreseeable" outcome
- Someone says "I knew this would happen" without contemporaneous records
- A decision is being evaluated against its outcome rather than the information available when made
- An investor, judge, or jury evaluates a past decision with knowledge of how it turned out
- Someone calls a market move "obvious in retrospect" — e.g. the AI boom, AI capex buildout, or frontier-AI valuations were "clearly inevitable" / "anyone should have seen the AI adoption wave coming"

**Not when:** pre-commitment documentation exists and matches current memory; the goal is pattern-recognition from outcomes; the failure to predict was a genuine process failure with clear pre-outcome signals.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific post-outcome narrative → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before judging a past decision by its outcome, ask what was actually knowable in advance — check the contemporaneous record, not your current memory.
2. Check fit against When to Use / When NOT to use. If records exist and match memory, bias is bounded.
3. Elicit the specific outcome and the claim of foreseeability. What outcome happened? Who is being credited/blamed?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: reconstruct the pre-outcome information set, decompose the three components, evaluate decision process vs. outcome.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight uncovered and the structural fix (decision journal, pre-mortem, blind post-mortem).
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State the outcome and the claim:** outcome that occurred / who is being credited-blamed / claim of foreseeability (verbatim) / time elapsed.

**Step 2 — Reconstruct the pre-outcome information set:** what was knowable / what was genuinely uncertain / what contemporaneous records exist / consensus view at the time. *Nixon test: if informed contemporaries gave the outcome ≤30%, "anyone should have seen it" is hindsight bias.*

**Step 3 — Decompose the three components:** memory distortion (current memory vs. records) / inevitability (is outcome framed as the only possible result?) / foreseeability ("anyone should have seen it" applied to genuinely uncertain ex-ante info?). Countermeasures: memory → pull records; inevitability → list 3-5 alternative outcomes; foreseeability → identify what pre-outcome info would have made it predictable.

**Step 4 — Evaluate the decision process, not the outcome:** was the decision reasonable given available info / expected value across plausible outcomes / would you make the same decision again with the same info. *Bridgewater matrix: good decision + bad outcome = bad luck (don't change). Bad decision + good outcome = good luck (don't celebrate).*

**Step 5 — Install pre-commitment documentation:** decision journal (who/what/when/why/probability) / pre-mortem record / public prediction logged to internal forum / pre-registered evaluation criteria.

**Step 6 — Run a blind post-mortem:** read decision journal before outcome data / evaluate against recorded reasoning / introduce outcome data only then / distinguish process error from outcome variance.

## Output Template

```markdown
# Hindsight Bias Analysis: <outcome>
Outcome / Foreseeability claim (verbatim) / Who is credited-blamed:
Pre-outcome info set (knowable / uncertain / records / consensus / ex-ante probability):
Three-component diagnosis (memory distortion Y/N / inevitability Y/N / foreseeability overclaim Y/N):
Decision-process evaluation (process quality 1-5 / reasonable Y/N / EV / same decision again Y/N):
Structural fix (decision journal owner / pre-mortem owner / blind post-mortem protocol Y/N):
```

*→ Method in Action: [Baruch Fischhoff's Nixon-China Trip Study, 1972-1975](examples/baruch-fischhoffs-nixon-china-trip-study-1972-1975.md) · [Anesthesia Malpractice Outcome-Bias Study, 1991](examples/caplan-posner-cheney-anesthesia-outcome-study-1991.md)*
*→ 2026 lens: ["The AI Boom Was Obviously Coming" — retrospective inevitability in the ChatGPT/Nvidia era (2022–2026)](examples/ai-boom-obviously-coming-hindsight-2022-2026.md)*

## Pack: Hindsight Bias Patterns

| Domain | Common hindsight manifestation | Structural countermeasure |
|---|---|---|
| Investment | "Obvious in retrospect" trade | Decision journal with logged thesis and probability |
| Engineering | "How did anyone miss that bug?" | Blameless post-mortem; reconstruct info state at time |
| Hiring | "I knew this person wouldn't work out" | Logged interview rubric and pre-hire confidence rating |
| Legal | "The defendant should have foreseen the harm" | Ex ante risk assessment; "reasonable person at the time" |

## Applying It Well

- Pull contemporaneous records before forming any judgment about what was "knowable"
- Evaluate decision quality and outcome quality on separate axes — never conflate them
- The structural fix is records, not vigilance — warnings reduce but do not eliminate the bias

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I remember exactly what I said at the time" | Confident-memory subjects were *just as biased*. Memory without records is unreliable. |
| [D] "But it was so obvious in retrospect" | Hindsight makes everything look obvious. Test: did informed contemporaries give it >50% probability before the outcome? |
| [D] "Anyone with sense would have predicted this" | Check the contemporaneous record — pre-event surveys, market prices, expert forecasts. |
| [D] "The outcome was inevitable given the structure" | List 3-5 plausible alternative outcomes the same structure could have produced. |
| [D] "Process doesn't matter; outcome is what matters" | Outcome alone confounds skill and luck. Evaluate them separately. |
| [D] "We learned the lesson — that's all that matters" | If the "lesson" is hindsight-biased, the next decision will be miscalibrated. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Post-mortem conducted with no pre-mortem record to compare against
- "Obvious in retrospect," "anyone should have seen it," "we knew this" without contemporaneous documentation
- "Lesson learned" focuses on the specific failure mode, not on the broader uncertainty space
- Decision-maker blamed/credited based primarily on outcome rather than process
- Emotional or financial stakes are high — the bias is *larger* in high-stakes cases

## Verification

- [ ] Contemporaneous records pulled (emails, memos, forecasts, market prices, decision journals)
- [ ] Three components diagnosed separately (memory / inevitability / foreseeability)
- [ ] At least 3 plausible alternative outcomes enumerated for the same starting structure
- [ ] Decision quality evaluated separately from outcome quality
- [ ] Ex-ante probability estimated using pre-outcome information only
- [ ] Pre-commitment documentation installed for future similar decisions
- [ ] Post-mortem protocol blind to outcome data until after process review

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/hindsight-bias** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
