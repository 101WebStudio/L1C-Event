"""Legal pages (legal/privacy.html, cookies.html, terms.html) and 404.html."""
from data.legal import LEGAL
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    for key, (title, sections) in LEGAL.items():
        text = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in sections)
        page(key, title, f"{title} for L1C — Level One Connect.", hero(title, "Last updated: September 2026", IM["off"]) + f'<section><div class="wrap art">{text}</div></section>', crumb=[(title, key + ".html")])
    page("404", "Page Not Found", "This page doesn't exist.", f'<section class="nf"><div class="wrap c"><h1>404</h1><h2>This page doesn\'t exist.</h2>{CTA("index.html", "Back to Home")}</div></section>')
