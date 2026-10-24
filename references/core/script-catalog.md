<!-- Generated from each script's docstring and real `--help` output (2026-10-23). -->

# Script Catalog

Run every script as `python <SKILL_DIR>/scripts/<name>.py ...` after `pip install -r <SKILL_DIR>/requirements.txt`.
Almost every script accepts `--json`; run `--help` for full options (sub-commands have their own `--help`).
Network failures are environment limitations, not site defects.

Optional dependencies (`requirements-optional.txt`): Playwright + `playwright install chromium` (`render_page`,
`capture_screenshot`, `analyze_visual`, `javascript_render_audit`, `mobile_render_checker`, `visual_regression_snapshot`);
Google client libraries (`gsc_*`, `ga4_report`, `indexing_notify`, `keyword_planner`, `nlp_analyze`, `youtube_search`);
`matplotlib`/`weasyprint`/`openpyxl`/`pypdf` (`google_report` PDF/XLSX); Pillow (`visual_regression_snapshot`);
Node 18+ (`unlighthouse_run`, `lighthouse_runner`).

## Fetch, render & crawl

| Script | Purpose | Usage |
|---|---|---|
| `fetch_page.py` | Fetch a web page with proper headers and error handling. | `fetch_page.py [-h] [--output OUTPUT] [--json] [--max-text MAX_TEXT] [--timeout TIMEOUT] [--no-redirects] [--user-agent USER_AGENT] [--googlebot] [--render {auto,always,never}] url` |
| `render_page.py` | Shared headless renderer for claude-seo. | `render_page.py [-h] [--mode {auto,always,never}] [--viewport {desktop,laptop,tablet,mobile}] [--timeout-ms TIMEOUT_MS] [--block {image,media,font,stylesheet}] [--no-extract] [--a11y-tree] [--json] [--max-text MAX_TEXT] [--json-ld-output JSON_LD_OUTPUT] [--output OUTPUT] url` |
| `parse_html.py` | Parse HTML and extract SEO-relevant elements. | `parse_html.py [-h] [--url URL] [--fetch FETCH] [--timeout TIMEOUT] [--json] [file]` |
| `crawl_audit.py` | Robots-aware shallow site crawler with SEO metadata checks. | `crawl_audit.py [-h] [--max-pages MAX_PAGES] [--depth DEPTH] [--timeout TIMEOUT] [--no-sitemap] [--json] site` |

## Crawlability & indexability

| Script | Purpose | Usage |
|---|---|---|
| `robots_checker.py` | Parse and analyze robots.txt for SEO and AI crawler management. | `robots_checker.py [-h] [--json] url` |
| `robots_path_tester.py` | Test URL paths against robots.txt for multiple crawlers. | `robots_path_tester.py [-h] [--agent AGENT] [--timeout TIMEOUT] [--json] site paths [paths ...]` |
| `x_robots_header_checker.py` | Inspect X-Robots-Tag headers. | `x_robots_header_checker.py [-h] [--url-file URL_FILE] [--timeout TIMEOUT] [--json] [urls ...]` |
| `canonical_checker.py` | Check canonical tags for self/cross-domain/chained targets. | `canonical_checker.py [-h] [--url-file URL_FILE] [--check-targets] [--timeout TIMEOUT] [--json] [urls ...]` |
| `indexability_matrix.py` | Build per-URL indexability verdicts. | `indexability_matrix.py [-h] [--url-file URL_FILE] [--site SITE] [--timeout TIMEOUT] [--json] [urls ...]` |
| `redirect_checker.py` | Check redirect chains for a URL. | `redirect_checker.py [-h] [--json] urls [urls ...]` |
| `url_quality.py` | Analyze URL hygiene and variant risks. | `url_quality.py [-h] [--url-file URL_FILE] [--json] [urls ...]` |
| `faceted_nav_audit.py` | Detect faceted navigation crawl traps from URLs and optional page fetches. | `faceted_nav_audit.py [-h] [--url-file URL_FILE] [--fetch] [--timeout TIMEOUT] [--json] [urls ...]` |
| `log_file_analyzer.py` | Analyze server logs for crawl budget and bot status-code patterns. | `log_file_analyzer.py [-h] [--max-lines MAX_LINES] [--json] log_files [log_files ...]` |
| `javascript_render_audit.py` | Compare raw HTML against rendered DOM SEO elements when Playwright is available. | `javascript_render_audit.py [-h] [--timeout TIMEOUT] [--render-timeout RENDER_TIMEOUT] [--json] source` |
| `duplicate_content.py` | Duplicate & Thin Content Detector | `duplicate_content.py [-h] [--depth DEPTH] [--max-pages MAX_PAGES] [--threshold THRESHOLD] [--json] url` |
| `orphan_pages_from_sitemap.py` | Find sitemap URLs that are not reachable from an internal crawl. | `orphan_pages_from_sitemap.py [-h] [--sitemap SITEMAP] [--depth DEPTH] [--max-pages MAX_PAGES] [--timeout TIMEOUT] [--json] site` |
| `indexnow_checker.py` | IndexNow Checker & Pinger | `indexnow_checker.py [-h] --key KEY [--json] [--ping [PING ...]] [--ping-sitemap] [--engine {bing,yandex,seznam,naver}] url` |
| `indexnow_submit.py` | IndexNow submitter. | `indexnow_submit.py [-h] --host HOST [--key KEY] [--key-location KEY_LOCATION] [--urls [URLS ...]] [--urls-file URLS_FILE] [--verify-only] [--json]` |

## Security, mobile & accessibility

| Script | Purpose | Usage |
|---|---|---|
| `security_headers.py` | Check security headers relevant to SEO trust signals. | `security_headers.py [-h] [--json] url` |
| `mobile_render_checker.py` | Check mobile rendering risks with static HTML plus optional Playwright signals. | `mobile_render_checker.py [-h] [--render] [--timeout TIMEOUT] [--json] source` |
| `a11y_seo_checker.py` | Accessibility checks with direct SEO/UX impact. | `a11y_seo_checker.py [-h] [--timeout TIMEOUT] [--json] source` |

## Performance / Core Web Vitals

| Script | Purpose | Usage |
|---|---|---|
| `pagespeed_check.py` | PageSpeed Insights v5 + CrUX API combined checker. | `pagespeed_check.py [-h] [--strategy {mobile,desktop,both}] [--api-key API_KEY] [--crux-only] [--psi-only] [--form-factor {PHONE,DESKTOP,TABLET}] [--json] url` |
| `pagespeed.py` | Fetch Core Web Vitals and performance data from Google PageSpeed Insights API. Kept because `generate_report.py` depends on it; prefer `pagespeed_check.py` (PSI + CrUX). | `pagespeed.py [-h] [--strategy {mobile,desktop,both}] [--json] [--api-key API_KEY] url` |
| `crux_history.py` | CrUX History API for Core Web Vitals trends over time. | `crux_history.py [-h] [--form-factor {PHONE,DESKTOP,TABLET}] [--api-key API_KEY] [--origin] [--json] url` |
| `lcp_subparts.py` | LCP subparts breakdown via CrUX API. | `lcp_subparts.py [-h] [--form-factor {PHONE,DESKTOP,TABLET,ALL_FORM_FACTORS}] [--json] url` |
| `lcp_lab_estimate.py` | Estimate LCP subparts from Lighthouse JSON or lightweight page evidence (lab, no API key). Lab estimate, no API key. Real-user subparts: `lcp_subparts.py`. | `lcp_lab_estimate.py [-h] [--lighthouse-json LIGHTHOUSE_JSON] [--timeout TIMEOUT] [--json] [source]` |
| `preload_check.py` | Speculation Rules / bfcache / prerender2 / preload detector. | `preload_check.py [-h] [--json] [--fail-under N] url` |
| `critical_request_chain.py` | Identify critical request chains and render-blocking resources from HTML. | `critical_request_chain.py [-h] [--fetch-css] [--timeout TIMEOUT] [--json] source` |
| `font_audit.py` | Audit font loading patterns that affect rendering and Core Web Vitals. | `font_audit.py [-h] [--fetch-fonts] [--timeout TIMEOUT] [--json] source` |
| `third_party_script_audit.py` | Audit third-party scripts and blocking JavaScript tags. | `third_party_script_audit.py [-h] [--fetch-scripts] [--timeout TIMEOUT] [--json] source` |
| `cache_compression_checker.py` | Check compression and caching headers for a page and optional assets. | `cache_compression_checker.py [-h] [--include-assets] [--max-assets MAX_ASSETS] [--timeout TIMEOUT] [--json] source` |
| `image_weight_audit.py` | Audit image weight, responsive image usage, and likely LCP image risk. | `image_weight_audit.py [-h] [--fetch-images] [--timeout TIMEOUT] [--json] source` |
| `lighthouse_runner.py` | Run local Lighthouse when available and normalize key audit output. | `lighthouse_runner.py [-h] [--strategy {mobile,desktop}] [--category {performance,seo,accessibility,best-practices}] [--timeout TIMEOUT] [--json] source` |
| `unlighthouse_run.py` | Thin wrapper around the Unlighthouse CLI (https://unlighthouse.dev). | `unlighthouse_run.py [-h] [--device {mobile,desktop}] [--max-routes MAX_ROUTES] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT] [--page-timeout PAGE_TIMEOUT] [--json] target` |

## On-page, content & E-E-A-T

| Script | Purpose | Usage |
|---|---|---|
| `article_seo.py` | Article SEO Optimizer & Keyword Researcher | `article_seo.py [-h] [--keyword KEYWORD] [--json] [--no-autocomplete] url` |
| `readability.py` | Content readability analysis — pure Python, no external NLP dependencies. | `readability.py [-h] [--url URL] [--text TEXT] [--json] [file]` |
| `eeat_signal_checker.py` | Check E-E-A-T signals in HTML content. | `eeat_signal_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `content_quality.py` | QRG-aligned content quality detector. | `content_quality.py [-h] [--json] [--threshold THRESHOLD] [source]` |
| `content_verify.py` | Claim extractor + citation-gap detector. | `content_verify.py [-h] [--json] [--threshold THRESHOLD] [source]` |
| `content_humanize.py` | AI-pattern remover. Rewrites filler / AI-typical phrasings into direct prose, and strips invisible Unicode artifacts ("text watermarks") that AI tools and copy-paste pipelines leave behind: zero-width characters, directi | `content_humanize.py [-h] [--output OUTPUT] [--json] [source]` |
| `metadata_template.py` | Templated-metadata detector. | `metadata_template.py [-h] [--title TITLE] [--description DESCRIPTION] [--url URL] [--pairs-file PAIRS_FILE] [--json] [--fail-on {none,any,site}]` |
| `freshness_checker.py` | Check content freshness signals and stale references. | `freshness_checker.py [-h] [--today TODAY] [--timeout TIMEOUT] [--json] source` |
| `content_intent_matcher.py` | Match page content to a target keyword and search intent. | `content_intent_matcher.py [-h] --keyword KEYWORD [--intent {commercial,informational,navigational,transactional}] [--timeout TIMEOUT] [--json] source` |
| `content_decay_detector.py` | Detect content decay and striking-distance keywords from CSV exports. | `content_decay_detector.py [-h] [--csv CSV_PATH] [--split-date SPLIT_DATE] [--decline-threshold DECLINE_THRESHOLD] [--min-impressions MIN_IMPRESSIONS] [--date-column DATE_COLUMN] [--url-column URL_COLUMN] [--query-column QUERY_COLUMN] [--clicks-column CLICKS_COLUMN] [--impressions-column IMPRESSIONS_COLUMN] [--position-column POSITION_COLUMN] [--json] [csv_file]` |
| `social_meta.py` | Validate Open Graph and Twitter Card meta tags. | `social_meta.py [-h] [--json] url` |
| `parasite_risk.py` | Parasite-SEO risk scanner. | `parasite_risk.py [-h] [--urls-file URLS_FILE] [--json] [urls ...]` |
| `domain_history.py` | Expired-domain heritage check. | `domain_history.py [-h] [--topic TOPIC] [--baseline-topic BASELINE_TOPIC] [--json] domain` |
| `nlp_analyze.py` | Google Cloud Natural Language API - Entity, sentiment, and content analysis. | `nlp_analyze.py [-h] [--text TEXT] [--url URL] [--features FEATURES] [--api-key API_KEY] [--json]` |

## Keywords, clusters & competitors

| Script | Purpose | Usage |
|---|---|---|
| `keyword_planner.py` | Google Ads API - Keyword Planner for SEO keyword research. | `keyword_planner.py [-h] [--limit LIMIT] [--language LANGUAGE] [--location LOCATION] [--json] {ideas,volume} keywords` |
| `keywordseverywhere_api.py` | Keywords Everywhere (formerly OpenPageRank) API client for Claude SEO. | `keywordseverywhere_api.py [-h] [--json] {rank} domains [domains ...]` |
| `topical_cluster_mapper.py` | Map topical clusters and internal-link coverage from URLs, HTML, or CSV. | `topical_cluster_mapper.py [-h] [--csv CSV_PATH] [--timeout TIMEOUT] [--json] [sources ...]` |
| `competitor_gap.py` | Competitor Topic Gap Analyzer | `competitor_gap.py [-h] --competitor COMPETITOR [--max-pages MAX_PAGES] [--json] url` |

## Internal & external links / backlinks

| Script | Purpose | Usage |
|---|---|---|
| `internal_links.py` | Analyze internal link structure of a website. | `internal_links.py [-h] [--depth DEPTH] [--max-pages MAX_PAGES] [--json] url` |
| `anchor_text_audit.py` | Audit internal anchor text quality and diversity. | `anchor_text_audit.py [-h] [--depth DEPTH] [--max-pages MAX_PAGES] [--timeout TIMEOUT] [--json] url` |
| `broken_links.py` | Check for broken links on a web page. | `broken_links.py [-h] [--json] [--internal-only] [--workers WORKERS] [--timeout TIMEOUT] url` |
| `external_link_quality.py` | Audit external links for status, redirects, rel attributes, and trust patterns. | `external_link_quality.py [-h] [--url-file URL_FILE] [--no-check-status] [--max-links MAX_LINKS] [--timeout TIMEOUT] [--json] [url]` |
| `link_profile.py` | Link Profile Analyzer | `link_profile.py [-h] [--max-pages MAX_PAGES] [--gsc-credentials GSC_CREDENTIALS] [--json] url` |
| `backlinks_auth.py` | Backlink API credential management for Claude SEO. | `backlinks_auth.py [-h] [--check [SERVICE]] [--setup] [--tier] [--json]` |
| `moz_api.py` | Moz Link Explorer API client for Claude SEO. | `moz_api.py [-h] [--limit LIMIT] [--json] {metrics,domains,anchors,pages} url` |
| `bing_webmaster.py` | Bing Webmaster Tools API client for Claude SEO. | `bing_webmaster.py [-h] [--page PAGE] [--json] {links,counts,compare} url [competitor_url]` |
| `commoncrawl_graph.py` | Common Crawl Web Graph parser for Claude SEO. | `commoncrawl_graph.py [-h] [--info] [--update] [--release RELEASE] [--timeout TIMEOUT] [--top-referrers TOP_REFERRERS] [--json] [domain]` |
| `verify_backlinks.py` | Backlink verification crawler for Claude SEO. | `verify_backlinks.py [-h] --target TARGET --links LINKS [--head-only] [--timeout TIMEOUT] [--json]` |
| `validate_backlink_report.py` | Backlink report validation for Claude SEO. | `validate_backlink_report.py [-h] --report REPORT [--json]` |
| `redirect_backlink_reclaim.py` | Find backlink reclaim opportunities from a backlink export. | `redirect_backlink_reclaim.py [-h] [--source-column SOURCE_COLUMN] [--target-column TARGET_COLUMN] [--max-rows MAX_ROWS] [--long-chain-threshold LONG_CHAIN_THRESHOLD] [--timeout TIMEOUT] [--json] csv_file` |

## Structured data

| Script | Purpose | Usage |
|---|---|---|
| `schema_required_props.py` | Validate required and recommended Schema.org properties in JSON-LD. | `schema_required_props.py [-h] [--type SCHEMA_TYPE] [--timeout TIMEOUT] [--json] source` |
| `rich_results_guard.py` | Guardrail checks for rich-result eligibility and retired schema types. | `rich_results_guard.py [-h] [--timeout TIMEOUT] [--json] source` |
| `validate_schema.py` | Post-edit schema validation hook for Claude Code. Also usable as a Claude Code PostToolUse hook (see its docstring). Exit 2 = blocking errors. |  |
| `schema_diff.py` | Compare existing JSON-LD against a recommended bundled schema template. | `schema_diff.py [-h] --type SCHEMA_TYPE [--timeout TIMEOUT] [--json] source` |
| `schema_template_generator.py` | Generate JSON-LD templates from bundled schema templates. | `schema_template_generator.py [-h] [--type SCHEMA_TYPE] [--detect-from DETECT_FROM] [--list] [--compact] [--timeout TIMEOUT] [--json]` |
| `schema_generate.py` | JSON-LD generators for the four high-leverage v2 Schema.org types: | `schema_generate.py [-h] [--indent INDENT] [--script-tag] {reservation,order,discussion,profile} ...` |
| `product_schema_checker.py` | Check Product and ProductGroup JSON-LD for ecommerce rich-result readiness. | `product_schema_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `review_schema_checker.py` | Check Review and AggregateRating markup for policy and misuse risks. | `review_schema_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `video_schema_checker.py` | Check VideoObject JSON-LD for video rich-result readiness. | `video_schema_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `schema_ecommerce_validate.py` | Product schema validator focused on Google merchant-listing fields. | `schema_ecommerce_validate.py [-h] [--eu] [--json] [source]` |

## Sitemaps & international

| Script | Purpose | Usage |
|---|---|---|
| `sitemap_discovery.py` | Discover sitemaps through robots.txt and common locations safely. | `sitemap_discovery.py [-h] [--json] url` |
| `sitemap_checker.py` | Discover and validate XML sitemaps. | `sitemap_checker.py [-h] [--sitemap SITEMAP] [--fetch-urls] [--max-urls MAX_URLS] [--timeout TIMEOUT] [--json] site` |
| `sitemap_generator.py` | Generate sitemap XML or sitemap indexes from URL manifests. | `sitemap_generator.py [-h] [--input INPUT] [--index] [--lastmod-today] [--json]` |
| `hreflang_checker.py` | Hreflang Validator | `hreflang_checker.py [-h] [--json] [--verify-returns] url` |
| `hreflang_sitemap_validator.py` | Validate hreflang annotations across sitemap indexes and sitemap URL sets. | `hreflang_sitemap_validator.py [-h] [--sitemap SITEMAP] [--timeout TIMEOUT] [--max-sitemaps MAX_SITEMAPS] [--json] site` |

## Images & visual

| Script | Purpose | Usage |
|---|---|---|
| `image_inventory.py` | Inventory images for SEO, accessibility, and performance signals. | `image_inventory.py [-h] [--fetch-images] [--timeout TIMEOUT] [--json] source` |
| `capture_screenshot.py` | Capture screenshots of web pages using Playwright. |  |
| `analyze_visual.py` | Analyze visual aspects of a web page using Playwright. |  |
| `visual_regression_snapshot.py` | Create or compare visual regression snapshots. | `visual_regression_snapshot.py [-h] [--url URL] [--output-dir OUTPUT_DIR] [--viewport {desktop,tablet,mobile}] [--all] [--full-page] [--timeout TIMEOUT] [--baseline BASELINE] [--current CURRENT] [--json]` |
| `iptc_ai_label.py` | IPTC ``DigitalSourceType`` audit + injection for AI-generated images. | `iptc_ai_label.py [-h] {audit,inject} ...` |

## AI search (GEO/AEO) & agent readiness

| Script | Purpose | Usage |
|---|---|---|
| `llms_txt_checker.py` | Check for llms.txt file and validate its format. | `llms_txt_checker.py [-h] [--json] url` |
| `llms_txt_generator.py` | Generate an llms.txt draft from site metadata and priority URLs. | `llms_txt_generator.py [-h] [--url-file URL_FILE] [--title TITLE] [--description DESCRIPTION] [--fetch-titles] [--timeout TIMEOUT] [--json] site [urls ...]` |
| `ai_crawler_policy_matrix.py` | Compare robots.txt and llms.txt signals for AI crawlers. | `ai_crawler_policy_matrix.py [-h] [--path PATH] [--timeout TIMEOUT] [--json] site` |
| `citation_readiness.py` | Assess citation and entity readiness for AI answers. | `citation_readiness.py [-h] [--timeout TIMEOUT] [--json] source` |
| `answer_block_scanner.py` | Scan pages for answer-block and featured-snippet-ready formatting. | `answer_block_scanner.py [-h] [--timeout TIMEOUT] [--json] source` |
| `entity_checker.py` | Entity SEO Checker | `entity_checker.py [-h] [--entity ENTITY] [--kg-api-key KG_API_KEY] [--json] url` |
| `agentic_check.py` | Agent-readiness HTTP auditor. | `agentic_check.py [-h] [--ua-matrix] [--json] url` |
| `agentic_fix.py` | Agent-readiness fix drafter. | `agentic_fix.py [-h] {robots,llms,ai-catalog,webmcp} ...` |
| `agent_ux_check.py` | Agent-friendly page auditor. | `agent_ux_check.py [-h] [--timeout-ms TIMEOUT_MS] [--json] url` |
| `lighthouse_agentic.py` | Lighthouse Agentic Browsing category reader. | `lighthouse_agentic.py [-h] [--from-json FROM_JSON] [--strategy {mobile,desktop,both}] [--api-key API_KEY] [--json] [url]` |
| `youtube_search.py` | YouTube Data API v3 - Search, video details, and channel data for SEO. |  |

## Local & e-commerce

| Script | Purpose | Usage |
|---|---|---|
| `local_seo_checker.py` | Check local SEO signals: NAP, LocalBusiness schema, GBP links, reviews, and maps. | `local_seo_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `gbp_deprecation_lint.py` | GBP feature-deprecation linter. | `gbp_deprecation_lint.py [-h] [--file] [--json] source` |
| `collection_page_checker.py` | Check ecommerce collection/category pages for copy, filters, pagination, and crawlability. | `collection_page_checker.py [-h] [--timeout TIMEOUT] [--json] source` |
| `dataforseo_merchant.py` | Fetch Google Shopping and Amazon marketplace data via DataForSEO API. | `dataforseo_merchant.py [-h] {search,sellers,compare} ...` |
| `ucp_check.py` | UCP (Universal Commerce Protocol) profile auditor. | `ucp_check.py [-h] [--probe-endpoints] [--timeout TIMEOUT] [--json] site` |

## Google APIs & analytics

| Script | Purpose | Usage |
|---|---|---|
| `google_auth.py` | Google API credential management for Claude SEO. | `google_auth.py [-h] [--check [SERVICE]] [--setup] [--tier] [--json] [--auth] [--exchange] [--creds CREDS] [--code CODE]` |
| `gsc_query.py` | Google Search Console Search Analytics query helper. |  |
| `gsc_inspect.py` | Google Search Console URL Inspection API helper. |  |
| `ga4_report.py` | GA4 Data API v1beta - organic traffic reporting. |  |
| `indexing_notify.py` | Google Indexing API v3 - notify Google of URL updates and removals. |  |
| `google_report.py` | Google SEO Report Generator - Professional PDF/HTML reports from API data. | `google_report.py [-h] --type {cwv-audit,gsc-performance,indexation,full} [--data DATA] --domain DOMAIN [--output-dir OUTPUT_DIR] [--format {pdf,html,xlsx,both,all}] [--json]` |
| `matomo_auth.py` | Matomo credential management for Claude SEO. | `matomo_auth.py [-h] [--check] [--setup] [--tier] [--json] [--local-target-hint URL]` |
| `matomo_report.py` | Matomo Reporting API client for Claude SEO. | `matomo_report.py [-h] {check,organic,top-pages,device,country,referrers,keywords} ...` |
| `seo_updates.py` | Primary-source Google updates query tool. | `seo_updates.py [-h] [--since SINCE] [--kind {core,spam,core+spam,policy,qrg,product,schema,cwv,discover,documentation}] [--limit LIMIT] [--unverified] [--json]` |

## DataForSEO helpers

| Script | Purpose | Usage |
|---|---|---|
| `dataforseo_costs.py` | DataForSEO API cost estimation, approval, and budget tracking. | `dataforseo_costs.py [-h] {estimate,check,log,summary,today,config,reset} ...` |
| `dataforseo_normalize.py` | Normalize DataForSEO API responses for consistent consumption by claude-seo skills. | *(lib)* |

## Monitoring (drift)

| Script | Purpose | Usage |
|---|---|---|
| `drift_baseline.py` | Capture an SEO baseline snapshot of a page's critical elements. | `drift_baseline.py [-h] [--skip-cwv] url` |
| `drift_compare.py` | Compare current page state to stored baseline and detect SEO drift. | `drift_compare.py [-h] [--skip-cwv] [--baseline-id BASELINE_ID] url` |
| `drift_history.py` | Query drift history for a URL from the SQLite database. | `drift_history.py [-h] [--limit LIMIT] url` |
| `drift_report.py` | Generate an HTML report for SEO drift comparison results. | `drift_report.py [-h] [--stdin] [--output OUTPUT] [file]` |

## Reporting & verification

| Script | Purpose | Usage |
|---|---|---|
| `generate_report.py` | Generate an interactive HTML SEO report. | `generate_report.py [-h] [--output OUTPUT] [--html HTML_OUTPUT] [--markdown MARKDOWN] [--action-plan ACTION_PLAN] [--no-html] [--no-markdown] url` |
| `audit_runner.py` | Run the bundled SEO audit checks and write machine-readable plus report artifacts. | `audit_runner.py [-h] [--json JSON_OUTPUT] [--html HTML] [--markdown MARKDOWN] [--action-plan ACTION_PLAN] [--no-html] [--no-json] [--no-markdown] url` |
| `finding_verifier.py` | Reusable finding verifier. | `finding_verifier.py [-h] [--findings-json FINDINGS_JSON] [--context-json CONTEXT_JSON] [--json]` |

## GitHub repository SEO

| Script | Purpose | Usage |
|---|---|---|
| `github_repo_audit.py` | GitHub Repository SEO Audit | `github_repo_audit.py [-h] [--repo REPO] [--token TOKEN] [--cwd CWD] [--provider {auto,api,gh}] [--json] [--output OUTPUT]` |
| `github_readme_lint.py` | GitHub README SEO Lint | `github_readme_lint.py [-h] [--repo REPO] [--provider {auto,api,gh}] [--token TOKEN] [--intent INTENT] [--json] [--output OUTPUT] [readme_path]` |
| `github_community_health.py` | GitHub Community Health Checker | `github_community_health.py [-h] [--repo REPO] [--token TOKEN] [--cwd CWD] [--provider {auto,api,gh}] [--json] [--output OUTPUT]` |
| `github_search_benchmark.py` | GitHub Search Benchmark | `github_search_benchmark.py [-h] [--repo REPO] [--token TOKEN] [--query QUERY] [--query-file QUERY_FILE] [--per-page PER_PAGE] [--max-pages MAX_PAGES] [--provider {auto,api,gh}] [--json] [--output OUTPUT]` |
| `github_competitor_research.py` | GitHub Competitor Research | `github_competitor_research.py [-h] [--repo REPO] [--token TOKEN] [--query QUERY] [--query-file QUERY_FILE] [--competitor COMPETITOR] [--per-page PER_PAGE] [--max-pages MAX_PAGES] [--top-n TOP_N] [--provider {auto,api,gh}] [--json] [--output OUTPUT]` |
| `github_traffic_archiver.py` | GitHub Traffic Archiver | `github_traffic_archiver.py [-h] [--repo REPO] [--token TOKEN] [--archive-dir ARCHIVE_DIR] [--provider {auto,api,gh}] [--no-write] [--json] [--output OUTPUT]` |
| `github_seo_report.py` | GitHub SEO Report Generator | `github_seo_report.py [-h] [--repo REPO] [--token TOKEN] [--provider {auto,api,gh}] [--readme-path README_PATH] [--query QUERY] [--query-file QUERY_FILE] [--competitor COMPETITOR] [--max-pages MAX_PAGES] [--per-page PER_PAGE] [--competitor-top-n COMPETITOR_TOP_N] [--auto-query-max AUTO_QUERY_MAX] [--archive-dir ARCHIVE_DIR] [--no-archive-write] [--markdown MARKDOWN] [--action-plan ACTION_PLAN] [--json] [--output OUTPUT]` |
| `github_weekly_scorecard.py` | Build a weekly GitHub SEO scorecard from local and API-backed checks. | `github_weekly_scorecard.py [-h] [--repo REPO] [--path PATH] [--token TOKEN] [--provider {auto,api,gh}] [--offline] [--json]` |
| `repo_docs_site_checker.py` | Check repository homepage/docs URLs and install CTA paths. | `repo_docs_site_checker.py [-h] [--repo REPO] [--path PATH] [--homepage HOMEPAGE] [--token TOKEN] [--provider {auto,api,gh}] [--timeout TIMEOUT] [--json]` |
| `repo_file_inventory.py` | Inventory repository SEO, docs, demo, and governance files. | `repo_file_inventory.py [-h] [--path PATH] [--json]` |
| `repo_release_seo.py` | Audit GitHub release cadence and release-note SEO quality. | `repo_release_seo.py [-h] [--repo REPO] [--path PATH] [--token TOKEN] [--provider {auto,api,gh}] [--keyword KEYWORD] [--limit LIMIT] [--json]` |
| `repo_social_preview_checker.py` | Check GitHub repository social-preview readiness signals. | `repo_social_preview_checker.py [-h] [--repo REPO] [--path PATH] [--token TOKEN] [--provider {auto,api,gh}] [--json]` |
| `repo_topic_suggester.py` | Suggest GitHub topics from repository metadata, README, and competitors. | `repo_topic_suggester.py [-h] [--repo REPO] [--path PATH] [--token TOKEN] [--provider {auto,api,gh}] [--competitor COMPETITOR] [--intent-term INTENT_TERM] [--limit LIMIT] [--json]` |

## Image generation (image_gen/)

| Script | Purpose | Usage |
|---|---|---|
| `image_gen/generate.py` | Claude Banana - Direct API Fallback: Image Generation | `generate.py [-h] --prompt PROMPT [--aspect-ratio ASPECT_RATIO] [--resolution RESOLUTION] [--model MODEL] [--api-key API_KEY] [--thinking {minimal,low,medium,high}] [--image-only]` |
| `image_gen/edit.py` | Claude Banana - Direct API Fallback: Image Editing | `edit.py [-h] --image IMAGE --prompt PROMPT [--model MODEL] [--api-key API_KEY]` |
| `image_gen/batch.py` | Claude Banana - CSV Batch Workflow | `batch.py [-h] --csv CSV --model MODEL [--unit-cost UNIT_COST]` |
| `image_gen/presets.py` | Claude Banana - Brand/Style Presets | `presets.py [-h] {list,show,create,delete} ...` |
| `image_gen/cost_tracker.py` | Claude Banana - Cost Tracker | `cost_tracker.py [-h] {log,summary,today,estimate,reset} ...` |
| `image_gen/setup_mcp.py` | Setup script for Claude Banana MCP server in Claude Code. |  |
| `image_gen/validate_setup.py` | Validate that the Claude Banana MCP server is properly configured. | `validate_setup.py [-h]` |

## Shared libraries (imported, not run directly)

| Script | Purpose | Usage |
|---|---|---|
| `url_safety.py` | Canonical URL safety module for claude-seo. | *(lib)* |
| `seo_common.py` | Small shared helpers for standalone SEO CLI scripts. | *(lib)* |
| `env_loader.py` | Lightweight .env loader for Agentic-SEO scripts. | *(lib)* |
| `github_api.py` | Shared GitHub API helpers for repository SEO scripts. | *(lib)* |
| `lib/safe_http.py` | Safe HTTP helpers shared by network-facing SEO scripts. | *(lib)* |
