from playwright.sync_api import Playwright

def test_popUps(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parent_page = context.new_page()

    parent_page.goto("https://testautomationpractice.blogspot.com/")

    with parent_page.expect_popup() as popup_info:
        parent_page.locator("button:has-text('New Tab')").click()


    popup= popup_info.value
    popup.wait_for_load_state()
