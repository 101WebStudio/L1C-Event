"""About page: about.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    ab = f'''{hero("About Level One Connect", "Your trusted partner in professional event management since 2020", IM["team"])}<section><div class="wrap two-col"><div class="rv"><h2>Redefining Business &amp; Networking Gatherings</h2><p>Transforming how executives connect and convene. As a global event partner, we design and execute executive gatherings across the US, EMEA, and beyond—bringing senior leaders together through experiences that enable connection, collaboration, and growth.</p><dl><dt>Strategic Approach</dt><dd>Every event is designed with clear business objectives and measurable outcomes in mind.</dd><dt>Industry Expertise</dt><dd>Deep understanding of technology and business trends.</dd><dt>Global Standards</dt><dd>International best practices combined with local insights for exceptional results.</dd></dl>{CTA("contact.html", "Partner With Us Today")}</div><div class="rv pic"><img src="{IM["off"]}" alt="City business district" loading="lazy" width="900" height="700"></div></div></section>
    <section class="alt"><div class="wrap grid3"><article class="card rv"><h3>Our Mission</h3><p>To transform business gatherings into strategic platforms for connection, innovation, and growth by delivering exceptional event experiences that exceed expectations and deliver measurable results for our clients.</p></article><article class="card rv"><h3>Our Vision</h3><p>To be the leading event management partner across the UK and EMEA, recognized for our innovative approach, strategic expertise, and ability to create meaningful connections that drive business success.</p></article><article class="card rv"><h3>Our Values</h3><p>Excellence, Integrity, Innovation, Collaboration, and Client-Centricity guide everything we do.</p></article></div></section>{stats()}'''
    page("about", "About Level One Connect", "Learn about L1C — Level One Connect: our mission, vision, values and approach to executive events.", ab, crumb=[("About", "about.html")])
