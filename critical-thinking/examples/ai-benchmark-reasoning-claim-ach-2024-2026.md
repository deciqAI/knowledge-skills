# Method in Action: "This Benchmark Proves the Model Reasons" — an ACH on AI Capability Claims (2024–2026)

> *Example for the [critical-thinking](../SKILL.md) skill.*

A worked example in the domain most saturated with motivated reasoning right now: evaluating an AI capability claim. A vendor (or an enthusiastic team) posts a chart: "Our model scores near-human on benchmark X — this proves it genuinely reasons." The claim is high-stakes (procurement, roadmap, safety decisions ride on it), multiple interpretations of the same score exist, and both buyer and seller have incentives to believe it. This is exactly the setup ACH exists for: do not accumulate confirming demos — score the headline hypothesis against the alternatives that would produce *the same benchmark number*.

During 2024–2026 this became a recurring, publicly documented pattern. Researchers repeatedly showed that a high score on a static benchmark is consistent with several very different underlying explanations. Notable public findings in this window include: evidence of **benchmark data contamination** (test items or close paraphrases leaking into training corpora); studies showing large accuracy drops when benchmark problems were **perturbed or re-templated** rather than shown verbatim (e.g., the GSM8K-style robustness/GSM-Symbolic line of work from Apple researchers, 2024); and disclosure controversies around **eval access** (e.g., the late-2024–early-2025 discussion, which grew after o3's December 2024 results were announced, over a frontier lab having prior access to portions of the FrontierMath dataset). The lesson is not "benchmarks are useless" — it is "a score is evidence for *several* hypotheses, so run the matrix."

Treat the score the way ACH demands: enumerate hypotheses first, then let *diagnostic* evidence — the evidence that separates the hypotheses — decide.

- **Hypotheses (Step 1)** — at least 3, obvious + contrarian + in-between:
  - **H1 — Genuine reasoning:** the model has a transferable reasoning capability; the benchmark measures it.
  - **H2 — Training-set contamination:** the benchmark (or near-duplicates) appeared in training data; the model is partly retrieving, not reasoning.
  - **H3 — Cherry-picked / favorable presentation:** the reported number reflects best-of-N sampling, prompt tuning on the eval, or selective reporting of the runs that looked best.
  - **H4 — Teaching-to-the-eval:** the model was optimized against this benchmark's format/distribution (directly or via similar public sets), inflating the score without general capability.

- **Evidence (Step 2)** — for and against, including expected-but-absent evidence:
  - **E1 — Perturbation drop:** when problems are re-worded, re-numbered, or restructured (held-out variants), accuracy falls substantially.
  - **E2 — Held-out / private test:** on a fresh, never-published test of the *same* skill, the score is far lower than the headline.
  - **E3 — Contamination check:** membership-inference / canary / n-gram overlap tests suggest benchmark items (or paraphrases) are in the training corpus.
  - **E4 — Reporting method:** the headline uses best-of-many sampling or eval-specific prompting rather than a single standardized pass; single-pass numbers are much lower or not shown.
  - **E5 (absence) — No transfer:** the capability that "proves reasoning" does **not** appear on structurally similar tasks the model was not tuned or exposed to — the transfer a genuine skill should produce is missing.

- **Matrix (Step 3), scored C / I / N/A** — "does this evidence sit *consistently* with the hypothesis?":

| Evidence | H1 (genuine) | H2 (contamination) | H3 (cherry-pick) | H4 (teach-to-eval) |
|---|---|---|---|---|
| E1 (perturbation drop) | I | C | N/A | C |
| E2 (private test far lower) | I | C | C | C |
| E3 (overlap detected) | I | C | N/A | C |
| E4 (best-of-N reporting) | I | N/A | C | N/A |
| E5 (no transfer) | I | C | C | C |
| **Inconsistencies** | **5** | **0** | **0** | **0** |

- **Refine the matrix (Step 4):** E5 (no transfer) is consistent with H2/H3/H4 and *inconsistent only with H1* — so it is the single most diagnostic separator between "real reasoning" and everything else. E4 (reporting method) is the sharpest separator *among* the non-reasoning hypotheses: it points specifically at H3 while being N/A for the contamination and teach-to-eval stories, which don't require selective reporting to explain the number.

- **Draw conclusions (Step 5):** count Inconsistencies. **H1 (genuine reasoning) carries 5 — it is eliminated by this evidence set.** H2, H3, and H4 each carry 0 and remain live. Critically, ACH does not force a single winner here: the honest output is "the full evidence best supports a *non-reasoning* explanation, and we cannot yet distinguish contamination vs. cherry-picking vs. teaching-to-the-eval." That is a more truthful conclusion than the vendor's H1.

- **Sensitivity analysis (Step 6):** the linchpins are E1, E2, and E3. **If the model holds up under perturbation (E1 reverses) AND scores comparably on a genuinely private, contamination-free test (E2 reverses), then H2/H3/H4 lose their inconsistency-free status and H1 revives.** In other words, "genuine reasoning" is not unfalsifiable — it is a claim you *can* rescue, but only with held-out, uncontaminated, single-pass, transfer-tested evidence, none of which a static leaderboard number supplies.

- **Report (Step 7):** the headline "this benchmark proves the model reasons" is not supported. Alternatives rejected: none of H2/H3/H4 can be dismissed on current evidence. Alternative *accepted provisionally*: some blend of contamination, favorable presentation, and eval-optimization better explains the score than transferable reasoning.

- **Milestones (Step 8):** re-run the matrix when (a) an independent group publishes a held-out or perturbed-variant evaluation, (b) contamination audits for the specific benchmark are released, or (c) the vendor reports a standardized single-pass number on a fresh private set. Each of these is exactly the diagnostic evidence the leaderboard lacked.

**The lesson the framework names:** a benchmark score is *confirming* evidence for reasoning — and equally confirming for three other explanations. Counting confirmations ("look how many it got right") cannot discriminate; only the disconfirming, diagnostic evidence (perturbation robustness, private-test transfer, contamination audits) can. The hypothesis that survives is the one with the fewest inconsistencies — and in 2024–2026 the raw-leaderboard version of "it reasons" repeatedly failed that test the moment anyone ran the matrix.

The mapped steps:
1. Identify hypotheses: genuine reasoning / contamination / cherry-pick / teach-to-eval (≥3)
2. List evidence including the absent expected evidence (E5: no transfer to un-tuned tasks)
3. Score the matrix C / I / N/A against every hypothesis
4. Isolate diagnostic evidence (transfer failure; reporting method) that discriminates
5. Count Inconsistencies: genuine-reasoning carries the most and is eliminated; three non-reasoning hypotheses remain live
6. Name the linchpins: held-out, uncontaminated, single-pass, transfer-tested results would revive H1

*Sources: Mirzadeh et al., "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" (Apple, arXiv:2410.05229, 2024); public reporting and discussion in late 2024 through early 2025 regarding a frontier lab's prior access to portions of Epoch AI's FrontierMath benchmark; and the broader 2023–2025 literature on benchmark data contamination in LLM evaluation (e.g., surveys and membership-inference/decontamination studies on arXiv). Figures and mechanisms are described in qualified terms; no specific score is asserted as fact.*
