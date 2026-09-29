# Context: Stephanie Galvis Portfolio

Step 1 of the loop (context, spec, build, validate, ship).

## What is this?
A single-page personal portfolio website that presents Stephanie's experience,
projects, and skills to recruiters and hiring managers.

## Who is it for?
- Recruiters and hiring managers for Data Analyst, Statistical Analyst, and
  Data Quality roles (healthcare, life sciences, clinical research).
- They spend under a minute on it, so the most important facts must be visible
  without scrolling.

## What problem does it solve?
Her resume is one page and cannot show project detail. A public link gives
recruiters proof of real work (methods, datasets, tools) and a place to link
code samples and Tableau dashboards.

## What's in scope
- One page: hero, about, experience, projects (filterable), skills, education, contact.
- Content taken only from her real, verified resume and project files.
- Static HTML, CSS, and a small amount of JavaScript. No build step.

## What's out of scope (for now)
- Blog, CMS, login, contact form (needs a backend, API keys, spam handling).
- Phone number and home address (privacy on a public page).

## Accuracy rules
- Nothing invented. Every claim must be defensible in an interview.
- Beta Analytic = data validation, reconciliation, root cause, documentation.
  No coding or AI at Beta.
- Datasets are never merged: GSE253260 = logistic regression + LOOCV;
  Rice STAT553 = Kaplan-Meier and Cox survival; Broad Repurposing Hub = drug repositioning.
