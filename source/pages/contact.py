"""Contact page: contact.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    page("contact", "Contact Us", "Contact L1C — Level One Connect to plan your conference, executive networking event or corporate gathering.",
         hero("Contact Us", "Ready to transform your next corporate event? Get in touch with our team today.", IM["off"]) + f'<section><div class="wrap two-col"><div class="rv"><h2>Let\'s Create Something Exceptional Together</h2><p>Whether you\'re planning a conference, executive networking event, or corporate gathering, our team is ready to help you create an unforgettable experience that delivers real business value.</p><h3>Email Us</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><h3>Call Us</h3>{"".join(f"<p>{p}</p>" for p in PHONES)}<h3>Location</h3><p>London, United Kingdom</p>{CTA("tel:" + PHONES[0].replace(" ", ""), "Call Now")}</div><div class="rv" id="form">{form()}</div></div></section>', crumb=[("Contact", "contact.html")])
