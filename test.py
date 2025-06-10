from playwright.sync_api import sync_playwright

import os

with sync_playwright() as p:
    website="https://example.com"
    if os.getenv("WEBSITE") != None:
        website=os.getenv("WEBSITE")
    
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(website)
    page.goto(website)
    print(page.content())
    browser.close()
