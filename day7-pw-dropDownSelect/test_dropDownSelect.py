from gettext import pgettext

from playwright.sync_api import Page, expect


def test_dropDowntest(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    country_drop=page.locator("#country")


    country_drop.select_option(label="Brazil")

    dropdown_options=page.locator("#country>option")
    #list all options from dropdown
    for text in dropdown_options.all_text_contents():
        print(text.strip())

    #no of options in dropdown
    expect(dropdown_options).to_have_count(10)

    #if India option is present in dropdown then select it
    country='India'
    for text in dropdown_options.all_text_contents():
        if(text.strip()==country):
            country_drop.select_option(label=country)
            break


    page.wait_for_timeout(5000)
    page.close()


