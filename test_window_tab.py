from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  # Create new browser context
    page = context.new_page()

    page.goto("https://demo.automationtesting.in/Windows.html")

    # Click the "click" button to open new tab
    #page.wait_for_selector("//a/button[contains(text(),'click')]").click()

    with context.expect_page() as new_page_info:
        page.wait_for_selector("//a/button[contains(text(),'click')]").click()
    # Wait for new page (tab) to open
    new_tab = new_page_info.value
    new_tab.wait_for_load_state()

    print("New tab title:", new_tab.title())
    print("New tab URL:", new_tab.url)

    # You can now interact with the new tab
    # For example, close it after use:
    new_tab.close()

    browser.close()
