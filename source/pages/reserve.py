"""Reserve a Seat page: events/reserve.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    UPC = [v for v in EVENTS if v["st"] != "past"]
    EVOPT = "".join(f'<option value="{e(v["t"])}" data-slug="{v["s"]}" data-when="{fd(v["d"])} · {v["tm"]}" data-loc="{e(v["l"])}">{e(v["t"])}, {fd(v["d"])}</option>' for v in UPC)
    RES = hero("Reserve a Seat", "Choose the event, tell us who is coming and we will confirm your seat by email.", IM["dinner"]) + '<section><div class="wrap sy"><form id="rf" class="form" novalidate data-subject="Seat reservation" data-ok="Thank you. We have your request and will confirm your seat by email." data-btn="Reserve My Seat" aria-label="Seat reservation">' + HP \
        + f'<div class="f"><label for="event">Event *</label><select id="event" name="event" required><option value="">Select an event</option>{EVOPT}</select><small class="err"></small></div><p id="evinfo" class="mut"></p>' \
        + two(fld("name", "Full Name", req=True, ac="name"), fld("company", "Company", req=True, ac="organization")) + two(fld("role", "Job title", ac="organization-title"), fld("email", "Email Address", "email", True, ac="email")) \
        + two(fld("phone", "Phone Number", "tel", mx=30, ac="tel"), fld("seats", "Number of seats", "select", True, ["1", "2", "3", "4", "5 or more"])) \
        + fld("notes", "Dietary or accessibility requirements", "area", rows=3, pl="Optional") + CONSENT \
        + '<button class="btn" type="submit"><span>Reserve My Seat</span></button><p class="st" role="status" aria-live="polite"></p></form><aside class="card rv side2"><h3>Good to know</h3><ul class="ck"><li>Seats are confirmed by email.</li><li>Some events are by invitation, so we may ask a few questions first.</li><li>Booking for a group? Tell us in the form.</li></ul><a class="lk" href="events.html">All events →</a></aside></div></section>'
    page("reserve", "Reserve a Seat", "Reserve a seat at an upcoming L1C event.", RES, crumb=[("Events", "events.html"), ("Reserve a Seat", "reserve.html")])
