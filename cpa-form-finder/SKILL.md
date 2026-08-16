---
name: cpa-form-finder
description: "Activate when: scoping or quoting a new tax engagement; a client describes a transaction and you need to place it; building a document request list; sanity-checking that a return has the schedules its facts imply; user says 'what forms does this need', 'which schedule', 'what do I file for', 'is there a form for', 'what filings am I forgetting?'. Do NOT activate when: the forms are known and the question is how to complete a line; the return is already prepared and the question is whether it is right (use cpa-return-review instead); the question is a threshold, limit, rate, or filing date — those are not in this skill and must come from current guidance. More: deciqai.com/s/cpa-form-finder"
---

# CPA — Form Finder

> **Not legal or tax advice.** This maps situations to form *families* only. No thresholds, limits, rates, phase-outs, eligibility tests or dates appear here — all of them expire. Verify against current IRS instructions for the applicable year and the relevant state authority.

**Activate when:** scoping, quoting, or building a document request; a client describes something you want to place quickly; checking that a prepared return has the schedules its facts imply.
**Do NOT activate when:** the question is a number, a limit, or a deadline; the return is already prepared and the question is whether it is right — that is [cpa-return-review].

## Why this skill

A client says "I sold some crypto, my wife started consulting, and we have a rental in another state." In that sentence are six forms, two states, and three questions you need answered before you can quote the job.

The output of this skill is always **two lists** — forms likely in scope, and what you still have to determine. The second is the more useful one. A form list without its open questions reads as a conclusion, and it is not one.

## Process

**1. Decompose.** Clients describe their year as a story; forms attach to events. For each element capture: what happened or what status holds · type (income / deduction / credit / information reporting / election / status) · which taxpayer or entity · timing, including whether it spans years · **jurisdiction**.

*Gate: ask about location for every element, separately. The most common scoping error is a missed jurisdiction, not a missed form — a rental elsewhere, months of remote work, a mid-year move, an owner living in a different state from the entity. Each can add a filing nobody priced.*

**2. Map to form families.**

**Form 1040 and schedules** — Schedule 1 (additional income and adjustments) · Schedule 2 (additional taxes) · Schedule 3 (additional credits) · Schedule A (itemized) · Schedule B (interest and dividends) · Schedule C (sole proprietorship) · Schedule D with Form 8949 (capital asset sales, including digital assets) · Schedule E (rental, royalty, pass-through) · Schedule F (farming) · Schedule H (household employees) · Schedule SE (self-employment) · Schedule 8812 (qualifying children and other dependents).

**Entity returns** — 1120-S with Schedule K-1 · 1065 with Schedule K-1 · 1120 · 1041 with Schedule K-1 · 990 series · single-member LLC on the owner's return by default.

**Event families**

| Event | Examine |
|---|---|
| Sale or exchange of property | Form 8949 and Schedule D; Form 4797 where business property is involved |
| Consideration received across more than one year | Form 6252 |
| Depreciable asset placed in service | Form 4562 |
| Business use of a home (Schedule C filers) | Form 8829 |
| Like-kind exchange of real property | Form 8824 |
| Sale of a principal residence | Schedule D and Form 8949, subject to exclusion rules |
| Retirement distribution or rollover | Reported on 1040; Form 5329 where additional taxes may apply |
| Roth conversion or nondeductible contributions | Form 8606 |
| Health savings account activity | Form 8889 |
| Education expenses | Form 8863; Form 1098-T as source |
| Child and dependent care | Form 2441 |
| Energy-related property | Form 5695 and related credit forms |
| Casualty or theft loss | Form 4684 |
| Noncash charitable contribution | Form 8283; appraisal requirements scale with value — verify against current instructions |
| Gifts to individuals during the year | Form 709, on its own filing schedule separate from the income tax return |
| Paid preparer claiming EITC, CTC/ACTC/ODC, AOTC, or head-of-household | Form 8867, one per covered credit — a per-return penalty gate, not a formality |
| Net operating loss (non-corporate) | Form 172 and carryover schedules |
| Passive activity involvement | Form 8582 |
| At-risk limitations | Form 6198 |
| Qualified business income | Form 8995 or 8995-A |
| S corp shareholder claiming a loss, taking a distribution, disposing of stock, or receiving a loan repayment | Form 7203, attached to that shareholder's return |
| Pass-through with international items | Schedules K-2 and K-3 |
| Alternative minimum tax exposure | Form 6251 |
| Underpayment of estimated tax | Form 2210 |
| Estimated payments during the year | Form 1040-ES |
| Payment card / third-party network receipts | Form 1099-K as source — **reconcile to** gross receipts, do not add on top |
| Extension of time to file | Form 4868 (individual), Form 7004 (business) |
| Amending a filed return | Form 1040-X, or amended entity return |
| Employment taxes | Forms 941 or 944, Form 940, annual W-2 and W-3 |
| Payments to non-employees | Form 1099-NEC; other 1099 series by payment type |
| Change of accounting method | Form 3115 |
| Entity classification election | Form 8832 |
| S corporation election | Form 2553 |
| Power of attorney | Form 2848 |

**Cross-border** — anything foreign expands scope sharply and carries reporting separate from the income tax return. The most commonly missed and most heavily penalized area in a small-firm practice.

FBAR (FinCEN Form 114) · Form 8938 · Form 1116 or 1118 · Form 2555 · Form 5471 · Form 5472 · Form 8865 · Form 8621 · Forms 3520 and 3520-A · Form 1040-NR · treaty position on Form 8833.

*Gate: FBAR is filed with FinCEN, not with the return, on its own schedule. Name it as a separate deliverable in the engagement letter or it gets missed.*

Two habits that catch most of what is otherwise missed:
- **Schedule B carries foreign account and foreign trust questions.** The cheapest foreign-reporting screen available, sitting on a schedule you are already completing. Do not let software default them.
- **Ask about foreign accounts by function, not by name.** Clients do not think of a foreign pension, a foreign policy with cash value, a brokerage account left behind after emigrating, or signature authority over an employer's or relative's account as "a foreign financial account." Ask what they can sign for, not what they own.

**State and local** — no general mapping exists; every state differs. What is portable is the **trigger list**, and clients volunteer none of it: residence during the year and any move date · physical presence for work in another state, including short stays · remote work from a different state than the employer · property owned, rented out, or sold elsewhere · business activity, customers, employees, contractors or inventory in other states · pass-through ownership where the entity operates elsewhere · entity formed in one state, operating in another · local income taxes at city, county or district level.

Every "yes" is a potential filing, a potential apportionment question, and a fee the quote did not include.

**3. Produce the two lists.**

```
LIKELY IN SCOPE   form — because [the specific fact that puts it in scope]
TO DETERMINE      question — because [what it changes]
                  verify against current guidance: [thresholds/dates/eligibility at issue]
JURISDICTIONS     federal + [states] + [foreign], each with its triggering fact
NOT ADDRESSED     valuations, elections requiring analysis, positions requiring research
```

*Gate: never present LIKELY IN SCOPE alone.*

**4. Convert to a document request.** Each form implies source documents; that mapping bridges scoping to the chase. Working backwards also catches gaps — if a form is in scope and you cannot name the document that will support it, either the form does not belong or you have found a real question for the client.

## Worked example

New client, one sentence: "I moved to Texas in June, sold my old house, and I do consulting."

Decomposed, the sentence carries a part-year residency in the origin state, a principal-residence sale, and a Schedule C. Forms are easy — the scoping value was elsewhere.

Asking about location per element produced two facts the client had not connected to tax: the consulting had two clients in a third state, and the old house had been rented for four months before sale. That added a state exposure question and converted the sale from one analysis into two — a period of rental use inside the ownership period.

**The forms were never the hard part. The jurisdiction question asked element by element was.** A quote built from the client's sentence would have been wrong by two filings.

## Compliance anchors

Circular 230 §10.22 (due diligence), §10.34 · AICPA SSTS §2.2 (tax return questions) · IRC §6694 · engagement letter scope, which is where unpriced state filings become disputes.

## Packs

- **Solo:** run it before quoting, not after. The two-list output is the quote's scope section.
- **Firm:** the TO DETERMINE list becomes the new-client intake questionnaire; jurisdiction triggers asked as a standing block on every engagement, not only new ones.

## Red flags

- A form list was produced without a jurisdiction question per element.
- Anything foreign appeared and the engagement letter did not change.
- The client "doesn't have anything overseas" but has lived or worked abroad.
- An entity's state of formation was assumed to be its state of operation.
- The TO DETERMINE list came back empty. On a real engagement, it never is.
- Someone quoted from the client's description without seeing prior-year returns.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| [O] "It's a simple return." | Simple describes the forms you know about. Simplicity is a conclusion of scoping, not an input. |
| [D] "They'd have told me if they had foreign accounts." | They do not classify a foreign pension or signature authority as an account. Ask by function. |
| [O] "One state — they only live in one place." | Residence is one trigger of eight. Property, remote work, customers and pass-through operations are the others. |
| [O] "I'll figure out the state part later." | Later is after the fee was quoted. State filings are where scoping errors turn into unbillable work. |
| [D] "The software will prompt for what's needed." | Software prompts on data entered. It cannot prompt on a state you never asked about. |

## Verification

- [ ] Situation decomposed into discrete elements, not treated as one narrative
- [ ] Jurisdiction asked separately for every element
- [ ] Foreign screen run by function, not by the client's own labels
- [ ] State trigger list run in full
- [ ] Both lists produced; TO DETERMINE is non-empty
- [ ] Every in-scope form has a named supporting document
- [ ] Engagement letter and fee reflect the jurisdictions found
- [ ] Every threshold, date and eligibility question routed to current guidance, not answered from memory

Related: [mece] for decomposing the situation without overlap or gaps · [cpa-doc-chase] for turning the form list into a request · [cpa-return-review] for checking the prepared return carries the schedules its facts imply · [tax-prep-8867-due-diligence] once a covered credit or head-of-household lands in scope · [estimated-tax-safety-buffer] once Form 1040-ES does.

---

*Part of **deciqAI Knowledge Skills** — 237 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/cpa-form-finder** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/cpa-form-finder.json*
