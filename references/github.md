<!-- Module: github | Load when: GitHub repository SEO, repo discoverability in GitHub search and Google, README SEO/conversion, topics/metadata, community health, repo traffic archiving. -->

# GitHub Repository SEO

Apply `<SKILL_DIR>/references/core/audit-rubric.md` for evidence format and
confidence labels, and `<SKILL_DIR>/references/github/readme-audit-rubric.md` for README scoring.
Ranking-factor notes: `<SKILL_DIR>/references/github/github-ranking-factors.md`; API operations
and rate limits: `<SKILL_DIR>/references/github/github-api-ops.md`.

## Trigger Mapping

Use this workflow when the user asks:

- "GitHub SEO"
- "optimize this repo for GitHub search"
- "improve repository discoverability"
- "README SEO audit"
- "topics and metadata optimization"
- "community profile audit"

## Inputs

- Repository URL or slug (`owner/repo`).
- Optional target query set for GitHub search benchmarking.
- Optional GitHub token (`GITHUB_TOKEN` or `GH_TOKEN`) for API checks.

### Auth Setup

Use either environment token or `gh` auth:

```bash
# Option A: token env vars (recommended for automation)
export GITHUB_TOKEN="ghp_xxx"
# or
export GH_TOKEN="ghp_xxx"

# Option B: GitHub CLI login fallback
gh auth login -h github.com
gh auth status -h github.com
```

## Workflow

### 1. Resolve Scope and Access

- Resolve target repo from input or local `origin` remote.
- Check whether token-based API access is available.
- If token is missing/invalid, continue with partial checks and mark API-based
  findings as `Unknown` or `Likely`.
- Generate query/competitor inputs via LLM reasoning and/or web search before
  benchmark stages when possible:
  - query list (`--query` / `--query-file`)
  - optional explicit competitors (`--competitor owner/repo`)
- If queries are not provided, `github_seo_report.py` auto-derives repo-specific
  benchmark queries from repo slug/metadata/title analysis.

### 2. Run Evidence Scripts

Run (all accept `--help`):

```bash
python <SKILL_DIR>/scripts/github_repo_audit.py --repo <owner/repo> --provider auto --json
python <SKILL_DIR>/scripts/github_readme_lint.py README.md --json
python <SKILL_DIR>/scripts/github_community_health.py --repo <owner/repo> --provider auto --json
python <SKILL_DIR>/scripts/github_search_benchmark.py --repo <owner/repo> --query "<llm_or_web_query>" --provider auto --json
python <SKILL_DIR>/scripts/github_competitor_research.py --repo <owner/repo> --query "<llm_or_web_query>" --provider auto --top-n 6 --json
python <SKILL_DIR>/scripts/github_competitor_research.py --repo <owner/repo> --competitor <owner/repo> --competitor <owner/repo> --provider auto --json
python <SKILL_DIR>/scripts/github_traffic_archiver.py --repo <owner/repo> --provider auto --json
python <SKILL_DIR>/scripts/github_seo_report.py --repo <owner/repo> --provider auto --markdown GITHUB-SEO-REPORT.md --action-plan GITHUB-ACTION-PLAN.md
# Optional: cap auto-derived query count used by github_seo_report.py
# python <SKILL_DIR>/scripts/github_seo_report.py --repo <owner/repo> --provider auto --auto-query-max 8 --markdown GITHUB-SEO-REPORT.md --action-plan GITHUB-ACTION-PLAN.md
# Optional explicit verifier step for custom pipelines:
# python <SKILL_DIR>/scripts/finding_verifier.py --findings-json raw-findings.json --json
```

### 3. Analyze by Area

- Metadata discoverability: repo name, description, topics, homepage, social preview.
- Title strategy: underscore vs hyphen checks, intent-keyword extraction, suggested slug/title.
- README SEO and conversion: heading structure, intent alignment, CTAs, proof sections.
- Community trust: governance files and contribution readiness.
- Search benchmarking: target query positions and sampled competitors.
- Competitor research: topic overlaps, README pattern gaps, and strategy opportunities.
- Traffic trend readiness: archival freshness and retention compliance.
- Backlink distribution: channel suggestions (Medium/blog/dev communities), post title ideas, and anchor-mix guidance.

### 4. Prioritize

Classify recommendations:

Use the shared severity scale (Critical / High / Medium / Low / Info): Critical = blocks
discovery, trust, or measurement continuity.

### 5. Output Artifacts

Required for `seo github` runs:

- `GITHUB-SEO-REPORT.md` — findings and evidence.
- `GITHUB-ACTION-PLAN.md` — prioritized fixes.

Optional:

- `GITHUB-WEEKLY-SCORECARD.md` — recurring snapshot (`python <SKILL_DIR>/scripts/github_weekly_scorecard.py --help`; template `<SKILL_DIR>/templates/github/github-weekly-scorecard.md`). Report template: `<SKILL_DIR>/templates/github/github-seo-report.md`.
- Extra checks: `repo_topic_suggester.py`, `repo_social_preview_checker.py`, `repo_release_seo.py`, `repo_docs_site_checker.py`, `repo_file_inventory.py`.

## Delegation Guidance

- Strategy synthesis: `<SKILL_DIR>/agents/seo-github-analyst.md`
- Competitor/query benchmark: `<SKILL_DIR>/agents/seo-github-benchmark.md`
- API collection/archival: `<SKILL_DIR>/agents/seo-github-data.md`
- Final verification: `<SKILL_DIR>/agents/seo-verifier.md`

## Critical Rules

1. Never claim a definitive GitHub ranking formula.
2. Treat token/API failures as environment limitations, not repo defects.
3. Keep topics relevant and capped at 20.
4. Preserve existing project voice/branding in README recommendations.
5. Archive traffic snapshots regularly due 14-day retention windows.
