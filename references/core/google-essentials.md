<!-- Updated: 2026-10-23 -->
# Google Search Quick Reference (Oct 2026)

Compact reference for every module. Primary sources at the bottom; when this file and a
module disagree, the dated module reference (schema-types.md, cwv-thresholds.md,
`data/google-updates.json`) wins.

## How Search works

**Crawling** (Googlebot discovers URLs via links and sitemaps; smartphone crawler is primary)
→ **Indexing** (renders, picks a canonical, stores content and signals; first 2 MB of HTML)
→ **Serving** (ranks indexed pages by relevance, quality, usability; AI Overviews and AI Mode
draw on the same index and ranking systems). A page must be crawlable, indexable and canonical
to appear anywhere, including AI features.

## Search Essentials

**Technical requirements**: Googlebot not blocked; page returns HTTP 200; indexable content
(no `noindex`) in a format Google can process. HTTPS is strongly recommended and a lightweight
signal, not an indexing requirement.

**Spam policies** (violations → manual action or algorithmic demotion):
cloaking · doorway pages · hidden text/links · keyword stuffing · link spam (buying/selling,
excessive exchanges, PBNs) · scraped content · sneaky redirects · thin affiliation · machine-
generated traffic · malware/malicious practices · misleading functionality · user-generated
spam · **scaled content abuse** (mass pages for ranking, however produced, since March 2024) ·
**expired domain abuse** (March 2024) · **site reputation abuse** (third-party content
exploiting a host's signals; clarified Nov 2024; since 2026-08-30 enforced per searcher region) ·
**back-button hijacking** (`history.pushState` tricks; added April 2026, enforced since
2026-06-15) · policy circumvention · scam and fraud.

**Best practices**: people-first content; clear hierarchy and crawlable `<a href>` links;
unique descriptive titles and meta descriptions; logical headings; descriptive alt text;
mobile parity; good Core Web Vitals; XML sitemap in Search Console; accurate JSON-LD.

## Content quality

Helpfulness signals live inside core ranking (the Helpful Content System merged into core in
March 2024; Google also ships smaller unannounced core updates). Apply E-E-A-T — Trust most
important — and the Who/How/Why test (content.md, `eeat-framework.md`). YMYL topics need the
strongest evidence of expertise and accuracy. AI-generated content is acceptable when it is
accurate, original and useful; scaled low-value output is spam regardless of how it is made.

## Core Web Vitals (75th percentile of field data)

| Metric | Good | Needs improvement | Poor |
|---|---|---|---|
| LCP | ≤ 2.5 s | 2.5-4.0 s | > 4.0 s |
| INP | ≤ 200 ms | 200-500 ms | > 500 ms |
| CLS | ≤ 0.1 | 0.1-0.25 | > 0.25 |

INP replaced FID on 2024-03-12; never mention FID. Field data (CrUX / Search Console) beats
lab data (Lighthouse). Details: `cwv-thresholds.md`.

## Structured data

JSON-LD; describe only visible content; required properties for eligibility; validate with the
Rich Results Test. Retired/no-rich-result types (never recommend for SERP benefit): HowTo
(2023), FAQPage (retired for all sites 2026-05-07), SpecialAnnouncement, CourseInfo,
EstimatedSalary, LearningVideo, ClaimReview (Fact Check Explorer only), VehicleListing,
Practice Problem; sitelinks search box (Nov 2024). Dataset is for Dataset Search only.
Full status: `schema-types.md`.

## Penalties & recovery

**Manual actions** (Search Console → Security & Manual Actions): unnatural links, thin content,
cloaking/sneaky redirects, UGC spam, structured-data spam, site reputation abuse. Fix the root
cause across the whole site, document it, then file a reconsideration request (weeks to review).

**Algorithmic drops** (no notice): correlate dates with confirmed updates
(`python <SKILL_DIR>/scripts/seo_updates.py --since <yyyy-mm> --json`), segment the loss by
page type/query/device/country, rule out tracking, indexation and seasonality, then improve
quality; recovery typically shows after later core updates. Never promise recovery dates.

## Primary sources

- Search Essentials & spam policies: developers.google.com/search/docs/essentials
- How Search works: developers.google.com/search/docs/fundamentals/how-search-works
- Helpful content: developers.google.com/search/docs/fundamentals/creating-helpful-content
- AI features & optimization guide: developers.google.com/search/docs/appearance/ai-features
- Crawling & robots: developers.google.com/crawling
- Structured data: developers.google.com/search/docs/appearance/structured-data/search-gallery
- Status dashboard (rollouts): status.search.google.com · Changelog: developers.google.com/search/updates
