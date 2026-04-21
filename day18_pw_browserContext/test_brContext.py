from playwright.sync_api import Playwright, expect


# browser---> context(user profile) -----> page
def test_browser_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context1=browser.new_context()
    context2=browser.new_context()

    page1=context1.new_page()
    page2=context2.new_page()

    page1.goto("https://playwright.dev/python/docs/intro")
    page1.wait_for_timeout(300)
    expect(page1).to_have_title("Installation | Playwright Python")


    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")

    # total_pages=context.pages
    # print(len(total_pages))


