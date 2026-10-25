# Method in Action: Moffatt v. Air Canada — A Customer-Facing Chatbot at the Wrong Autonomy Level (2022–2024)

> *Example for the [agent-delegability-assessment](../SKILL.md) skill.*

The facts here come from the tribunal's written reasons: *Moffatt v. Air Canada*, 2024 BCCRT 149, British Columbia Civil Resolution Tribunal, issued February 14, 2024. The decision does not describe how Air Canada configured its chatbot. Air Canada "did not provide any information about the nature of its chatbot" (para. 14). The scoring below is therefore this skill's reconstruction from the record, and is labeled that way.

**What happened.** On November 11, 2022, after his grandmother died, Jake Moffatt asked the support chatbot on Air Canada's website about bereavement fares. The parties agreed he "was not chatting with an Air Canada employee." The chatbot's reply, quoted in the decision, said in part: "If you need to travel immediately or have already travelled and would like to submit your ticket for a reduced bereavement rate, kindly do so within 90 days of the date your ticket was issued." The words "bereavement fares" linked to Air Canada's own "Bereavement travel" page, which said the policy "does not apply to requests for bereavement consideration after travel has been completed" (paras. 15–17).

Relying on the chatbot, Moffatt bought two full-fare tickets and applied for the partial refund within the 90 days. Air Canada refused. In February 2023 an Air Canada representative admitted the chatbot had provided "misleading words" and said the issue had been noted "so it could update the chatbot" (para. 22).

**The defense and the ruling.** Air Canada argued it could not be held liable for information provided by "one of its agents, servants, or representatives – including a chatbot." The tribunal called this "a remarkable submission": "While a chatbot has an interactive component, it is still just a part of Air Canada's website… It makes no difference whether the information comes from a static page or a chatbot." It found Air Canada "did not take reasonable care to ensure its chatbot was accurate." It also rejected the argument that the customer should have checked the other page: there was no reason he "should know that one section of Air Canada's webpage is accurate, and another is not" (paras. 27–29). Air Canada was ordered to pay $812.02 (damages of $650.88, plus interest and fees) (para. 44).

**Run the Process on the task "answer customer questions about fare policy".**

1. **Decompose.** Input: a customer's policy question. Output: a statement of policy the customer will act on. This is not "chat". It is an **external commitment on behalf of the company**, and that is what the tribunal treated it as.
2. **Score six dimensions (reconstruction).**
   - Frequency: high (a public support channel).
   - Rule clarity: high. The policy existed in writing on the linked page.
   - Data access: available. The correct page was linked from the answer itself.
   - Cost of error: low per case in dollars (an $812.02 order here), but each wrong answer becomes a commitment the company can be held to.
   - Reversibility: low. The customer bought tickets on the strength of the answer before anyone could correct it.
   - Verifiability: low from the recipient's side. The tribunal said a customer cannot be expected to double-check one part of a website against another. No internal check happened before the answer reached him.
3. **Assign a level.** Two caps fire. "High cost of error **and** irreversible → max L2" applies to any statement the customer will act on, and "low verifiability → max L2" applies whatever the other scores. In practice the chatbot ran at L4: it answered alone, in real time, with no gate. The high frequency and clear written rules are exactly the scores that make L4 *look* safe on a demo, and the skill's caps are designed to override them.
4. **Attach gates (what L2 would mean here).** Real-time human approval of every chat is impractical. The skill's other moves fit instead. Split the task: plain informational answers become their own task, constrained to quote the canonical policy text. Anything that promises money, eligibility or an exception goes to a human or carries an explicit "submit for review" handoff. That turns the irreversible part into a gated L2 step and leaves the high-volume part at L3.
5. **Set promotion and demotion rules.** The February 2023 admission ("misleading words") was a demotion trigger: a confirmed wrong policy statement. The rule would demote policy answers one level until the fix was verified.
6. **Stop-rule check.** The task is valuable (high volume, real deflection), so the answer is to restructure the gates, not to keep it manual.

**The lesson.** The tribunal's reasoning restates two of this skill's principles in legal terms. First, delegating the work does not delegate the accountability: the agent "is still just a part of" the company. Second, verifiability must be scored from the recipient's side, because the person relying on the answer cannot be expected to audit it.

Primary sources:
- *Moffatt v. Air Canada*, 2024 BCCRT 149, Civil Resolution Tribunal of British Columbia, reasons for decision issued February 14, 2024 (Tribunal Member Christopher C. Rivers). https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do
- Corroborating summary: American Bar Association, *Business Law Today*, "BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot," February 2024. https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
