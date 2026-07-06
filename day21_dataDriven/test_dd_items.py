import pytest
from playwright.sync_api import Playwright, expect


search_items=['Laptop','Gift card','smartphone','monitor']


@pytest.mark.parametrize('item',search_items)
def test_dd_items(item,playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)

    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page=context.new_page()

    page.goto("https://demowebshop.tricentis.com/")
    search_box=page.locator("#small-searchterms")

    search_box.clear()
    search_box.fill(item)
    page.wait_for_timeout(2000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)


    #
    first_result=page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item,ignore_case=True)




    page.close()
    context.close()
    browser.close()