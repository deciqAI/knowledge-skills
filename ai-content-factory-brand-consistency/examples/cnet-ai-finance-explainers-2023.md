# Method in Action: CNET's AI-Written Finance Explainers (2022–2023)

> *Example for the [ai-content-factory-brand-consistency](../SKILL.md) skill.*

A worked example of a content factory that had a human editor on every piece and still shipped errors in more than half of its output — documented in CNET's own editor's note of January 25, 2023, and in contemporaneous reporting by *The Verge*. It shows why "a human reviewed it" is not a gate, and why the riskiest content was the content treated as routine.

**The setup.** In November 2022, CNET's CNET Money team began a test using "an internally designed AI engine – not ChatGPT" to help editors produce "a set of basic explainers around financial services topics." It published **77 short stories** with the tool, "about 1% of the total content published on our site during the same period." Per CNET's own description, "editors generated the outlines for the stories first, then expanded, added to and edited the AI drafts before publishing," and "every one of our articles is reviewed and modified by a human editor."

**The break.** In January 2023, *Futurism* reported that CNET had been publishing AI-written articles without a formal announcement, and in a follow-up flagged errors in a CNET explainer on compound interest, which received a lengthy correction (as summarized by *The Verge*). CNET then audited the whole set. *The Verge* reported that CNET **issued corrections on 41 of the 77 stories**, including "What Is Compound Interest?" and "How Much Should You Keep in a CD?"; some corrections read "We've replaced phrases that were not entirely original." CNET's editor-in-chief wrote that the audit found "a small number requiring substantial correction and several stories with minor issues such as incomplete company names, transposed numbers or language that our senior editors viewed as vague," and that the plagiarism checker "either wasn't properly used by the editor or it failed to catch" close matches. CNET paused the tool.

## Running the Process against the record

1. **Voice spec.** Not the failure point. The pieces were short, formulaic explainers; tone was not what went wrong. This is the trap: the factory looked consistent, so the spec gate looked passed.

2. **Fact base.** This is where it broke. Finance explainers are built from numbers — interest calculations, deposit amounts, product terms. CNET's corrective steps included "automatic citations and external links for proprietary information such as data points or direct quotes" — which is the fact-base gate added after the fact. *Gate the Process would have fired: any number in a draft not traceable to a sourced entry → reject.*

3. **Risk tiers.** Personal-finance guidance is high-risk content by the skill's own tiering (financial topic, numbers a reader may act on). It was produced as low-risk, volume content — "basic explainers," 1% of output. *Gate: a high-risk piece needs a line-by-line check against the fact base, not an edit pass.*

4. **Generate → review gates.** A human editor touched every piece, and 41 of 77 still needed correction. The review existed; the check did not. The automated gate that did exist — plagiarism detection — "wasn't properly used" or missed matches. *Gate: an untraceable claim is deleted or rewritten, whoever wrote it.*

5. **Disclosure.** CNET's own lesson was that "bylines and disclosures should be as visible as possible": it changed the byline to "CNET Money" and moved the disclosure "so you don't need to hover over the byline to see it." A disclosure a reader has to hunt for is a red flag in this skill.

6. **Cadence and metrics.** The metric that mattered was the correction rate — 41 of 77 once measured. CNET's response matches the skill's gate exactly: when corrections rise, cut volume and fix the process. It paused the tool and said it would restart "when we feel confident the tool and our editorial processes will prevent both human and AI errors."

7. **Stop-rule.** The pause is the stop-rule in action: until a sourced fact base and real verification exist, high-risk volume production halts.

## The mapped steps

1. Voice spec: adequate; not where the damage came from
2. Fact base: absent for numbers and quotes; citations added only after the audit
3. Risk tier: high-risk finance content produced as routine volume
4. Gates: human edit on every piece, but no source check; plagiarism gate misused or ineffective
5. Disclosure: initially behind a byline hover; moved to visible placement
6. Metric: corrections on 41 of 77 stories
7. Stop-rule: AI tool paused pending process changes

**The lesson.** Human presence is not verification. A content factory's risk lives in its numbers and quotes, so the fact base and the high-risk tier are where the gates must be hardest — especially for content that looks too basic to need them.

Primary sources: Connie Guglielmo, "CNET Is Testing an AI Engine. Here's What We've Learned, Mistakes and All," CNET, January 25, 2023, https://www.cnet.com/tech/cnet-is-testing-an-ai-engine-heres-what-weve-learned-mistakes-and-all/ · Mia Sato and Emma Roth, "CNET found errors in more than half of its AI-written stories," *The Verge*, January 25, 2023, https://www.theverge.com/2023/1/25/23571082/cnet-ai-written-stories-errors-corrections-red-ventures
