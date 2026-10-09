"""Page shell, link handling and file output.

Pages are written with simple link names such as href="contact.html" or href="event-<slug>.html".
localize() turns them into the real relative paths for the folder each page lives in.
"""
import re, posixpath
from pathlib import Path
from config import *
from util import e, JS

BASE = Path(__file__).resolve().parent
SITE_DIR = BASE.parent / "site"
TPL_DIR = BASE / "templates"
PAGES = []

def route(name):
    """Page name -> file path inside site/."""
    if name.startswith("event-"): return f"events/{name[6:]}.html"
    if name.startswith("blog-"): return f"blog/{name[5:]}.html"
    return ROUTES.get(name, f"{name}.html")

def canon(path):
    """File path -> public address (folder pages use the folder address)."""
    if path == "index.html": return SITE + "/"
    if path.endswith("/index.html"): return f"{SITE}/{path[:-10]}"
    return f"{SITE}/{path}"

def tpl(name, **ctx):
    text = (TPL_DIR / f"{name}.html").read_text(encoding="utf-8")
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(ctx[m.group(1)]), text)   # a missing value raises an error on purpose

_URL = re.compile(r'(href|src)="([^"]*)"')
def localize(html, out):
    here = posixpath.dirname(out) or "."
    def fix(m):
        attr, url = m.groups()
        if not url or re.match(r"(?:[a-z][a-z0-9+.-]*:|//|#)", url, re.I): return m.group(0)
        path, rest = re.match(r"([^?#]*)(.*)", url).groups()
        target = route(path[:-5]) if path.endswith(".html") else path
        return f'{attr}="{posixpath.relpath(target, here)}{rest}"'
    return _URL.sub(fix, html)

def breadcrumbs(items):
    return JS({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": a, "item": canon(route(b[:-5]))} for n, (a, b) in enumerate([("Home", "index.html")] + items)]})

def page(f, title, desc, body, extra="", img=IM["hero"], crumb=None, og="website"):
    out = route(f)
    full = title if f == "index" else f"{title} | L1C — Level One Connect"
    current = lambda k: f == k or ((f.startswith("event-") or f == "reserve") and k == "events") or (f.startswith("blog-") and k == "blog")
    nav = "".join(f'<li><a href="{k}.html"{" aria-current=page" if current(k) else ""}>{v}</a></li>' for k, v in NAV)
    quick = "".join(f'<li><a href="{k}.html">{"Our Process" if k == "process" else v}</a></li>' for k, v in NAV)
    contact = f'<li>{LOCATION}</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>' + "".join(f'<li><a href="tel:{p.replace(" ", "")}">{p}</a></li>' for p in PHONES)
    html = tpl("layout", title=e(full), description=e(desc), canonical=canon(out), og_type=og, image=e(img),
               schema=JS(ORG) + (breadcrumbs(crumb) if crumb else "") + extra, nav=nav, quick_links=quick,
               contact_items=contact, email=EMAIL, logo_w=NW, logo_h=NH, body=body)
    dest = SITE_DIR / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(localize(html, out), encoding="utf-8")
    PAGES.append(out)

def finish():
    urls = "".join(f"<url><loc>{canon(p)}</loc></url>" for p in sorted(PAGES) if p != "404.html")
    (SITE_DIR / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
    (SITE_DIR / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    (SITE_DIR / ".nojekyll").write_text("")
