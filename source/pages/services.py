"""Services page: services.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    SVL = ["start-your-event.html?type=Conference+%2F+Summit", "start-your-event.html?type=Executive+Networking", "contact.html"]
    sv = ""
    for i, s in enumerate(SERV):
        sv += f'<section class="{"alt" if i % 2 else ""}"><div class="wrap two-col {"rev" if i % 2 else ""}"><div class="rv pic"><img src="{s[5]}" alt="{s[0]}" loading="lazy" width="900" height="700"></div><div class="rv"><h2>{s[0]}</h2><p>{s[1]}</p><ul class="ck">{"".join(f"<li>{x}</li>" for x in s[4])}</ul>{CTA(SVL[i], s[3])}</div></div></section>'
    sv += f'<section class="dark"><div class="wrap">{head("Additional Services")}<div class="grid3">{"".join(f"<article class=card><h3>{a}</h3><p>{b}</p></article>" for a, b in EXTRA)}</div></div></section><section class="cta"><div class="wrap rv"><h2>Ready to Transform Your Next Event?</h2>{CTA("start-your-event.html", "Get Started Today")}</div></section>'
    page("services", "Our Premium Event Services", "Corporate event planning, executive networking and strategic event consulting from L1C — Level One Connect.", hero("Our Premium Event Services", "Comprehensive event solutions designed to elevate your corporate gatherings and maximize ROI.", IM["conf"]) + sv, crumb=[("Services", "services.html")])
