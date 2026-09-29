# ADR 0003: Technology and deployment

Status: Accepted (2026-09-28)

## Decision
Plain HTML, CSS, and vanilla JavaScript. Deploy by dragging the folder into
Netlify Drop (app.netlify.com/drop) on a free Netlify account.

## Why
- No build tools or installs needed (this Mac has no Node.js).
- Netlify Drop publishes a static folder in about a minute and gives a live URL.

## Considered and rejected
- React/Vite: needs Node.js and a build step; unnecessary for one static page.
- GitHub Pages: good option later once the repo is on GitHub.

## Security
No secrets, tokens, or API keys are used or stored in this project.
