# Method in Action: Everalbum and the FTC Model-Deletion Order (2017–2021)

> *Example for the [proprietary-data-moat](../SKILL.md) skill.*

Everalbum, Inc. ran "Ever," a consumer photo-storage app. By the FTC's account, it had what looks on paper like a textbook data moat: millions of user-uploaded photos no competitor could scrape, a feature that had users label faces by name, and an enterprise facial-recognition business built on top. In 2021 the FTC's settlement required the company to delete not only the data but **the models and algorithms built from it**. The case shows why step 5 (rights) is a hard gate rather than a compliance footnote: an asset that fails it is not merely weaker — it can be ordered out of existence, along with everything trained on it.

**Primary sources (FTC).**
- Press release, January 2021: https://www.ftc.gov/news-events/news/press-releases/2021/01/california-company-settles-ftc-allegations-it-deceived-consumers-about-use-facial-recognition-photo
- Final settlement press release, 7 May 2021: https://www.ftc.gov/news-events/news/press-releases/2021/05/ftc-finalizes-settlement-photo-app-developer-related-misuse-facial-recognition-technology
- Case page (complaint, decision and order, 2022 compliance report filed by Paravision, Inc.): https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter

The facts below are the FTC's allegations as stated in its press release. The company settled; a consent order is not an adjudicated finding.

## The facts (per the FTC)

- **February 2017:** Ever launched "Friends," which "used facial recognition technology to group users' photos by the faces of the people who appear in them and allowed users to 'tag' people by name." Facial recognition was allegedly **on by default** for all mobile users.
- **July 2018 – April 2019:** Everalbum allegedly represented that it would not apply facial recognition unless users affirmatively turned it on. From May 2018, only users in Illinois, Texas, Washington, and the EU could choose. For everyone else it stayed on until April 2019 "and could not be turned off."
- **September 2017 – August 2019:** Everalbum "combined millions of facial images that it extracted from Ever users' photos with facial images that Everalbum obtained from publicly available datasets to create four datasets" for developing its facial recognition technology. Technology from one of those datasets powered the Friends feature and was also used "to develop the facial recognition services sold to its enterprise customers."
- Everalbum promised to delete content from deactivated accounts but allegedly, "until at least October 2019," retained it indefinitely.
- **Order:** delete the photos and videos of deactivated users; delete "all face embeddings… derived from the photos of Ever users who did not give their express consent"; delete "any facial recognition models or algorithms developed with Ever users' photos or videos"; obtain express consent before future biometric use. Commission vote: 5–0. Finalized May 2021.

## Running the steps

**1. Inventory the data.** Two classes. (a) **User-uploaded photos and videos** — arising from product use, millions of faces, refreshed continuously. (b) **Public face datasets** — public, purchased-equivalent.

**2. Uniqueness test.** Class (b) fails: "publicly available datasets" are obtainable by any competitor — an operating asset, not a moat. Class (a) passes: a competitor cannot buy or scrape millions of private user photos. *On uniqueness alone, (a) looks like the moat.*

**3. Compounding test.** The record shows the user-derived data fed four training datasets and an enterprise product — a sign the company believed it compounded. The FTC materials cited here contain no lift measurements, so the test cannot be scored from the public record. A pitch would have asserted it; the Process asks for the measured lift.

**4. Feedback loop.** Friends let users "tag" people by name — exactly the kind of user-generated label signal step 4 looks for, produced free as a by-product of use. (The FTC release does not say whether tags were used in training; the loop design is what matters here.) On paper this is the strongest part of the asset: labels are scarcer than raw images.

**5. Rights and consent — the gate fails.** Facial recognition was on by default and, for most users, could not be turned off; the company represented an opt-in it did not provide for most users; and user faces went into datasets for an *enterprise* product the users had no relationship with — cross-customer, cross-purpose use. *Gate: no clear right → exclude the data.* Everalbum had not excluded it, so the regulator did: data, embeddings, **and models** ordered deleted. The FTC has since described this remedy in general terms, warning that it has "required businesses that unlawfully obtain consumer data to delete any products—including models and algorithms developed in whole or in part using that unlawfully obtained data" (Tech@FTC, January 2024).

**6. Quality.** Not addressed in the public record. Moot once step 5 fails.

**7. Productize.** The data produced two customer-visible advantages: consumer face grouping and enterprise facial-recognition services. Both depended on class (a); both were exposed to the deletion order.

**8. Stop-rule.** After step 5, no class passes steps 2, 3, and 5 together: (b) fails uniqueness, (a) fails rights. The Process's verdict is "no data moat" — whatever the volume, the labels, or the enterprise revenue built on it.

## The mapped steps

1. **Inventory:** user photos (product use) + public face datasets.
2. **Uniqueness:** public datasets fail; user photos pass.
3. **Compounding:** believed, not publicly measured.
4. **Loop:** user face-tagging = free label signal.
5. **Rights:** default-on recognition, misrepresented opt-in, cross-purpose enterprise use → fail → data, embeddings, and models ordered deleted.
6. **Quality:** n/a.
7. **Productize:** consumer grouping + enterprise FR services, both exposed.
8. **Verdict:** no moat.

**The lesson:** uniqueness and a clever feedback loop are what founders and investors check first. Everalbum had both. The test it failed was the one usually deferred — and failing it removed the models trained on the data along with the data itself.
