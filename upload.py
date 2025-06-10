from playwright.async_api import async_playwright

async def upload_pdf(pdf_path, parqet_id, timeout_ms):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state="auth.json")  # Use saved login session
        page = await context.new_page()

        # Navigate to upload page
        await page.goto(f'https://app.parqet.com/p/{parqet_id}/activities/create?&highlight=files')

        # Set the file directly using the id "import-files" of input
        await page.set_input_files("#import-files", pdf_path)

        try:
            #Wait for positive feedback. if there is none -> print message on server/bot
            await page.wait_for_selector("text=1 Aktivität erfolgreich importiert", timeout=timeout_ms)
        except Exception as e:
            print(e);

        print("✅ PDF-Upload was successful.")
        await browser.close()
