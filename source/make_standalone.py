"""Makes a self-contained copy of the site in ../site-standalone/.

Every page gets the CSS, JavaScript, font and logo inside the file itself, so a page still looks and works
when it is opened on its own (for example straight from a zip file or an email attachment).
Links between pages still need the folder structure (events/, blog/, legal/) to stay together.
Run after build.py:   python3 make_standalone.py
The normal site/ folder, with shared files in assets/, is the one to publish.
"""
import base64, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC, OUT = ROOT / "site", ROOT / "site-standalone"
mime = {".png": "image/png", ".woff2": "font/woff2"}
uri = lambda f: f"data:{mime[f.suffix]};base64," + base64.b64encode(f.read_bytes()).decode()

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(SRC, OUT)
shutil.rmtree(OUT / "assets")          # everything is inside the pages now

css = (SRC / "assets/style.css").read_text(encoding="utf-8")
css = css.replace('url("inter-latin-wght-normal.woff2")', f'url("{uri(SRC / "assets/inter-latin-wght-normal.woff2")}")')
js = {n: (SRC / f"assets/{n}.js").read_text(encoding="utf-8") for n in ("theme", "config", "main")}
assert not any("</script" in v for v in js.values()) and "</style" not in css

count = 0
for page in OUT.rglob("*.html"):
    t = page.read_text(encoding="utf-8")
    t = re.sub(r'<link\b[^>]*rel="preload"[^>]*>\s*', "", t)
    t = re.sub(r'<link\b[^>]*href="[^"]*assets/style\.css"[^>]*>', lambda m: f"<style>{css}</style>", t)
    t = re.sub(r'<script\b[^>]*src="[^"]*assets/(\w+)\.js"[^>]*>\s*</script>', lambda m: f"<script>{js[m.group(1)]}</script>", t)
    t = re.sub(r'(src|href)="[^"]*assets/([\w-]+\.png)"', lambda m: f'{m.group(1)}="{uri(SRC / "assets/img" / m.group(2))}"', t)
    left = re.sub(r"<(style|script)>.*?</\1>", "", t, flags=re.S)       # ignore the inlined code
    left = re.sub(r"https?://[^\s\"']+", "", left)                       # absolute web addresses are meant to stay
    assert "assets/" not in left, f"{page.name}: a local asset is still referenced"
    page.write_text(t, encoding="utf-8")
    count += 1
print(f"Wrote {count} self-contained pages to {OUT}")
