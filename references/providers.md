<!-- Module: providers | Load when: the user names or has a data provider — Ahrefs, Bing Webmaster / IndexNow / Copilot, Firecrawl crawling, Matomo analytics, Profound or SE Ranking AI visibility, Unlighthouse site-wide Lighthouse, or the `seo` CLI/MCP (npm package "seo"). DataForSEO has its own module (dataforseo.md); Google APIs are in google.md. -->

# Data Providers & External Engines

Rules for every provider:

- **Check availability first** (MCP tool present, env var/API key set, CLI on PATH). If missing,
  say which provider is unavailable and how to enable it, then continue with free sources.
- **Label every metric with its source** and freshness, e.g. "Ahrefs (live)", "Common Crawl
  (snapshot 2026-08)". Vendor authority scores (DR, DA, AS) are estimates, not Google metrics.
- **Cost guardrail**: for metered APIs, estimate before batches ≥ 50 calls, tell the user, log
  actual spend (`python <SKILL_DIR>/scripts/dataforseo_costs.py --help` is a generic ledger).
- Provider output is evidence, not a finding: interpret it through the audit rubric.

## Provider routing

| Need | First choice | Fallbacks |
|---|---|---|
| Live SERP, keywords, volumes, SERP features | DataForSEO MCP | Google Ads Keyword Planner (`keyword_planner.py`), SE Ranking, GSC queries |
| Backlinks | Ahrefs MCP / DataForSEO | Moz + Bing + Common Crawl (backlinks.md), SE Ranking |
| AI visibility / share of voice | SE Ranking (ChatGPT, Gemini, Perplexity, AIO, AI Mode), Profound (time series) | DataForSEO AI-optimization endpoints, manual sampling (geo.md) |
| Full-site crawl / JS rendering at scale | Firecrawl MCP | `crawl_audit.py`, `render_page.py`, Screaming Frog export |
| Site-wide Lighthouse | Unlighthouse | PSI per URL (`pagespeed_check.py`), `lighthouse_runner.py` |
| Analytics without Google | Matomo | GA4 (google.md) |
| Bing / Copilot / IndexNow | Bing Webmaster API + `indexnow_submit.py` | Manual BWT |
| Report-based workflow with evidence registry | `seo` CLI / MCP | The modules of this skill |

---

## Ahrefs (MCP `@ahrefs/mcp`, API token)

| Task | Use |
|---|---|
| Domain/URL rating, referring domains, traffic estimate | metrics tools |
| Top referring domains, anchors, follow ratio | backlinks tools |
| Organic keywords, positions, traffic by country | organic tools |
| Content Explorer for a topic | content tools |

When Ahrefs and Moz disagree, prefer Ahrefs and note the gap. Combine its toxicity signals with
the Common Crawl + verification crawler checks in backlinks.md. For live SERP features prefer
DataForSEO.

## Bing Webmaster Tools & IndexNow (non-Google indexing, Copilot)

Google does not use IndexNow. Bing, Yandex, Naver, Seznam, Yep (and Amazon) consume it, and
Microsoft Copilot answers come from the Bing index — so Bing indexation matters for AI visibility.

```bash
python <SKILL_DIR>/scripts/bing_webmaster.py links <url> --json            # inbound links (BWT API key)
python <SKILL_DIR>/scripts/bing_webmaster.py compare <urlA> <urlB> --json   # both properties must be in your account
python <SKILL_DIR>/scripts/indexnow_checker.py <url> --json                 # key file present and valid?
python <SKILL_DIR>/scripts/indexnow_submit.py --help                        # submit URLs (verify-only mode available)
```

IndexNow needs a 32+ character key file hosted at the declared key location. Submitting
publishes externally: dry-run/verify first and submit only with the user's approval.

## Firecrawl (MCP; free tier ~500 credits/month)

| Tool | Use |
|---|---|
| `firecrawl_map` | Fast URL discovery (cheap). Compare with sitemaps → orphans, missing, stale URLs; URL pattern breakdown |
| `firecrawl_crawl` | Full crawl with content (`limit`, `maxDepth`, `includePaths`, `excludePaths`) feeding technical/content/schema analysis |
| `firecrawl_scrape` | One JS-rendered page as clean markdown (`onlyMainContent`, `waitFor`, `actions`) |
| `firecrawl_search` | Search inside a site: content-gap checks, internal-link opportunities, duplicate phrases |

Audit pattern: map → pick top ~50 important URLs → crawl them → hand content to specialists.
Use `fetch_page.py` for static pages and response headers (free); Firecrawl for SPAs, anti-bot
sites and clean extraction. Tell the user the credit estimate before large crawls. Errors:
402 credits exhausted · 429 back off 60 s · 403 site blocks crawling (respect it).

## Matomo (self-hosted or cloud analytics; GA4 alternative/complement)

```bash
python <SKILL_DIR>/scripts/matomo_auth.py --check
python <SKILL_DIR>/scripts/matomo_report.py organic --site-id <id> --days 28 --json
python <SKILL_DIR>/scripts/matomo_report.py top-pages|device|country|referrers|keywords --json
```

Needs `MATOMO_URL`, a `token_auth` with view access, optional `MATOMO_SITE_ID`. Private-network
instances must be allowlisted with `CLAUDE_SEO_LOCAL_TARGETS="host:port"` (never disable the
SSRF guard). Many keywords show "(not provided)" — normal. Numbers will not match GA4 exactly
(segment and attribution rules differ). Label as "Matomo Reporting API (live)".

## SE Ranking (REST API key)

AI share of voice for a brand across ChatGPT, Gemini, Perplexity, AI Overviews and AI Mode
(report each as % of sampled prompts with sample size), top-100 SERP + features for a keyword,
backlink profile, organic competitors and shared-keyword gaps. ~1 unit per platform per prompt.

## Profound (API key)

Continuous LLM brand-mention tracking with time series: citation rate per LLM with 30-day trend,
prompts that surface (or miss) the brand, co-cited competitors, spike/drop alerts vs a 7-day
baseline. Native coverage is ChatGPT + Perplexity; use SE Ranking for Gemini/AIO/AI Mode.

## Unlighthouse (Node 18+, no key)

```bash
python <SKILL_DIR>/scripts/unlighthouse_run.py <url> --json                       # mobile, up to 200 routes
python <SKILL_DIR>/scripts/unlighthouse_run.py <url> --device desktop --max-routes 50 --output-dir ./reports --json
```

Returns route count, median category scores (performance, accessibility, best practices, SEO)
and per-route results. Good for site-wide regression checks after deploys or when PSI quota is
not enough. Lab data only: confirm with CrUX field data (google.md).

## `seo` CLI / MCP (npm package `seo`, Apache-2.0)

An evidence-first report engine with a registry of report ids. Use it when installed
(`command -v seo`); install only with the user's consent (`npm i -g seo`, then `seo start` or
`seo doctor`).

```bash
seo reports list --json
seo reports describe <report-id> --json          # always describe before the first run
seo reports run <report-id> --params '<json>' --json
seo report --url <absolute-url> [--search-console-export <path>] --actions-only --json   # broad audit
```

MCP equivalents: `seo_list_reports`, `seo_describe_report`, `seo_run_report`; providers via
`seo providers list|describe|run`. Follow each report's `readOrder`, `doNotClaim` and `verify`.

| Job | Report ids |
|---|---|
| Page not indexed | `index-coverage`, `index-monitor`, `audit-page`, `redirect-trace` |
| Traffic or clicks dropped | `search-performance-overview`, `traffic-anomaly`, `update-correlation`, `segment-impact`, `decaying-pages`, `link-recovery` |
| Whole-site audit | `report`, then `site-crawl`, `top-fixes`, `ai-search-scorecard` |
| More clicks from existing pages | `quick-wins`, `ctr-underperformers`, `striking-distance`, `second-page`, `internal-links` |
| AI search visibility | `ai-readiness`, `agent-readiness`, `geo-gaps`, `ai-mention-research`, `ai-prompt-observations`, `ai-referrals` |
| Content from real demand | `query-clusters`, `page-opportunities`, `content-optimization`, `cannibalisation` |
| Keywords & competitors | `competitive-opportunities`, `keyword-research`, `serp-results`, `ranked-keywords`, `ranking-pages`, `serp-competitors`, `competitor-keyword-gap` |
| Local / programmatic | `local-search-demand`, `pseo-patterns`, `pseo-opportunities`, `pseo-audit` |
| Links, Bing, logs | `domain-rating`, `link-evidence`, `bing-webmaster-overview`, `server-log-analysis` |
| Regressions | `technical-watch`, `crawl-diff`, `index-watch`, `measure-change` |
| Client reporting | `monthly-report`, `narrative-report`, `monthly-action-plan` |
| Crawl findings → tickets | `top-fixes`, `affected-urls`, `explain-crawl-issue` |

Broad-audit discipline from that engine (apply it to any findings list): track every finding id
and inventory URL; for a `fix` choose fixed / deferred / not-needed, for a `review` answer the
question and choose changed / no-change / deferred, each with evidence; rerun the same report
after changes; fetch every `nextPage`; never pipe JSON through `head`. Missing, partial, capped,
sampled or filtered evidence never supports a zero or an all-clear. Grouped GSC totals can
undercount. Intentional `noindex`/canonical/robots rules are observations until the user confirms
they are unintended.
