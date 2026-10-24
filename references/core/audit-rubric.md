<!-- Updated: 2026-10-23 -->

# Audit Rubric (applies to every module)

One evidence standard for full-site audits, single pages, articles, and every narrow module.

## 1. Scope

State it in the first paragraph: `full-site` · `single-page` · `article` · `module:<name>`.

## 2. Evidence standard

Every finding carries:

- **Finding** — one sentence
- **Evidence** — observable proof: HTML element, header, metric, URL, script output
- **Impact** — consequence for indexing, ranking, CTR, UX, crawl efficiency, or AI citation
- **Fix** — a concrete implementation step (copy-paste code where possible)

Missing evidence → `Unknown`, never a guess.

## 3. Confidence labels

- `Confirmed` — directly observed in source or script output
- `Likely` — strong signal, incomplete verification (e.g. script failed, LLM read of the page)
- `Hypothesis` — plausible, needs another check

Never present `Likely` or `Hypothesis` as fact.

## 4. Severity (one scale for all modules)

| Severity | Meaning | Fix window |
|---|---|---|
| **Critical** | Blocks indexing/rendering, causes a penalty or spam-policy violation, breaks required schema | Now |
| **High** | Significant ranking / CTR / citation impact | ≤ 1 week |
| **Medium** | Optimization opportunity with measurable impact | ≤ 1 month |
| **Low** | Nice to have | Backlog |
| **Info** | Context, not applicable, or retired feature (e.g. existing FAQPage) | — |
| **Pass** | Meets the baseline (show in tables, not in the action plan) | — |

Escalate to Critical only with clear evidence of a direct search-impacting failure.

## 5. Prioritization

Rank by Impact × (1 / Effort), respecting dependencies (fix indexation before content, fix
rendering before schema). Tag each action: `Quick win` (high impact, low effort) ·
`Strategic` (high impact, higher effort) · `Maintenance`.

Each recommendation in a full audit also carries: the first-principle observation (THINK),
its dependency/unblock relation (CONNECT-system), a falsifiability check — "how would we know
this failed?" (ACCEPT) — and a leading indicator to watch (GROW).

## 6. Scoring protocol

Scores are directional summaries, not truth. For each scored category:

1. List up to 5 positive signals, each with evidence.
2. List up to 5 deficits, each with evidence.
3. `base = positives / (positives + deficits) × 100`
4. `final = max(0, base − 15 × Critical − 5 × High − 2 × Medium)`, penalty capped at −50.
5. One justification sentence: what raised it, what lowered it.

Cannot complete steps 1-3 → `Score: Insufficient data`. Partial data → `Score confidence: Low`.
No decimal "precision theater".

## 7. Output contract

A. **Summary** — scope, score/band, top 3 issues, top 3 opportunities
B. **Findings table** — Area · Severity · Confidence · Finding · Evidence · Fix
C. **Action plan** — blockers → quick wins → strategic
D. **Unknowns & follow-ups** — checks that would move Likely/Hypothesis to Confirmed
E. **Environment limitations** — checks that could not run, and why

Finding block:

```text
[Area] <name>
Severity: <Critical|High|Medium|Low|Info>   Confidence: <Confirmed|Likely|Hypothesis>
Finding: <one sentence>
Evidence: <specific proof>
Impact: <why it matters>
Fix: <implementation step>
```

## 8. Anti-hallucination guardrails

Never claim without data: rankings, traffic, penalties/manual actions, PSI/CrUX values,
search volumes, competitor facts, AI-citation uplift, or the cause of a traffic change.
Never promise rankings, clicks, indexing, or AI citations. Say exactly which data is missing
and how to collect it. Third-party statistics are labelled as such, with their source.

## 9. Verification before reporting

Run the verifier (`<SKILL_DIR>/agents/seo-verifier.md`;
`python <SKILL_DIR>/scripts/finding_verifier.py --findings-json raw.json --json`):
dedupe same-root-cause findings, drop contradicted ones (log why), downgrade evidence-free
ones, and keep environment limitations out of the defect list.
