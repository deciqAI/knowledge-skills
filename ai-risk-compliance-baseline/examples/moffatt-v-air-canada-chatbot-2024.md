# Method in Action: Moffatt v. Air Canada — The Chatbot That Was "a Separate Legal Entity" (2024)

> *Example for the [ai-risk-compliance-baseline](../SKILL.md) skill.*

A small-claims decision with a small award became one of the most cited AI-liability cases of 2024, because it answered a question every team deploying a customer-facing bot eventually faces: *when the AI says something wrong, whose statement is it?* The decision is *Moffatt v. Air Canada*, 2024 BCCRT 149, issued by the British Columbia Civil Resolution Tribunal (member Christopher C. Rivers) on February 14, 2024.

**What happened.** After his grandmother died in November 2022, Jake Moffatt used the support chatbot on Air Canada's website to ask about bereavement fares. The chatbot told him (per the screenshot he provided): "If you need to travel immediately or have already travelled and would like to submit your ticket for a reduced bereavement rate, kindly do so within 90 days of the date your ticket was issued by completing our Ticket Refund Application form." He bought full-fare tickets on that basis. Air Canada refused the partial refund: a separate "Bereavement travel" page — which the chatbot itself had hyperlinked — said the policy did not apply after travel was completed.

An Air Canada representative admitted the chatbot had provided "misleading words" and said the issue had been noted so the chatbot could be updated. Moffatt filed a claim.

**The airline's defence, and the tribunal's answer.** Air Canada argued it could not be held liable for information from one of its "agents, servants or representatives — including a chatbot," and that the chatbot was "a separate legal entity that is responsible for its own actions." The tribunal:

> "This is a remarkable submission. While a chatbot has an interactive component, it is still just a part of Air Canada's website. It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot."

> "I find Air Canada did not take reasonable care to ensure its chatbot was accurate."

> "There is no reason why Mr. Moffatt should know that one section of Air Canada's webpage is accurate, and another is not."

Air Canada was found liable for negligent misrepresentation and ordered to pay about CA$812 in total — the fare difference plus interest and tribunal fees.

Now run the **Baseline Checklist** on the deployment as the decision describes it. (The decision does not describe Air Canada's internal governance; the walk-through marks what the public record shows and flags what it cannot.)

**1. Inventory.** Tool: customer-facing support chatbot. Purpose: answer policy questions. Input: customer questions plus the airline's policy content. **Output destination: directly to the public.** Can act: it does not issue refunds, but it makes statements customers rely on when spending money — functionally a commitment. A register entry written this way flags the use as high-exposure on day one: external output, reliance, money.

**2. Baseline items.**

- **Data privacy & consent:** not at issue in the decision. **Not assessable.**
- **Confidential data:** not at issue. **Not assessable.**
- **Intellectual property:** not at issue. **Not assessable.**
- **Customer disclosure & claims — RED.** This is the item the case turns on. The question is not only *whether* customers know they are talking to a bot, but whether the company treats the bot's words as its own. Air Canada's litigation position — that the bot was a separate entity — is the opposite of the baseline principle "treat what a customer-facing AI says as the company's own statement." The tribunal held exactly that principle. The bot's answer also contradicted a page it linked to: two company sources, inconsistent, with the customer left to guess which was authoritative.
- **Security:** no injection or permission issue alleged. **Not at issue.**
- **Vendor terms:** the decision does not discuss who built the chatbot. **Not assessable** — but note the general rule the case implies: whoever built it, the deploying company owns the output.
- **Record keeping — AMBER at best.** The decisive record of what the bot said was the *customer's* screenshot. A baseline register would keep the company's own record of key outputs, so it is never relying on the other side's evidence to know what its system told a customer.

*Gate check:* a red item touching external output → **that use pauses until the item is amber.** Concretely: policy answers involving money or eligibility either quote the authoritative policy text verbatim, or route to a human, until accuracy against the policy source is checked.

**3. Owner and deadline.** The representative's reply — "noted the issue so it could update the chatbot" — is a remediation with no visible owner or date. The baseline turns it into: remediation (align bot answers with the bereavement policy page; test against it), owner, due date.

**4. Re-checks.** Policy pages change; the bot must be re-checked whenever the policy source it answers from changes. That trigger belongs in the register.

**5. Route every figure.** The 90-day window in the case is a *quote of what the bot said*, not a rule to reuse. Applied forward, the same discipline applies to the deployer's own obligations: whether and how a bot must disclose that it is AI, and what liability attaches, depends on the jurisdiction's current law — record the instrument, verify the current text, do not fill it in from memory.

### The mapped steps

1. **Inventory:** customer-facing chatbot; output goes to the public; customers rely on it for money decisions
2. **Baseline:** disclosure & claims **red** (company disowned bot output; bot contradicted its own linked page); records **amber** (only the customer had the transcript); others not at issue
3. **Owner/deadline:** "noted the issue" had neither
4. **Re-check trigger:** any change to the policy source the bot answers from
5. **Figures:** case facts are not rules; jurisdictional duties routed to current law

**The lesson.** The cheapest control in the baseline — writing down that a customer-facing AI speaks for the company, and keeping your own record of what it says — would have put this use in red before launch. The tribunal's reasoning is the baseline's reasoning: a customer cannot be expected to know which part of your website is accurate, and the interactive part is still your website.

*Primary source: Moffatt v. Air Canada, 2024 BCCRT 149 (B.C. Civil Resolution Tribunal, February 14, 2024), https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do (also indexed on CanLII as 2024 BCCRT 149). Quotations from the decision as reported verbatim by CBC News, Jason Proctor, "Air Canada found liable for chatbot's bad advice on plane tickets," February 15, 2024, https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416 ; corroborated by the American Bar Association, Business Law Today, February 29, 2024, https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ .*
