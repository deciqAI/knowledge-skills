# Method in Action: AI Coding Assistants Crossing the Chasm (2023–2026)

> *Example for the [pmf-crossing-the-chasm](../SKILL.md) skill.*

A worked example applying the PMF + Chasm Audit to a category, not a single company: **AI coding assistants and agents** — GitHub Copilot, Cursor, and the broader wave of AI-native coding tools that emerged after ChatGPT (late 2022) and matured through 2025. The point is not to grade any one vendor but to show *where the chasm sits* for the whole category, and which whole-product gaps stall the crossing from visionary early adopters into a pragmatist mainstream.

Because the framework separates PMF from chasm, we run Part A first, then Part B.

## Part A — Measure PMF

**A1 — Active-user cohort.** The relevant cohort is not "developers who tried an AI autocomplete once," but developers who kept using an assistant across multiple sessions over weeks. GitHub Copilot launched in preview in mid-2021 and became generally available in mid-2022; by the mid-2020s GitHub reported that Copilot had well over a million paying subscribers and was used across a large share of enterprises. Cursor, built on top of the VS Code lineage, grew rapidly through 2024–2025 among developers who adopted an AI-native editor. These are genuine repeat-use cohorts, not signup vanity.

**A2 — Ellis Test (equivalent signal).** No public vendor ran a formal "How would you feel if you could no longer use this?" survey at category scale, so we read the equivalent signal. Two things stand out: (1) developer surveys through 2024–2025 (e.g., Stack Overflow's annual Developer Survey) reported that a large majority of developers were using or planning to use AI tools in their workflow; (2) strong retention and word-of-mouth among the early cohort — developers who adopted assistants overwhelmingly reported they would be reluctant to give them up. By the Ellis proxy, the early-adopter segment clears the bar.

**A3 — Score / verdict.** For the **early-adopter developer segment** — individual engineers and small teams who tolerate rough edges (occasional wrong suggestions, hallucinated APIs) in exchange for speed — the category has clear PMF. The "very disappointed if I lost it" signal is high among daily users.

**A4 — Follow-ups.**
- *Who benefits most?* Individual developers and small, autonomy-heavy teams writing greenfield or boilerplate-heavy code.
- *Main benefit?* Speed on well-trodden tasks — scaffolding, tests, boilerplate, unfamiliar-API lookup.
- *Top improvements requested?* Reliability on large existing codebases, correctness guarantees, and control over what the tool sees and does.

**A5 — Retention curve.** Among daily-active early adopters the curve flattens into a smile — the tool becomes part of the workflow. That is a PMF signal, and it holds specifically for the early-adopter segment.

**Verdict on Part A:** PMF is real — *in the visionary early-adopter segment.* That is exactly the setup the chasm framework warns about: PMF with early adopters does not license the assumption that the pragmatist mainstream will follow on the same product.

## Part B — Assess the Chasm

**B1 — Rogers classification.** Position today's buyers on the diffusion curve:
- **Innovators / Early Adopters:** individual developers, indie hackers, startups, and forward-leaning teams who adopt for competitive edge and tolerate imperfection.
- **Early Majority (the mainstream not yet fully crossed):** large enterprise engineering orgs — banks, healthcare, defense, regulated industries — whose adoption is gated by security review, legal, and platform teams rather than by individual developer enthusiasm.

**B2 — Chasm geography (today → next).**
- *Selling today to:* individual developers and small teams (bottom-up, seat-by-seat).
- *Next mainstream sub-segment:* regulated-enterprise engineering organizations, where the buyer is a CIO/CISO/platform lead, not the developer who loves the tool.

The chasm is the gap between "developers love it" and "the enterprise will standardize on it." This is the classic Moore chasm: visionaries buy transformation; pragmatists buy proven, safe, complete, referenceable.

**B3 — Whole-product gap.** The gap that stalls the crossing is almost entirely *ecosystem*, not model capability:
- **Security & data governance:** guarantees about where code goes, whether proprietary code trains a model, and tenant isolation.
- **IP / licensing indemnity:** enterprises need protection against suggestions that reproduce licensed code — several vendors responded by offering IP indemnification for enterprise tiers, precisely because it was a crossing blocker.
- **Compliance & certification:** SOC 2, and sector requirements (finance, healthcare, government/FedRAMP-style).
- **Identity & admin controls:** SSO/SAML, org-wide policy, audit logs, per-repo permissions.
- **Reliability on large legacy codebases:** the early-adopter win case (greenfield, boilerplate) is not the enterprise pain (millions of lines of existing, idiosyncratic code).
- **Vertical references:** a bank's platform team buys after peer banks vouch — not after a demo.

Note the pattern the skill predicts: the gap is **not "the model isn't smart enough."** Frontier model capability advanced dramatically over 2023–2025. The stalls are governance, indemnity, references, and integration — the whole product.

**B4 — Beachhead choice (bowling pin, not "the enterprise").** The winning move is a specific first pin, not "go enterprise." A defensible beachhead in this period looked like: *one regulated vertical or one workflow where the whole-product case can be completed and referenced* — for example, an enterprise tier hardened for security-conscious software organizations, or an agentic workflow scoped to a narrow, verifiable task (test generation, migration, code review) where correctness can be checked. Land that, reference it, then knock down the next pin.

**B5 — Whole-product plan & positioning shift.**
- *Build:* enterprise admin/security controls, IP indemnity, compliance certifications, on-prem/VPC deployment options, and audit-grade logging.
- *References:* named peer-vertical customers, not aggregate usage stats.
- *Positioning shift:* from the early-adopter pitch ("10x your speed, the future of coding") to the pragmatist pitch ("secure, compliant, governed, and proven at organizations like yours"). This is the framework's hardest interpersonal cost — the transformational story that won the visionaries actively repels the risk-averse pragmatist buyer.

## What the framework surfaces

The seductive misread through this period is that the AI-coding race is a *model-capability* race — that whoever has the smartest model crosses. The chasm lens says otherwise: PMF with developers is not PMF with enterprises, and the crossing is won by whoever first completes the **whole product** (security, indemnity, compliance, references, integration into large codebases) for a **specific beachhead** — then shifts positioning from "transformative" to "proven and safe." The AI-capex boom funds better models; it does not, by itself, close the whole-product gap that gates the mainstream. A vendor that answers stalling enterprise growth by shipping a bigger model (more features) rather than the governance-and-reference whole product is making exactly the anti-pattern this skill flags.

*Sources: Geoffrey Moore, Crossing the Chasm (1991; 3rd ed. 2014); Everett Rogers, Diffusion of Innovations (1962; 5th ed. 2003); GitHub public statements and blog on Copilot availability, adoption, and enterprise controls (2021–2025); Stack Overflow Annual Developer Survey, AI-tools sections (2023–2025); public reporting on AI-coding tools offering enterprise IP indemnification and security/compliance tiers (2023–2025). Specific figures are stated qualitatively where exact public numbers vary by reporting date.*
