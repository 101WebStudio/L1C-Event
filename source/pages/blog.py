"""Blog: the listing (blog/index.html) and one page per article, all built from templates/post.html."""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    page("blog", "Insights & Perspectives", "Articles on event strategy, executive networking, leadership and technology from L1C — Level One Connect.",
         hero("Insights &amp; Perspectives", "Event strategy, executive networking, leadership, technology and industry insights.", IM["off"]) + f'<section><div class="wrap"><p class="cats">{"".join(f"<span class=tag>{c}</span>" for c in ("Event Strategy", "Executive Networking", "Leadership", "Technology", "Corporate Events", "Industry Insights"))}</p><div class="grid3">{"".join(bcard(p) for p in POSTS)}</div></div></section>', crumb=[("Blog", "blog.html")])

    for p in POSTS:
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": p["t"], "datePublished": p["d"],
                  "author": {"@type": "Organization", "name": "L1C — Level One Connect"}, "image": p["i"], "publisher": {"@type": "Organization", "name": "Level One Connect"}}
        related = "".join(bcard(x) for x in [y for y in POSTS if y is not p][:2])
        body = tpl("post", category=e(p["c"]), title=e(p["t"]), meta=f'By the L1C team · {fd(p["d"])} · {p["r"]} min read', image=p["i"],
                   paragraphs="".join(f"<p>{e(x)}</p>" for x in p["b"]), related=related, cta=cta())
        page("blog-" + p["s"], p["t"], p["ex"], body, JS(schema), p["i"], [("Blog", "blog.html"), (p["t"], f'blog-{p["s"]}.html')], "article")
