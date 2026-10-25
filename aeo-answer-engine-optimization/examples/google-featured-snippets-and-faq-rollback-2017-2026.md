# Method in Action: Google's Featured-Snippet Failures and the FAQ/HowTo Rich-Result Rollback (2017–2026)

> *Example for the [aeo-answer-engine-optimization](../SKILL.md) skill.*

This case is told from the answer engine's side, in the engine operator's own words. Google has publicly described how its featured snippets go wrong and has changed, in writing, which structured data it rewards. Read together, those documents show each step of the AEO Process failing or holding up. Every fact below comes from a Google publication linked at the end.

**The setup.** Google began showing featured snippets in January 2014: a box at the top of results where "the page's description … comes first." Google says the format is "especially helpful for those on mobile or searching by voice," and that for spoken answers it cites the source page aloud. That is the AEO prize: one passage, read out as *the* answer (Sullivan, Google, January 30, 2018).

**Failure 1: the near-match ("How did the Romans tell time at night").** Google's featured snippet for this query recommended sundials, "which would be useless in the dark." Google explained that the snippet "was actually a response for 'How did Romans tell time.'" Many pages discussed that broader question, while "how they told time at night was less discussed." The correct answer, water clocks, sat on the same source page, but Google "didn't then have enough confidence" to lift it.

**Failure 2: phrasing decides the passage ("are reptiles good pets" vs. "bad pets").** The two queries returned contradictory featured snippets "because sometimes our systems favor content that's strongly aligned with what was asked."

**Failure 3: structure without authority ("Obama was planning a coup").** In 2017 featured snippets surfaced claims such as "former U.S. President Barack Obama was planning a coup." Google's explanation: "we didn't weigh the authoritativeness of results strongly enough for such rare and fringe queries." In response it updated its rater guidelines and said that where results are prone to low-quality content, "we may opt not to show a featured snippet."

**Failure 4: schema treated as the strategy.** On August 8, 2023, Google announced that FAQ rich results "will only be shown for well-known, authoritative government and health websites" and that How-To rich results would be limited to desktop (Mueller, Google Search Central Blog). By September 2023 its changelog recorded that the How-to documentation was removed "as this rich result is no longer shown in search results, on both desktop and mobile." In May 2026 Google added a deprecation notice saying the FAQ rich result "will no longer appear in Google Search starting May 7, 2026," and then removed the FAQ documentation. Meanwhile Google's featured-snippet documentation answers "How can I mark my page as a featured snippet?" with: "You can't."

Map the record against the Process:

1. **Map the questions (Step 1).** The sundial failure is a question-mapping failure in reverse. The night-time question was rare on the web, so the engine fell back to a near-neighbor question. A publisher who had mapped the real question from users and answered it under its own heading would have given the engine the passage it lacked.
2. **One question, one anchor (Step 2).** The reptile case shows engines matching the asker's exact framing. A page that heads one section "Are reptiles good pets?" and states both sides in the first paragraph serves both phrasings. A one-sided page wins only the phrasing it echoes.
3. **Answer first (Step 3).** The water-clock answer existed but was not where the engine could lift it with confidence. The fix is positional: put the specific answer directly under the specific question.
4. **Definition block (Step 4).** Google's general structured-data guidelines bar marking up "content that is not visible to readers of the page." Definitions must live in visible text, not only in markup.
5. **Structured data (Step 5).** Sites that treated FAQ and HowTo markup as the strategy lost those rich results to policy changes they did not control: first a restriction (2023), then removal (HowTo 2023, FAQ 2026). Google noted that unused structured data "does not cause problems for Search, but also has no visible effects." That is why the skill's gate ties schema to visible content and never treats it as a promise of display.
6. **Track (Step 6).** Each of these changes would surface only in a log that re-checks which passage is selected. Google said Search Console's FAQ and How-To reports would show the drop in impressions.
7. **Stop-rule (Step 7).** The coup case is the stop-rule in practice. On sensitive or fringe queries the engine weights authoritativeness above passage fit and may show no snippet at all. More editing will not fix an authority deficit.

**The lesson.** The engine's own post-mortems name the variables AEO controls (question phrasing, answer position, standalone accuracy) and the ones it does not (authority thresholds, which rich-result types exist this year). The Process works on the first set and routes the second set to tracking and the stop-rule.

Primary sources:
- Danny Sullivan, "A reintroduction to Google's featured snippets," Google, January 30, 2018. https://blog.google/products/search/reintroduction-googles-featured-snippets/
- John Mueller, "Changes to HowTo and FAQ rich results," Google Search Central Blog, August 8, 2023. https://developers.google.com/search/blog/2023/08/howto-faq-changes
- Google Search Central, "Latest Google Search documentation updates" (changelog: September 2023 How-to removal; May 2026 FAQ deprecation). https://developers.google.com/search/updates
- Google Search Central, "Featured snippets and your website." https://developers.google.com/search/docs/appearance/featured-snippets
- Google Search Central, "General structured data guidelines." https://developers.google.com/search/docs/appearance/structured-data/sd-policies
