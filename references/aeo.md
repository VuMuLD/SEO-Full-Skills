<!-- Module: aeo | Load when: featured snippet, answer box, People Also Ask (PAA), knowledge panel, zero-click, entity/brand SERP, "AEO". AI Overviews / ChatGPT citation work belongs to geo.md; both share the answer-block pattern. -->

# Answer Engine Optimization (SERP features)

AEO targets answers Google shows **on the results page**: featured snippets, People Also Ask,
knowledge panels, and the brand SERP. GEO (geo.md) targets passages cited inside AI answers.
The same answer-first writing serves both.

| Target | What selects it | Main lever |
|---|---|---|
| Featured snippet | Best direct answer to the exact query, from a page already ranking (usually top 10) | 40-60 word answer right under a matching heading; list/table formats |
| People Also Ask | Semantically related questions | Question-phrased H2/H3 + 30-50 word answer each |
| Knowledge panel | Knowledge Graph entity match | Consistent entity data: Wikidata/Wikipedia, Organization/Person schema with `sameAs`, GBP |
| Brand SERP / site name | Entity + site signals | `WebSite` name/alternateName, Organization logo, consistent naming |
| AI Overview (geo.md) | Passage citability from ranking pages | Answer blocks, sources, freshness |

Retired features — do not recommend: the **sitelinks search box** (removed November 2024;
`SearchAction` markup is harmless but gives no SERP feature) and **FAQ rich results** (removed for
all sites May 7, 2026). HowTo rich results were removed in 2023.

## Evidence

```bash
python <SKILL_DIR>/scripts/answer_block_scanner.py <url> --json   # answer-first paragraphs, lists, tables under headings
python <SKILL_DIR>/scripts/entity_checker.py <url> --json         # Wikidata QID, Wikipedia, sameAs, KG signals
python <SKILL_DIR>/scripts/parse_html.py page.html --url <url> --json
```

Current snippet/PAA ownership needs SERP data: GSC (queries + positions), DataForSEO
`serp_organic_live_advanced` (SERP features), or a manual check. Without it, mark ownership
`Unknown`.

## 1. Featured snippets

The page must already rank on page one for the query; formatting decides *which* ranking page
wins the box.

**Paragraph snippet** (definitions, "what/why" queries)
- [ ] Heading that mirrors the query ("What is X?")
- [ ] First paragraph answers in 40-60 words, starting with the subject: "X is…", "To do X, …"
- [ ] Plain language in the first sentence; detail follows in the next paragraph

**List snippet** (steps, rankings)
- [ ] `<ol>`/`<ul>` directly under the question heading
- [ ] 5-9 items, each ≤ ~12 words; longer lists show "More items" (that can drive clicks)

**Table snippet** (comparisons, prices, specs)
- [ ] Real `<table>` with a `<th>` header row, ≤ 4 columns, entity in the first column

Avoid: answers hidden in tabs/accordions on load, answers inside images, filler intros
("In this article we will…"). To opt a passage out, use `data-nosnippet`; `max-snippet` limits
length.

## 2. People Also Ask

- [ ] Collect 5-8 PAA questions for the primary keyword (SERP, DataForSEO, AlsoAsked, GSC queries)
- [ ] One H2/H3 per question, phrased the way users ask it
- [ ] 30-50 word direct answer immediately below, then supporting detail
- [ ] Mark up genuine user Q&A pages with `QAPage`; FAQPage markup is optional and has no Google rich result

Example:

```html
<h2>How long does a roof replacement take?</h2>
<p>Most residential roof replacements take one to three days. A standard 2,000 sq ft asphalt
roof usually takes one day; steep, multi-layer or tile roofs take two to three days, longer if
rot repairs or rain delays occur.</p>
```

## 3. Knowledge panel & entity signals

- [ ] Wikidata item (QID) with accurate claims and references; Wikipedia article only where the
      entity is genuinely notable (no promotional editing)
- [ ] `Organization` (or `Person`) JSON-LD on the homepage/about page: `name`, `url`, `logo`,
      `sameAs` → Wikidata, Wikipedia, LinkedIn, X, YouTube, Crunchbase, GitHub (only live URLs)
- [ ] Identical entity name everywhere (no "Example Corp" vs "Example Corporation")
- [ ] Google Business Profile claimed with consistent NAP for local entities (local.md)
- [ ] Logo at a stable, crawlable URL; About page stating who, what, where, since when
- [ ] Claim the panel via Google's "Claim this knowledge panel" flow when it appears

## 4. Brand SERP

`WebSite` schema with `name` and `alternateName` on the homepage (site name in results),
Organization logo, consistent titles for the homepage, sitelinks earned through clear navigation
and internal linking (not markup).

## Output

```markdown
## AEO Audit — <URL>
### Featured snippet readiness
- Ownership: Yes/No/Unknown (source)
- Answer block: present/absent — location, word count (target 40-60), format (paragraph/list/table)
### PAA coverage
- Questions found: [...]; covered with heading + direct answer: N/M; gaps: [...]
### Entity / knowledge panel
- Wikidata: QID/absent · Wikipedia: present/absent · sameAs: N (missing: [...]) · name consistency: OK/issues
### Priority fixes (Critical → Low, with confidence labels)
```
