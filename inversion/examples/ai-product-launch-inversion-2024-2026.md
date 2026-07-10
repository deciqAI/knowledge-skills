# Method in Action: Inverting an AI Product Launch (2024–2026)

> *Example for the [inversion](../SKILL.md) skill.*

A worked example on a live decision most teams faced in 2024–2026: shipping a generative-AI feature into production. The default framing is forward — *"how do we win with AI?"* Inversion flips it: *"how would this AI product be guaranteed to fail?"* — then designs the launch around eliminating those paths. This runs the skill's own seven Process steps against the anchor case.

The 2024–2026 backdrop makes the failure modes concrete rather than hypothetical. Public incidents in this window turned each abstract risk into a documented one: an airline was held liable for a customer-facing chatbot that invented a refund policy (Moffatt v. Air Canada, British Columbia Civil Resolution Tribunal, February 2024); several lawyers were sanctioned in U.S. courts for filing briefs containing AI-fabricated case citations (the earliest and most cited being *Mata v. Avianca*, S.D.N.Y., 2023); and industry reporting through 2024–2025 repeatedly flagged that inference (serving) costs, not training, can dominate the ongoing economics of a deployed LLM feature. These are the raw material for an uncharitable enumeration.

### 1. State decision + measurable target outcome

Not "launch an AI assistant." The decision: **ship a customer-facing LLM feature to 100% of users by Q3, hitting ≥ 25% weekly-active adoption within 90 days at a gross margin ≥ 60% on the feature, with zero trust-destroying public incidents.** Numbers and a timeframe — so failure is observable, not a vibe.

### 2. Invert

"If, 90 days after launch, this AI feature is a total failure — pulled from production, margin-negative, or the subject of a viral trust incident — the most likely reasons are ___." The team is given explicit permission to speak badly of the plan: the person who names the ugliest path is doing the most valuable work in the room.

### 3. Enumerate failure paths (uncharitably)

1. **Hallucination in production** — the model asserts a false policy, price, or fact to a user who acts on it; the company is held to it (the Air Canada pattern).
2. **Inference-cost blowup** — per-request token cost times real usage exceeds revenue; the feature is margin-negative at the scale that "success" implies.
3. **A single trust-destroying incident** — one screenshot of a toxic, biased, or absurd output goes viral and becomes the feature's public identity.
4. **Prompt-injection / data exfiltration** — untrusted input (a web page, a document, an email) hijacks the model into leaking system prompts or other users' data.
5. **Silent quality regression** — a model-provider version change or a prompt edit degrades outputs, and no evaluation harness catches it before users do.
6. **Adoption cliff after novelty** — users try it once, it fails their real task, and weekly-active collapses; the 25% target was demo-driven, not task-driven.
7. **Latency-driven abandonment** — end-to-end response time makes the feature feel slower than the non-AI path it replaced.
8. **Vendor/dependency shock** — a price change, deprecation, rate-limit, or policy shift from the model provider breaks the unit economics or the feature overnight.

### 4. Classify and weight

| # | Path | Category | P(occur) | Impact |
|---|------|----------|----------|--------|
| 1 | Hallucination in production | Assumption | H | fatal |
| 2 | Inference-cost blowup | Internal | M | fatal |
| 3 | Trust-destroying incident | External | M | fatal |
| 4 | Prompt injection / exfiltration | External | M | major |
| 5 | Silent quality regression | Internal | H | major |
| 6 | Adoption cliff after novelty | Assumption | H | major |
| 7 | Latency abandonment | Internal | M | minor |
| 8 | Vendor/dependency shock | External | M | major |

The **load-bearing paths** (high-P and/or fatal-Impact) are 1, 2, 3, 5, and 6.

### 5. Design a response for every load-bearing path

- **Path 1 — Hallucination → MITIGATE.** For any answer with legal/financial consequence, constrain the model to retrieval-grounded responses over an approved knowledge base, cite the source, and refuse rather than guess when confidence is low. Route consequential actions (refunds, commitments) through deterministic code, not free-form generation.
- **Path 2 — Inference cost → HEDGE.** Instrument cost-per-request before full launch; set a per-user and global spend cap; use a smaller/cheaper model for the common case and escalate only when needed; load-test economics at 100% scale, not at demo volume.
- **Path 3 — Trust incident → MITIGATE.** Output moderation/guardrails on the response path; red-team adversarial prompts before launch; a staged rollout (internal → small cohort → 100%) so a bad pattern surfaces at 1% of blast radius.
- **Path 5 — Silent regression → ELIMINATE (the blind spot).** A held-out evaluation set that runs on every prompt change and every provider version bump; pin model versions; block deploys on eval regression. This is the path teams most often leave unguarded.
- **Path 6 — Adoption cliff → MITIGATE.** Define success on a *real task completion* metric, not first-try rate; ship to a small cohort first and measure week-2 and week-4 retention before claiming the 25% target is reachable.

### 6. Build your Not-to-Do list

- We will **not** let a generative model make a legally or financially binding statement to a user without a grounded source and a deterministic guardrail.
- We will **not** ship to 100% of users before a staged rollout has cleared its cohort gates.
- We will **not** change a prompt or accept a provider version bump without the evaluation harness passing.
- We will **not** report adoption from a novelty spike as evidence of product-market fit.

### 7. Name the abort trigger

"We commit to the launch, *and* we will abort (roll back to the non-AI path and re-invert) if, by day 30 of the staged rollout, any of the following is observed: a hallucination causes a real customer-commitment error in production; blended inference margin is below 40%; or week-2 cohort retention is below 10%."

### What this surfaced that the forward plan did not

The forward "how do we win" plan almost always lists paths 1, 3, and 6 (accuracy, brand, adoption). The path teams systematically miss is **5 — silent quality regression** — because the feature works on launch day and degrades invisibly afterward when a prompt is tweaked or a provider ships a new model version. That is the new entry on the not-to-do list: *no prompt or model change ships without the eval harness passing.* Inversion's job here is not to kill the AI launch — it is to eliminate the handful of ways it was guaranteed to fail, so what ships carries only the risks the team can live with.

*Sources: Moffatt v. Air Canada, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, Feb. 14, 2024) — chatbot-hallucination liability; Mata v. Avianca, Inc., No. 22-cv-1461 (S.D.N.Y., June 22, 2023) — sanctions for AI-fabricated legal citations; OWASP Top 10 for Large Language Model Applications (2023–2025), owasp.org — prompt injection (LLM01) and related deployment risks; Klein, Gary, "Performing a Project Premortem," Harvard Business Review, September 2007 — the structured-inversion (pre-mortem) practice this audit follows. Inference-cost dominance is a widely reported pattern in 2024–2025 industry coverage of LLM operations rather than a single figure, and is stated here qualitatively.*
