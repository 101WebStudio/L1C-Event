# L1C — Level One Connect

**Creating experiences that bring leaders together.**

L1C — Level One Connect is a corporate events and executive networking brand focused on creating meaningful experiences for business leaders, decision-makers, and industry professionals.

Our website showcases our services, company, event portfolio, planning process, and insights into the world of executive networking and corporate experiences.

---

## 🌐 Website

**Live Website:** [Visit Level One Connect]


## ✨ What We Do

* **Corporate Event Planning** — Strategic planning and delivery of professional business events.
* **Executive Networking** — Bringing senior leaders and decision-makers together.
* **Strategic Event Consulting** — Turning business objectives into meaningful event experiences.
* **Event Management** — Coordinating the details from initial concept through execution.
* **Industry Events & Experiences** — Creating opportunities for conversations, connections, and collaboration.

## 🎨 Brand Identity

The L1C website uses a modern, premium visual direction designed to reflect professionalism, innovation, and connection.

* **Primary colours:** Black, white, and blue (`#5170FF`)
* **Design style:** Clean, modern, and corporate
* **Layout:** Responsive pages with clear navigation and structured content
* **Experience:** Designed for business leaders, partners, and prospective clients

## 📄 Website Pages

| Page             | Description                                      |
| ---------------- | ------------------------------------------------ |
| Home             | Brand introduction and key services              |
| Services         | Corporate event planning and networking services |
| About            | Company background and vision                    |
| Process          | Our approach to planning and delivering events   |
| Events           | Upcoming and featured events                     |
| Blog             | Articles, insights, and industry perspectives    |
| Contact          | Contact information and enquiries                |
| Start Your Event | A starting point for new event projects          |
| Legal            | Privacy policy, terms, and cookie policy         |

## 🛠️ Technology

The website is built with standard web technologies:

* HTML
* CSS
* JavaScript
* Python-based site generation
* GitHub Actions
* GitHub Pages

The website uses a template-and-data structure to keep pages organised and make updates easier.

## 📁 Project Structure

```text
L1C-Event/
├── source/
│   ├── data/
│   │   ├── events.py
│   │   └── posts.py
│   ├── config.py
│   ├── build.py
│   └── check_site.py
├── site/
│   ├── assets/
│   ├── events/
│   ├── blog/
│   └── index.html
├── README.md
└── README.txt
```

* `source/data/events.py` — Event information and content.
* `source/data/posts.py` — Blog post content.
* `source/config.py` — Website configuration and contact details.
* `source/build.py` — Generates the website pages.
* `source/check_site.py` — Checks the generated website.
* `site/` — Contains the generated website ready for publishing.

## 🚀 Build & Run

Make sure Python 3 is installed.

Navigate to the source directory:

```bash
cd source
```

Build the website:

```bash
python3 build.py
```

Check the generated website:

```bash
python3 check_site.py
```

On Windows, you can use `python build.py` and `python check_site.py` if `python3` is not recognised.

## 📦 Deployment

The website is published through GitHub Pages using GitHub Actions.

1. Push your changes to the `main` branch.
2. GitHub Actions rebuilds and checks the website.
3. The generated `site/` directory is published to GitHub Pages.

**Initial setup:** Open your repository's Settings → Pages and select **GitHub Actions** as the publishing source.

## 📬 Contact

For corporate event enquiries, executive networking opportunities, and potential partnerships, visit the [L1C website](https://101-studio.github.io/L1C-Event/site/contact.html).

---

**L1C — Level One Connect**
*Experiences that redefine how leaders meet, think, and decide.*

Website crafted by [101WebStudio](https://101webstudio.github.io/).
