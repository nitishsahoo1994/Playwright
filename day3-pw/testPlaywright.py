from playwright.sync_api import Page, expect


def test_verifyPageUrl(page: Page):
    page.goto("http://www.automationpractice.pl/index.php")
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")


def test_verifyTitle(page: Page):
    page.goto("http://www.automationpractice.pl/index.php")
    pageTitle = page.title()
    # print(pageTitle)
    expect(page).to_have_title("My Shop")
