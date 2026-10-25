# Method in Action: Mata v. Avianca — The Fabricated Citations (2023)

> *Example for the [ai-output-verification-trust-tiers](../SKILL.md) skill.*

A worked example of a high-cost, easily verifiable AI output released with no verification at all — documented in Judge P. Kevin Castel's *Opinion and Order on Sanctions*, U.S. District Court for the Southern District of New York, June 22, 2023 (22-cv-1461 (PKC), ECF 54). Every fact below is from the court's findings. The case is useful because nearly every fake move in this skill's rationalization table appears in the record.

**The setup.** Roberto Mata sued Avianca over a knee injury from a serving cart on a flight. Avianca moved to dismiss the claims as time-barred under the Montreal Convention. On March 1, 2023, plaintiff's counsel filed an "Affirmation in Opposition" that "cited and quoted from purported judicial decisions that were said to be published in the Federal Reporter, the Federal Supplement and Westlaw." The research had been done by an attorney who turned to ChatGPT because the firm's research service had limited access to federal cases; he testified he "falsely assumed" ChatGPT "was like a super search engine." The court found that the "Varghese," "Shaboon," "Petersen," "Martinez," "Durden" and "Miller" opinions did not exist.

**What happened next.** Avianca's March 15 brief questioned whether the cases existed. The court issued orders on April 11 and 12 requiring their production. The court found that counsel "doubled down and did not begin to dribble out the truth until May 25." It found bad faith on the part of the individual attorneys, imposed a **$5,000 penalty** jointly and severally on them and their firm, and ordered them to send letters to their client and to each judge falsely identified as the author of a fake opinion.

The court was explicit that the tool was not the problem: "there is nothing inherently improper about using a reliable artificial intelligence tool for assistance. But existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings."

## Running the Process

1. **List output types.** One type: *case citations and quotations in a court filing*. Specific, not "the AI's answers."

2. **Score two dimensions.** Error cost: **high** — sanctions, client harm, harm to the court and to the judges named as authors of fake opinions. Verifiability: **high** — every citation can be pulled from a reporter or a legal database in minutes.

3. **Assign the tier.** High cost → at least **T3 (every item reviewed before release)**. Signing and filing an affirmation under penalty of perjury is an external commitment a human must execute (T4 for the act of filing). The AI's role is draft-only.

4. **Verification method.** *Source check* — open every cited opinion in the original. The record shows the method that was used instead: the signing attorney "reviewed the affirmation for style," looking "for a flow, make sure there was nothing untoward or no large grammatical errors," and "did not review any judicial authorities cited." That is the rationalization "a human looked at it" — re-reading prose is not checking evidence.

5. **Evidence requirement.** Each citation needs the opinion itself attached or located. Instead, the drafting attorney asked ChatGPT "Is Varghese a real case" and "Are the other cases you provided fake"; ChatGPT "responded that it had supplied 'real' authorities that could be found through Westlaw, LexisNexis and the Federal Reporter." That is the rationalization "I asked the AI whether it was sure" — self-confirmation by the same system that produced the error. *Gate: no source = unverified.*

6. **Escalation.** Two textbook triggers fired: the opposing party disputed the output (March 15), then the court ordered production (April 11–12). Under this skill, either one moves the output to immediate source verification by a named reviewer. The court's own framing is that the record "would look quite different" had counsel come clean after either point.

7. **Re-tier with data.** The firm's research process had one known weakness — limited federal-case access — that pushed the work to an unverified tool. Pulling any one of the six disputed opinions from a reporter would have exposed the fabrication, and that single result should have moved the output type to the top tier permanently. (The court found that several citations pointed to real reporter pages occupied by different cases — exactly what a source check catches and a style read does not.)

## The mapped steps

1. Output type: case citations in a court filing
2. Error cost high; verifiability high
3. Tier: T3 for the content, T4 for filing — AI as drafter only
4. Method used: style read for "flow"; method required: open each opinion
5. Evidence: the model was asked to vouch for itself; no source was retrieved
6. Escalation: two triggers (opponent's brief, court orders) ignored
7. Outcome: bad-faith finding, $5,000 penalty, letters to the client and to the judges named

**The lesson.** The cheapest possible check — opening the cited source — was available the whole time. The failure was not the AI; it was a high-cost output given the verification of a low-cost one, and an escalation signal treated as noise.

Primary source: *Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC), Opinion and Order on Sanctions (S.D.N.Y. June 22, 2023), ECF 54, 678 F. Supp. 3d 443. https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54/ · Docket: https://www.courtlistener.com/docket/63107798/mata-v-avianca-inc/
