# Method in Action: "AI Changes Everything" vs. Measured Enterprise ROI (2023–2026)

> *Example for the [narrative-fallacy](../SKILL.md) skill.*

Between the November 2022 launch of ChatGPT and early 2026, a single, clean, causal-sounding story swept boardrooms, markets, and media: **generative AI changes everything, and every company must adopt it now or be disrupted.** This walkthrough applies the skill's six-step Process to that narrative — not to argue AI is unimportant, but to separate the *story* from what was actually *measured*.

## Step 1 — Identify the narrative

- **Story:** A general-purpose technology (large language models) arrived, is improving on a steep curve, and will transform every knowledge-work function. Firms that move fastest win; laggards get disrupted.
- **Outcome explained:** Explosive capability demos, record enterprise interest, and a historic run-up in AI-exposed equities — most visibly Nvidia, whose market capitalization crossed roughly $1 trillion in mid-2023, then approximately $2 trillion in early 2024, and approximately $3 trillion by mid-2024.
- **Causes identified:** Transformer architecture + scaling compute → emergent capability → inevitable, near-universal enterprise value.
- **Implied lesson:** Adopt aggressively and immediately; capex on AI infrastructure is self-justifying because the transformation is certain.

## Step 2 — Test selection bias

The narrative is built almost entirely from **visible winners and vivid demos**. What it strips out:

- **Pilots that never reach production.** By 2024, industry surveys and consultancy reporting repeatedly flagged that a large share of enterprise generative-AI pilots stalled before delivering measurable ROI. The successful deployments circulate as case studies; the quiet, abandoned pilots do not (see [`survivorship-bias`](../survivorship-bias/SKILL.md)).
- **The demo-to-durable-value gap.** Impressive one-off demonstrations are selected for sharing precisely because they are impressive; the median unglamorous integration effort is invisible.
- **Would the same method "explain" failures?** Yes — and that is the tell. The same confident causal framing ("AI transforms this workflow") is applied both to the deployments that worked and, in retrospect, to the ones that didn't ("they lacked the right data / talent / culture"). A narrative that explains every outcome equally well is post-hoc, not predictive.

## Step 3 — Reconstruct pre-event uncertainty

What did contemporaneous evidence actually show, as opposed to the retrofitted "obvious" story?

- **Adoption was real but uneven.** Through 2024–2025, reputable surveys (e.g., McKinsey's annual State of AI work) reported climbing *usage* of generative AI, while consistently noting that enterprise-wide *bottom-line impact* remained concentrated in a minority of functions and firms. Usage ≠ measured P&L effect.
- **Capability progress was genuine but contested.** The premise that scaling compute reliably produces proportional capability gains was an *assumption under active debate*, not a settled law — this matters for Step 4.
- **The cost side was largely invisible in the bull narrative.** The story emphasized upside and treated multi-hundred-billion-dollar industry capital-expenditure plans as obviously warranted, while the measured return on that capex remained an open question as of early 2026.

## Step 4 — Test counterfactuals

Two events puncture the "smooth, inevitable, single-cause" framing:

- **The DeepSeek shock (January 2025).** The Chinese lab DeepSeek released a competitive open-weight model reported to have been trained at a small fraction of the cost assumed for frontier models. The market reaction was severe: on **January 27, 2025**, Nvidia's stock fell sharply in a single session — a roughly $500+ billion drop in market value, among the largest single-day losses for any company on record. *Counterfactual force:* if frontier capability required the enormous, ever-rising compute spend the narrative assumed, a low-cost competitor could not have appeared. Its appearance shows the "scaling capex is self-justifying" premise was contingent, not necessary.
- **US export controls.** Successive rounds of US restrictions on advanced AI-chip exports to China (from October 2022 onward, tightened in October 2023 and again in subsequent rounds) show the trajectory was shaped by *policy contingency*, not by technology alone. A different regulatory path yields a different competitive map — exactly the kind of contingency a clean causal story omits.

If the identified cause (compute scaling → inevitable universal ROI) were the true driver, neither a cheap competitor nor policy-driven supply constraints should have moved the story much. Both did.

## Step 5 — Probabilistic re-expression

Replace *"AI changes everything, so adopt now and capex is justified"* with:

> Generative AI is a genuine, broadly applicable capability advance (high confidence). It has produced measurable value in specific, well-scoped functions — coding assistance, customer support, content drafting — for firms that invested in data and integration (medium-high confidence). Its enterprise-wide, bottom-line ROI as of early 2026 was **real but narrower and slower than the dominant narrative implied** (medium confidence). Whether the industry's aggregate infrastructure capex earns an adequate return remains genuinely open (low confidence, actively debated). The precise pace and distribution of future value is uncertain.

## Step 6 — Document lessons cautiously

- **Transferable insight:** A clean, causal-sounding technology narrative can outrun the evidence for years, especially when a visible proxy (a soaring stock, a viral demo) stands in for the harder-to-measure thing (durable, firm-level ROI). Track the *measured* variable, not the *narrated* one.
- **Evidence base beyond the focal case:** This is the recurring shape of technology hype cycles — railroads, radio, the dot-com build-out, each of which paired a substantially-true long-run thesis with a substantially-wrong near-term certainty about timing and returns. The AI case is one more instance, not a unique one.
- **Operational lesson (calibrated):** Adopt where you can *measure* ROI in a scoped pilot; treat "everyone must go all-in immediately" as a narrative to be tested, not a fact. Size irreversible bets to survive the scenario where the timing story is wrong (compose with [`margin-of-safety`](../margin-of-safety/SKILL.md) and [`black-swan`](../black-swan/SKILL.md)).

The point is not that the AI thesis is false. It is that a story which is *directionally* right can still be *operationally* dangerous when its clean causality is mistaken for measured certainty.

*Sources: Nvidia investor-relations disclosures and widely reported market-capitalization milestones (approximately $1T mid-2023, $2T early 2024, $3T mid-2024); widely reported ~$500B+ single-session drop in Nvidia's market value on 2025-01-27 following DeepSeek's model release; DeepSeek's January 2025 model release and public claims of low training cost as reported by major outlets; US Bureau of Industry and Security (Department of Commerce) advanced-computing/AI-chip export-control rules of October 2022 and October 2023 and subsequent rounds; McKinsey "The State of AI" annual global surveys (2024–2025) on generative-AI adoption vs. measured value; Nassim Taleb, The Black Swan (2007), ch. 6, on the narrative fallacy.*
