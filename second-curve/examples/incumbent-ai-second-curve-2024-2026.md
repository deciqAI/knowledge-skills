# Method in Action: The Incumbent's AI Second Curve (2024–2026)

> *Example for the [second-curve](../SKILL.md) skill.*

The 2024–2026 generative-AI wave is a live, textbook second-curve moment for software incumbents. The pattern: a company whose first curve is mature, high-margin *legacy* software (licenses or seat-based SaaS) must reinvest that cash flow into an **AI-native** offering — new pricing, new architecture, new customer expectations — *before* the first curve peaks, while the AI product still cannibalizes the very seats that fund it. Microsoft's Copilot build-out is the most-documented instance and is used here as the worked case; the same audit applies to Adobe, Salesforce, ServiceNow, SAP, Intuit, and any vendor watching AI-native startups attack its core.

This walks the case through the skill's five Process steps.

---

## Step 1 — Diagnose first-curve position

Microsoft's first curve here is its productivity and cloud franchise — Windows, Office/Microsoft 365, and Azure. As of early 2026 this is best classified as **late growth / early maturity**, not decline:

- Microsoft 365 is a very large, high-margin seat-based business with deep enterprise lock-in and still-growing seats — a classic late-growth cash engine.
- Azure was still growing at strong double-digit rates through 2024–2025, but cloud is a maturing category with entrenched competitors (AWS, Google Cloud).
- The disruption signal is unambiguous: generative AI (catalyzed by OpenAI's ChatGPT launch in late 2022) created a plausible path for AI-native tools to reshape how knowledge work is done — i.e., to erode the value of the very seats Microsoft sells.

This is exactly the highest-leverage moment the skill flags: **the first curve still funds the investment, and the team can already see the need.** Waiting for the productivity franchise to actually decline would mean funding the second curve from a shrinking base.

## Step 2 — Identify candidate second curves

Candidates an incumbent in this position weighs, scored by distance from core (1 = same customers, new feature → 5 = new customers, new product, new capabilities):

- **AI copilots embedded in the existing suite** (Microsoft 365 Copilot) — *distance ~2.* Same customers, same channel, but a new value proposition (assistive generation), new per-user pricing, and a new cost structure driven by inference compute. Microsoft made this its primary bet, announcing Microsoft 365 Copilot in 2023 and reaching general availability for enterprises on 2023-11-01.
- **AI platform / infrastructure for others to build on** (Azure OpenAI Service, Azure AI) — *distance ~3.* Partly new customers (AI developers, model-consuming startups) and genuinely new capabilities (GPU-dense datacenters, model hosting). Rooted in Microsoft's multi-year, multi-billion-dollar partnership with OpenAI, first announced in 2019 and expanded in January 2023.
- **A standalone consumer AI assistant** (Copilot as a consumer product / Bing Chat, launched 2023) — *distance ~3–4.* Adjacent-to-new customers and a different competitive arena (consumer search and assistants).

The suite-embedded copilot is the load-bearing second curve because it defends and re-prices the existing franchise; the AI platform is the deeper, longer-horizon curve.

## Step 3 — Time the start

The first-curve diagnosis (late growth / early maturity) maps to the skill's rule: **start now, urgently.** Microsoft did — moving in 2023 rather than waiting. The tell that the timing was deliberate rather than reactive is that the enabling second-curve *option* pre-dated the crisis: the OpenAI partnership and Azure AI investment began in 2019, years before ChatGPT made the need obvious to everyone. As the Intel case shows, the second curve is easiest to jump to when the option was built *before* it was needed.

## Step 4 — Allocate resources

The skill caps second-curve spend at 10–20% during late-growth/early-maturity and demands a separate team, separate space, direct CEO sponsorship, and metrics measured on learning rather than near-term revenue. In the AI wave, incumbents blew past the *low* end of that band — because the enabling resource (AI compute) is capital-intensive:

- Microsoft publicly committed to very large AI/datacenter capital expenditure, stating that it was on track to invest on the order of **approximately $80 billion in AI-enabled datacenters in its fiscal year 2025** (announced early January 2025). This is the defining feature of *this* second curve versus historical ones: the reinvestment shows up as enormous capex, not just R&D headcount.
- Direct CEO sponsorship is explicit — CEO Satya Nadella repeatedly framed AI as the company's central priority, and Microsoft reorganized around AI (including creating a dedicated Microsoft AI organization in 2024).

The generalizable caution: when the second-curve resource is capex-heavy inference/training infrastructure, the "10–20%" allocation heuristic understates the check size, and the identity strain (see Step 5) is amplified by capital-market scrutiny of near-term returns.

## Step 5 — Defend against three failures

- **Success-attribution.** What tailwinds drove first-curve success that could reverse? The seat-based SaaS model assumed the *human seat* was the unit of value. If AI agents do work formerly done by seated humans, the pricing unit itself is threatened — the very success metric (seats sold) could become the thing being disrupted.
- **Resource-attachment.** What would the incumbent cut from the first curve if the second were real? The hardest version: AI features that automate work may reduce the number of paid seats. An honest audit forces the question of whether the AI offering is allowed to cannibalize the license/seat business — the skill's test of whether the second curve is treated as real.
- **Identity threat.** Can the team become a different *kind* of company — from "we sell productivity software seats" to "we sell AI capability priced on consumption/outcomes"? This is the same identity move Intel made from "memory company" to "microprocessor company." For a seat-licensing incumbent, shifting toward consumption-based, compute-driven economics is a genuine self-conception change, not a feature release.

---

## Second-Curve Audit: incumbent software vendor (AI wave, 2024–2026)

```markdown
First-curve stage: late growth / early maturity  Evidence: high-margin seat-based suite still growing; AI-native disruption signal clear
Candidates: suite-embedded AI copilot (distance ~2) / AI platform-for-others (distance ~3) / standalone consumer AI assistant (distance ~3–4)
Recommended: suite-embedded copilot (defends + re-prices core) backed by AI-platform curve
Timing: start now, urgently — option was built pre-crisis (2019 partnership)
Investment: capex-heavy (far above the 10–20% R&D heuristic); direct CEO sponsorship; dedicated AI org
Defense: success-attribution = "seat" as value unit may reverse / resource-attachment = must let AI cannibalize seats / identity = seat-licensing → consumption/compute economics
90-day actions: ship AI into the suite with its own pricing; ring-fence an AI org with learning metrics; model the seat-cannibalization case explicitly
```

## What this case teaches

**The second curve was optioned before the crisis was obvious.** Microsoft's AI infrastructure and OpenAI partnership began in 2019 — the same "build the option early" move as Intel starting microprocessors in 1971. Incumbents that had no pre-built AI option in 2022 found the jump far harder and more expensive.

**This second curve is unusually capex-intensive.** Unlike a software-only pivot, the AI second curve requires massive datacenter and compute investment (Microsoft's stated ~$80B FY2025 plan), which strains the "modest reserved allocation" heuristic and invites capital-market pressure for fast returns.

**The identity/timing tension is the crux.** The AI product can undercut the seat that funds it. Treating the second curve as *real* means letting it cannibalize the first — the exact discipline most incumbents rationalize away with "it's just a new feature." The skill's value is forcing that question before the first curve peaks, not after.

*Sources: Microsoft, "Microsoft and OpenAI extend partnership" (Jan 23, 2023, and the original 2019 announcement); Microsoft, "Announcing Microsoft 365 Copilot general availability" (Nov 1, 2023); Brad Smith / Microsoft, "The Golden Opportunity for American AI" blog stating Microsoft was on track to invest ~$80B in AI-enabled datacenters in FY2025 (Jan 3, 2025); Microsoft FY2024–FY2025 quarterly earnings materials on Microsoft Cloud and Azure growth; Grove, A. S. (1996), *Only the Paranoid Survive* (for the incumbent second-curve pattern). Figures are as publicly reported; treat forward capex and growth rates as reported intent/estimates, not audited outcomes.*
