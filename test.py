from pathlib import Path
from playwright.sync_api import sync_playwright

import os

with sync_playwright() as p:
    website="https://example.com"
    if os.getenv("WEBSITE") != None:
        website=os.getenv("WEBSITE")

    browser = p.chromium.launch(headless=True)
    auth_file = Path("auth.json")
    if auth_file.exists():
        context = browser.new_context(storage_state="auth.json")

    page = browser.new_page()
    page.goto(website)
    print(page.content())
    browser.close()
