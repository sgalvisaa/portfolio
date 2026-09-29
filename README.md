# Stephanie Galvis Portfolio

A single-page portfolio built with Claude Code using the loop:
context, spec, build, validate, ship.

- `docs/CONTEXT.md`: what this is, who it's for, what's in and out of scope
- `docs/adr/`: decision records (scope, content and privacy, tech and deploy)
- `index.html`, `styles.css`, `script.js`: the site (no build step)
- `tests/check_site.py`: automated checks (run `python3 tests/check_site.py`)

## Ship it (about 10 minutes)
1. Open the site locally first: double-click `index.html` and read every section.
2. Run the checks: `python3 tests/check_site.py` should print PASS.
3. Create a free account at https://app.netlify.com (sign up with email or GitHub).
4. Go to https://app.netlify.com/drop and drag this whole `portfolio` folder onto the page.
5. Netlify gives you a live URL. In Site configuration > Change site name,
   rename it to something like `stephanie-galvis`.
6. Open the live URL on your phone to check the mobile layout.

## Later
- Add the real Tableau Public profile link to the Tableau card.
- Push this repo to GitHub, then connect Netlify to GitHub for automatic deploys.
