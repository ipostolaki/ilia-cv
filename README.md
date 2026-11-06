# Ilia Postolaki — CV

Personal CV site for [Ilia Postolaki](https://github.com/ipostolaki): a static HTML page, a printable PDF, and an interactive career graph.

**Live site:** [https://ipostolaki.github.io/ilia-cv/](https://ipostolaki.github.io/ilia-cv/)  
Served from GitHub Pages (`master`, repo root). There is no custom domain.

## Main page

[`index.html`](index.html) is the CV. It is styled by [`styles.css`](styles.css) (Solarized warm palette). The header links to a download of [`cv_ilia_postolaki.pdf`](cv_ilia_postolaki.pdf).

## Career graph

[`graph/`](graph/) is a separate page at [https://ipostolaki.github.io/ilia-cv/graph/](https://ipostolaki.github.io/ilia-cv/graph/). It draws companies and technologies as a Cytoscape.js network (roles are the edges). Layout sliders on the page adjust the force-directed layout. The graph is not used when printing the PDF.

## PDF script

[`html_to_pdf.py`](html_to_pdf.py) prints the CV to A4 with a flat paper background. It serves the folder locally, opens it in headless Chromium via Playwright, and writes `cv_ilia_postolaki.pdf`.

```bash
# Playwright + Chromium from the Astroswing venv on this machine
/root/astroswing/.venv/bin/python html_to_pdf.py
```

## robots.txt

[`robots.txt`](robots.txt) sends `Disallow: /` to well-behaved crawlers so the site is not indexed.
