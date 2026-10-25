---
name: ai-risk-compliance-baseline
description: "Activate when: user says 'what are our compliance risks from using AI?', 'can we feed client data into AI?', 'do we have to tell customers we use AI?', 'who owns the copyright on AI output?', 'how do we stop prompt injection?', 'a client asked how we manage AI risk', or a small team is starting to use AI tools/agents in the business and needs a minimum baseline.
  Do NOT activate when: the organization already runs a mature AI governance program with dedicated compliance staff; purely personal, non-commercial use; the question is a specific number, deadline, fine or applicability test under a named law (route it to the current text of that law and its regulator — this skill answers none of them). More: deciqai.com/s/ai-risk-compliance-baseline"
---

# AI Risk & Compliance Baseline

> **Not legal advice.** This is a baseline-practice checklist, not a legal determination for any jurisdiction. It carries no thresholds, fines, risk-classification tests, applicability criteria or effective dates — AI-specific law is being enacted, amended and phased in across jurisdictions, and every such figure expires. Verify each against the current text of the applicable law, current regulator guidance, and the vendor's current terms.


## Overview

Small teams rarely get hurt by exotic AI risk. They get hurt by basic gaps: client data pasted into a tool that may train on it, AI output reaching customers with nobody accountable for it, an agent that reads untrusted email and can also send money, vendor terms nobody read. None of these needs a governance department to prevent — they need a written inventory and a short list checked against it.

The core mechanism: **inventory every AI use → walk each one through a 7-item baseline → record a green/amber/red result per item → re-check on defined triggers.** The frameworks — NIST AI RMF and its Generative AI Profile, ISO/IEC 42001, the OWASP Top 10 for LLM Applications, the EU AI Act, GDPR, copyright-office and consumer-protection guidance — are used as comparison checklists for baseline practice, scaled to the size of the business, never as a legal conclusion.

**Runtime rule for the agent running this skill:** never state from memory a threshold, fine amount, risk tier, applicability test or effective date — not in analysis and not inside text drafted for a client or regulator. Name the governing instrument and tell the user to read its current text. Remembered figures in this domain are the most likely thing to be wrong.

Compose with: [checklist](../checklist/SKILL.md) (the baseline is a checklist; run it like one) · [ai-output-verification-trust-tiers](../ai-output-verification-trust-tiers/SKILL.md) (output-side risk) · [agent-ops-monitoring](../agent-ops-monitoring/SKILL.md) (records and incidents) · [premortem](../premortem/SKILL.md) (imagine the incident before giving an agent new permissions) · [principal-agent](../principal-agent/SKILL.md) (an AI acting for the firm is still the firm).

## When to Use

- First time an AI tool or agent is brought into a business workflow
- AI will touch client data, contracts, financials, or content published externally
- A client, partner or investor asks "how do you manage AI risk?"
- An agent is about to get a new permission (send, pay, delete, publish)

**When NOT to use:** dedicated AI governance already in place · purely personal non-commercial use · the question is a specific legal threshold or deadline (go to the current law and regulator).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user lists the AI tools in use and what they do → run The Process directly.
- **Coach mode:** user is unfamiliar → one question per step. Each [WAIT] is a hard stop — output only that step's question.

1. **What it is.** "First write down who uses which AI, what data goes in, and where the output goes — then fill the gaps item by item."
2. **Check fit.** "Does any AI here touch client data or produce anything that leaves the company?"
3. **Elicit the real case.** "List the AI tools in use, what each is used for, and the kinds of data each one sees."
> **[WAIT — do not advance until user responds]**
4. **Run steps 1–2:** walk each tool through the 7 baseline items, marking green/amber/red.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** Which items are red, who fixes each, and by when.
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** AI Use Register + Baseline Checklist

1. **Inventory.** For every AI tool/agent: purpose · users · input data types · where outputs go · whether it can take actions. *Gate: unregistered "shadow AI" use exists → register it first; stop.*
2. **Walk the 7-item baseline (green/amber/red each):**
   - **Data privacy & consent:** the purpose and consent for collecting personal data cover AI processing; handled under the applicable regime (e.g. GDPR where it applies).
   - **Confidential data:** client/trade secrets go only into tools that do not train on inputs and have data-processing terms; minimize and redact inputs.
   - **Intellectual property:** you have the right to use the inputs; the copyright status and permitted use of outputs are understood (check the relevant copyright authority's current position).
   - **Customer disclosure & claims:** disclose AI interaction or AI-generated content where the applicable rules require it (e.g. EU AI Act transparency obligations); do not overstate AI capability in marketing; treat what a customer-facing AI says as the company's own statement.
   - **Security:** untrusted content must not directly drive tool calls (prompt injection) · least privilege · no secrets in prompts · outputs are not executed directly (see OWASP Top 10 for LLM Applications).
   - **Vendor terms:** retention period, training use, sub-processors, data location, incident notification, deletion on exit — read for the tier you actually use.
   - **Record keeping:** use register, key outputs, review records and incident records are retrievable.
   *Gate: any red item touching client data or external output → pause that use until it is amber.*
3. **Assign owner and deadline.** For every red/amber item: remediation · owner · due date.
4. **Set re-checks.** Re-run immediately on a new tool, a vendor-terms change, or an incident; plus a fixed periodic review.
5. **Route every figure.** Any threshold, deadline, fine or applicability question that arises → record the governing instrument and "verify current text"; do not fill it in. *Gate: a number or date appears in the register without a cited current source → remove it.*
6. **Stop-rule:** if the AI handles only public information and nothing it produces leaves the company, compress to step 1 plus the security item.

**Output template:**
`Tool | Purpose | Data types | Output destination | Can act? | Privacy | Confidential | IP | Disclosure/claims | Security | Vendor terms | Records | Red/amber fixes + owner + due date | Next re-check`

*→ Method in Action: [Moffatt v. Air Canada — the chatbot that was "a separate legal entity" (2024)](examples/moffatt-v-air-canada-chatbot-2024.md)*

## Applying It Well

1. **Inventory before rules.** Most exposure comes from tools nobody knew were in use.
2. **Confidential data is out by default.** Exceptions are registered, not assumed.
3. **Everything external is untrusted input.** Email, web pages, uploaded files — none may steer an agent's tool calls unchecked.
4. **The bot speaks for the company.** A customer cannot be expected to know which part of your website is accurate.
5. **Frameworks are comparison lists.** Take the minimum necessary items for the business's size; do not import a governance program.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We're too small for regulators to care" | Exposure comes from clients and their data, not from company size. |
| [D] "The vendor is a big company, the terms must be fine" | Free and enterprise tiers often differ on training and retention; read the tier you use. |
| [D] "Telling customers we use AI will scare them off" | Being found out without disclosure costs more trust than disclosing. |
| [D] "Prompt injection is a big-company problem" | Any agent that reads outside content and can call tools is exposed. |
| [D] "If the bot gets it wrong, that's the bot's error" | A tribunal has already rejected that argument; the output is the company's statement. |
| [D] "I remember the deadline / fine — I'll just put it in" | Figures in this domain expire. Cite the instrument and verify the current text. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No AI use register · staff process client data on personal AI accounts · an agent can read email *and* send payments or messages · marketing says "fully automated, zero errors" · a customer-facing bot with no owner for its answers · a hard number or date in the register with no current source

## Verification

- [ ] Every AI use is registered
- [ ] All 7 baseline items marked per tool
- [ ] Red items paused, or have remediation, owner and due date
- [ ] Key vendor-term items checked and archived for the tier in use
- [ ] Re-check triggers and periodic cycle set
- [ ] No threshold, fine, tier or date answered from memory — each routed to the current instrument

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-risk-compliance-baseline** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-risk-compliance-baseline.json*
