---
name: abductive-reasoning
description: "Activate when: user says 'what's the most likely explanation,' 'why did this happen,' 'we think it's X but not sure,' 'we only have one theory,' 'the team has converged on an answer without checking alternatives,' or when diagnosing a bug/outage/symptom/anomaly under uncertainty.
  Do NOT activate when: the problem is purely deductive or mathematical (direct proof, not hypothesis); the situation allows direct observation or measurement that bypasses inference. More: deciqai.com/s/abductive-reasoning"
---

# Abductive Reasoning

## Overview

Abduction — *inference to the best explanation* — is the only mode of reasoning that introduces new ideas. Deduction works out consequences; induction generalizes instances; **abduction generates the hypotheses themselves** (Peirce, 1903).

Formal schema: *The surprising fact C is observed. But if A were true, C would be a matter of course. Hence, there is reason to suspect A is true.*

The "best" qualifier carries the weight: consistent-with-evidence is not enough — the hypothesis must beat rivals on coverage, simplicity, prior probability, and predictive power (Harman 1965; Lipton 2004).

Composes with [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md) (Bayes scores hypotheses abduction generates), [`occams-razor`](../occams-razor/SKILL.md) (simplicity criterion), [`critical-thinking`](../critical-thinking/SKILL.md) (competing-hypotheses analysis), and `debugging-and-error-recovery` (technical debugging is iterated abduction).

## When to Use

- A surprising observation needs explanation (bug, symptom, outage, customer behavior, financial anomaly)
- A diagnostic decision must be made under uncertainty (medical, technical, investigative)
- Someone is treating "consistent with X" as proof of X
- A team has converged on one explanation without enumerating alternatives
- An investigation has stalled at the first plausible-sounding hypothesis

**Not when:** the problem is deductive (math, formal logic); evidence is sufficient for direct measurement; you have no domain knowledge to generate candidate hypotheses.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: instead of "this looks like X, so it's X," abduction enumerates every hypothesis that would explain the observation and picks the one that best accounts for all the evidence — coverage, simplicity, prior plausibility, predictive power.
2. Check fit: deductive / direct-observation problems → not this lens.
3. Elicit the surprising observation — what happened that didn't match expectations?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input — generate alternatives, score each on the four criteria.
> **[WAIT — do not advance until user responds]**
5. Close: name the chosen hypothesis, the closest rival, and the test that would distinguish them.
> **[WAIT — do not advance until user responds]**

## The Process

**S1 — State the surprising observation:** what was expected vs what happened.
**S2 — Generate candidates:** H1…H5 + H_unknown (the explanation not yet considered). Force ≥3. Techniques: domain expertise, inversion, failure modes, adversarial generation, base rates.
**S3 — Score each** on four criteria: Coverage (explains all evidence?), Simplicity (fewest auxiliary assumptions?), Prior (base-rate plausibility?), Predictive power (new testable predictions?).
**S4 — Select the best:** highest combined score, not just "most consistent." State why it beats the runner-up.
**S5 — Name the discriminating test:** what evidence would confirm it, what would refute it, what would distinguish it from the runner-up.
**S6 — Commit provisionally:** treat as current best hypothesis. Specify an update trigger; if the test fails, return to S2.

## Output: Abductive Inference
```
# Abductive Inference: <surprising observation>
Observation: <what> / Why surprising: <expected vs actual>
Candidates: H1 | H2 | H3 | H_unknown
| H | Coverage | Simplicity | Prior | Predictive power |
|---|---|---|---|---|
Best explanation: <chosen> — why over runner-up: <…>
Discriminating test: predicts <…> / refuted by <…> / distinguishes from runner-up by <…>
Action: provisional decision <…> / update trigger <…>
```

*→ Method in Action: [Peirce, the Wine Cellar, and the Watch — 1879](examples/peirce-the-wine-cellar-and-the-watch-1879.md) · [The Discovery of Neptune — 1846](examples/the-discovery-of-neptune-from-uranus-anomalies-1846.md)*

## Pack: Abduction in Practice

| Domain | Surprising observation | Common abductive failure |
|---|---|---|
| Medical diagnosis | Unusual symptom cluster | Settling on first matching diagnosis; ignoring prior |
| Software debugging | Test fails unexpectedly | Blaming the change; ignoring environment/build causes |
| Business performance | Revenue drop in a segment | Blaming sales without checking market/product/measurement |

## Applying It Well

- Generate broadly before committing narrowly — most failures are failures to enumerate
- "Consistent with X" is the weakest criterion; always compare across all four criteria
- State the conclusion as provisional; name the update trigger — *→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The first explanation that fits is correct" | The first explanation rarely is. Abduction requires enumeration. |
| [D] "This is consistent with X, so X" | Consistency is necessary, not sufficient. Compare against rivals. |
| [D] "I can't think of another explanation" | Generation step is incomplete. Use inversion, base rates, adversarial generation. |
| [D] Picking a hypothesis because it's vivid or interesting | Storytelling fallacy. Vividness is not evidence. Apply the four criteria. |
| [D] Treating abductive conclusion as proven | Abduction is provisional. Always state the discriminating test. |
| [D] Skipping the H_unknown placeholder | Commits to the best hypothesis you happened to think of — absence of imagination ≠ absence of possibility. |
| [D] Selecting based on coverage alone | Coverage is one of four criteria. High-coverage + wildly improbable prior = still wrong. |
| [D] "Abduction is the same as guessing" | Abduction is structured: enumerate, score, select. Guessing skips the scoring. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Only one hypothesis was considered
- Selected hypothesis was the first that "matched"
- No comparison across multiple criteria
- No discriminating test stated
- No H_unknown placeholder
- Confidence framed as proof rather than best-current-explanation
- Explanation requires auxiliary coincidences without acknowledging them

## Verification

- [ ] At least 3-5 candidate hypotheses generated, plus H_unknown
- [ ] Each scored on coverage, simplicity, prior, predictive power
- [ ] Selected hypothesis compared to runner-up explicitly
- [ ] Discriminating test identified
- [ ] Conclusion stated as provisional, not proven
- [ ] Update trigger specified

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/abductive-reasoning** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/abductive-reasoning.json*
