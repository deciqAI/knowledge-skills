# Method in Action: Back-Casting a Failed AI Agent Startup 12 Months Out (2024–2026)

> *Example for the [premortem](../SKILL.md) skill.*

**Context.** A startup is one signature away from committing: it has a term sheet in hand and is about to spend it building and scaling an AI *agent* product — an autonomous workflow assistant for a specific enterprise function, built on a third-party frontier model with a fine-tuning and orchestration layer on top. The demo lands every time. The lead investor is leaning in and the founding team has quietly converged on "ship it and grow." That is precisely the profile this skill flags: a hard-to-reverse capital and go-to-market commitment, made by a team that agreed fast with little visible dissent.

The distinctive move here is **back-casting**. Rather than asking "what could go wrong?", the team fixes a single imagined outcome — *the company failed 12 months from now* — and reasons backward from that endpoint to the causal chain that produced it. The 2024–2026 backdrop makes three failure vectors especially live: (a) the model gets *commoditized by the next release* so the wrapper's value collapses, (b) *unit economics break* because metered inference costs outrun a flat subscription price, and (c) a *safety incident* destroys enterprise trust. Below, the case is walked through the skill's own six Process steps.

---

### Step 1 — Frame

- **Decision/plan:** Sign the term sheet and spend it building/scaling the enterprise AI agent on a third-party frontier model; commit to a flat per-seat subscription and an aggressive growth plan.
- **Imagined failure date:** 12 months after launch.
- **Failure type:** Company failure — the product is being wound down or hard-pivoted; the next round could not be raised, or was raised only on punishing terms.
- **Participants:** The two founders, the lead engineer, the head of go-to-market, a finance/ops lead, and one operator who has shipped in this space but is *not* on the cap table (imported outside view).
- **Facilitator:** Someone with no personal stake in whether the term sheet gets signed.

### Step 2 — Set up the fiction

The facilitator reads aloud: *"It is 12 months from launch. We executed the plan exactly as written. The company has failed — we are shutting down or pivoting hard. Write down, in silence, for the next 5–10 minutes, the specific reasons why it failed. Failure already happened; your job is to explain it, not to weigh whether it could."*

The grammatical mood is enforced throughout: **failure is a fact to be explained**, not a risk to be scored. That is the whole point of back-casting — starting from a fixed endpoint forces the mind to construct a concrete causal chain rather than list vague worries.

### Step 3 — Private silent generation

Each participant writes alone, no talking. This is non-negotiable. With a term sheet on the table and an investor leaning in, an open discussion would converge on the founders' enthusiasm within minutes. Silent writing is what lets the finance lead and the non-cap-table operator write down the uncomfortable causes they would otherwise keep to themselves.

### Step 4 — Consolidate

Round-robin read-out, captured without judgment, then clustered. Back-casting from the "we failed" endpoint produced causal chains, not just risk labels. The clusters that recurred across writers — the ones tied to durable, well-documented features of the 2024–2026 AI landscape rather than to this one team — were:

1. **Commoditized by the next release.** A subsequent foundation-model version, or a first-party feature shipped by the model provider or a platform, absorbed most of what the product did. Because the moat was an orchestration-and-prompt layer rather than proprietary data, deep workflow integration, or distribution, the differentiation evaporated the moment the base model got better and cheaper. This is the widely-discussed "is it a feature or a company?" problem for application-layer AI. Back-cast chain: *model upgrade → our wrapper's marginal value → drops toward zero → customers see no reason to keep paying → churn spikes → growth story dies.*

2. **Unit economics broke under success.** Agent workflows are token-hungry: multi-step reasoning, tool calls, and retrieval multiply inference cost per task. Against a flat per-seat price, the *heaviest* users — the ones who adopted most deeply and were least likely to churn — cost the most to serve. Engagement therefore *increased* losses. Falling per-token prices helped but were offset by users demanding more steps, larger context, and more calls. Back-cast chain: *deep adoption → many agent steps per user → COGS per seat exceeds revenue per seat → gross margin goes negative → the growth-spend model stops working → out of runway.*

3. **A safety / trust incident.** An autonomous agent took a wrong action, leaked data, was manipulated by prompt injection, or produced a harmful output at a customer. Because the product *acts* rather than merely suggests, the blast radius was larger than for a chat product. A single incident at a reference customer paused every enterprise pipeline. There was no evaluation gate, no human-in-the-loop checkpoint, and no incident runbook proportional to an agent that can take actions. Back-cast chain: *no eval gate → agent takes a damaging action at a large account → public trust event → enterprise buyers pause → pipeline freezes → no revenue to raise on.*

4. **Weak habit / value-realization gap.** Trial-to-paid looked healthy, but the agent impressed in the demo without becoming embedded in a workflow the customer returned to daily. Net revenue retention quietly fell below the level the growth plan assumed.

5. **Single-vendor platform dependency.** An upstream change — pricing, rate limits, terms, or a competing first-party agent — invalidated an assumption the whole business rested on. There was no second-provider fallback.

6. **Funding-regime shift.** The bar for AI-application startups tightened between raises. Metrics that cleared at the term-sheet stage did not clear at the next round, and the runway had been planned assuming the friendlier prior environment would hold.

Each cluster was rated for probability, severity, and detectability (how early a warning signal would appear).

### Step 5 — Mitigate

For the high-probability / high-severity clusters, the team assigned a mitigation, an owner, and a monitoring trigger:

| # | Failure mode | Prob | Sev | Detect | Mitigation | Owner | Trigger |
|---|---|---|---|---|---|---|---|
| 1 | Commoditized by next model release | High | High | Med | Move the moat off the model: proprietary workflow data, deep integrations, and switching cost that survive a base-model upgrade; treat each release as capability to absorb, not a threat to fear | Founders | Major upstream model/feature release overlapping our core use case |
| 2 | Unit economics break under deep use | High | High | High | Instrument per-seat gross margin from day one; add usage-based pricing or step caps for heavy users; route routine sub-tasks to a cheaper model | Finance | Per-seat COGS trending toward or above per-seat revenue |
| 3 | Safety / trust incident (agent acts) | Med | High | Low | Pre-launch eval gate; human-in-the-loop for high-impact actions; input/output guardrails; scoped permissions and data handling; incident runbook | Lead eng | Any near-miss in eval or production |
| 4 | Weak habit / NRR gap | Med | High | Med | Define an activation event tied to real workflow embedding; track cohort retention and NRR, not signups | GTM | Cohort retention or NRR below pre-set floor |
| 5 | Single-vendor dependency | Med | High | Med | Abstract the model interface; qualify a second provider; make rate-limit and terms exposure explicit | Lead eng | Upstream pricing/terms/rate-limit change |
| 6 | Funding-regime shift | Med | High | Med | Budget to a "default alive" path that does not assume the next round; set a burn cap and runway floor | Finance | Runway below floor, or milestone slip vs. raise plan |

The deliverable is the **modified plan**, not the failure list: usage-aware pricing, a per-seat margin dashboard, a pre-launch eval gate with human-in-the-loop on high-impact actions, a second-provider abstraction, and a default-alive budget were all written into the plan *before* the term sheet was signed.

### Step 6 — Schedule the re-premortem

Failure modes shift as the product and market move, so the team locked the next premortem to the launch milestone before leaving the room — with a standing rule that a **major upstream model release triggers an off-cycle re-premortem**, since that single event is the most likely to re-price every assumption on the board.

---

**What back-casting surfaced that a prospective review missed.** An ordinary "what are the risks?" pass with this team would have logged "competition" and "execution" and moved on. Fixing the failed endpoint and reasoning backward pulled out mechanism-level causes specific to this era: that *deep adoption can lose money* when metered agent costs meet a flat price, that an agent which *acts* has a larger safety blast radius than a chat product, and that the moat lived in the wrong layer — an orchestration wrapper on a commoditizing model rather than in data, integration, or distribution. Those are exactly the causes an enthusiastic room suppresses, and exactly what the silent back-casting step is built to recover.

*Sources: Klein, G. (2007). "Performing a project premortem." Harvard Business Review, 85(9), 18–19. Mitchell, D. J., Russo, J. E., & Pennington, N. (1989). "Back to the future: Temporal perspective in the explanation of events." Journal of Behavioral Decision Making, 2(1), 25–38 — the prospective-hindsight / back-casting evidence base. Kahneman, D. (2011). Thinking, Fast and Slow, Ch. 24 (premortem endorsement). Graham, P. "Default Alive or Default Dead?" (2015, paulgraham.com) for the runway/funding-regime framing. On the 2024–2026 AI landscape used as backdrop — large AI capital expenditure, rapidly falling per-token inference prices, fast model-release cadence, the "is it a feature or a company?" debate for the application layer, and enterprise caution around autonomous agents — see contemporaneous reporting and analysis in outlets such as The Information, Stratechery (Ben Thompson), and a16z's writing on the AI application layer. Specific figures are intentionally omitted; treat all market characterizations as directional and as of early 2026.*
