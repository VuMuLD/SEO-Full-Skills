<!-- Module: schema | Load when: Detect, validate, or generate Schema.org JSON-LD for a supplied page or entity. Use only when structured data or rich-result markup is requested. -->

# Schema Markup Analysis & Generation

## Core principles

1. **Accuracy first** — markup must describe content that is visible on the page; never mark up
   content that does not exist (spam-policy risk, manual action for structured data).
2. **JSON-LD only** in `<head>` or end of `<body>`; one `@graph` per page with stable `@id`s.
3. **Only Google-supported, non-retired types** for rich results; other types are fine for entity
   clarity but promise no SERP feature.
4. **Server-render it** — especially Product/Offer (price, availability).
5. **Validate** (Rich Results Test, validator.schema.org, Search Console enhancement reports).

## Evidence scripts

```bash
python <SKILL_DIR>/scripts/render_page.py <url> --mode auto --json-ld-output found.json --json   # catches JS-injected JSON-LD
python <SKILL_DIR>/scripts/schema_required_props.py <url> --json     # required/recommended props per type
python <SKILL_DIR>/scripts/rich_results_guard.py <url> --json        # retired / ineligible types
python <SKILL_DIR>/scripts/schema_diff.py <url> --type Product --json  # compare against bundled template
python <SKILL_DIR>/scripts/product_schema_checker.py <url> --json    # Product / ProductGroup readiness
python <SKILL_DIR>/scripts/review_schema_checker.py <url> --json     # Review / AggregateRating misuse
python <SKILL_DIR>/scripts/video_schema_checker.py <url> --json      # VideoObject readiness
python <SKILL_DIR>/scripts/validate_schema.py page.html              # local files / pre-commit (exit 2 = block)
```

> **Detection caveat:** many CMS plugins inject JSON-LD with JavaScript, and simple fetch tools
> strip `<script>` tags. Never report "no schema" from raw/stripped HTML alone; confirm with a
> rendered DOM (`render_page.py`), the browser console, or the Rich Results Test.

## Detection

1. Extract JSON-LD with `python <SKILL_DIR>/scripts/parse_html.py --url <url> --json`
   (or scan `<script type="application/ld+json">` in the page source). Flag any
   block without `@context` or `@type`: Google cannot attach it to an entity (a
   rating in such a block does not reach the Product).
2. Check for Microdata (`itemscope`, `itemprop`)
3. Check for RDFa (`typeof`, `property`)
4. Always recommend JSON-LD as primary format (Google's stated preference)

## Validation

- Check required properties per schema type
- Validate against Google's supported rich result types
- Test for common errors:
  - Missing @context
  - Invalid @type
  - Wrong data types
  - Placeholder text
  - Relative URLs (should be absolute)
  - Invalid date formats
- Flag deprecated types (see below)

## Schema Type Status (as of June 2026)

Read `<SKILL_DIR>/references/core/schema-types.md` for the full list and `<SKILL_DIR>/references/schema/deprecated-types-2024-2026.md` for retirements and replacements. Key rules:

### ACTIVE (recommend freely):
Organization, LocalBusiness, SoftwareApplication, WebApplication, Product (with Certification markup as of April 2025), ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

### VIDEO & SPECIALIZED (recommend freely):
BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode

Ready-to-use templates (17 types) live in `<SKILL_DIR>/assets/schema/templates.json`; render one with `python <SKILL_DIR>/scripts/schema_template_generator.py <url-or-file> --json`. High-leverage action types (Reservation, OrderAction, ...) come from `schema_generate.py`.

> **JSON-LD and JavaScript rendering:** Google supports structured data generated with JavaScript, but its "Generate structured data with JavaScript" guide (last updated 2025-12-10) warns that dynamically generated Product markup can make Shopping crawls less frequent and less reliable for fast-changing price and availability. For time-sensitive markup (especially Product, Offer), include JSON-LD in the initial server-rendered HTML.

### NO RICH RESULTS, KEEP IF USEFUL:
- **FAQPage**: Google retired FAQ rich results for ALL sites on May 7, 2026 (supersedes the Aug 2023 gov/health restriction). No Google SERP rich-result benefit; flag existing FAQPage at Info (not Critical) rather than removal. For genuine user Q&A pages, use **QAPage**.

### DEPRECATED (never recommend):
- **HowTo**: Rich results removed September 2023
- **SpecialAnnouncement**: Deprecated July 31, 2025
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired June 2025
- **ClaimReview**: No Search rich result since June 2025. Google's Fact Check Explorer still uses the markup, so fact-checking publishers may keep it; never recommend it for SERP features
- **VehicleListing**: Retired from rich results June 2025
- **Practice Problem**: Deprecation notice 2025-11-05; tooling support removed starting January 2026; documentation removed 2026-01-06
- Search Console / Rich Results Test / appearance-filter support for CourseInfo, ClaimReview, EstimatedSalary, LearningVideo, SpecialAnnouncement, VehicleListing was removed 2025-09-09 (Search Console API through December 2025).

### Still supported (despite earlier phase-out notices):
- **Book Actions**: NOT deprecated. The June 2025 phase-out banner was removed on 2025-11-05 because a Search feature still uses the markup.

### Supported for Dataset Search only:
- **Dataset**: Not discontinued; consumed by Google Dataset Search, with no Google Search rich-result surface. Don't advise removal as if it were killed.

### Still supported (do not flag):
- QAPage (expanded comment-thread properties 2026-03-24), DiscussionForumPosting, Education Q&A (Quiz / `eduQuestionType=Flashcard`). For e-commerce, **hasAdultConsideration** (added 2026-05-20; value `https://schema.org/SexualContentConsideration`) is required for adult products. `Product.category` accepts `Text`, `CategoryCode`, or arrays mixing both.

## Generation

When generating schema for a page:
1. Identify page type from content analysis
2. Select appropriate schema type(s)
3. Generate valid JSON-LD with all required + recommended properties
4. Include only truthful, verifiable data. Use placeholders clearly marked for user to fill
5. Validate output before presenting
6. For review markup, reject fake reviews and undisclosed incentivized reviews.
   An incentive must be clearly and prominently disclosed on the page.

## Common Schema Templates

### Organization
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}
```

### LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
```

### Article/BlogPosting
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}
```

### Connected graph pattern (recommended site-wide)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": "https://example.com/#organization",
     "name": "Example Co", "url": "https://example.com/",
     "logo": {"@type": "ImageObject", "url": "https://example.com/logo.png"},
     "sameAs": ["https://www.linkedin.com/company/example", "https://www.wikidata.org/wiki/Q..."]},
    {"@type": "WebSite", "@id": "https://example.com/#website", "url": "https://example.com/",
     "name": "Example", "alternateName": "Example Co", "publisher": {"@id": "https://example.com/#organization"}},
    {"@type": "WebPage", "@id": "https://example.com/page/#webpage", "url": "https://example.com/page/",
     "isPartOf": {"@id": "https://example.com/#website"},
     "breadcrumb": {"@id": "https://example.com/page/#breadcrumb"}},
    {"@type": "BreadcrumbList", "@id": "https://example.com/page/#breadcrumb",
     "itemListElement": [
       {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
       {"@type": "ListItem", "position": 2, "name": "Page", "item": "https://example.com/page/"}]}
  ]
}
```

`WebSite` drives the site name shown in Google; a `SearchAction` is optional and no longer
produces a sitelinks search box (retired November 2024).

## Implementation by stack

| Stack | How |
|---|---|
| Static / templated HTML | JSON-LD partial per page type, filled from page data |
| Next.js / React | Render `<script type="application/ld+json">` server-side; serialize with `JSON.stringify(data).replace(/</g, '\u003c')` to avoid `</script>` injection |
| WordPress | Yoast / Rank Math / AIOSEO graph; extend via their filters rather than duplicating a second graph |
| Shopify / headless commerce | Theme snippet for Product + Offer + MerchantReturnPolicy; keep price/availability in sync with the feed |
| Programmatic pages | Template the schema with the same data source as the visible content (programmatic.md) |

## Output

- `SCHEMA-REPORT.md`: detection and validation results
- `generated-schema.json`: ready-to-use JSON-LD snippets

### Validation Results
| Schema | Type | Status | Issues |
|--------|------|--------|--------|
| ... | ... | ✅/⚠️/❌ | ... |

### Recommendations
- Missing schema opportunities
- Validation fixes needed
- Generated code for implementation

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL and checking if the page requires authentication. |
| No schema markup found | Report that no JSON-LD, Microdata, or RDFa was detected. Recommend appropriate schema types based on page content analysis. |
| Invalid JSON-LD syntax | Parse and report specific syntax errors (missing brackets, trailing commas, unquoted keys). Provide corrected JSON-LD output. |
| Deprecated schema type detected | Flag the deprecated type with its retirement date. Recommend the current replacement type or advise removal if no replacement exists. |
