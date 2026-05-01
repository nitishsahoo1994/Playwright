# from playwright.sync_api import Playwright
#
#
# def test_popUps(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.wait_for_load_state()
#     page.goto("https://testautomationpractice.blogspot.com/")
#
#     # def handle_popUp(popup):
#     #     popup.wait_for_load_state()
#     #
#     # page.on("popup",handle_popUp)
#
#
#     page.on("popup", lambda popup: popup.wait_for_load_state())
#     page.locator("#PopUp").click()
#
#     page.wait_for_timeout(3000)
#     all_popups=context.pages
#     print("total no of popup/pages are:",len(all_popups))
#     page.close()


from playwright.sync_api import Playwright, expect


def test_popUps(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_popup() as popup_info:
        page.locator("#PopUp").click()

    popup = popup_info.value
    popup.wait_for_load_state()

    all_popups = context.pages
    print("Total number of pages:", len(all_popups))

    for pop in all_popups:
        print("url of pops are:",pop.url)
        title=pop.title()
        if title=="Selenium":
            pop.locator("a:has-text('Docs')")
            pop.wait_for_timeout(5000)




    popup.close()
    page.close()
    browser.close()
