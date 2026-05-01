import pytest
from playwright.sync_api import Playwright, expect

list_items=['laptop','Gift card','smartphone','monitor']

@pytest.mark.parametrize('items',list_items)
def test_dd_items(items,playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(items)
    page.locator(".search-box-button").click()

    actual_text=page.locator(".product-title a")
    expect(actual_text).to_contain_text(items,ignore_case=True)

    page.close()
    context.close()
    browser.close()
