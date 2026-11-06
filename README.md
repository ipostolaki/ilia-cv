# Ilia Postolaki — CV

This repository is a static CV site: an HTML page, a printable PDF, and an interactive career graph. GitHub Pages serves the site at https://ipostolaki.github.io/ilia-cv/ from the master branch, using the repository root.

## index.html

index.html is the CV. styles.css next to it provides the layout and colours. The page header includes a control that downloads cv_ilia_postolaki.pdf from the same directory.

## graph/

graph/ is a second page, opened as graph/index.html (https://ipostolaki.github.io/ilia-cv/graph/). It shows companies and technologies as a node-edge network in the browser (Cytoscape.js). Roles are the connections between company and technology nodes. Controls on that page adjust the layout. The graph is not part of the printed PDF.

## html_to_pdf.py

html_to_pdf.py generates cv_ilia_postolaki.pdf from index.html. From the repository root, run: python html_to_pdf.py

The script starts a local HTTP server for this directory, opens the CV in headless Chromium through Playwright, and writes an A4 PDF with a flat paper background. Playwright and Chromium must be available; the Chromium path is set in the script itself. Output is always cv_ilia_postolaki.pdf in the repository root.

## robots.txt

robots.txt tells well-behaved crawlers not to index the site (User-agent: all, Disallow: /).
