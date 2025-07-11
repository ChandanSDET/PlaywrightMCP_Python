from playwright.sync_api import Page

class DemoPage:

    def __init__(self, page:Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.enterButton = page.locator("#enterimg")
        self.first_name_input = page.locator("input[placeholder='First Name']")

