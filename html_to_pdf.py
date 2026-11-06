#!/usr/bin/env python3
"""Print the CV to a flat A4 PDF with a solid --paper background."""

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
CHROME = Path("/root/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome")
OUT = ROOT / "portfolio.pdf"
PAPER = "#fdf6e3"
PRINT_CSS = f"""
@page {{
  size: A4;
  margin: 14mm 16mm 16mm;
  background: {PAPER};
}}
html, body, .page {{
  background: {PAPER} !important;
  background-image: none !important;
  box-shadow: none !important;
}}
.page {{
  width: auto !important;
  max-width: none !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
}}
"""


def main() -> None:
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ROOT), **kwargs)

        def log_message(self, format, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=str(CHROME),
            headless=True,
            args=["--no-sandbox", "--disable-gpu"],
        )
        page = browser.new_page()
        page.goto(f"{base}/", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(400)
        page.add_style_tag(content=PRINT_CSS)
        page.pdf(
            path=str(OUT),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
        )
        print(OUT)
        browser.close()
    server.shutdown()


if __name__ == "__main__":
    main()
