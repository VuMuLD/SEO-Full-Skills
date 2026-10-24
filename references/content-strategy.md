<!-- Module: content-strategy | Load when: content strategy, editorial calendar, "what should we write", content pillars, topic ideas, content prioritization, link-earning content, content distribution. For SERP-based keyword clustering use cluster.md; for one brief use content-brief.md; for the overall roadmap use plan.md. -->

# Content Strategy (searchable + shareable)

Goal: plan content that captures demand (search), creates demand (shareable), earns links and
AI citations, and leads to the product. Treat every piece as a launch: plan, ship, distribute.

## 1. Intake (read `.agents/product-marketing.md` first if it exists)

- **Business**: what the company does, ideal customer, primary content goal (traffic, leads,
  authority), problems the product solves.
- **Customer research**: pre-purchase questions, sales objections, recurring support topics,
  the customer's own words for the problem.
- **Current state**: existing content and what works (GSC/GA4), team, budget, formats possible.
- **Competition**: main competitors and visible gaps.

## 2. Searchable vs shareable

Every piece must be searchable, shareable, or both; search is the foundation.

| | Searchable (captures demand) | Shareable (creates demand) |
|---|---|---|
| Built for | A specific query and its intent | A novel insight, data, or a strong argument |
| Must have | Intent match, query-shaped title/headings, complete answer, sources, answer blocks (aeo.md) | Original data or POV, story, a reason to share or cite |
| Types | Use-case pages ([persona] + [use case]), hub/spoke guides, template libraries, how-tos, glossaries, comparisons | Thought leadership, data studies, expert roundups (15-30 experts, one question), case studies (challenge → solution → results), build-in-public posts |

Most posts live fine under `/blog/` with strong internal links; reserve dedicated hub URL trees
(`/guides/topic/...`) for major topics with layered depth.

## 3. Pillars and clusters

Choose 3-5 pillars the brand can own: product-led (problems solved), audience-led (what the
ICP must learn), search-led (topics with demand), competitor-led (what rivals rank for). Each
pillar must align with the product, matter to the audience, have demand, and be broad enough
for many subtopics. Build the hub first, then spokes. For SERP-overlap clustering and the
hub-spoke link matrix use cluster.md.

Industry examples:

| Industry | Pillar | Cluster topics |
|---|---|---|
| SaaS | Product documentation | Getting started, API reference, integrations, troubleshooting, migration |
| E-commerce | Product category | Buying guide, comparisons, care guide, reviews, accessories |
| Local service | Service area | City pages (unique), pricing, before/after, testimonials |
| B2B expertise | Core discipline | Methodology, tools, compliance, reporting, case studies |

## 4. Keywords by buyer stage

| Stage | Modifiers | Example |
|---|---|---|
| Awareness | what is, how to, guide to | "what is agile project management" |
| Consideration | best, top, vs, alternatives, comparison | "asana vs trello" |
| Decision | pricing, reviews, demo, trial | "[product] pricing" |
| Implementation | template, example, tutorial, setup | "sprint planning template" |

## 5. Ideation sources

1. **Keyword data** (GSC, Ahrefs, Semrush, DataForSEO, `keyword_planner.py`): group into
   clusters, tag stage and intent, find quick wins and competitor gaps. Output:
   `| Keyword | Volume | Difficulty | Stage | Content type | Priority |`.
2. **Sales/support calls & tickets**: questions → posts; pains in the customer's words;
   objections → pre-emptive content; competitor mentions → comparison pages.
3. **Surveys**: themes mentioned by 30%+ of respondents are high priority.
4. **Forums**: `site:reddit.com <topic>`, `site:quora.com <topic>`, Hacker News, niche
   communities — FAQs, misconceptions, debates, terminology.
5. **Competitors**: `site:competitor.com/blog`; topics they repeat, gaps, outdated pieces to beat
   (`python <SKILL_DIR>/scripts/competitor_gap.py --help`).
6. **Existing performance**: `content_decay_detector.py` on a GSC export for decaying pages and
   striking-distance queries (positions 8-20) — refreshing often beats writing new.

## 6. Prioritize

Score each idea 1-10 per factor, multiply by weight, sum:

| Factor | Weight | Questions |
|---|---|---|
| Customer impact | 40% | How often it came up, share of customers affected, pain intensity, LTV |
| Content-market fit | 30% | Ties to what the product solves; unique insight or stories available |
| Search potential | 20% | Volume, difficulty, long-tail depth, trend |
| Resources | 10% | Expertise on hand, research and assets needed |

## 7. Link-earning and AI-citation formats

One vendor study of B2B SaaS sites (Foundation Inc., March 2026 — directional only) measured
backlinks relative to page share: statistics/data roundups **4.25×**, glossary pages 1.47×,
interactive tools/calculators 1.38×, how-tos 1.36×, original research 0.80×, ultimate guides
0.77×, thought leadership 0.74×, templates 0.68×. Implication: maintain a fresh statistics page
for your category (citable one-line facts are also what AI answers quote, see geo.md), and pair
original research with a roundup page presenting findings as citable one-liners. Judge each
format by its job (rankings, conversion, brand, links).

## 8. Calendar and execution

- **Split** (starting ratio): 60% searchable · 30% shareable · 10% experimental formats.
- **Blog post**: write 10 title options, then ~5 editing passes (structure, clarity, evidence,
  line edit, title/SEO). Use content-brief.md for the brief and `templates/content/` for
  blog, news, and technical-article structures.
- **Flagship guide**: the pillar hub; table of contents; links to every spoke.
- **Video/podcast**: script the hook first; plan clips, transcript, and recap at creation time.

## 9. Distribution: create once, distribute twice

Build distribution hooks into the piece (stand-alone subheads, liftable stats, pull quotes).
Route attention borrowed (podcasts, guest posts, partners) → rented (social, ads) → owned
(email, blog, community), the only durable asset. Avoid spray-and-pray and dependence on rented
platforms. Atomization checklist and platform half-lives:
`<SKILL_DIR>/references/content-strategy/content-distribution.md`. CMS/content-model choices for
headless sites: `<SKILL_DIR>/references/content-strategy/headless-cms.md`.

## 10. Output

1. **Pillars** (3-5) with rationale, clusters, and link to the product.
2. **Priority topics** table: title · searchable/shareable/both · type · target keyword · stage ·
   score · evidence (customer quote, GSC data, competitor gap).
3. **Cluster map** (hub → spokes → internal links); optionally `templates/cluster-map.html`.
4. **Calendar** (`CONTENT-CALENDAR.md`) with owners, dates, and the distribution plan per piece.
5. **KPIs**: impressions/clicks per cluster, rankings for target queries, AI citations, links
   earned, assisted conversions. Never promise traffic or rankings.
