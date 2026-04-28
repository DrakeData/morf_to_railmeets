from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    # Go to RailMeets
    page.goto("https://morf.railmeets.com/")

    # Click "Sign in with Google"
    page.get_by_text("Sign in with Google").click()

    print("👉 Complete Google login in the browser window")

    # Give you time to log in manually
    page.wait_for_timeout(120000)  # 2 minutes (adjust if needed)

    # Save authenticated session
    context.storage_state(path="railmeets_state.json")

    print("✅ Session saved")

    browser.close()