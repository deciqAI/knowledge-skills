# Method in Action: Four Fallacies in the 2024–2026 AI Debate

> *Example for the [logical-fallacies](../SKILL.md) skill.*

The Linda problem shows the fallacy filter under laboratory conditions. This example runs the same **Fallacy Audit** on messy public discourse — the argument about artificial intelligence as it circulated across roughly 2024–2025. This is the environment the skill was built for: claims that *sound* authoritative, move fast, and carry high stakes, where naming the fallacy is only useful if you can also say what would actually settle the question.

We audit four representative arguments, each a real pattern that recurred across essays, interviews, and social threads in this period. No individual quote is reconstructed verbatim below; each argument is stated as a clean paraphrase of a widely-circulated *pattern* of reasoning, then run through the process.

---

## Step 1 — State each argument cleanly (premises → conclusion)

**Argument A (authority).**
- P1: The CEO of a leading AI lab says transformative AI is a few years away.
- P2: They run the lab and see the frontier models first.
- C: Therefore transformative AI is a few years away.

**Argument B (false dilemma).**
- P1: AI leads either to catastrophe ("doom") or to radical abundance ("utopia").
- P2: The doom scenario is implausible / the utopia scenario is implausible (whichever the speaker rejects).
- C: Therefore the other outcome is what we should expect.

**Argument C (hasty generalization).**
- P1: A single demo went viral showing a model doing task X impressively.
- C: Therefore models can now do X (and tasks like X) reliably.

**Argument D (affirming the consequent).**
- P1: If a system is intelligent, it will pass benchmark B.
- P2: This system passed benchmark B.
- C: Therefore this system is intelligent.

All four are genuine arguments (premises and a conclusion), so none collapses at Step 1 into "an assertion dressed as an argument." Good — that means the work is in the passes.

## Step 2 — Structural pass

**Argument D is a textbook formal fallacy: affirming the consequent.** The form is "If P then Q; Q; therefore P." That is invalid: Q can be true for reasons unrelated to P. Passing benchmark B is consistent with intelligence *and* with narrow pattern-matching, benchmark contamination (test items leaking into training data), or overfitting to the benchmark's format. The inference fails because P1 only licenses the reverse direction (intelligent → passes B), not (passes B → intelligent). Benchmark saturation across this period — models scoring very high on tests that older models failed — is exactly the observation that makes the invalid direction tempting.

**Argument C is hasty generalization.** One vivid, curated, possibly cherry-picked instance is generalized to reliable capability across a class of tasks. A viral demo is a maximally-filtered sample: the impressive run is the one that got posted. The inference from "did X once, on camera" to "does X reliably" ignores variance, failure rate, and selection.

## Step 3 — Linguistic pass

**Argument D also hides an equivocation** on the word "intelligent." P1 uses "intelligent" in a rich sense (general, flexible, understanding). The conclusion inherits that rich sense — but all the evidence established was a benchmark score, which at most supports "intelligent" in a thin, task-specific sense. The key term shifts meaning between premise and conclusion. This is why benchmark-driven "it's intelligent now" claims feel stronger than they are: the word does double duty.

**Argument B smuggles a definitional move** on "AI" and on "doom/utopia" — the terms are left vague enough that any outcome can be sorted into one bucket, which is what makes the dilemma feel exhaustive.

## Step 4 — Cognitive pass

**Argument C is powered by the availability heuristic** (Tversky & Kahneman, 1974): a dramatic, emotionally salient demo is easy to recall and therefore feels representative of typical performance. The vivid case crowds out the invisible base rate of failures that were never posted.

**Argument A leans on base-rate neglect.** Even if lab leaders are somewhat better calibrated than outsiders, the base rate of confident near-term timeline predictions in the history of AI that did *not* come true is high. A forecast should update on that base rate, not just on the forecaster's seat.

## Step 5 — Rhetorical-trap pass

**Argument A is appeal to authority (*ad verecundiam*).** Note the disciplined version of this finding: a lab CEO *is* a domain expert, and their testimony is legitimate *evidence* about, say, what a model can do today. The fallacy is not "they're an executive so ignore them." The fallacy is (a) treating a prediction as *proof*, and (b) the conflict-of-interest overhang — the same person is raising capital, recruiting, and setting expectations, so their timeline is also a business artifact. Expertise about present capability does not transfer into authority over a multi-year forecast.

**Argument B is a false dilemma (false dichotomy).** "Doom or utopia" presents two extremes as the only options, when the outcome space plainly includes a wide middle: uneven diffusion, sector-by-sector disruption, muddling through, partial gains with real harms. Once one horn is knocked down, the argument rushes to the other — but the disjunction was never exhaustive, so knocking down one horn establishes nothing about the other.

## Step 6 — Judge the argument, not the moves

Each argument *fails to establish its conclusion*. That is the verdict — and it is **not** the claim that the conclusions are false:

- Transformative AI genuinely *might* be near (A) — the CEO's prediction just doesn't prove it.
- One of doom/utopia *could* occur (B) — the dilemma just doesn't force it.
- Models genuinely *may* do X reliably (C) — one demo just doesn't show it.
- The system *may* be intelligent in some sense (D) — the benchmark just doesn't entail it.

## Step 7 — Fallacy-fallacy check

The temptation here is strong and worth naming: it is easy to shout "appeal to authority!" and treat the CEO as rebutted, or "affirming the consequent!" and treat the model as *proven* unintelligent. Both would be the fallacy fallacy — using a flaw in the argument to assert the negation of the conclusion. Every finding above specifies *which inference step* fails and *why*, not merely a label. That is the line between an audit and a dismissal.

## Step 8 — Output: the Fallacy Audit

```
Argument A: CEO predicts near-term transformative AI / they see the frontier / therefore it's near
  Structural: —
  Linguistic: —
  Cognitive: base-rate neglect (history of failed AI timelines)
  Rhetorical: appeal to authority — expert on present capability ≠ authority on multi-year forecast; conflict of interest
  Verdict: fails to establish | still open — needs track record of calibrated forecasts, not a single seat
  Repair: aggregate multiple independent forecasters; score them against past calibration; treat timelines as probability distributions

Argument B: AI → doom or utopia / one is implausible / therefore the other
  Structural: —
  Linguistic: vague terms make the dilemma feel exhaustive
  Cognitive: —
  Rhetorical: false dichotomy — ignores the large middle of outcomes
  Verdict: fails to establish | still open — enumerate the full outcome space, assign probabilities to each
  Repair: replace binary with a distribution over scenarios; argue each on its own evidence

Argument C: one viral demo of task X / therefore reliable at X
  Structural: hasty generalization from a filtered sample of one
  Linguistic: —
  Cognitive: availability heuristic — vivid demo feels typical
  Rhetorical: —
  Verdict: fails to establish | still open — needs pass rate over many unfiltered trials
  Repair: measure success rate on a held-out, contamination-checked test set; report variance and failure modes

Argument D: if intelligent then passes B / passed B / therefore intelligent
  Structural: affirming the consequent (invalid form)
  Linguistic: equivocation on "intelligent" (rich sense vs. thin task sense)
  Cognitive: —
  Rhetorical: —
  Verdict: fails to establish | still open — define "intelligent" operationally, test generalization beyond B, rule out benchmark contamination
  Repair: use held-out tasks the model wasn't optimized for; check for train/test leakage; specify which capability the benchmark actually measures

Fallacy-fallacy check: no conclusion is asserted false — each is left open pending real evidence.
```

---

Why this is the right modern companion to the Linda problem: Tversky-Kahneman showed the fallacies live inside individual cognition even under lab control. The AI debate shows the same fallacies scaled up to a public argument moving at social-media speed, wrapped in real expertise and real stakes — precisely the conditions ("speed is the sophist's friend," "supported entirely by authority") the skill's *When to Use* section flags. The audit does not tell you whether transformative AI is near. It tells you that none of these four popular arguments has earned that conclusion yet — and exactly what evidence would.

*Sources: Tversky, A., & Kahneman, D. (1974), "Judgment under Uncertainty: Heuristics and Biases," Science 185(4157), 1124–1131, https://doi.org/10.1126/science.185.4157.1124 (availability heuristic; base-rate neglect). Aristotle, Sophistical Refutations, c. 350 BCE — affirming the consequent, equivocation, false cause, hasty generalization, https://classics.mit.edu/Aristotle/sophist_refut.html . Stanford Encyclopedia of Philosophy, "Fallacies," https://plato.stanford.edu/entries/fallacies/ (formal vs. informal fallacies; false dilemma; ad verecundiam). On benchmark contamination and saturation as a documented measurement problem in this period: Stanford HAI, AI Index Report 2024, https://aiindex.stanford.edu/report/ .*
