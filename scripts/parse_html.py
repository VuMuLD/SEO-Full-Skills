#!/usr/bin/env python3
"""
Parse HTML and extract SEO-relevant elements.

Usage:
    python parse_html.py page.html --url https://example.com --json
    python parse_html.py --fetch https://example.com --json   # SSRF-safe fetch + parse
    cat page.html | python parse_html.py --url https://example.com
"""

# Force UTF-8 console output (Windows code pages such as cp1258 cannot print emoji).
import sys as _sys
for _stream in (_sys.stdout, _sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


import argparse
import json
import os
import re
import sys
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 required. Install with: pip install beautifulsoup4")
    sys.exit(1)

try:
    import lxml  # noqa: F401
    _HTML_PARSER = "lxml"
except ImportError:
    _HTML_PARSER = "html.parser"

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
from url_safety import decode_response_text, safe_requests_get  # noqa: E402, I001

# Lazy-loader detection: covers native + the major JS lazy-loaders found on
# WordPress/WooCommerce sites (Perfmatters, EWWW Image Optimizer, generic
# `data-src` patterns). Sites optimized by these plugins strip native
# `loading="lazy"` and replace `src` with a placeholder, so a check on `loading`
# alone reports "not lazy-loaded" when the page is in fact heavily lazy-loaded.
_PERFMATTERS_ATTRS = ("data-perfmatters-src", "data-perfmatters-srcset")
_EWWW_ATTRS = ("data-ewww-src", "data-eio")
_GENERIC_LAZY_ATTRS = ("data-src", "data-lazy-src", "data-original", "data-srcset")
_PERFMATTERS_CLASSES = {"perfmatters-lazy", "perfmatters-lazy-loaded"}
_EWWW_CLASSES = {"lazyload-eio", "lazyloaded-eio"}
_GENERIC_LAZY_CLASSES = {"lazyload", "lazyloaded", "lazy", "lazy-loaded"}


def _has_rel_token(tag, token: str) -> bool:
    """Case-insensitively check whether a tag's ``rel`` attribute carries ``token``.

    bs4 treats ``rel`` as a multi-valued attribute for ``<a>`` and ``<link>``
    tags, splitting it on whitespace into a list. Both the attribute *name*
    (``REL=``) and the surrounding tag name are lower-cased by the underlying
    HTML parser, but the attribute *value* is preserved verbatim, so
    ``rel="Alternate"`` or ``rel="CANONICAL"`` never matched an exact,
    lower-case comparison such as ``soup.find("link", rel="canonical")``.
    """
    rel = tag.get("rel", [])
    if isinstance(rel, str):
        rel = rel.split()
    return any(isinstance(value, str) and value.lower() == token for value in rel or [])


def _detect_lazy_method(img) -> str:
    """Return a coarse classification of the image's lazy-loading mechanism.

    Order of detection: native -> perfmatters -> ewww -> js-generic -> none.
    Specific JS lazy-loaders are checked before the generic bucket so reports
    can attribute the optimization to the right plugin (which informs whether
    a site is using a specific WP optimization stack).

    Returns one of: 'native', 'perfmatters', 'ewww', 'js-generic', 'none'.
    """
    if img.get("loading", "").lower() == "lazy":
        return "native"

    class_list = set(img.get("class", []) or [])

    if any(img.get(a) for a in _PERFMATTERS_ATTRS) or class_list & _PERFMATTERS_CLASSES:
        return "perfmatters"

    if any(img.get(a) for a in _EWWW_ATTRS) or class_list & _EWWW_CLASSES:
        return "ewww"

    if any(img.get(a) for a in _GENERIC_LAZY_ATTRS) or class_list & _GENERIC_LAZY_CLASSES:
        return "js-generic"

    return "none"


def _is_responsive_fill_image(img) -> bool:
    """Next.js ``fill`` images / absolutely positioned cover images size from their container."""
    if img.get("data-nimg") == "fill":
        return True
    style = re.sub(r"\s+", "", (img.get("style") or "").lower())
    return "position:absolute" in style and "width:100%" in style and "height:100%" in style


_RESOURCE_HINTS = ("preload", "preconnect", "dns-prefetch", "prefetch", "prerender", "modulepreload")


def parse_html(html: str, base_url: Optional[str] = None, headers: Optional[dict] = None) -> dict:
    """
    Parse HTML and extract SEO-relevant elements.

    Args:
        html: HTML content to parse
        base_url: Base URL for resolving relative links

    Returns:
        Dictionary with extracted SEO data
    """
    soup = BeautifulSoup(html, _HTML_PARSER)
    header_lookup = {str(k).lower(): v for k, v in (headers or {}).items()}

    result = {
        "title": None,
        "meta_description": None,
        "meta_robots": None,
        "x_robots_tag": header_lookup.get("x-robots-tag"),
        "canonical": None,
        "lang": None,
        "charset": None,
        "viewport": None,
        "favicon": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "h4": [],
        "h5": [],
        "h6": [],
        "images": [],
        "links": {
            "internal": [],
            "external": [],
        },
        "pagination": {"prev": None, "next": None},
        "resource_hints": {hint: [] for hint in _RESOURCE_HINTS},
        "schema": [],
        "open_graph": {},
        "twitter_card": {},
        "word_count": 0,
        "hreflang": [],
    }

    html_tag = soup.find("html")
    if html_tag:
        result["lang"] = html_tag.get("lang")

    # Title
    title_tag = soup.find("title")
    if title_tag:
        result["title"] = title_tag.get_text(strip=True)

    # Meta tags
    for meta in soup.find_all("meta"):
        name = meta.get("name", "").lower()
        property_attr = meta.get("property", "").lower()
        content = meta.get("content", "")

        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content
        elif name == "viewport":
            result["viewport"] = content

        if meta.get("charset"):
            result["charset"] = meta.get("charset")
        elif meta.get("http-equiv", "").lower() == "content-type":
            charset_match = re.search(r"charset=([^;\s]+)", content, re.I)
            if charset_match:
                result["charset"] = charset_match.group(1)

        # Open Graph
        if property_attr.startswith("og:"):
            result["open_graph"][property_attr] = content

        # Twitter Card
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    # Canonical
    canonical = next(
        (link for link in soup.find_all("link") if _has_rel_token(link, "canonical")), None
    )
    if canonical:
        result["canonical"] = canonical.get("href")

    # Favicon, pagination, resource hints
    for link in soup.find_all("link"):
        href = link.get("href")
        if not href:
            continue
        absolute = urljoin(base_url, href) if base_url else href
        if result["favicon"] is None and (
            _has_rel_token(link, "icon") or _has_rel_token(link, "apple-touch-icon")
        ):
            result["favicon"] = absolute
        for rel_name in ("prev", "next"):
            if _has_rel_token(link, rel_name) and result["pagination"][rel_name] is None:
                result["pagination"][rel_name] = absolute
        for hint in _RESOURCE_HINTS:
            if _has_rel_token(link, hint):
                result["resource_hints"][hint].append({
                    "href": absolute,
                    "as": link.get("as"),
                    "type": link.get("type"),
                    "crossorigin": link.get("crossorigin"),
                    "fetchpriority": link.get("fetchpriority"),
                })

    # Hreflang
    for link in soup.find_all("link"):
        if not _has_rel_token(link, "alternate"):
            continue
        hreflang = link.get("hreflang")
        if hreflang:
            result["hreflang"].append({
                "lang": hreflang,
                "href": link.get("href"),
            })

    # Headings
    for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                result[tag].append(text)
                # Flag suspiciously short or purely numeric headings (likely counters/stats)
                stripped = text.strip()
                is_suspicious = (
                    len(stripped) <= 3
                    or stripped.replace(",", "").replace(".", "").replace("+", "").replace("-", "").replace("%", "").replace(" ", "").isdigit()
                )
                if is_suspicious:
                    key = f"{tag}_suspicious"
                    if key not in result:
                        result[key] = []
                    result[key].append(text)

    # Images
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src:
            src = urljoin(base_url, src)

        result["images"].append({
            "src": src,
            "alt": img.get("alt"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
            "lazy_method": _detect_lazy_method(img),
            "srcset": img.get("srcset") or img.get("data-srcset"),
            "sizes": img.get("sizes"),
            "fetchpriority": img.get("fetchpriority"),
            "is_responsive_fill": _is_responsive_fill_image(img),
        })

    # Links
    if base_url:
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue

            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            link_data = {
                "href": full_url,
                "text": a.get_text(strip=True)[:100],
                "rel": a.get("rel", []),
            }

            if parsed.netloc == base_domain:
                result["links"]["internal"].append(link_data)
            else:
                result["links"]["external"].append(link_data)

    # Schema (JSON-LD)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            schema_data = json.loads(script.string)
            # Flatten @graph containers so each @type is a separate entry
            if isinstance(schema_data, dict) and "@graph" in schema_data:
                for item in schema_data["@graph"]:
                    if isinstance(item, dict):
                        result["schema"].append(item)
            elif isinstance(schema_data, list):
                for item in schema_data:
                    if isinstance(item, dict):
                        result["schema"].append(item)
            else:
                result["schema"].append(schema_data)
        except (json.JSONDecodeError, TypeError):
            pass

    # Word count (visible text only)
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r"\b\w+\b", text)
    result["word_count"] = len(words)

    return result


def main():
    parser = argparse.ArgumentParser(description="Parse HTML for SEO analysis")
    parser.add_argument("file", nargs="?", help="HTML file to parse")
    parser.add_argument("--url", "-u", help="Base URL for resolving links")
    parser.add_argument("--fetch", help="Fetch (SSRF-safe) and parse a URL directly")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="Fetch timeout in seconds")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    headers = {}

    if args.fetch:
        try:
            resp = safe_requests_get(args.fetch, timeout=args.timeout, allow_redirects=True)
        except Exception as exc:  # network / URL-safety refusal
            print(f"Error fetching {args.fetch}: {exc}", file=sys.stderr)
            sys.exit(1)
        html = decode_response_text(resp)
        headers = dict(resp.headers)
        args.url = args.url or resp.url
    elif args.file:
        real_path = os.path.realpath(args.file)
        if not os.path.isfile(real_path):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(real_path, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()
        if not html and args.url:
            resp = safe_requests_get(args.url, timeout=30, allow_redirects=True)
            html = decode_response_text(resp)
            args.url = resp.url

    result = parse_html(html, args.url, headers=headers)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Title: {result['title']}")
        print(f"Meta Description: {result['meta_description']}")
        print(f"Canonical: {result['canonical']}")
        print(f"H1 Tags: {len(result['h1'])}")
        print(f"H2 Tags: {len(result['h2'])}")
        print(f"Images: {len(result['images'])}")
        print(f"Internal Links: {len(result['links']['internal'])}")
        print(f"External Links: {len(result['links']['external'])}")
        print(f"Schema Blocks: {len(result['schema'])}")
        print(f"Word Count: {result['word_count']}")


if __name__ == "__main__":
    main()
