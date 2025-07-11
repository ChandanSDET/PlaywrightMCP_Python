from playwright.sync_api import sync_playwright

def test_alert_message():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page() 
        page.goto("https://demo.automationtesting.in/Index.html")

        # Fill the email and click Enter
        page.wait_for_selector("#email").fill("abc@gmail.com")
        page.locator("#enterimg").click()

        # Register a single dialog handler
        def handle_dialog(dialog):
            print("Dialog message:", dialog.message)
            # if dialog.message == "Press a Button !":
            #     dialog.dismiss()
            # elif dialog.message == "Please enter your name":
            #     dialog.accept(prompt_text="chandan")
            match dialog.message:
                case "Press a Button !":
                    dialog.dismiss()
                case "Please enter your name":
                    dialog.accept(prompt_text="chandan")
                case _:
                    dialog.accept()

        page.on("dialog", handle_dialog)

        # Hover on SwitchTo and click Alerts
        page.get_by_text('SwitchTo').hover()
        page.get_by_text('Alerts').click()

        # Trigger the confirm alert
        page.get_by_text('Alert with OK & Cancel ').click()
        page.get_by_text('click the button to display a confirm box ').click()
        page.wait_for_timeout(1000)

        # Trigger the prompt alert
        page.get_by_text("Alert with Textbox ").click()
        page.get_by_text("click the button to demonstrate the prompt box ").click()
        page.wait_for_timeout(3000)

        browser.close()
