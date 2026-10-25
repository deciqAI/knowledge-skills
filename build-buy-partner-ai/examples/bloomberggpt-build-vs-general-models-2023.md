# Method in Action: BloombergGPT and the General-Purpose Models (2023)

> *Example for the [build-buy-partner-ai](../SKILL.md) skill.*

BloombergGPT is the clearest public example of an organization that passed the hardest gate in this skill — *proprietary data* — chose to build a foundation model, documented the build in detail, and then saw a general-purpose model released two weeks earlier measured against it by an outside team. It is useful precisely because Bloomberg had a strong case for building; the lesson is about what the strong case still has to survive.

**The build (paper submitted March 30, 2023).** Bloomberg's team trained a 50-billion-parameter language model for finance. Its training data combined "a 363 billion token dataset based on Bloomberg's extensive data sources" — FinPile, assembled from decades of Bloomberg-curated financial documents — with 345 billion tokens of general-purpose data. The paper reports a compute budget of 1.3 million GPU hours on 40GB A100 GPUs, a cluster of 512 A100s, and about 53 days of training. Its stated result: the model "outperforms existing models on financial tasks by significant margins without sacrificing performance on general LLM benchmarks." The comparison set was open models of the time (GPT-NeoX, OPT-66B, BLOOM-176B).

**The general model (March 15, 2023).** OpenAI's GPT-4 Technical Report was posted two weeks before the BloombergGPT paper. GPT-4 was available by API — i.e., something a firm could *buy*.

**The outside measurement (May 2023, revised October 2023).** Li et al., "Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics?", evaluated ChatGPT and GPT-4 on financial benchmarks including several that BloombergGPT had reported on, using BloombergGPT's published numbers for comparison. On FiQA sentiment analysis: "With a few-shot examples GPT-4 is better than all other models here. BloombergGPT has relatively close performance to zero-shot ChatGPT and is inferior to GPT-4." On commodity news-headline classification: "GPT-4 outperforms ChatGPT and Prior LLMs as well as BloombergGPT." Their overall conclusion was more balanced: general models "outperform models fine-tuned with domain-specific data on some tasks, but still fall short on others, particularly when deeper semantics and structural analysis are needed."

Two caveats are part of the record: Li et al. compared against BloombergGPT's *reported* numbers rather than re-running it, and BloombergGPT's paper also reports Bloomberg-internal tasks that outsiders cannot test. Bloomberg's internal TCO and its later sourcing decisions are not public, and nothing here infers them.

Now run the **Build/Buy/Partner matrix** on the decision as the public record allows.

**1. Define the capability.** A language model for financial text tasks (sentiment, NER, classification, QA) serving Bloomberg's products and internal workflows. Metrics: the public financial benchmarks plus internal ones. **Pass** — the paper defines its evaluation in detail.

**2. Differentiation test.** Would customers notice if a competitor used the same off-the-shelf model? The paper's premise is that a model trained on Bloomberg's own archive would be measurably better at finance, and against the open models it was compared with, it was. **Pass at the time of comparison — and this is the gate's weak point.** The test compares you against what competitors can buy *now*; GPT-4 changed the comparison set two weeks before publication.

**3. Data & IP control.** FinPile is proprietary — the paper states it cannot be released — and keeping that data out of a vendor's training pipeline is a legitimate reason to build. **Strong pass.** This is the strongest part of Bloomberg's case, and it holds regardless of benchmark rankings.

**4. Time to value.** Roughly 53 days of training alone, after dataset construction, against API access to a general model. Using the skill's heuristic, build took far more than ~3× as long as buy, so the differentiation value had to cover the gap. **The record does not show whether it did.**

**5. Three-year TCO.** The public numbers cover the training run (1.3M GPU-hour budget), not maintenance, evaluation, serving, or **rework when a better base model appears**. That last line is the one the 2023 sequence made concrete: a general model released two weeks earlier matched or beat the build on some public tasks. *Gate: model replacement not costed → no comparison allowed.* **Not auditable from the public record — and this is exactly the line a build case must contain.**

**6. Lock-in & vendor risk.** Building avoids dependence on a single model vendor and keeps proprietary data in-house. Buying GPT-4 would have meant a single-vendor dependency and data-terms review. **Build scores well here.**

**7. Score and choose — with the re-evaluation trigger.** On the record, a defensible matrix in early 2023 could favor *build* on data control (step 3) and lock-in (step 6) while showing uncertainty on differentiation (step 2) and TCO (step 5). What the skill adds is the trigger: **re-run the matrix on every major general-model release**, comparing your model against the newest one you could buy, on your own evaluation set. Li et al. is that re-run, done from outside.

### The mapped steps

1. **Capability:** financial-text LLM, with published and internal benchmarks
2. **Differentiation:** better than the open models compared against; matched or beaten on some public tasks by GPT-4 soon after
3. **Data/IP:** proprietary FinPile, not releasable — strongest reason to build
4. **Time to value:** ~53 days of training plus dataset build, vs. API access
5. **3-yr TCO:** only training compute published; model-replacement cost not visible
6. **Lock-in:** build avoids single-vendor dependency
7. **Verdict + trigger:** data control justifies building; the differentiation claim needs re-measuring at every major model release

**The lesson.** Proprietary data is necessary for a build decision, not sufficient. The differentiation that justifies building is measured against the best model a competitor can *buy*, and that bar moves on the general-model makers' schedule, not yours. Keep an owned evaluation set, price model replacement into the three-year TCO, and treat each major release as a scheduled re-evaluation — so the question "is our model still better than what we could buy?" is answered by your own measurement rather than someone else's paper.

*Primary sources: Wu, S., et al. "BloombergGPT: A Large Language Model for Finance." arXiv:2303.17564 (March 30, 2023; rev. December 21, 2023), https://arxiv.org/abs/2303.17564 · OpenAI. "GPT-4 Technical Report." arXiv:2303.08774 (March 15, 2023), https://arxiv.org/abs/2303.08774 · Li, X., et al. "Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? A Study on Several Typical Tasks." arXiv:2305.05862 (May 10, 2023; rev. October 10, 2023), https://arxiv.org/abs/2305.05862 . Quotations are from the papers' abstracts, results sections and conclusion.*
