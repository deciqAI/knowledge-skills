# Method in Action: A Chipmaker's Leading-Edge Fab Investment Under AI Uncertainty (2024–2026)

> *Example for the [decision-tree](../SKILL.md) skill.*

Between 2024 and 2026, one of the largest irreversible capital bets in the economy was a semiconductor manufacturer's decision to commit to leading-edge fabrication capacity. A single advanced logic fab is a multi-year, multi-billion-dollar commitment made *years* before the demand that would fill it is confirmed. The AI wave made this sharper on both sides: the *upside* case (AI accelerators and their supply chain filling every wafer) and the *downside* case (a capacity glut if AI demand or monetization disappoints, echoing prior semiconductor boom-bust cycles). This is a textbook decision-tree problem — sequential, uncertain, quantifiable — and the tree does exactly what Magee promised in 1964: it converts "AI demand is unstoppable, we must break ground now" into "what probability do you put on sustained high demand, and what does the tree say if you are wrong?"

This worked example applies the skill's six Process steps to a **stylized composite** of that decision. The framing (large fab now vs. phased/modular fab vs. defer, under high/low AI-driven demand) mirrors the real 2024–2026 debate; the probabilities and dollar payoffs below are **illustrative inputs chosen to demonstrate the method**, not figures from any company's filings.

---

**Step 1 — Root.** Define the decision. A chipmaker's board must choose how to commit leading-edge wafer capacity over a multi-year horizon. Draw the root square with three branches:

- **Large fab now** — commit to a full-scale advanced fab immediately. Highest fixed cost and longest lead time, best unit economics *if* demand shows up, most stranded capital if it does not.
- **Phased / modular fab** — build the shell and a first module now, with a pre-engineered *option to expand* tooling later once demand is clearer (directly the small-plant-with-expansion structure Magee introduced in 1964).
- **Defer** — hold the large commitment ~12 months, gather adoption and pricing signal, then decide. Deferral is not free: a fab's multi-year construction-and-qualification lead time means capacity decided late arrives late, potentially after the window of peak demand.

Decision-maker: the board / CFO. Timeline: leading-edge fab lead times run into years — which is precisely why "wait" carries a real delay cost.

**Step 2 — Chance nodes.** Each branch runs into an uncertainty the firm does not control. Draw a circle on each. The dominant chance node is **AI-driven wafer demand**, which must be MECE:

- *High, durable demand* — AI-accelerator and adjacent demand keeps leading-edge capacity near-full for years.
- *Low / disappointing demand* — AI adoption or monetization stalls, or competitors add capacity too; the new fab runs underutilized (the "AI capex glut / bubble" fear that ran through the 2024–2026 debate).

For **Phased / modular**, a second-stage decision node follows the year-1 signal: having observed high or low demand, *then* choose to install the expansion tooling or hold — the learn-then-decide structure that makes a tree worth more than a one-shot EV.

**Step 3 — Probabilities.** Assign a number and a basis to every branch; reject an unjustified "50/50." Illustrative inputs for this composite:

| Node | Branch | p | Basis (illustrative) |
|---|---|---|---|
| AI wafer demand | High, durable | 0.60 | Sustained AI-accelerator demand and leading-edge order signals reported during the 2024–2025 build-out |
| AI wafer demand | Low / disappointing | 0.40 | Historical semiconductor boom-bust base rate; overbuild / bubble concerns aired publicly in the same period |

The number matters less than forcing its owners to state and defend it — which is where a boardroom's "the AI opportunity is enormous" becomes a concrete, revisable argument about one probability.

**Step 4 — Payoffs.** Assign consistent-unit payoffs (illustrative multi-year NPV, arbitrary units) to every terminal leaf:

- Large fab + High demand → **+100** (full-scale capacity, best margins, near-full utilization)
- Large fab + Low demand → **−45** (stranded, underutilized leading-edge assets; the overbuild downside)
- Phased + High demand → **+70** (installs expansion after the signal; captures most upside but pays a modularity premium and some ramp delay)
- Phased + Low demand → **+5** (holds expansion; limited loss — the bounded-downside branch)
- Defer, then build after signal → payoffs as above **minus a delay cost** (share and pricing ceded during the wait, plus a scarcity premium on equipment if everyone breaks ground at once)

**Step 5 — Rollback.** Right to left, EV at each chance node = Σ(p × value):

- **Large fab EV** = 0.60(+100) + 0.40(−45) = 60 − 18 = **+42**
- **Phased EV** = 0.60(+70) + 0.40(+5) = 42 + 2 = **+44**
- **Defer EV** = the value of deciding *after* the signal, minus the delay cost. Its appeal is highest when the demand probability sits near the middle (uncertainty is greatest, so learning is worth most) and lowest when demand looks clearly high (deferral just cedes ground) or clearly low (little worth waiting to build).

At assigned inputs, **Phased narrowly leads (+44 vs. +42)** — the bounded-downside branch beats the full commitment precisely because the 0.40 weight on disappointing demand makes the large fab's −45 tail expensive. Mark the losing branch `//`. Per the skill, the recommendation is not "go phased," it is "go phased *at these probabilities*."

**Step 6 — Sensitivity + stop-rule.** Find where the choice flips. Setting Large-fab EV = Phased EV:

`p(100) + (1−p)(−45) = p(70) + (1−p)(5)`
→ `145p − 45 = 65p + 5`
→ `80p = 50`
→ **p\* = 0.625.**

So the Large fab only beats Phased once p(high demand) exceeds **≈0.625**. At the assumed 0.60 the tree favors Phased, but the gap is thin: a modestly *more* bullish demand read (above 0.625) flips it to the full-scale fab, and a *more* bearish read widens Phased's lead. That single threshold is the real output. It reframes the whole "is AI-fab capacity a rational bet or a bubble?" debate as: *do you believe durable-high-demand probability sits above or below ~0.625?*

**EVPI / stop-rule.** Compute the value of resolving the demand uncertainty before committing. With perfect foresight the firm picks the best action in each state: +100 (Large) if high, +5 (Phased-hold) if low → EV(perfect info) = 0.60(100) + 0.40(5) = 62. Best action now (Phased, +44) → **EVPI = 62 − 44 = 18** (illustrative units). If a year of adoption data, customer pre-commitments, or a smaller pilot line costs *less* than that 18, buy the information first — the disciplined case for the phased/defer path. If resolving the uncertainty would cost *more* than 18 (deferral cedes irrecoverable position, or lead times mean late capacity is worthless), commit now. Stop refining once the leading option's EV advantage exceeds the value of further analysis.

---

**The insight the tree delivers.** Not "build the fab" or "don't," but three contestable objects: (1) the demand probability everyone is really arguing about, (2) the **p\* ≈ 0.625 threshold** at which full commitment overtakes the phased option, and (3) an EVPI that says whether a year's wait or a pilot line is worth its cost. Note how this differs from the [hyperscaler build-vs-buy-vs-wait example](ai-capex-build-vs-buy-vs-wait-2024-2026.md): a chipmaker cannot "buy" leading-edge capacity from a cloud provider, so its middle branch is *modularity* (phase the fab) rather than *rental* — and that structural difference moves the switchover threshold. Missing-branch audit: this composite omits a joint-venture / customer-prepay structure, a trailing-edge fallback, and competitor-first dynamics — real trees are always simplifications, and naming what's left out is mandatory.

*Sources: Magee, J. F. (1964), "Decision Trees for Decision Making," Harvard Business Review, and "How to Use Decision Trees in Capital Investment," HBR (method, incl. the small-plant-with-option-to-expand structure). Raiffa, H. (1968), Decision Analysis, Addison-Wesley (rollback, sensitivity, EVPI). Contemporary context — the 2024–2026 surge in AI-related demand for leading-edge semiconductors and the accompanying public "AI capex / overbuild / bubble" debate, alongside the semiconductor industry's well-documented history of boom-bust capacity cycles — is drawn from widely reported industry and financial-press coverage of that period; the probabilities and dollar payoffs in this example are illustrative inputs to demonstrate the method, not figures from any filing.*
