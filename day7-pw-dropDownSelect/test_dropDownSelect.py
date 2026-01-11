from playwright.sync_api import Page


def test_dropDowntest(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator()