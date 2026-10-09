# L1C — Level One Connect website

Static website (HTML, CSS, JavaScript). Pages are generated from templates and data in `source/`; the finished site is in `site/`.

- Full guide: `README.txt`
- Events: `source/data/events.py` · Blog posts: `source/data/posts.py` · Email, phone, domain: `source/config.py`
- Build and check: `cd source && python3 build.py && python3 check_site.py`
- Publish: push to `main`. GitHub Actions rebuilds, checks and publishes `site/` to GitHub Pages
  (once: Settings > Pages > Source: GitHub Actions).
