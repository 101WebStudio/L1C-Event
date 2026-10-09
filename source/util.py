"""Small helpers shared by every module."""
import json, datetime, html as H
e = H.escape
fd = lambda d: datetime.date.fromisoformat(d).strftime("%d %b %Y")
CTA = lambda h, t, cls="btn": f'<a class="{cls}" href="{h}">{t}</a>'
def JS(o):
    return '<script type="application/ld+json">' + json.dumps(o).replace("</", "<\\/") + "</script>"
