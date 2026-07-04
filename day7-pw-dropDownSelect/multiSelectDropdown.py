from playwright.sync_api import Page, Playwright
import pytest


@pytest.mark.skip
def test_mutiselectDropDown(page:Page) -> None:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    multi_dropdown=page.locator("select[name='Month']")
    multi_dropdown.select_option(['September','May','July'])
    page.wait_for_timeout(3000)

    page.close()


def test_multiValue(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    country_dropdown=page.locator("select[name='country'] >option")

    values=country_dropdown.all_inner_texts()
    first_country=country_dropdown.first_
    print(type(country_dropdown))
    print(type(values))
    for country in values:
        print(country)

