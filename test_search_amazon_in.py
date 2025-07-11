import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("search_term", ["xiaomi mobile"])
def test_search_amazon_in(search_term):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in")
        page.fill("input[name='field-keywords']", search_term)
        page.press("input[name='field-keywords']", "Enter")
        page.wait_for_selector("span.a-size-medium")
        product_titles = page.query_selector_all("span.a-size-medium")
        assert product_titles, "No products found."
        for title in product_titles:
            text = title.inner_text().lower()
            assert "xiaomi" in text, f"Product title does not contain 'xiaomi': {text}"
        browser.close()
