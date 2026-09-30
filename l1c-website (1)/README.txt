L1C website (static). CSS and JS are inlined in every page. Replace assets/logo.* with the official logo, set the real domain/email in build.py, set window.L1C_ENDPOINT in build.py (CFG), run `python3 build.py`.
Security headers (CSP, X-Frame-Options, HSTS) must be set at host/CDN level; set the CSP header at host level too (it is not in the HTML so the site also works when opened locally).
