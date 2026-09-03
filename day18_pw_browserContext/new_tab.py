
from playwright.sync_api import Page

def test_newTab(page: Page):

    new_tab = page.context.new_page()

    new_tab.goto("https://www.google.com")

    page.wait_for_timeout(2000)

    print(new_tab.title())