# run_login.py
from playwright.sync_api import sync_playwright

# logs in and saves the result to auth.json
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.parqet.com/auth/login")

    print("⚠️  Bitte logge dich manuell bei Parqet ein und drücke danach [ENTER].")
    input()

    context.storage_state(path="auth.json")
    browser.close()

sync_playwright()
