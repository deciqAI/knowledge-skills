# Method in Action: United States v. Verkada — 30 Million Prospecting Emails and the Largest CAN-SPAM Penalty (2024)

> *Example for the [agent-outreach-lead-nurturing](../SKILL.md) skill.*

This is not an AI-agent case. The conduct dates from 2019–2021. It is included because it is the clearest public record of what happens when B2B outbound scales faster than its compliance plumbing, and that is the risk an agent multiplies. Facts come from the FTC's August 30, 2024 press release and Verkada's own statement the same day. The claims are **allegations**: Verkada settled without agreeing with them, and its statement says, "We do not agree with the FTC's allegations."

**What was alleged.** Verkada, a California company selling cloud-connected security cameras to organizations, "relied on commercial email campaigns to help market its products, sending more than 30 million commercial emails over a three-year period." The Department of Justice filed the complaint on referral from the FTC. It alleged that Verkada violated the CAN-SPAM Act "by flooding prospective customers with a barrage of commercial emails and failing to include the option to unsubscribe or opt-out, honor opt-out requests, and provide a physical postal address in the emails." Per the FTC, the emails violated the Act "in four ways, including not honoring email recipients' requests to unsubscribe."

**The outcome.** Under the stipulated order, Verkada agreed to pay a **$2.95 million** civil penalty, which the FTC called "the largest penalty obtained by the FTC for a CAN-SPAM violation." The order also prohibits future CAN-SPAM violations. The same action covered separate data-security and undisclosed-review allegations, which are outside this skill's scope.

**The company's account.** Verkada said the FTC "investigated the marketing emails we sent to businesses and other organizations from 2019 to 2021" and claimed it "did not follow certain CAN-SPAM Act requirements (such as the requisite language in email footers and certain opt-out protocols)." Its stated remediation: tools to facilitate compliance, "a dedicated webpage where customers can control their email preferences," and a "mandated… standardized email footer that always includes a physical address and a link to the webpage."

**Run the Process against the record.**

1. **ICP + exclusion list.** The recipients were "prospective customers", so this was classic outbound. The exclusion list must include everyone who has opted out, synced across every sending tool. The alleged failure to honor opt-outs is an exclusion-list failure as much as a footer failure.
2. **Trigger signals.** The record describes volume ("a barrage"), not signals. The skill's rule (send when a verifiable signal fires) is the structural check on barrage-style volume.
3. **Sourced personalization.** Not addressed in the record.
4. **Sequence design.** Thirty million emails over three years with a capped, value-per-touch sequence is hard to square with the skill's "set a maximum total duration" gate. The record does not show sequence design, so this remains an inference.
5. **Human approval gate.** A standardized, mandated footer is what a template-approval gate produces. Verkada's own remediation was to put one in place. In the skill, no template is sent until it carries the required elements.
6. **Compliance and deliverability.** The three named failures line up with items on the FTC's compliance checklist: a clear opt-out mechanism, honoring opt-outs promptly, and a valid physical postal address. The FTC guide also says the law "makes no exception for business-to-business email." Selling to organizations rather than consumers was no shield.
7. **Reply handling.** "Unsubscribe" must stop all channels immediately. An opt-out that is offered but not processed is the exact failure alleged.
8. **Metrics and stop-rule.** A program reporting only sends would not surface unprocessed opt-outs. A program tracking unsubscribe-processing and complaint rates against a pause threshold would.

**Why it matters more with agents.** An agent can draft and send at many times a human team's rate, so every gap in steps 1, 5, 6 and 7 compounds faster. CAN-SPAM's guide is explicit that "you can't contract away your legal responsibility." That applies equally when the sender is a vendor's tool or your own agent.

Primary sources:
- U.S. Federal Trade Commission, "FTC Takes Action Against Security Camera Firm Verkada over Charges it Failed to Secure Videos, Other Personal Data and Violated CAN-SPAM Act," press release, August 30, 2024. https://www.ftc.gov/news-events/news/press-releases/2024/08/ftc-takes-action-against-security-camera-firm-verkada-over-charges-it-failed-secure-videos-other
- Verkada, "FTC Settlement: Explained," August 30, 2024 (the company's account and stated remediation). https://www.verkada.com/blog/ftc-settlement-explained/
- U.S. Federal Trade Commission, "CAN-SPAM Act: A Compliance Guide for Business." https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
