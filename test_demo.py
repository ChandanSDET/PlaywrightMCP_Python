from playwright.sync_api import sync_playwright
from pages.demo_page import DemoPage;

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    demo_page = DemoPage(page)

    print(page.title())
    #email_input = page.wait_for_selector("#email")
    #enterButton = page.locator("#enterimg")
   

    #email_input.type("abc@gmail.com")
    demo_page.email_input.fill("abc@gmail.com")
    demo_page.enterButton.click()
    firstName = page.locator("input[placeholder='First Name']")
    firstName.type('Chandu')
    page.wait_for_selector("#checkbox2").click()
    page.select_option("xpath=//select[@id='Skills']", label="Java")
    page.wait_for_timeout(3000)
    page.set_input_files("#imagesrc", "happy4.jpeg")
    page.wait_for_timeout(3000)
    browser.close()
    