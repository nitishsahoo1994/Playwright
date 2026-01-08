import re
from playwright.sync_api import Page, expect


# page.get_by_alt_text()
# page.get_by_text()
# page.get_by_role()
# page.get_by_label()
# page.get_by_placeholder()
# page.get_by_title()


def test_verifyLogo(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    # 1) page.get_by_alt_text()
    logo=page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()  #full text
    expect(page.get_by_text("Welcome")).to_be_visible() # partial text
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() # regular expression

    # 3) page.get_by_role()

    # 4) page.get_by_label()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(2000)
    page.get_by_label("First name: ").fill("Nitish")
    page.wait_for_timeout(2000)

    # 5) page.get_by_placeholder()
    page.get_by_placeholder("Search store").fill("iphone 16")
    page.wait_for_timeout(2000)

    # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")