(function () {
  var d = document,
    rm = matchMedia("(prefers-reduced-motion:reduce)").matches,
    h = d.getElementById("hd"),
    mb = d.getElementById("mb"),
    m = d.getElementById("menu");
  function sc() {
    h.classList.toggle("sc", scrollY > 30);
  }
  sc();
  addEventListener("scroll", sc, { passive: true });
  mb.onclick = function () {
    var o = m.classList.toggle("open");
    mb.setAttribute("aria-expanded", o);
    d.body.style.overflow = o ? "hidden" : "";
  };
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && m.classList.contains("open")) mb.click();
  });
  var io = new IntersectionObserver(
    function (es) {
      es.forEach(function (x) {
        if (x.isIntersecting) {
          x.target.classList.add("in");
          io.unobserve(x.target);
          var b =
            x.target.querySelector("[data-n]") ||
            (x.target.dataset.n ? x.target : null);
          if (b && !rm) cnt(b);
        }
      });
    },
    { threshold: 0.15 },
  );
  d.querySelectorAll(".rv").forEach(function (e) {
    io.observe(e);
  });
  function cnt(b) {
    var n = +b.dataset.n,
      s = b.dataset.s,
      t = 0;
    (function f() {
      t += n / 50;
      if (t >= n) {
        b.textContent = n + s;
        return;
      }
      b.textContent = Math.floor(t) + s;
      requestAnimationFrame(f);
    })();
  }
  var hb = d.querySelector(".hero");
  if (hb && !rm)
    addEventListener(
      "scroll",
      function () {
        hb.style.backgroundPositionY = "calc(50% + " + scrollY * 0.25 + "px)";
      },
      { passive: true },
    );
  d.querySelectorAll(".steps button").forEach(function (b) {
    b.onclick = function () {
      d.querySelectorAll(".steps button").forEach(function (x) {
        x.classList.remove("on");
        x.setAttribute("aria-selected", "false");
      });
      d.querySelectorAll(".sp").forEach(function (x) {
        x.classList.remove("on");
      });
      b.classList.add("on");
      b.setAttribute("aria-selected", "true");
      d.querySelectorAll(".sp")[b.dataset.i].classList.add("on");
    };
  });
  var fs = d.querySelectorAll("#cf");
  fs.forEach(function (f) {
    var t0 = Date.now(),
      st = f.querySelector("#st");
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      st.textContent = "";
      var ok = true,
        data = {};
      f.querySelectorAll(".f").forEach(function (w) {
        var i = w.querySelector("input,select,textarea"),
          v = i.value.replace(/[\u0000-\u001f<>]/g, " ").trim(),
          er = "";
        if (i.required && !v) er = "This field is required.";
        else if (i.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v))
          er = "Enter a valid email address.";
        else if (i.type === "tel" && v && !/^[+\d\s()-]{6,30}$/.test(v))
          er = "Enter a valid phone number.";
        w.classList.toggle("bad", !!er);
        w.querySelector(".err").textContent = er;
        i.setAttribute("aria-invalid", !!er);
        if (er && ok) {
          ok = false;
          i.focus();
        }
        data[i.name] = v;
      });
      if (!ok) return;
      if (f.website.value || Date.now() - t0 < 2500) {
        st.textContent = "Thank you. We'll be in touch shortly.";
        f.reset();
        return;
      }
      var b = f.querySelector("button"),
        l = b.firstChild;
      b.disabled = true;
      b.querySelector("span").textContent = "Sending…";
      function done(s, msg) {
        b.disabled = false;
        b.querySelector("span").textContent = "Send Message";
        st.textContent = msg;
        if (s) f.reset();
      }
      if (window.L1C_ENDPOINT) {
        fetch(window.L1C_ENDPOINT, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify(data),
        })
          .then(function (r) {
            if (!r.ok) throw 0;
            done(
              1,
              "Thank you! Your message has been sent. We'll reply shortly.",
            );
          })
          .catch(function () {
            done(
              0,
              "Something went wrong. Please email us directly at " +
                window.L1C_EMAIL +
                ".",
            );
          });
      } else {
        var body = Object.keys(data)
          .map(function (k) {
            return k + ": " + data[k];
          })
          .join("\n");
        location.href =
          "mailto:" +
          window.L1C_EMAIL +
          "?subject=" +
          encodeURIComponent("Event enquiry from " + data.name) +
          "&body=" +
          encodeURIComponent(body);
        done(1, "Your email app should open with the message ready to send.");
      }
    });
  });

  /* theme toggle */
  var tt = d.getElementById("tt"),
    root = d.documentElement;
  function setT(t) {
    root.dataset.theme = t;
    tt.setAttribute("aria-pressed", t === "dark");
    try {
      localStorage.setItem("l1c-theme", t);
    } catch (e) {}
  }
  tt.setAttribute("aria-pressed", root.dataset.theme === "dark");
  tt.onclick = function () {
    setT(root.dataset.theme === "dark" ? "light" : "dark");
  };

  /* blue glow that follows the mouse on hero, dark sections and cards */
  d.querySelectorAll(".glow,.dark,.card,.tile").forEach(function (el) {
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty("--mx", e.clientX - r.left + "px");
      el.style.setProperty("--my", e.clientY - r.top + "px");
    });
  });

  /* soft page-wide cursor glow (mouse devices only) */
  if (matchMedia("(hover:hover) and (pointer:fine)").matches && !rm) {
    var c = d.createElement("div"),
      x = 0,
      y = 0,
      cx = 0,
      cy = 0;
    c.className = "cur";
    c.setAttribute("aria-hidden", "true");
    d.body.appendChild(c);
    addEventListener(
      "pointermove",
      function (e) {
        x = e.clientX;
        y = e.clientY;
        c.classList.add("on");
      },
      { passive: true },
    );
    d.addEventListener("pointerleave", function () {
      c.classList.remove("on");
    });
    (function tick() {
      cx += (x - cx) * 0.12;
      cy += (y - cy) * 0.12;
      c.style.transform = "translate(" + cx + "px," + cy + "px)";
      requestAnimationFrame(tick);
    })();
  }

  /* rotating event words in the hero */
  var rw = d.getElementById("rw");
  if (rw && !rm) {
    var ws = [
        "Executive Networking",
        "Leadership Dinners",
        "Business Summits",
        "Corporate Conferences",
        "Product Launches",
        "Technology Events",
      ],
      wi = 0;
    setInterval(function () {
      rw.classList.add("out");
      setTimeout(function () {
        wi = (wi + 1) % ws.length;
        rw.textContent = ws[wi];
        rw.classList.remove("out");
      }, 400);
    }, 2600);
  }

  /* if a photo cannot load, show the dark placeholder instead of a broken image */
  d.querySelectorAll("img").forEach(function (im) {
    function bad() {
      im.classList.add("nophoto");
    }
    im.addEventListener("error", bad);
    if (im.complete && im.naturalWidth === 0 && im.src.indexOf("data:") !== 0)
      bad();
  });
})();
