L1C — LEVEL ONE CONNECT WEBSITE
===============================

A static website (HTML, CSS and JavaScript only). There is no server, no database and no login.
The finished pages are generated from templates and data files, so each page type is written once.

START HERE
  1. Extract the zip first (Windows: right-click > Extract All). Do not open pages from inside the zip.
  2. Open site/index.html. The pages, the assets/ folder and the events/, blog/ and legal/ folders must
     stay together, because every page loads its CSS, JavaScript, font and logo from site/assets/.
  3. If you need a single page to work completely on its own (to send it or preview it alone), run
     python3 make_standalone.py inside source/ and use the page from the new site-standalone/ folder.

CONTENTS
  1. Folder structure
  2. How the pages are connected
  3. Where the content of each page lives
  4. Where every button goes
  5. How to change things (contact details, events, blog posts, text, photos, colours, logo, forms)
  6. Rebuilding and checking the site
  7. Publishing
  8. Security: what was checked and what is in place
  9. Before launch checklist
 10. Troubleshooting


1. FOLDER STRUCTURE
-------------------

l1c-website/
|-- README.txt                    This file.
|-- README.md                     Short note shown on the GitHub repository page.
|-- .gitignore                    Files Git should skip.
|-- .github/workflows/deploy.yml  Builds, checks and publishes the site to GitHub Pages on every push.
|-- site/                         THE WEBSITE. This is what gets published.
|   |-- index.html                Home (main entry point).
|   |-- services.html, about.html, process.html, contact.html, start-your-event.html
|   |-- 404.html                  "This page doesn't exist" page.
|   |-- events/                   index.html (listing + search), reserve.html, one page per event.
|   |-- blog/                     index.html (listing), one page per article.
|   |-- legal/                    privacy.html, cookies.html, terms.html
|   |-- assets/                   style.css (the whole design), main.js (behaviour), theme.js (dark/light),
|   |                             config.js (form settings, editable), logo.png (original), logo-nav.png
|   |                             (transparent, header/footer), logo-fav.png (tab icon),
|   |                             inter-latin-wght-normal.woff2 (font) and its licence.
|   |-- sitemap.xml, robots.txt   For search engines (generated).
|   `-- .nojekyll                 Tells GitHub Pages to serve the files as they are.
`-- source/                       The generator. Not published.
    |-- build.py                  Run this to regenerate every page.
    |-- config.py                 Domain, email, phone, photos list, menu, page locations.
    |-- check_site.py             Checks links, files and security basics.
    |-- make_standalone.py        Optional: makes site-standalone/ (every page with its CSS, JS, font and logo inside).
    |-- _headers                  Optional security headers for Netlify / Cloudflare Pages (see section 8).
    |-- components.py, render.py, util.py   The machinery that fills templates and fixes link paths.
    |-- data/                     events.py, posts.py, content.py, legal.py
    |-- pages/                    One file per page (home.py, services.py, about.py, ...).
    `-- templates/                layout.html, event.html (all events), post.html (all articles).

Important: every .html file in site/ is generated. Do not edit them by hand, because the next
build replaces them. Change the data, template or page file in source/ and rebuild (section 6).
The only files in site/ you edit directly are those in site/assets/.


2. HOW THE PAGES ARE CONNECTED
------------------------------

- index.html is the entry point. Its sections link on to Services, About, Process, Events, Blog,
  Start Your Event and Contact.
- Every page has the same header and footer (templates/layout.html):
    Header menu:  Home, Services, About, Process, Events, Blog, Contact, plus the blue "Start Your Event" button.
    Footer:       Quick Links (same pages), Legal (Privacy, Terms, Cookies), contact details.
  Because of this, every page can reach every other main page in one click.
- Services, About, Process, Contact and Start Your Event are separate pages in the main folder.
  They are not part of the Events or Blog structures.
- Events: events/index.html lists the events. Each card opens events/<name>.html. An event page links back
  to "All events" and to events/reserve.html (Reserve a Seat) with that event already selected.
- Blog: blog/index.html lists the articles. Each card opens blog/<name>.html. An article links back to
  "All articles" and shows two related articles.
- You write links as simple names (for example contact.html or event-<name>.html). build.py converts them
  to the correct path for the folder each page is in, so links work from every depth.


3. WHERE THE CONTENT OF EACH PAGE LIVES
---------------------------------------

Page                         Generated file                  Edit this in source/
Home                         index.html                      pages/home.py (+ data/content.py, events.py, posts.py)
Services                     services.html                   pages/services.py + data/content.py (SERV, EXTRA)
About                        about.html                      pages/about.py (+ STATS in data/content.py)
Process                      process.html                    pages/process.py + data/content.py (PROC, PRIN, CASES)
Contact                      contact.html                    pages/contact.py; email and phone in config.py
Start Your Event             start-your-event.html           pages/start.py (+ TYPES, SIZES, SERVICES in data/content.py)
Events listing               events/index.html               pages/events.py + data/events.py
Event pages                  events/<name>.html              templates/event.html + data/events.py
Reserve a Seat               events/reserve.html             pages/reserve.py (event list comes from data/events.py)
Blog listing                 blog/index.html                 pages/blog.py + data/posts.py
Blog articles                blog/<name>.html                templates/post.html + data/posts.py
Privacy, Cookies, Terms      legal/*.html                    data/legal.py
404                          404.html                        pages/legal.py
Header, menu, footer         every page                      templates/layout.html (menu names in config.py: NAV)

Page title, Google description and social preview text are the 2nd and 3rd values in each page(...) call.


4. WHERE EVERY BUTTON GOES
--------------------------

Every page
  Logo                                   index.html
  Menu items                             the page with the same name
  "Start Your Event" (blue button)       start-your-event.html
  Sun / moon button                      switches dark / light mode (remembered on the visitor's device)
  Footer quick links                     same pages as the menu
  Footer legal links                     legal/privacy.html, legal/terms.html, legal/cookies.html
  Footer email / phone                   opens the email app / starts a call
  "Website crafted by 101WebStudio"      https://101webstudio.github.io/ (new tab)

Home
  Start Planning Your Event              start-your-event.html
  Explore Our Services                   services.html
  Service cards (Learn More, ...)        services.html
  Partner With Us                        about.html
  Process steps 01-04                    no link, they switch the text below
  Featured Events tiles                  that event's page; "All events" goes to events/index.html
  Latest Insights articles               that article; "All articles" goes to blog/index.html
  Start Your Event Journey               start-your-event.html
  Contact Our Team                       contact.html#form
  Call Now                               calls the first number in config.py

Other pages
  Services: Inquire About Corporate Events / Plan a Networking Event    start-your-event.html (event type pre-selected)
  Services: Schedule a Consultation                                     contact.html
  Services: Get Started Today                                           start-your-event.html
  About: Partner With Us Today                                          contact.html
  Process and articles: Start Your Event Journey / Contact Our Team     start-your-event.html / contact.html#form
  Events: each card                                                     that event's page (search box filters the cards, no link)
  Event page: Reserve a Seat                                            events/reserve.html with the event selected
                                                                        (past events show "See upcoming events" instead)
  Event page: Contact Our Team                                          contact.html#form
  404: Back to Home                                                     index.html

To change where a button goes, find its text in the page file (section 3) and change the first value
in CTA("contact.html", "Button text").


5. HOW TO CHANGE THINGS
-----------------------

5.1 Domain, email, phone
  Edit source/config.py (SITE, EMAIL, PHONES), then rebuild. They update the footer, Contact page,
  Terms, search-engine data, canonical addresses and the sitemap.

5.2 Add a new event
  Open source/data/events.py and add one block (copy an existing one):

    dict(s="summit-vienna-2027",       # page address -> events/summit-vienna-2027.html (lowercase, hyphens, unique)
         t="Executive Summit Vienna",  # title
         c="Business Summits",         # category label
         d="2027-09-15",               # date, always YYYY-MM-DD
         tm="09:00",                   # time
         l="Vienna, Austria",          # location
         st="upcoming",                # "upcoming", "featured" or "past"
         i=IM["conf"],                 # photo: a name from IM in config.py, or "assets/your-file.jpg"
         ds="Short description for the cards and the event page."),

  Optional extras: sp=["Name, Role, Company", ...] (speakers), ag=[("09:00", "Registration"), ...] (agenda),
  gal=[photo, photo, photo] (gallery), reg="https://..." (where Reserve a Seat goes).
  Rebuild. The event appears on the Events page (Upcoming / Featured / Past by "st"), gets its own page,
  appears in the Reserve a Seat list and in the sitemap. Home shows the first three events that are not past;
  the large tile is the second of them. When an event is over, change "st" to "past".

5.3 Add a blog post
  Open source/data/posts.py and add one block:

    dict(s="my-new-article",           # page address -> blog/my-new-article.html
         t="Article title", c="Leadership", d="2026-10-05", r=5,    # title, category, date, minutes to read
         i=IM["cons"],                 # photo
         ex="One or two lines for the cards.",
         b=["First paragraph.", "Second paragraph.", "Third paragraph."]),   # one string per paragraph

  Rebuild. Posts are sorted by date, newest first. The newest is the large article on Home.

5.4 Change text on a page
  Find the sentence in the page file listed in section 3 (use search) and edit it, then rebuild.
  Services, process steps, statistics and success stories are in source/data/content.py.

5.5 Photos
  The photo list is IM in source/config.py. The photos are currently stock images loaded from Unsplash.
  To use your own, copy the file into site/assets/ and use "assets/your-file.jpg" as the photo value.
  If a photo cannot load, the site shows a dark placeholder instead of a broken image.
  The Home carousel is the SLIDES list in source/pages/home.py; True puts the L1C logo on that photo.

5.6 Colours and design
  Top of site/assets/style.css (:root). --b is the L1C blue #5170FF, --nv is the dark navy.

5.7 Logo
  Replace the three files in site/assets/ and keep the names: logo.png (original), logo-nav.png
  (transparent background, header and footer), logo-fav.png (browser tab icon). If the shape of
  logo-nav.png changes, update NH and NW in source/config.py (header size) and rebuild.

5.8 Forms (Contact, Start Your Event, Reserve a Seat)
  The site cannot store messages itself. Create a form endpoint with a form service (for example Formspree
  or Web3Forms) and paste its address in site/assets/config.js (L1C_ENDPOINT). No rebuild is needed.
  Until you do, the Send button opens the visitor's email app with the message filled in, addressed to the
  email in config.py. Use a service that checks messages on its own servers and filters spam.

5.9 Hero rotating words and the cursor glow
  Words: the "ws" list in site/assets/main.js. Glow: the ".cur" rules in style.css and the "cursor glow"
  block in main.js. One glow follows the mouse on every page and section; it picks a stronger layer over
  light backgrounds so it looks the same everywhere.

5.10 Add a new page
  Copy a file in source/pages/ (for example contact.py), change its content, add it to the import line and
  the loop in source/build.py, and add it to NAV in source/config.py if it should be in the menu.


6. REBUILDING AND CHECKING THE SITE
-----------------------------------

You need Python 3 (free). Nothing else is required.

  cd source
  python3 build.py              regenerates all pages into ../site/
  python3 check_site.py   checks links, files, anchors, sitemap, security basics and scans for secrets
  python3 make_standalone.py   (optional) rebuilds site-standalone/ with everything inside each page

Optional: to format the generated HTML neatly, run   npx prettier --write "../site/**/*.html"

The build never touches site/assets/. If a build fails with "KeyError", a template value is missing,
which is intentional so mistakes are not published silently.


7. PUBLISHING (GITHUB)
----------------------

Direct way (recommended): push the whole project and GitHub publishes it for you.
  1. Create an empty repository on GitHub.
  2. Push this whole folder (the one that contains README.txt, site/, source/ and .github/):
       git init
       git add .
       git commit -m "feat: launch L1C – Level One Connect website"
       git branch -M main
       git remote add origin https://github.com/<your-user>/<your-repo>.git
       git push -u origin main
     GitHub Desktop works too: Add local repository, then Publish repository.
  3. On GitHub, once: Settings > Pages > Build and deployment > Source: GitHub Actions.
  4. The Actions tab now shows "Build and deploy to GitHub Pages". It runs on every push to main:
     it rebuilds the pages, runs the checker (a broken link or a secret stops the deploy) and publishes site/.
  5. Custom domain: Settings > Pages > Custom domain, then tick Enforce HTTPS.
     Put the same domain in source/config.py (SITE).
  From then on: change the data in source/, commit, push. No folder uploads.

Manual way (no Actions): upload the CONTENTS of site/ to the repository (index.html in the main folder, with
assets/, events/, blog/ and legal/ next to it) and set Settings > Pages > Source: Deploy from a branch.
Publish site/, not site-standalone/. Always upload the whole site/ folder. The CSS, JS, logo and font are
separate files in assets/; if they are missing, pages show as plain unstyled text and the logo shows its
alternative text.


8. SECURITY: WHAT WAS CHECKED AND WHAT IS IN PLACE
---------------------------------------------------

Checked (python3 check_site.py repeats this):
  - No API keys, passwords, tokens, credentials or private keys in any file (68 files scanned). The site does
    not use any API, so there is nothing to hide.
  - The only contact details in the project are the public placeholders: info@l1c.example, +44 20 0000 0000
    and www.l1c.example. No personal data.
  - No environment files, backups, source maps or other hidden files. Only .nojekyll, which is intentional.
  - The generator and data (source/) and hosting/ are outside site/, so they are not published.
  - No inline scripts or inline event handlers; every script is a file from this site (no third-party
    JavaScript). This also allows a strict Content Security Policy at hosting level.
  - The font is hosted on this site (no request to Google Fonts).
  - The GitHub workflow uses only official GitHub actions, read-only access to the code and write access to
    Pages only. It needs no secrets or tokens.
  - Every link that opens a new tab uses rel="noopener noreferrer". No http:// resources.

Real measures in place:
  - Referrer policy meta tag (strict-origin-when-cross-origin).
  - Page text is escaped when pages are generated, and "</" is escaped inside the structured data.
  - No cookies. The only stored value is your light/dark choice in the browser's local storage.
  - Forms: validation and a hidden honeypot field plus a minimum-time check. These only filter simple bots.
    They are not a security boundary, because anyone can bypass browser code. Real validation, rate limiting
    and spam protection must come from your form service (for example Cloudflare Turnstile).
  - The form endpoint address is public by design. Never put a password or secret key in any file in site/.

Not possible on a static site, and not faked here:
  - Server-side input checks, rate limiting, CSRF, login, database rules: there is no server or database.
  - HTTP security headers and Content Security Policy: GitHub Pages cannot set them, and a CSP meta tag would
    stop the pages loading when opened from your computer. source/_headers contains ready-to-use headers
    (CSP, HSTS, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy) for Netlify or Cloudflare Pages,
    or put the site behind Cloudflare. If you use a form service, add its address to connect-src there.

What you still need to do:
  - Turn on 2-step verification for GitHub, your domain registrar and your email. Account takeover is the
    most realistic risk for this kind of site.
  - Never commit passwords or keys to the repository.
  - Third parties still used: Unsplash photos (until you replace them), the 101WebStudio link, and the form
    service you choose. Keep the Privacy Policy accurate when this changes.


9. BEFORE LAUNCH CHECKLIST
--------------------------

  [ ] Real domain, email and London phone number in source/config.py
  [ ] Form endpoint set in site/assets/config.js and a test message received
  [ ] Sample events and articles replaced with real ones; Unsplash photos replaced with your own or licensed ones
  [ ] Success Stories and statistics are accurate and provable (figures and names were supplied by you)
  [ ] Vision text on About ("across the UK and EMEA") confirmed
  [ ] Legal pages reviewed by a qualified person; "Governing law" filled in the Terms; company details added if required
  [ ] GitHub Pages source set to GitHub Actions (the deploy shows a yellow warning until the placeholders in config.py are replaced)
  [ ] HTTPS enforced; security headers set at hosting level
  [ ] 2-step verification on GitHub, domain and email
  [ ] python3 check_site.py shows "OK, nothing broken"


10. TROUBLESHOOTING
-------------------

  Pages look unstyled or the logo shows text   The page was opened without the assets/ folder next to it (for example
                                               from inside the zip, or only the .html files were uploaded). Extract
                                               the zip and keep the folders together, or use a page from site-standalone/.
  A new event or post does not appear          You did not rebuild, or "s" is not unique.
  Build error "KeyError"                       A template value is missing; the message names it.
  Link checker reports a missing file          A photo path or page name is mistyped.
  Form button opens an email app               L1C_ENDPOINT in site/assets/config.js is empty.
  Actions deploy fails                         Pages source is not set to GitHub Actions, or the checker found a problem (open the run log).
  Old content still shows after publishing     Hard-refresh the browser (Ctrl+F5) or wait a minute for the host.
