# Method in Action: Emergent Capabilities in Large Language Models (2023–2026)

> *Example for the [emergence](../SKILL.md) skill.*

Between roughly 2020 and 2026, the most-discussed live case of emergence outside biology was the claim that large language models (LLMs) exhibit **emergent abilities** — capabilities that are absent in smaller models and appear, seemingly sharply, only once model scale (parameters, data, compute) crosses some threshold. The 2022 paper "Emergent Abilities of Large Language Models" (Wei et al., *Transactions on Machine Learning Research*) defined an emergent ability as one that "is not present in smaller models but is present in larger models," and catalogued tasks — multi-step arithmetic, certain reasoning benchmarks, in-context following of complex instructions — where accuracy stayed near random until a scale threshold, then rose.

This is a near-perfect stress test for the emergence framework, because it comes with a built-in controversy: in 2023, "Are Emergent Abilities of Large Language Models a Mirage?" (Schaeffer, Miranda & Koyejo, NeurIPS 2023) argued that many "sharp" emergence curves are an artifact of the **metric** chosen — discontinuous, all-or-nothing scoring (e.g., exact-match) manufactures the appearance of a sudden jump, while continuous or per-token metrics on the same models reveal smooth, predictable improvement. So the case forces the discipline the skill demands: classify the system honestly, separate real structural emergence from measurement artifact, and refuse the reductionist relapse in *both* directions.

Walking it through the skill's Process:

## 1. Identify

- **System:** a trained transformer LLM — billions of parameters interacting through attention over trained weights — plus the surrounding ecosystem of training data, users, and downstream applications.
- **Parts:** enormous. Individual parameters (billions), attention heads, layers; at the ecosystem level, millions of prompts and users.
- **Central control:** No, in the sense that matters here. No engineer specifies "this weight encodes arithmetic carry." Capabilities are not placed; they arise from gradient descent over a training objective.
- **Outcome sought:** understand *whether* a capability genuinely emerges at scale (so we can anticipate it, price the compute, and govern it) versus whether it was smoothly present and only *looked* sudden.

## 2. Diagnose

The narrow object (a frozen model doing next-token prediction) is deterministic and, in principle, **complicated** — a large but analyzable function. But the object of interest — *which high-level competencies exist and when they appear as scale grows* — behaves as **complex**: whole-level properties (chained reasoning, instruction-following, tool use) are not readable off any single parameter and were not reliably predicted in advance from smaller models. This matches Anderson's "More Is Different": you cannot reconstruct the capability from the microphysics of the weights.

Crucially, the diagnosis must stay honest. The "mirage" critique shows that *apparent* sharpness can be an artifact of discontinuous metrics. Emergence-as-structure (new competencies genuinely appear) and emergence-as-measurement-artifact (smooth curve made to look like a cliff by the scoring rule) are different claims. The skill's job is to shape conditions and observe — not to over-assert a mystical jump, and not to explain it away entirely.

## 3. Structural drivers (complex)

- **Feedback loops (reinforcing):** capability gains attract users and capital → more compute and data → larger models → more capability. Through 2024–2025 this drove historically large AI capital-expenditure commitments by the major labs and cloud providers, a trend that was still accelerating heading into 2026.
- **Network / information flows:** capabilities are unevenly legible; benchmarks act as the shared "sensor," and the choice of benchmark metric partly *constructs* what looks emergent (the mirage argument).
- **Thresholds / initial conditions:** scale (compute × data × parameters) is the tuning knob; architecture and training recipe are the seed conditions.
- **Time delays:** a capability can exist latently in a model yet stay invisible until the right prompt, decoding strategy, or evaluation reveals it — a delay between "present" and "observed."

## 4. Design seed conditions

Because you cannot place a capability directly, you shape conditions and watch:
- **Initial conditions / seeds:** architecture, training-data composition, scale target, and training objective.
- **Local rules:** the next-token objective plus techniques (instruction tuning, RLHF-style preference training) that reshape what emerges without dictating specific competencies.
- **Feedback structures:** evaluation suites with *both* discontinuous and continuous metrics, so that a jump in exact-match is cross-checked against the smooth underlying curve — the direct operational answer to the mirage critique.
- **Constraints against destructive dynamics:** safety evaluation and red-teaming for capabilities (deception, hazardous knowledge) that could emerge unbidden at scale.

## 5. Probe-observe-adjust

The right rhythm is empirical, not oracular. You cannot deduce the next capability from first principles; you scale, then measure across many tasks and multiple metrics, then adjust. Observe with continuous metrics to see whether the curve is truly discontinuous; probe with new task families to see what appears; adjust training data and evaluation when you find capabilities (or failures) you did not anticipate. Predicting the exact capability profile of the next model in advance remains unreliable — which is itself the signature of a complex system.

## 6. Defend against "we'll plan it"

The reductionist relapse here has two faces. One is over-claiming: treating every benchmark jump as proof of a mystical new faculty. The other is over-explaining-away: concluding from the mirage paper that "nothing emerges, it's all measurement," and therefore that scale holds no surprises. The disciplined stance holds both: measurement choices genuinely manufacture some apparent discontinuities *and* genuinely new, hard-to-predict competencies do arise at scale that were not present in smaller models. Pre-commit to probe-and-observe across metrics rather than to a single tidy story.

**Operational lesson.** For anyone allocating AI capex, planning AI-native product bets, or writing capability governance, the emergence lens says: you are steering a complex system, not executing a blueprint. Shape the seed conditions (scale, data, objective, evaluation), instrument with metrics that can tell real structure from artifact, and run probe-observe-adjust — because the whole is, once again, more than a simple extrapolation of the parts.

*Sources: Wei, J. et al. (2022), "Emergent Abilities of Large Language Models," Transactions on Machine Learning Research (arXiv:2206.07682). Schaeffer, R., Miranda, B. & Koyejo, S. (2023), "Are Emergent Abilities of Large Language Models a Mirage?", NeurIPS 2023 (arXiv:2304.15004). Anderson, P. W. (1972), "More Is Different," Science 177(4047), 393–396.*
