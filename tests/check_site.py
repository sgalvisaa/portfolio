"""Validate step: basic automated checks for the portfolio.

Run with:  python3 tests/check_site.py
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text()


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.cards = set(), [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "article" and "card" in a.get("class", ""):
            self.cards += 1


p = Collector()
p.feed(html)
failures = []

# 1. Every required section exists.
for section in ["top", "about", "experience", "projects", "skills", "education", "contact"]:
    if section not in p.ids:
        failures.append(f"missing section #{section}")

# 2. Every in-page link points to a real section.
for link in p.links:
    if link.startswith("#") and link[1:] not in p.ids:
        failures.append(f"broken anchor {link}")

# 3. Privacy: no phone number on the public page (ADR 0002).
if re.search(r"\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}", html):
    failures.append("phone number found on public page")

# 4. Accuracy guardrails (CONTEXT.md): no coding or AI claims at Beta.
beta = html.split("Beta Analytic &middot;")[1].split("TD Bank")[0]
for word in ["Python", "SQL", "R script", "AI", "Claude"]:
    if re.search(rf"\b{word}\b", beta):
        failures.append(f"Beta section mentions {word}")

# 5. Datasets never conflated: GSE253260 only with logistic regression.
card = html.split("GSE253260")[0].rsplit("<article", 1)[1]
if "Logistic" not in card:
    failures.append("GSE253260 appears outside the logistic regression project")

# 6. Project filter has cards to filter, and every card has tags.
if p.cards < 4:
    failures.append("fewer than 4 project cards")
if html.count('data-tags="') != p.cards:
    failures.append("a project card is missing data-tags")

# 7. No secrets in the project (ADR 0003).
for f in ROOT.rglob("*"):
    if f.is_file() and f.suffix in {".html", ".js", ".css", ".md"}:
        if re.search(r"(api[_-]?key|token|secret)\s*[:=]", f.read_text(), re.I):
            failures.append(f"possible secret in {f.name}")

if failures:
    print("FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"PASS: 7 checks, {p.cards} project cards, {len(p.links)} links")
