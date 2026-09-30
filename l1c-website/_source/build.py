import os, json, shutil, glob, zipfile, html as H
SITE = "https://www.l1c.example"  # CONFIG: your real domain
EMAIL = "info@l1c.example"        # CONFIG: your real L1C email
PHONES = ["+383 49 620 196", "+383 49 222 951"]
OUT = "site"
U = lambda i: f"https://images.unsplash.com/photo-{i}?auto=format&fit=crop&w=1600&q=75"
IM = dict(hero=U("1511795409834-ef04bbd61622"), team=U("1556761175-5973dc0f32e7"), net=U("1511578314322-379afb476865"),
          conf=U("1505373877841-8d25f7d46678"), conf2=U("1540575467063-178a50c2df87"), dinner=U("1519167758481-83f550bb49b3"),
          dine2=U("1414235077428-338989a2e8c0"), cons=U("1486406146926-c627a92ad1ab"), off=U("1477959858617-67f85cf4f1df"),
          lights=U("1492684223066-81342ee5ff30"), nyc=U("1480714378408-67cf0d13bc1b"), lon=U("1513635269975-59663e0ac1ad"),
          dxb=U("1512453979798-5ea266f8880c"), par=U("1502602898657-3e91760cbb34"))
e = H.escape
THEME = '''<script>document.documentElement.classList.add("js");try{document.documentElement.dataset.theme=localStorage.getItem("l1c-theme")||(matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light")}catch(e){document.documentElement.dataset.theme="light"}</script>'''
TT = '<button id="tt" class="tt" type="button" aria-label="Switch between dark and light mode"><svg class="moon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>'
CSS = open("style.css").read()
APP = open("app.js").read()
CFG = 'window.L1C_ENDPOINT = ""; /* set your form endpoint URL here; no secrets */ window.L1C_EMAIL = "' + EMAIL + '";'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + "/assets")
if os.path.exists("logo.png"):  # official L1C logo, used unchanged
    shutil.copy("logo.png", f"{OUT}/assets/logo.png"); LOGO = "assets/logo.png"
else:
    LOGO = "assets/logo.svg"
    open(f"{OUT}/assets/logo.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 40"><text x="0" y="31" font-family="Inter,Arial,sans-serif" font-weight="800" font-size="34" fill="#fff">L1<tspan fill="#5170FF">C</tspan></text></svg>')

import base64
LOGO_URI = "data:image/png;base64," + base64.b64encode(open("logo-inline.png", "rb").read()).decode() if os.path.exists("logo-inline.png") else LOGO
b64 = lambda f: "data:image/png;base64," + base64.b64encode(open(f, "rb").read()).decode()
LOGO_NAV, LOGO_FAV = b64("logo-nav.png"), b64("logo-fav.png")
NH = 38; NW = round(NH * 188 / 76)
NAV = [("index", "Home"), ("services", "Services"), ("about", "About"), ("process", "Process"), ("events", "Events"), ("blog", "Blog"), ("contact", "Contact")]
EVENTS = [
 dict(s="executive-leaders-dinner", t="Executive Leaders Dinner", c="Leadership Dinners", d="2026-11-12", tm="19:00", l="Prishtina, Kosovo", st="upcoming", i=IM["dinner"], ds="An invitation-only dinner where senior leaders exchange ideas in an intimate setting."),
 dict(s="technology-leadership-summit", t="Technology Leadership Summit", c="Business Summits", d="2027-02-18", tm="09:00", l="Tirana, Albania", st="featured", i=IM["conf"], ds="A one-day summit for technology and business decision-makers on strategy and growth."),
 dict(s="executive-networking-evening", t="Executive Networking Evening", c="Executive Networking", d="2027-04-22", tm="18:30", l="Vienna, Austria", st="upcoming", i=IM["net"], ds="A curated evening connecting decision-makers across industries."),
 dict(s="leaders-roundtable-series", t="Leaders Roundtable Series", c="Leadership Dinners", d="2026-12-03", tm="19:00", l="Prishtina, Kosovo", st="upcoming", i=IM["dine2"], ds="A small-group roundtable dinner for senior leaders to discuss the decisions shaping their industries."),
 dict(s="cx-ai-executive-forum", t="CX & AI Executive Forum", c="Technology Events", d="2027-03-10", tm="10:00", l="Munich, Germany", st="upcoming", i=IM["cons"], ds="An executive forum on customer experience and AI, for technology and CX decision-makers."),
 dict(s="annual-business-conference", t="Annual Business Conference", c="Conferences", d="2027-05-14", tm="09:30", l="Skopje, North Macedonia", st="featured", i=IM["conf2"], ds="A full-day conference bringing together business leaders, partners and sponsors."),
 dict(s="product-launch-evening", t="Product Launch Evening", c="Product Launches", d="2027-06-04", tm="18:00", l="Prishtina, Kosovo", st="upcoming", i=IM["lights"], ds="An evening launch experience for invited partners, press and clients."),
 dict(s="executive-dinner-series-2025", t="Executive Dinner Series 2025", c="Leadership Dinners", d="2025-05-15", tm="19:30", l="Prishtina, Kosovo", st="past", i=IM["dine2"], ds="A dinner series that brought senior leaders together for candid conversations."),
 dict(s="regional-tech-meetup", t="Regional Tech Meetup", c="Technology Events", d="2025-03-20", tm="17:30", l="Tirana, Albania", st="past", i=IM["off"], ds="A meetup for technology leaders and partners across the region."),
 dict(s="regional-product-showcase", t="Regional Product Showcase", c="Product Launches", d="2025-10-09", tm="17:00", l="Prishtina, Kosovo", st="past", i=IM["lights"], ds="A showcase event bringing partners and press together for a product reveal."),
]
POSTS = [
 dict(s="designing-events-that-lead-to-decisions", t="Designing Events That Lead to Decisions", c="Event Strategy", d="2026-09-10", r=5, i=IM["cons"], ex="Why the best executive events start with the outcome, not the venue.",
      b=["Every strong event begins with a clear question: what should be different for attendees and for the organiser once the event is over?", "Start with objectives and audience, then design the format, agenda and room around them. Small, well-curated groups tend to produce better conversations than large, unfocused ones.", "Finally, plan the follow-up before the event starts. Introductions and next steps are where an event turns into business value."]),
 dict(s="what-makes-executive-networking-work", t="What Makes Executive Networking Work", c="Executive Networking", d="2026-08-21", r=4, i=IM["net"], ex="Curation, format and follow-up: three levers behind meaningful connections.",
      b=["Senior leaders value their time. The right guest list matters more than the size of the guest list.", "Structured formats such as seated dinners and roundtables create natural conversation and reduce small talk.", "A short, personal follow-up after the event helps relationships continue."]),
 dict(s="measuring-event-roi", t="Measuring Event ROI Without the Guesswork", c="Corporate Events", d="2026-07-02", r=6, i=IM["off"], ex="Define success metrics early and measure what matters to your business.",
      b=["ROI starts in the planning phase. Agree which outcomes matter: pipeline, partnerships, brand reach or relationships.", "Pick a few measurable indicators and collect them consistently, before, during and after the event.", "Use the results to improve the next event. Continuous improvement is where measurement pays off."]),
]
SERV = [("Corporate Event Planning", "From product launches to annual conferences, we design and execute events that align with your brand identity and business objectives, ensuring seamless experiences that exceed expectations.", "Learn More", "Inquire About Corporate Events", ["Full-Service Planning", "Brand Integration", "Vendor Management", "Budget Management", "ROI Tracking"], IM["conf"]),
 ("Executive Networking", "Strategic gatherings designed to connect industry leaders, decision-makers from Fortune 500 companies, and influencers. We create environments for meaningful business relationships that drive growth and opportunity.", "Explore Networking", "Plan a Networking Event", ["Targeted Invitations", "Strategic Matchmaking", "Industry-Specific Events", "Follow-up Support", "Exclusive Venues"], IM["net"]),
 ("Strategic Event Consulting", "Expert guidance on event strategy, audience engagement, and ROI measurement. We ensure your events deliver tangible business results and strengthen your organization's market position.", "Get Consultation", "Schedule a Consultation", ["Event Strategy Development", "Audience Analysis", "Technology Integration", "Sustainability Planning", "Crisis Management"], IM["cons"])]
EXTRA = [("Speaker Management", "Comprehensive speaker coordination including sourcing, contracting, briefing, and logistics."), ("Hybrid Event Production", "Seamless integration of in-person and virtual components."), ("Post-Event Analysis", "Comprehensive reporting and analysis to measure ROI and gather attendee feedback."), ("Team Building Events", "Customized team building experiences."), ("Award Ceremonies", "Premium award ceremonies recognizing achievement."), ("International Events", "Global event management with cross-cultural communication and international logistics expertise.")]
PROC = [("Discovery & Strategy", "Discovery & Strategy Development", "We begin by understanding your business objectives, target audience, and desired outcomes to create a strategic event blueprint.", ["Initial Consultation", "Audience Analysis", "Goal Setting", "Budget Planning"], "2–4 Weeks"),
 ("Concept Development", "Concept & Design Phase", "Our creative team designs a unique event concept tailored to your specific requirements, audience, and brand identity.", ["Creative Concepting", "Brand Integration", "Venue Selection", "Program Design"], "3–6 Weeks"),
 ("Planning & Coordination", "Planning & Coordination", "Meticulous planning of every detail, from venue selection and speaker coordination to logistics and technology setup.", ["Detailed Planning", "Logistics Management", "Technology Setup", "Speaker Management"], "4–12 Weeks"),
 ("Execution & Management", "Execution & Post-Event Analysis", "On-site management ensuring flawless execution, seamless attendee experience, and real-time problem-solving.", ["On-Site Management", "Attendee Experience", "Real-time Adjustments", "ROI Measurement"], "2–4 Weeks Post-Event")]
PRIN = ["Strategic Alignment", "Collaborative Approach", "Data-Driven Decisions", "Risk Management", "Continuous Improvement", "Sustainability Focus"]
CASES = [("Kosovo Tech Summit 2023", "Technology Conference", "500+ industry leaders from across the Balkan region.", [("92%", "Attendee Satisfaction"), ("45+", "Partnerships Formed"), ("280%", "ROI Achieved")]),
 ("Balkan Business Leaders Forum", "Executive Networking", "150+ C-level executives from four countries.", [("85%", "New Connections"), ("€2.3M", "Deals Facilitated"), ("97%", "Would Attend Again")]),
 ("Innovate Kosovo Product Reveal", "Product Launch", "A multi-sensory product launch for a leading technology company.", [("150%", "Media Coverage"), ("3.2K", "Social Media Reach"), ("€850K", "Pre-orders Generated")])]
STATS = [("100", "+", "Events Successfully Managed"), ("98", "%", "Client Satisfaction Rate"), ("1000", "+", "Executives Connected"), ("120", "+", "Corporate Partners")]
ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Level One Connect", "alternateName": "L1C", "url": SITE, "logo": f"{SITE}/{LOGO}",
       "description": "Premium corporate event management and executive networking company.", "address": {"@type": "PostalAddress", "addressLocality": "Prishtina", "addressCountry": "XK"}, "telephone": PHONES[0], "email": EMAIL}
fd = lambda d: __import__("datetime").date.fromisoformat(d).strftime("%d %b %Y")
CTA = lambda h, t, cls="btn": f'<a class="{cls}" href="{h}">{t}</a>'
JS = lambda o: f'<script type="application/ld+json">{json.dumps(o)}</script>'

def crumbs(items):
    return JS({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": a, "item": f"{SITE}/{b}"} for n, (a, b) in enumerate(items)]})

def page(f, title, desc, body, extra="", img=IM["hero"], crumb=None, og="website"):
    nav = "".join(f'<li><a href="{k}.html"{" aria-current=page" if f == k or (f.startswith("event-") and k == "events") or (f.startswith("blog-") and k == "blog") else ""}>{v}</a></li>' for k, v in NAV)
    fl = "".join(f'<li><a href="{k}.html">{v if k != "process" else "Our Process"}</a></li>' for k, v in NAV)
    can = f"{SITE}/{'' if f == 'index' else f + '.html'}"
    full = f"{title} | L1C — Level One Connect" if f != "index" else title
    cr = crumbs([("Home", "")] + crumb) if crumb else ""
    out = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(full)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{can}">

<meta name="referrer" content="strict-origin-when-cross-origin"><meta name="theme-color" content="#000000">
<meta property="og:type" content="{og}"><meta property="og:site_name" content="L1C — Level One Connect"><meta property="og:title" content="{e(full)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{can}"><meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(full)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{img}">
<link rel="icon" type="image/png" href="{LOGO_FAV}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"><style>{CSS}</style>
{JS(ORG)}{cr}{extra}{THEME}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header id="hd"><div class="wrap bar"><a class="logo" href="index.html" aria-label="L1C — Level One Connect, home"><img src="{LOGO_NAV}" alt="L1C — Level One Connect" class="lg" width="{NW}" height="{NH}"></a>
<nav aria-label="Main"><ul id="menu">{nav}<li class="mcta"><a class="btn" href="contact.html">Start Your Event</a></li></ul></nav>
<a class="btn hcta" href="contact.html">Start Your Event</a>{TT}<button id="mb" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span></button></div></header>
<main id="main">{body}</main>
<footer><div class="wrap fg"><div><a class="logo" href="index.html"><img src="{LOGO_NAV}" alt="L1C — Level One Connect" class="lg" width="{NW}" height="{NH}" loading="lazy"></a><p class="fn">Level One Connect</p><p class="mut">Executive networking across industries and decision-makers.</p></div>
<div><h3>Quick Links</h3><ul>{fl}</ul></div><div><h3>Legal</h3><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms &amp; Conditions</a></li><li><a href="cookies.html">Cookie Policy</a></li></ul></div>
<div><h3>Contact</h3><ul><li>Prishtina, Kosovo</li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>{"".join(f'<li><a href="tel:{p.replace(" ", "")}">{p}</a></li>' for p in PHONES)}</ul></div></div>
<div class="wrap fb"><p>© 2026 L1C — Level One Connect. All rights reserved.</p><p>Website crafted by <a href="https://101webstudio.github.io/" target="_blank" rel="noopener noreferrer">101WebStudio</a></p></div></footer>
<script>{CFG}
{APP}</script></body></html>'''
    open(f"{OUT}/{f}.html", "w", encoding="utf-8").write(out)

def hero(h, sub, im, eyebrow=""):
    return f'<section class="ph glow"><div class="wrap"><p class="eb">{eyebrow}</p><h1>{h}</h1><p class="lead">{sub}</p></div></section>'
def head(t, s="", c=""):
    return f'<div class="sh rv {c}"><h2>{t}</h2>{f"<p>{s}</p>" if s else ""}</div>'
def scard(i, s):
    return f'<article class="card rv"><span class="n">0{i + 1}</span><h3>{s[0]}</h3><p>{s[1]}</p><a class="lk" href="services.html">{s[2]} →</a></article>'
def stats():
    return '<section class="dark"><div class="wrap sg">' + "".join(f'<div class="rv"><b data-n="{n}" data-s="{s}">{n}{s}</b><span>{l}</span></div>' for n, s, l in STATS) + '</div></section>'
def ecard(v):
    return f'<article class="card ev rv"><a href="event-{v["s"]}.html" class="im"><img src="{v["i"]}" alt="{e(v["t"])}" loading="lazy" width="800" height="500"></a><div class="cb"><span class="tag">{v["c"]}</span><h3><a href="event-{v["s"]}.html">{v["t"]}</a></h3><p class="mut">{fd(v["d"])} · {v["tm"]} · {v["l"]}</p><p>{v["ds"]}</p><a class="lk" href="event-{v["s"]}.html">View Event →</a></div></article>'
def erow(v):
    return f'<article class="card ec rv"><a class="eth" href="event-{v["s"]}.html" tabindex="-1" aria-hidden="true"><img src="{v["i"]}" alt="" loading="lazy" width="400" height="225"></a><div class="ecb"><span class="tag">{v["c"]}</span><h3><a href="event-{v["s"]}.html">{v["t"]}</a></h3><p>{fd(v["d"])} · {v["tm"]} · {v["l"]}</p><a class="btn sm ghost dk" href="event-{v["s"]}.html">View Event</a></div></article>'
def bcard(p):
    return f'<article class="card ev rv"><a href="blog-{p["s"]}.html" class="im"><img src="{p["i"]}" alt="{e(p["t"])}" loading="lazy" width="800" height="500"></a><div class="cb"><span class="tag">{p["c"]}</span><p class="mut">{fd(p["d"])} · {p["r"]} min read</p><h3><a href="blog-{p["s"]}.html">{p["t"]}</a></h3><p>{p["ex"]}</p><a class="lk" href="blog-{p["s"]}.html">Read Article →</a></div></article>'
def cta():
    return f'<section class="dark cta"><div class="wrap rv"><h2>Let\'s Create Something Exceptional Together</h2><p class="lead">Whether you\'re planning a conference, executive networking event, or corporate gathering, our team is ready to help you create an unforgettable experience that delivers real business value.</p><div class="row">{CTA("contact.html", "Start Your Event Journey")}{CTA("contact.html#form", "Contact Our Team", "btn ghost")}</div></div></section>'

def form():
    op = lambda l: "".join(f"<option>{x}</option>" for x in l)
    return f'''<form id="cf" novalidate class="form" aria-label="Contact form"><div class="hp" aria-hidden="true"><label>Leave empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="two"><div class="f"><label for="name">Full Name *</label><input id="name" name="name" required maxlength="100" autocomplete="name"><small class="err"></small></div><div class="f"><label for="company">Company *</label><input id="company" name="company" required maxlength="120" autocomplete="organization"><small class="err"></small></div></div>
<div class="two"><div class="f"><label for="email">Email Address *</label><input id="email" name="email" type="email" required maxlength="150" autocomplete="email"><small class="err"></small></div><div class="f"><label for="phone">Phone Number</label><input id="phone" name="phone" type="tel" maxlength="30" autocomplete="tel"><small class="err"></small></div></div>
<div class="two"><div class="f"><label for="type">Event Type *</label><select id="type" name="type" required><option value="">Select event type</option>{op(["Conference / Summit", "Executive Networking", "Product Launch", "Gala Dinner / Awards", "Team Building", "Corporate Training", "Other"])}</select><small class="err"></small></div>
<div class="f"><label for="size">Estimated Attendees *</label><select id="size" name="size" required><option value="">Select attendees</option>{op(["10–50", "50–100", "100–200", "200–500", "500+"])}</select><small class="err"></small></div></div>
<div class="f"><label for="msg">Tell us about your event *</label><textarea id="msg" name="msg" rows="5" required maxlength="2000"></textarea><small class="err"></small></div>
<button class="btn" type="submit"><span>Send Message</span></button><p id="st" role="status" aria-live="polite"></p></form>'''

def tile(v, big=False):
    return f'<a class="tile rv{" big" if big else ""}" href="event-{v["s"]}.html"><img src="{v["i"]}" alt="{e(v["t"])}" loading="lazy" width="900" height="600"><div class="tc"><span class="tag2">{v["c"]}</span><h3>{v["t"]}</h3><p>{fd(v["d"])} · {v["l"]}</p></div><span class="go" aria-hidden="true">↗</span></a>'
def pmeta(p):
    return f'{p["c"]} · {fd(p["d"])} · {p["r"]} min read'
def pit(p):
    return f'<a class="it" href="blog-{p["s"]}.html"><img src="{p["i"]}" alt="{e(p["t"])}" loading="lazy" width="300" height="300"><div><span class="cat">{pmeta(p)}</span><h3>{p["t"]}</h3></div></a>'
fe = [x for x in EVENTS if x["st"] != "past"][:3]
FEAT = f'<section><div class="wrap"><div class="shl rv"><div><p class="eb">Upcoming</p><h2>Featured Events</h2></div><a class="lk" href="events.html">All events →</a></div><div class="feat">{tile(fe[1], True)}{tile(fe[0])}{tile(fe[2])}</div></div></section>'
pa = POSTS[0]
INS = f'<section class="alt"><div class="wrap"><div class="shl rv"><div><p class="eb">Perspectives</p><h2>Latest Insights</h2></div><a class="lk" href="blog.html">All articles →</a></div><div class="ins"><a class="lead rv" href="blog-{pa["s"]}.html"><div class="lim"><img src="{pa["i"]}" alt="{e(pa["t"])}" loading="lazy" width="900" height="560"></div><span class="cat">{pmeta(pa)}</span><h3>{pa["t"]}</h3><p>{pa["ex"]}</p><span class="lk">Read Article →</span></a><div class="side rv">{"".join(pit(x) for x in POSTS[1:])}</div></div></div></section>'
CITY = '<section><div class="wrap">' + head("Across the US, EMEA, and beyond", "Executive gatherings designed and delivered in the world’s leading business cities.") + '<div class="cities">' + "".join(f'<div class="ct rv"><img src="{IM[k]}" alt="City skyline" loading="lazy" width="600" height="800"></div>' for k in ("nyc", "lon", "dxb", "par")) + '</div></div></section>'
# ---------- pages
home = f'''<section class="hero glow"><div class="wrap"><p class="eb rotw rv">Level One Connect &nbsp;/&nbsp; <span id="rw">Executive Networking</span></p><h1 class="rv">Experiences that redefine how leaders meet, think, and decide.</h1><p class="lead rv">Where the world’s most influential senior leaders come together to shape the future across industries.</p><div class="row rv">{CTA("contact.html", "Start Planning Your Event")}{CTA("services.html", "Explore Our Services", "btn ghost")}</div></div></section>
<section><div class="wrap">{head("Our Premium Services", "We design and deliver high-impact events—from concept to execution—focused on success and ROI.")}<div class="grid3">{"".join(scard(i, s) for i, s in enumerate(SERV))}</div><p class="c">{CTA("services.html", "View Our Services", "btn ghost dk")}</p></div></section>
<section class="alt"><div class="wrap two-col"><div class="rv pic"><img src="{IM["team"]}" alt="Executives in discussion at a corporate event" loading="lazy" width="900" height="700"></div><div class="rv"><p class="eb">About L1C</p><h2>Redefining Business &amp; Networking Gatherings</h2><p class="mut">Your trusted partner in professional event management since 2020</p><p>Transforming how executives connect and convene. As a global event partner, we design and execute executive gatherings across the US, EMEA, and beyond—bringing senior leaders together through experiences that enable connection, collaboration, and growth.</p><dl><dt>Strategic Approach</dt><dd>Every event is designed with clear business objectives and measurable outcomes in mind.</dd><dt>Local Expertise</dt><dd>We collaborate with leading organizations across various industries to deliver exceptional events.</dd><dt>Global Standards</dt><dd>International best practices combined with local insights for exceptional results.</dd></dl>{CTA("about.html", "Partner With Us")}</div></div></section>
<section><div class="wrap">{head("Our Strategic Process", "A systematic approach to delivering exceptional events that drive results.")}<div class="steps" role="tablist" aria-label="Process steps">{"".join(f'<button role="tab" class="{"on" if i == 0 else ""}" aria-selected="{"true" if i == 0 else "false"}" data-i="{i}"><span>0{i + 1}</span>{p[0]}</button>' for i, p in enumerate(PROC))}</div>{"".join(f'<div class="sp {"on" if i == 0 else ""}" role="tabpanel"><h3>0{i + 1} — {p[0]}</h3><p>{p[2]}</p></div>' for i, p in enumerate(PROC))}</div></section>
{stats()}{CITY}{FEAT}{INS}{cta()}
<section><div class="wrap two-col"><div class="rv"><h2>Contact</h2><p>Prishtina, Kosovo</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>{" · ".join(PHONES)}</p>{CTA("tel:" + PHONES[0].replace(" ", ""), "Call Now")}</div><div class="rv" id="form">{form()}</div></div></section>'''
page("index", "L1C — Level One Connect | Premium Corporate Events & Executive Networking", "L1C — Level One Connect designs premium corporate events and executive networking gatherings for senior leaders across the US, EMEA and beyond.", home)

sv = ""
for i, s in enumerate(SERV):
    sv += f'<section class="{"alt" if i % 2 else ""}"><div class="wrap two-col {"rev" if i % 2 else ""}"><div class="rv pic"><img src="{s[5]}" alt="{s[0]}" loading="lazy" width="900" height="700"></div><div class="rv"><h2>{s[0]}</h2><p>{s[1]}</p><ul class="ck">{"".join(f"<li>{x}</li>" for x in s[4])}</ul>{CTA("contact.html", s[3])}</div></div></section>'
sv += f'<section class="dark"><div class="wrap">{head("Additional Services")}<div class="grid3">{"".join(f"<article class=card><h3>{a}</h3><p>{b}</p></article>" for a, b in EXTRA)}</div></div></section><section class="cta"><div class="wrap rv"><h2>Ready to Transform Your Next Event?</h2>{CTA("contact.html", "Get Started Today")}</div></section>'
page("services", "Our Premium Event Services", "Corporate event planning, executive networking and strategic event consulting from L1C — Level One Connect.", hero("Our Premium Event Services", "Comprehensive event solutions designed to elevate your corporate gatherings and maximize ROI.", IM["conf"]) + sv, crumb=[("Services", "services.html")])

ab = f'''{hero("About Level One Connect", "Your trusted partner in professional event management since 2020", IM["team"])}<section><div class="wrap two-col"><div class="rv"><h2>Redefining Business &amp; Networking Gatherings</h2><p>Transforming how executives connect and convene. As a global event partner, we design and execute executive gatherings across the US, EMEA, and beyond—bringing senior leaders together through experiences that enable connection, collaboration, and growth.</p><dl><dt>Strategic Approach</dt><dd>Every event is designed with clear business objectives and measurable outcomes in mind.</dd><dt>Industry Expertise</dt><dd>Deep understanding of technology and business trends.</dd><dt>Global Standards</dt><dd>International best practices combined with local insights for exceptional results.</dd></dl>{CTA("contact.html", "Partner With Us Today")}</div><div class="rv pic"><img src="{IM["off"]}" alt="The L1C team collaborating" loading="lazy" width="900" height="700"></div></div></section>
<section class="alt"><div class="wrap grid3"><article class="card rv"><h3>Our Mission</h3><p>To transform business gatherings into strategic platforms for connection, innovation, and growth by delivering exceptional event experiences that exceed expectations and deliver measurable results for our clients.</p></article><article class="card rv"><h3>Our Vision</h3><p>To be the leading event management partner in the Balkan region, recognized for our innovative approach, strategic expertise, and ability to create meaningful connections that drive business success.</p></article><article class="card rv"><h3>Our Values</h3><p>Excellence, Integrity, Innovation, Collaboration, and Client-Centricity guide everything we do.</p></article></div></section>{stats()}'''
page("about", "About Level One Connect", "Learn about L1C — Level One Connect: our mission, vision, values and approach to executive events.", ab, crumb=[("About", "about.html")])

pr = "".join(f'<article class="card rv pr"><span class="n">0{i + 1}</span><h3>{p[1]}</h3><p>{p[2]}</p><ul class="ck">{"".join(f"<li>{x}</li>" for x in p[3])}</ul><p class="tag">Duration: {p[4]}</p></article>' for i, p in enumerate(PROC))
cs = "".join(f'<article class="card rv"><span class="tag">{c[1]}</span><h3>{c[0]}</h3><p>{c[2]}</p><div class="mt">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in c[3])}</div></article>' for c in CASES)
page("process", "Our Strategic Event Process", "A systematic four-step approach to delivering exceptional events that drive measurable business results.",
     hero("Our Strategic Event Process", "A systematic approach to delivering exceptional events that drive measurable business results.", IM["cons"]) + f'<section><div class="wrap"><div class="grid2">{pr}</div></div></section><section class="alt"><div class="wrap grid3">{"".join(f"<article class=\"card rv\"><h3>{x}</h3></article>" for x in PRIN)}</div></section><section><div class="wrap">{head("Success Stories")}<div class="grid3">{cs}</div></div></section>' + cta(), crumb=[("Process", "process.html")])

sec = lambda t, l: f'<section><div class="wrap">{head(t)}<div class="elist">{"".join(erow(v) for v in l) or "<p>No events at the moment.</p>"}</div></div></section>'
page("events", "Events", "Upcoming, featured and past executive networking events, summits and dinners by L1C — Level One Connect.",
     hero("Events", "Executive networking, conferences, leadership dinners and business summits.", IM["net"]) + sec("Upcoming Events", [v for v in EVENTS if v["st"] == "upcoming"]) + '<div class="alt">' + sec("Featured Events", [v for v in EVENTS if v["st"] == "featured"]) + "</div>" + sec("Past Events", [v for v in EVENTS if v["st"] == "past"]) + "<!-- Sample listings: edit EVENTS in build.py -->", crumb=[("Events", "events.html")])
for v in EVENTS:
    ev = {"@context": "https://schema.org", "@type": "Event", "name": v["t"], "startDate": f'{v["d"]}T{v["tm"]}', "location": {"@type": "Place", "name": v["l"]}, "description": v["ds"], "image": v["i"], "organizer": {"@type": "Organization", "name": "Level One Connect", "url": SITE}}
    SPK = "<ul class=ck>" + "".join(f"<li>{e(x)}</li>" for x in v["sp"]) + "</ul>" if v.get("sp") else '<p class="mut">Speakers to be announced.</p>'
    AGD = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in v.get("ag", [(v["tm"], "Welcome & arrival"), ("+1h", "Keynote / opening conversation"), ("+2h", "Roundtables & networking")]))
    GAL = "".join(f'<div class="pic rv"><img src="{x}" alt="Event photography" loading="lazy" width="600" height="400"></div>' for x in v.get("gal", (IM["dinner"], IM["net"], IM["conf"])))
    body = f'''{hero(v["t"], f'{fd(v["d"])} · {v["tm"]} · {v["l"]}', v["i"], v["c"])}<section><div class="wrap two-col"><div class="rv"><h2>About this event</h2><p>{v["ds"]}</p><h3>Speakers</h3>{SPK}<h3>Agenda</h3><table><tr><th>Time</th><th>Session</th></tr>{AGD}</table></div><aside class="card rv"><h3>Details</h3><p><b>Date</b><br>{fd(v["d"])}</p><p><b>Time</b><br>{v["tm"]}</p><p><b>Location</b><br>{v["l"]}</p>{CTA(v.get("reg", "contact.html"), "Register Your Interest")}<p></p>{CTA("contact.html#form", "Contact Our Team", "btn ghost dk")}</aside></div></section>
<section class="alt"><div class="wrap">{head("Gallery")}<div class="grid3">{"".join(f'<div class="pic rv"><img src="{x}" alt="Event photography" loading="lazy" width="600" height="400"></div>' for x in (IM["dinner"], IM["net"], IM["conf"]))}</div></div></section>'''
    page("event-" + v["s"], v["t"], v["ds"], body, JS(ev), v["i"], [("Events", "events.html"), (v["t"], f'event-{v["s"]}.html')])
page("blog", "Insights & Perspectives", "Articles on event strategy, executive networking, leadership and technology from L1C — Level One Connect.",
     hero("Insights &amp; Perspectives", "Event strategy, executive networking, leadership, technology and industry insights.", IM["off"]) + f'<section><div class="wrap"><p class="cats">{"".join(f"<span class=tag>{c}</span>" for c in ("Event Strategy", "Executive Networking", "Leadership", "Technology", "Corporate Events", "Industry Insights"))}</p><div class="grid3">{"".join(bcard(p) for p in POSTS)}</div></div></section>', crumb=[("Blog", "blog.html")])
for p in POSTS:
    ar = {"@context": "https://schema.org", "@type": "Article", "headline": p["t"], "datePublished": p["d"], "author": {"@type": "Organization", "name": "L1C — Level One Connect"}, "image": p["i"], "publisher": {"@type": "Organization", "name": "Level One Connect"}}
    rel = "".join(bcard(x) for x in POSTS if x is not p)
    page("blog-" + p["s"], p["t"], p["ex"], f'{hero(p["t"], f"L1C Editorial · {fd(p["d"])} · {p["r"]} min read", p["i"], p["c"])}<section><div class="wrap art"><img class="rv" src="{p["i"]}" alt="{e(p["t"])}" width="1000" height="560">{"".join(f"<p>{x}</p>" for x in p["b"])}</div></section><section class="alt"><div class="wrap">{head("Related Articles")}<div class="grid2">{rel}</div></div></section>' + cta(), JS(ar), p["i"], [("Blog", "blog.html"), (p["t"], f'blog-{p["s"]}.html')], "article")

page("contact", "Contact Us", "Contact L1C — Level One Connect to plan your conference, executive networking event or corporate gathering.",
     hero("Contact Us", "Ready to transform your next corporate event? Get in touch with our team today.", IM["off"]) + f'<section><div class="wrap two-col"><div class="rv"><h2>Let\'s Create Something Exceptional Together</h2><p>Whether you\'re planning a conference, executive networking event, or corporate gathering, our team is ready to help you create an unforgettable experience that delivers real business value.</p><h3>Email Us</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><h3>Call Us</h3>{"".join(f"<p>{p}</p>" for p in PHONES)}<h3>Location</h3><p>Prishtina, Kosovo</p>{CTA("tel:" + PHONES[0].replace(" ", ""), "Call Now")}</div><div class="rv" id="form">{form()}</div></div></section>', crumb=[("Contact", "contact.html")])

def legal(f, t, secs):
    b = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in secs)
    page(f, t, f"{t} for L1C — Level One Connect.", hero(t, "Last updated: September 2026", IM["off"]) + f'<section><div class="wrap art">{b}<p class="mut">This is a template and does not constitute legal advice. Have it reviewed by a qualified professional before publishing.</p></div></section>', crumb=[(t, f + ".html")])
legal("privacy", "Privacy Policy", [("Information we collect", "We collect the details you submit through our contact form (name, company, email, phone, event details) and basic technical data such as browser type."), ("Contact forms", "Form data is used only to respond to your enquiry."), ("Cookies", "See our Cookie Policy. Non-essential cookies are used only with consent."), ("Analytics", "This website does not include analytics by default. If added, it will be disclosed here and require consent."), ("How we use information", "To respond to enquiries, provide event services and improve our website."), ("Data retention", "We keep enquiry data only as long as needed for the purposes above or as required by law."), ("Security", "We use reasonable technical and organisational measures. No online transmission is fully secure."), ("Third-party services", "This site loads fonts from Google Fonts and images from Unsplash, and may use a form-processing service."), ("Your rights", "Depending on your location you may request access, correction or deletion of your data."), ("Contact", f"Contact us at {EMAIL}."), ("Policy updates", "We may update this policy; the date above shows the latest revision.")])
legal("cookies", "Cookie Policy", [("Essential cookies", "Required for the website to function. This site currently sets none."), ("Functional cookies", "Remember preferences such as your cookie choice."), ("Analytics cookies", "Not used currently. If added, they will load only after your consent."), ("Third-party cookies", "Embedded third-party services may set their own cookies."), ("Cookie management", "You can delete or block cookies in your browser settings."), ("Consent", "Non-essential cookies are only set with your consent, which you can withdraw at any time.")])
legal("terms", "Terms & Conditions", [("Website usage", "By using this website you agree to these terms and to use it lawfully."), ("Intellectual property", "All content, logos and designs belong to L1C — Level One Connect or its licensors."), ("Event services", "Event services are provided under separate written agreements."), ("Enquiries and booking", "Submitting an enquiry does not create a booking or contract."), ("Third-party services", "We are not responsible for third-party services or content."), ("Liability", "To the extent permitted by law, we are not liable for losses from use of this website."), ("External links", "External sites are outside our control."), ("Website changes", "We may modify the website and these terms at any time."), ("Governing law", "[Governing law and jurisdiction to be specified.]"), ("Contact information", f"{EMAIL} · Prishtina, Kosovo")])
page("404", "Page Not Found", "This page doesn't exist.", f'<section class="nf glow"><div class="wrap c"><h1>404</h1><h2>This page doesn\'t exist.</h2>{CTA("index.html", "Back to Home")}</div></section>')
os.rename(f"{OUT}/404.html", f"{OUT}/404.html")

pages = [f[len(OUT) + 1:-5] for f in glob.glob(OUT + "/*.html") if not f.endswith("404.html")]
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}/{'' if p == 'index' else p + '.html'}</loc></url>" for p in sorted(pages)) + "</urlset>")
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(f"{OUT}/README.txt", "w").write("L1C website (static). CSS and JS are inlined in every page. Replace assets/logo.* with the official logo, set the real domain/email in build.py, set window.L1C_ENDPOINT in build.py (CFG), run `python3 build.py`.\nSecurity headers (CSP, X-Frame-Options, HSTS) must be set at host/CDN level; set the CSP header at host level too (it is not in the HTML so the site also works when opened locally).\n")
