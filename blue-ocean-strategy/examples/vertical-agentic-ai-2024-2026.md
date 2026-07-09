# Method in Action: Escaping the Red Ocean of General AI Chatbots (2024–2026)

> *Example for the [blue-ocean-strategy](../SKILL.md) skill.*

By 2024–2026, general-purpose AI chatbots had become a textbook red ocean. A handful of well-funded assistants — OpenAI's ChatGPT, Google's Gemini, Anthropic's Claude, Microsoft Copilot, Meta AI, and a long tail of open-weight models — converged on the same value curve: a chat box, a general model, broad knowledge, and a monthly subscription in a similar price band (consumer tiers commonly around $20/month as of early 2026). Underlying model capability was expensive to build yet increasingly hard to differentiate at the surface, and reported industry AI capital expenditure ran into the tens of billions of dollars per major player per year. The strategic question a vertical software team faced: *how do we avoid competing head-to-head with trillion-dollar platforms on "best general chatbot"?* Blue Ocean answers: stop competing on that curve. This walks the anchor case — **vertical, agentic AI built around one industry's actual workflow** — through the skill's six process steps.

**Step 1 — Current strategy canvas (As-Is).** The general-assistant category converged on a recognizable set of buyer-perceived factors, each scored 1–5 for a typical leading chatbot:

| Factor | General chatbot (typical) |
|---|---|
| Breadth of general knowledge | 5 |
| Raw model reasoning quality | 4–5 |
| Conversational, open-ended UX | 5 |
| Price competitiveness (low $/mo) | 3 (converged ~$20) |
| Fits a specific job's workflow end-to-end | 1 |
| Takes real actions in the user's systems of record | 1 |
| Verifiable, auditable, domain-correct output | 2 |
| Accountability for a completed outcome | 1 |

Every major assistant draws nearly the same curve — high on general capability and open-ended chat, low on doing a specific job to completion inside a specific system. That convergence is the red ocean.

**Step 2 — Three tiers of non-customers.** The decisive input was people who were *not* buying a general chatbot seat, or were paying but not getting a job done:
- *Soon-to-be (dissatisfied users):* professionals who tried a chatbot for real work but reverted to legacy tools because the assistant produced a draft, not a finished, correct, filed outcome — it lived in a separate tab, disconnected from their systems of record.
- *Refusing (using substitutes):* teams solving the workflow with incumbent vertical software plus manual labor, or with outsourced/offshore human process work — refusing general AI because it was unaccountable and did not integrate.
- *Unexplored:* regulated and high-stakes functions (clinical documentation, legal review, accounting, claims) that had never seriously considered a consumer chatbot because generic output carried unacceptable audit and liability risk.

Shared dissatisfaction across all three: *"It can talk about my job, but it can't do my job."*

**Step 3 — Six Paths.** 
- *Path 1 (substitute industries):* the real substitute is not another chatbot — it is the incumbent SaaS suite and the human labor doing the workflow today. Benchmark against those, not against Gemini.
- *Path 3 (buyer chain):* the economic buyer is a function owner (a clinic administrator, a firm's operations lead) who buys *outcomes and hours saved*, not a curious individual buying a general model seat.
- *Path 4 (complementary offerings):* the value sits in integration, data connectors, verification, and audit trails wrapped *around* a model — not in the model alone.
- *Path 5 (functional vs. emotional):* general assistants sell open-ended possibility; the vertical buyer wants a bounded, reliable, functional guarantee that a specific task is done right.

Primary opportunity selected: an **agent that owns one industry workflow end-to-end** — integrated into the systems of record, taking actions, and producing verifiable, accountable output.

**Step 4 — ERRC grid.**
- *Eliminate:* the open-ended "ask me anything" general-knowledge positioning; the burden on the user to prompt, verify, and re-enter the result into their real system.
- *Reduce:* surface breadth (support one workflow deeply, not all of them); dependence on the user's prompting skill.
- *Raise:* domain correctness and verifiability; depth of integration into existing systems of record; accountability for a completed outcome.
- *Create:* autonomous multi-step action inside the workflow; a domain-specific audit trail; outcome- or usage-based pricing tied to work actually completed rather than a flat seat.

*Arithmetic check.* Eliminating the general-model arms race is the cost lever: a vertical product can build a thinner orchestration and verification layer on top of existing frontier models via API rather than funding the multi-billion-dollar training capex the platforms carry. Those eliminated/reduced costs fund the Raise/Create investments (integrations, domain evaluation, guardrails). Savings on the cost side exceed the added spend on the value side — this passes the value-innovation test rather than being differentiation-at-higher-cost.

**Step 5 — Target strategy canvas (To-Be).** The vertical-agentic curve diverges sharply: near-zero on general breadth and open-ended chat, high on workflow-fit, action-taking, verifiability, and outcome accountability — exactly the factors where general chatbots score 1–2.
- *Focus:* three to four dimensions (workflow-fit, action-taking, verifiable/auditable output, outcome accountability).
- *Divergence:* an inverted curve versus the general-assistant pack, not a taller version of the same shape.
- *Tagline a non-customer understands in one sentence:* *"It doesn't chat about the job — it does the job, in your systems, and you can audit every step."*

**Step 6 — Buyer utility validation.** Stop-rule: does the function owner say *"I've never seen anything that actually closes this loop"* — or *"nice demo, but I still wouldn't switch"*? The signal to pursue is a refusing/unexplored non-customer (a team currently using incumbent SaaS plus manual labor) adopting because the agent completes and files the work, not because it has a marginally better model. If the response is the second — polite interest, no switch — the Eliminate row is under-committed (the product is still a general chatbot with a domain skin) and ERRC must iterate.

**Caveat — blue oceans turn red.** This water is filling fast: through 2024–2026 the platforms themselves pushed toward agents and tool use, and vertical AI startups multiplied. The durable moat is not the model — it is the integrations, proprietary workflow data, and switching costs accumulated inside the customer's systems of record. Treat the value innovation as a window, and build the moat from day one (see [switching-costs](../../switching-costs/SKILL.md) and [first-mover-advantage](../../first-mover-advantage/SKILL.md)).

The mapped steps:
1. Current canvas: general chatbots converged on breadth/chat/~$20 price, near-zero on doing a specific job in a specific system — red ocean visible
2. Non-customers: soon-to-be (reverted to legacy tools), refusing (incumbent SaaS + manual labor), unexplored (regulated high-stakes functions) — shared dissatisfaction: "it can talk about my job, not do it"
3. Six Paths: Path 1 (substitute = incumbent SaaS + human labor), Path 3 (buyer = function owner buying outcomes), Path 4 (value in integration/audit around the model), Path 5 (functional guarantee over open-ended possibility)
4. ERRC: Eliminate general positioning/user verification burden; Reduce breadth/prompt-dependence; Raise correctness/integration/accountability; Create autonomous action/audit trail/outcome pricing — eliminated training-capex arms race funds the value jump
5. Target canvas: inverted, focused curve; one-sentence tagline; divergence from the general-assistant pack
6. Buyer utility: validated when a substitute-using non-customer switches because the loop closes, not because the model is marginally better

*Sources: Kim, W.C. & Mauborgne, R. (2005). *Blue Ocean Strategy.* Harvard Business Review Press, ch. 1–2 (value innovation, strategy canvas, ERRC, non-customer tiers, Six Paths). Contemporary market context — the convergence of general assistants (ChatGPT, Gemini, Claude, Microsoft Copilot, Meta AI), the roughly $20/month consumer-tier price band, large-scale AI capital expenditure, and the 2024–2026 shift toward agentic/tool-using AI and vertical AI applications — is drawn from widely reported public coverage as of early 2026 (e.g., the companies' own product pages and pricing pages; ongoing reporting in outlets such as The Wall Street Journal, The Information, and Stratechery). Figures are described in qualified terms because exact, current numbers move quickly; this example asserts only the durable, well-documented structure of the market, not precise point-in-time values.*
