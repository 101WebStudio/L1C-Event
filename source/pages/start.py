"""Start Your Event page: start-your-event.html"""
from util import *
from config import *
from components import *
from data.events import EVENTS
from data.posts import POSTS
from data.content import *
from render import page, tpl


def build():
    START = hero("Start Your Event", "Tell us what you have in mind. The more detail you give us now, the more useful our first reply will be.", IM["lights"]) + '<section><div class="wrap sy"><form id="sf" class="form" novalidate data-subject="Event brief" data-ok="Thank you. We have your brief and a member of the team will reply by email." data-btn="Submit Your Brief" aria-label="Event brief">' + HP \
        + sub(1, "About the event", two(fld("type", "Event Type", "select", True, TYPES, "Select event type"), fld("ename", "Event name or working title", pl="Optional")),
              two(fld("goal", "Main goal", "select", True, ["Build relationships", "Generate leads or pipeline", "Launch a product", "Recognise or reward people", "Share knowledge", "Train or align a team", "Other"], "Select main goal"), fld("format", "Format", "select", True, ["In person", "Hybrid", "Virtual"], "Select format")),
              two(fld("size", "Estimated Attendees", "select", True, SIZES, "Select attendees"), fld("audience", "Who should attend?", req=True, pl="e.g. CIOs and heads of customer experience"))) \
        + sub(2, "When and where", two(fld("date", "Preferred date", "date"), fld("flex", "Date flexibility", "select", False, ["The date is fixed", "Flexible by a few days", "Flexible by a few weeks", "Not decided yet"])),
              two(fld("city", "Preferred city or region", pl="e.g. London"), fld("venue", "Venue preference", "select", False, ["Hotel", "Restaurant or private dining", "Conference centre", "Distinctive or unusual venue", "Need recommendations"])),
              fld("length", "Duration", "select", False, ["An evening", "Half a day", "A full day", "More than one day"])) \
        + sub(3, "Budget and support", fld("budget", "Estimated budget", "select", False, ["Under £10,000", "£10,000 – £25,000", "£25,000 – £50,000", "£50,000 – £100,000", "£100,000+", "Not sure yet"]), chk("services", "Services you may need", SERVICES)) \
        + sub(4, "Anything else", fld("msg", "Tell us about your event", "area", True, pl="Objectives, themes, speakers you have in mind, anything we should know"), fld("contactpref", "How should we reach you?", "select", False, ["Email", "Phone", "Either is fine"])) \
        + sub(5, "Your details", two(fld("name", "Full Name", req=True, ac="name"), fld("company", "Company", req=True, ac="organization")), two(fld("role", "Job title", ac="organization-title"), fld("email", "Email Address", "email", True, ac="email")), fld("phone", "Phone Number", "tel", mx=30, ac="tel"), CONSENT) \
        + '<button class="btn" type="submit"><span>Submit Your Brief</span></button><p class="st" role="status" aria-live="polite"></p></form><aside class="card rv side2"><h3>What happens next</h3><ol class="steps2"><li><b>We read your brief.</b> A member of the team reviews it and replies by email.</li><li><b>A short call.</b> We confirm goals, audience, timing and budget.</li><li><b>Your proposal.</b> A concept, timeline and costs for you to review.</li></ol><p class="mut">Prefer to talk first? Email <a href="mailto:' + EMAIL + '">' + EMAIL + '</a> or read about <a href="process.html">our process</a>.</p></aside></div></section>'
    page("start-your-event", "Start Your Event", "Tell L1C about your event: goals, audience, date, venue and budget, and we will come back with a plan.", START, crumb=[("Start Your Event", "start-your-event.html")])
