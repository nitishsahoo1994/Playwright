from gettext import pgettext

from playwright.sync_api import Page


def test_dropDowntest(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    country_drop=page.locator("#country")

    # 3 ways to select option from drop down
    # country_drop.select_option(label="Germany")
    # country_drop.select_option(value="")
    country_drop.select_option(index=5)
    page.wait_for_timeout(2000)



    # check no of options avl in dropdown
    dropDown_options=page.locator("#country>option")
    print("total no of options avl is",dropDown_options.count())

    country_list=[text.strip() for text in  dropDown_options.all_text_contents()]
    print(country_list)
    for country in country_list:
        print(country.strip())