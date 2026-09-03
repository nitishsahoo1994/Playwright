from playwright.sync_api import Page

def test_twoTabs(page: Page):

    page.goto("https://www.google.com")

    second_tab = page.context.new_page()

    second_tab.goto("https://www.bing.com")

    print(page.title())

    print(second_tab.title())

    page.wait_for_timeout(2000)
    page.bring_to_front()
    page.wait_for_timeout(2000)

    second_tab.bring_to_front()

    page.wait_for_timeout(2000)