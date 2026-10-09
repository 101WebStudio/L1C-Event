"""Process page: process.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    pr = "".join(f'<article class="card rv pr"><span class="n">0{i + 1}</span><h3>{p[1]}</h3><p>{p[2]}</p><ul class="ck">{"".join(f"<li>{x}</li>" for x in p[3])}</ul><p class="tag">Duration: {p[4]}</p></article>' for i, p in enumerate(PROC))
    cs = "".join(f'<article class="card rv"><span class="tag">{c[1]}</span><h3>{c[0]}</h3><p>{c[2]}</p><div class="mt">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in c[3])}</div></article>' for c in CASES)
    page("process", "Our Strategic Event Process", "A systematic four-step approach to delivering exceptional events that drive measurable business results.",
         hero("Our Strategic Event Process", "A systematic approach to delivering exceptional events that drive measurable business results.", IM["cons"]) + f'<section><div class="wrap"><div class="grid2">{pr}</div></div></section><section class="alt"><div class="wrap grid3">{"".join(f"<article class=\"card rv\"><h3>{x}</h3></article>" for x in PRIN)}</div></section><section><div class="wrap">{head("Success Stories")}<div class="grid3">{cs}</div></div></section>' + cta(), crumb=[("Process", "process.html")])
