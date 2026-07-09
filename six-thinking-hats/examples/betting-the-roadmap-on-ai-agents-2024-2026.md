# Method in Action: Betting the Roadmap on AI Agents (2024–2026)

> *Example for the [six-thinking-hats](../SKILL.md) skill.*

Between 2024 and 2026, a recurring decision landed on many software leadership teams: **should we bet the roadmap on AI agents** — re-architecting the product around autonomous, tool-using LLM workflows rather than shipping isolated "AI features"? This is exactly the kind of decision that degenerates into circular debate: the optimists cite competitive urgency, the skeptics cite reliability, and neither side is wrong within its own hat. Below is the anchor case run through the skill's seven-phase Process. The company is a generic illustrative mid-market B2B SaaS team; the framework and market context are real, the internal numbers are stand-ins.

## 1. Blue Hat opens (setup)

Facilitator states the question and the sequence:

> "Decision: do we commit the next 12 months of roadmap to an agent-native architecture, or continue adding discrete AI features on top of the existing product? Sequence: White → Yellow → Black → Green → Red → Blue. Time-boxed, no mode-switching mid-hat."

Sequence is Yellow-before-Black by design — the team has strong internal skeptics, so value must be established before threats are named.

## 2. White Hat — facts and data

Confirmed facts only, no interpretation:

- Frontier model capability rose sharply across 2024–2025; vendors (Anthropic, OpenAI, Google) shipped explicit **tool-use / function-calling and "agent" tooling**, and Anthropic published the **Model Context Protocol (MCP)** as an open standard for connecting models to tools and data (late 2024).
- Enterprise AI **adoption** rose materially over the period, but organizations widely reported a gap between piloting and production-grade deployment.
- Industry-wide **AI capital expenditure** by the large cloud/hyperscaler players reached historically large levels through 2025, signaling durable platform investment rather than a passing cycle.
- Internal (illustrative): current AI features drive roughly a fifth of new-trial signups; agent reliability in the team's own eval harness passes some multi-step tasks and fails others.

**Information gaps:** production reliability of long-horizon agents at the team's own error tolerance; true migration cost of the existing codebase; whether customers will grant the data/permission access agents require.

## 3. Yellow Hat — optimism and value

Specific benefits with a logical basis:

- **Category redefinition** — if agents can complete end-to-end workflows, the product shifts from "tool the user operates" to "outcome the user delegates," a larger value proposition per seat.
- **Defensibility via integration depth** — an agent wired into customer systems (via MCP-style connectors) accrues switching cost as it accumulates context and permissions.
- **Timing** — sustained hyperscaler capex means the underlying models keep improving on someone else's balance sheet; building agent-native now rides that curve.

## 4. Black Hat — caution and risk

Specific, evidence-based risks (not "I don't like it"):

- **Reliability compounds against you** — a multi-step agent's success rate is the product of each step's success rate; even 95%-per-step over ten steps drops below two-in-three end-to-end. For irreversible actions this is a correctness and liability risk, not a UX nit.
- **Pilot-to-production gap is industry-wide** — the widely reported pattern is that agent demos impress while production deployments stall on reliability, oversight, and integration; betting the whole roadmap assumes the team clears a bar most have not.
- **Platform-dependency and margin risk** — token costs and vendor terms are outside the team's control; an agent-native product's unit economics move with model pricing.
- **AI-native competition** — well-funded new entrants are building agent-first with no legacy migration tax; a slow, hedged migration could lose on both axes.

**Most critical Black Hat risk:** committing 12 months before the team's own eval harness clears its production reliability bar for *irreversible* actions.

## 5. Green Hat — creativity and alternatives

Generated without evaluation:

- **Thin-slice agent** — ship one narrow, high-value, *reversible* workflow agent-native; keep the rest feature-based.
- **Human-in-the-loop by default** — agent proposes, human confirms irreversible steps; relax the gate only where eval data earns it.
- **Adopt MCP-style connectors now** regardless of the bigger bet, so integration depth accrues either way.
- **Reliability-gated roadmap** — tie each phase of migration to a measured eval threshold rather than a calendar.
- **Buy/partner** for the agent runtime instead of building it.

## 6. Red Hat — gut feeling (one sentence each)

- Head of Product: "Exhilarated — this is the platform shift we've waited for."
- Lead Engineer: "Nervous — the demos lie and we'll own the failures."
- CEO: "Impatient — I don't want to be the one explaining why we waited."
- CFO: "Uneasy about tying margin to someone else's token pricing."

## 7. Blue Hat closes

- **Decision:** No all-in 12-month commitment. Adopt the **thin-slice + reliability-gated** path: ship one reversible workflow agent-native this quarter, instrument it against the eval harness, and gate further migration on measured thresholds. Add MCP-style connectors now regardless.
- **Actions:** define the production reliability bar for irreversible actions; build the eval harness; ship the thin slice; re-run this session in one quarter with real reliability data replacing the White Hat gaps.
- **Most critical Black risk carried forward:** multi-step reliability against irreversible actions.
- **Best Green direction:** reliability-gated, human-in-the-loop thin slice that keeps optionality while the model curve improves.

**What the hats surfaced that debate would have missed:** the real decision was never "agents: yes or no." Yellow and Black were both right, about different things — so the Green Hat's *reversible thin-slice* reframing dissolved the deadlock the Red Hat had exposed as pure emotional split (excitement vs. dread).

*Sources: Anthropic, "Introducing the Model Context Protocol" (2024), https://www.anthropic.com/news/model-context-protocol; McKinsey, "The State of AI" survey (2025), https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai; de Bono, Edward, *Six Thinking Hats*, revised edition (Back Bay Books/Little, Brown, 1999).*
