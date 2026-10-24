<!-- Module: directories | Load when: directory submissions, launch listings (Product Hunt, G2, Capterra, AlternativeTo, AI/SaaS/MCP directories), citation-building for software products, review-site strategy. Local business citations (NAP) live in local.md. -->

# Directory Submissions & Review Sites (software products)

Directories are the **foundation layer** of off-site discovery, not the strategy. They give
(1) some followed links from established sites, (2) in-market discovery traffic, and (3) presence
on third-party pages that AI answers draw on for "best [category]" queries. Most value comes
from a small number of relevant, moderated directories and from **reviews**.

Google treats links as a ranking input only when they are editorial; mass or paid directory
submission is a link scheme. Never buy submission packages or use spammy/low-quality
directories (no moderation, no real traffic).

## Three rules

1. **Foundation before submission** — the landing page is live, indexed, server-rendered, has
   one H1 and a clean heading hierarchy, a public pricing page, privacy/terms, logo set (PNG,
   SVG, 1024×1024, favicon), 5-8 real screenshots, a 60-90 s demo video, and accurate
   Organization + Product/SoftwareApplication schema.
2. **Destinations before directories** — build pages that can convert the traffic first:
   3-5 `/alternatives/<competitor>` pages (competitor-pages.md), 3-5 use-case or `/for/<audience>`
   pages, a template gallery if the category supports it, integration pages when integrations
   exist, and an honest category roundup.
3. **Positioning varies by directory type** — never paste one description everywhere:

| Surface | Lead with |
|---|---|
| Startup directories | Outcome |
| SaaS directories | Alternative framing ("X alternative for …") |
| AI directories | AI-first capability |
| Agent / MCP registries | Agent / MCP angle |
| No-code directories | Ease + power |
| Developer directories | Technical depth |
| B2B review sites | ROI + use case |

Variant copy library: `<SKILL_DIR>/references/directories/positioning-variations.md`.

## Workflow

1. **Readiness check** — public product (no password wall)? pricing page? privacy/terms? logo
   set? screenshots + video? landing pages ready (rule 1)? ≥3 alternatives + ≥3 use-case pages
   indexed? template gallery/lead magnet (if applicable)? ≥20 users who could review on G2?
   Items 1-7 missing = hard block; 8-9 = soft block.
2. **Choose tiers** (full catalog with DR and follow status: `<SKILL_DIR>/references/directories/directory-list.md`):
   Tier 1 launch (Product Hunt, BetaList, Show HN, DevHunt) · Tier 2 SaaS/startup (AlternativeTo,
   SaaSHub, G2, Capterra, SourceForge) · Tier 3 AI directories · Tier 4 agent/MCP registries ·
   Tier 5 no-code · Tier 6 "best of" list inclusions via outreach · Tier 7 integration
   marketplaces · Tier 8 profile/content platforms · Tier 9 local · Tier 10 forums (participate
   first) · Tier 11 press-release sites (low value, milestones only) · Tier 13 niche verticals.
   Submit only where the product genuinely fits the category.
3. **Prepare assets per tier** — tagline (<10 words), 60-char short description, ~150-word long
   description (varied opening and emphasis), 5-8 tags, logo, screenshots, video, founder story.
4. **Batch submit** with the tracker `<SKILL_DIR>/templates/directory-submission-tracker.csv`
   (date, URL, status, moderator notes).
5. **Verify links once live**:
   `python <SKILL_DIR>/scripts/verify_backlinks.py --target https://yoursite.com --links live_listings.txt --json`
   (checks the listing still links to you and reads the anchor's `rel`). Re-check quarterly.

## Product Hunt (anchor event)

- 3 weeks before: use the maker account genuinely (comment on launches daily), create the
  "Upcoming" page and collect subscribers; optionally line up a hunter (never pay).
- 1 week before: gallery images (1270×760), tagline, 260-char description, maker first comment,
  a customer comment; warm up the email list.
- Launch 12:01 AM Pacific, Tuesday-Thursday. Reply to every comment fast. Ask for **feedback**,
  never upvotes, and do not cold-message strangers (moderators hide such posts).
- After: honest recap post with numbers on day 2; Show HN only with a genuine technical angle.

## Reviews (G2 / Capterra / TrustRadius)

Listings without reviews do little. "10 in 30" protocol: pick 20 users who completed a
meaningful action, send a personal email with the direct review link, follow up once after
5 days, aim for 10 reviews. Small, disclosed thank-you incentives are allowed by these
platforms; never fake or gate reviews (and Google's review-snippet guidelines forbid undisclosed
incentivized reviews). Plan drives before G2 report cut-offs. Free listing + "Users Love Us"
badge is enough in year one.

## Off-site presence that also feeds AI answers

Crunchbase, LinkedIn company page, Wikidata (accurate, referenced), GitHub, relevant community
participation (Reddit 90/10 helpful/promotional, Indie Hackers, Dev.to/Hashnode cross-posts with
canonical URLs). Measure monthly with the AI visibility workflow in geo.md.

## KPIs (weekly)

Referring domains (followed, relevant) · listings live and verified · reviews per platform ·
indexed destination pages · organic clicks to destination pages · signups from directory
referrals · AI mentions for "best [category]" prompts (sampled, geo.md). Third-party DR is a
vendor estimate, not a Google metric. If numbers stall, fix destinations and reviews before
submitting more directories.

## Do not

Pay for bulk submissions · submit to spam directories · reuse one description everywhere ·
submit before destination pages exist · lie on comparison pages · ask for upvotes · edit
listings weekly · treat launch day as the strategy.

## Output

Readiness gaps → tier selection with reasons → week 1/2/3 batches → destination pages to build →
positioning copy per tier → Product Hunt timeline (dated if launch day known) → review plan →
weekly targets → tracker CSV.
