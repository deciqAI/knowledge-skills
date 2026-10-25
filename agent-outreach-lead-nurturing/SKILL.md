---
name: agent-outreach-lead-nurturing
description: "Activate when: user says 'use an AI agent for outreach / cold email', 'automate lead follow-up', 'multi-touch nurture sequence', 'personalized prospecting emails', asks 'how do we let the agent send email without it looking like spam?', or is designing an agent-driven outbound and lead-nurturing process.
  Do NOT activate when: sending newsletters to existing subscribers (ordinary email marketing); there is no defined ICP; compliance preconditions for the target region or channel are not met (e.g., no lawful basis for the personal data). More: deciqai.com/s/agent-outreach-lead-nurturing"
---

# Agent Outreach & Lead Nurturing

> **Guidance, not professional advice.** No legal, tax, financial or regulatory advice; verify anything jurisdiction- or rate-dependent against current authority. The professional who acts owns the decision.

## Overview

AI agents can research every prospect before writing to them, at close to the cost of a mass blast. The same agents make it just as cheap to **send spam at scale**, which damages domain reputation and the brand. Optimizing for send volume brings low reply rates and rising complaints. Then the domain lands on blocklists, and even normal email starts going to spam.

Core mechanism: **precise ICP × trigger signal × sourced personalization × human approval gate × compliance and deliverability discipline.** The agent researches and drafts. A human approves. A message goes out only when a signal says *why now*, and every send follows the rules.

The rules are concrete and they apply to B2B. The U.S. FTC's CAN-SPAM guidance states the law "makes no exception for business-to-business email." Gmail and Yahoo require authenticated mail and one-click unsubscribe from bulk senders. Under the GDPR, a recipient may object to direct marketing "at any time."

Compose with [jobs-to-be-done](../jobs-to-be-done/SKILL.md) (find the real pain) · [reciprocity](../reciprocity/SKILL.md) (give value first) · [agent-ops-monitoring](../agent-ops-monitoring/SKILL.md) (watch what the agent actually sends) · [agent-delegability-assessment](../agent-delegability-assessment/SKILL.md) (outbound sends are an irreversible action; gate them).

## When to Use

- A clear ICP exists and outreach must scale from manual to hundreds per week while staying personal
- Inbound leads go unanswered or follow-up cadence is chaotic
- An agent already sends email, but reply rates are low and bounces or complaints are rising

**When NOT to use:** ICP undefined · demand for the product not yet validated · you cannot provide a working unsubscribe and a real sender identity.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has an ICP and a lead source → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** "The agent researches and drafts; a human approves. Send only when the signal is right, and follow the rules when you send."
2. **Check fit.** "Can you say who needs you, at what moment, and why?"
3. **Elicit the real case.** "Your target customer profile, one buying-trigger signal, and the first piece of value you can give."
> **[WAIT — do not advance until user responds]**
4. **Run The Process.** Draft one trigger-signal rule and one sourced, personalized first email. Mark the source behind every personalized sentence.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** "The value of personalization is *why now*, not inserting their name."

## The Process

**Output:** Outreach Spec (ICP / signals / sequence / gates / compliance / metrics)

1. **ICP + exclusion list.** Industry, size, role, tech stack. List who is off-limits: current customers, competitors, restricted regions, anyone who has opted out on any channel. *Gate: the ICP can be written as an executable filter → otherwise stop.*
2. **Trigger signals.** Define public "contact now" signals: hiring for a role, a funding round, a product launch, a technology change, an active site visit. *Gate: each signal's source can be verified by the agent → otherwise drop it.*
3. **Sourced personalization.** The agent researches public information. The first sentence links the signal to the prospect's likely pain. Every personalized claim carries a source link. *Gate: delete any personalization without a source; never invent facts or relationships.*
4. **Sequence design.** 3–5 touches across email, LinkedIn and content. Each touch adds new value (a case, a checklist, a diagnostic), never another "just following up." Set a maximum total duration. *Gate: every touch has standalone value → otherwise merge or cut it.*
5. **Human approval gate.** A human reviews new sequences, new segments, the first batch, and high-value accounts. Lower the spot-check rate only as quality stays stable. *Gate: an unapproved template is never sent.*
6. **Compliance and deliverability.** U.S. CAN-SPAM: accurate header and sender identity, non-deceptive subject line, valid physical postal address, a clear opt-out honored promptly, and responsibility that stays with you even when a vendor sends. EU/UK: a confirmed lawful basis (legitimate interests for B2B requires an assessment) and the UK PECR rules (sole traders and some partnerships count as individuals; named work addresses at companies still carry data-protection duties). Mailbox providers: SPF, DKIM and DMARC authentication; one-click unsubscribe (RFC 8058) for bulk sends; complaint-rate and volume limits; warm up new domains. Pull current thresholds and deadlines from the live regulator and provider pages; never state them from memory. *Gate: any item unmet → stop sending.*
7. **Reply handling.** The agent classifies replies: interested / later / no / unsubscribe / referral / auto-reply. "No" and "unsubscribe" stop **all channels** immediately. "Interested" goes to a human within an agreed time.
8. **Metrics and iteration.** Track positive-reply rate, meetings, complaint rate, bounce rate and unsubscribe rate, split by signal and segment. **Stop-rule:** complaints or bounces cross the pause threshold → pause all sequences and return to steps 1–3.

**Output template:**
`Segment | Trigger signal | Personalization source (link) | Touches 1–5 (channel/value) | Approver | Compliance check | Positive-reply % | Complaint % | Next step`

*→ Method in Action: [United States v. Verkada — 30 million prospecting emails and the largest CAN-SPAM penalty (2024)](examples/verkada-can-spam-settlement-2024.md)*

## Applying It Well

1. **Fewer and precise beats many and generic.** Send when the signal fires.
2. **Unsubscribes and refusals are hard stops,** not a cue to "try another channel."
3. **Feed every reply back into the ICP and the signals,** not only into the copy.
4. **You own what your agent sends.** CAN-SPAM holds both the promoted company and the sender responsible. Outsourcing the sending does not outsource the liability.
5. **Report the honest metrics.** Positive replies, complaints and bounces, not sends and opens.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Merge-field name and company is personalization" | Recipients can spot a template. Personalization has to answer *why now*. |
| [D] "Send enough and someone will reply" | Rising complaints drag down deliverability for the whole domain. |
| [D] "B2B isn't covered by GDPR / CAN-SPAM" | A named work address (firstname.lastname@company) can be personal data, which the UK ICO flags for B2B email. CAN-SPAM "makes no exception for business-to-business email." |
| [D] "The agent is good enough, no human review" | One invented fact or offensive line damages the brand. Gates come before scale. |
| [D] "The opt-out link is in the template, so we comply" | It has to *work* and be honored across every list and tool. Verkada's alleged violations included not honoring unsubscribe requests. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Personalization with no source · an unsubscribed contact reached on another channel · reporting only sends and opens · bulk sends on day one of a new domain · no exclusion list · no postal address in the footer

## Verification

- [ ] ICP and exclusion list are executable filters
- [ ] Every personalized claim has a source link
- [ ] Approval gate decisions are logged
- [ ] Authentication, unsubscribe (tested end-to-end), postal address and lawful basis checked against current official pages
- [ ] Metrics include complaint and bounce rates with a pause threshold set
- [ ] No regulatory threshold, penalty amount or deadline in any draft was supplied from memory

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/agent-outreach-lead-nurturing** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/agent-outreach-lead-nurturing.json*
