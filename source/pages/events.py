"""Events: the listing (events/index.html) and one page per event, all built from templates/event.html."""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    SEARCH = '<section class="sb"><div class="wrap"><form class="sbar" role="search"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="es" type="search" placeholder="Search events by name, city or category" aria-label="Search events" autocomplete="off"></form><p id="ecount" class="mut" role="status" aria-live="polite"></p></div></section>'
    sec = lambda t, l: f'<section class="evs"><div class="wrap">{head(t)}<div class="elist">{"".join(erow(v) for v in l) or "<p>No events at the moment.</p>"}</div></div></section>'
    page("events", "Events", "Upcoming, featured and past executive networking events, summits and dinners by L1C — Level One Connect.",
         hero("Events", "Executive networking, conferences, leadership dinners and business summits.", IM["net"]) + SEARCH + sec("Upcoming Events", [v for v in EVENTS if v["st"] == "upcoming"]) + '<div class="alt">' + sec("Featured Events", [v for v in EVENTS if v["st"] == "featured"]) + "</div>" + sec("Past Events", [v for v in EVENTS if v["st"] == "past"]), crumb=[("Events", "events.html")])

    for v in EVENTS:
        past = v["st"] == "past"
        reserve = ('<p class="mut">This event has taken place.</p>' + CTA("events.html", "See upcoming events")) if past \
            else CTA(v.get("reg", f'reserve.html?event={v["s"]}'), "Reserve a Seat")
        speakers = "<ul class=ck>" + "".join(f"<li>{e(x)}</li>" for x in v["sp"]) + "</ul>" if v.get("sp") else '<p class="mut">Speakers to be announced.</p>'
        agenda = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in v.get("ag", [(v["tm"], "Welcome & arrival"), ("+1h", "Keynote / opening conversation"), ("+2h", "Roundtables & networking")]))
        gallery = "".join(f'<div class="pic rv"><img src="{x}" alt="Event photography" loading="lazy" width="600" height="400"></div>' for x in v.get("gal", (IM["dinner"], IM["net"], IM["conf"])))
        schema = {"@context": "https://schema.org", "@type": "Event", "name": v["t"], "startDate": f'{v["d"]}T{v["tm"]}', "location": {"@type": "Place", "name": v["l"]},
                  "description": v["ds"], "image": v["i"], "organizer": {"@type": "Organization", "name": "Level One Connect", "url": SITE}}
        body = tpl("event", category=e(v["c"]), title=e(v["t"]), date=fd(v["d"]), time=v["tm"], location=e(v["l"]), description=e(v["ds"]),
                   speakers=speakers, agenda=agenda, gallery=gallery, reserve=reserve)
        page("event-" + v["s"], v["t"], v["ds"], body, JS(schema), v["i"], [("Events", "events.html"), (v["t"], f'event-{v["s"]}.html')])
