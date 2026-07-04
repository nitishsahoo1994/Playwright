

import pytest
from playwright.sync_api import Playwright, expect




def test_dd_items(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://demowebshop.tricentis.com/")
    search_box=page.locator("#small-searchterms")

    search_box.clear()
    search_box.fill("Laptop")
    page.wait_for_timeout(2000)
    page.keyboard.press("Control+A")
    page.wait_for_timeout(2000)
    page.keyboard.press("Backspace")
    page.wait_for_timeout(2000)

    page.close()
    context.close()
    browser.close()