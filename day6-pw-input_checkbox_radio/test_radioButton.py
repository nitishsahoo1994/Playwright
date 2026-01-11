from playwright.sync_api import Page, expect


def test_radioButton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_button=page.locator("#male")


    # check enable or visible
    expect(male_button).to_be_visible()
    expect(male_button).to_be_enabled()

    # Male radio button should not be checked ( default)
    expect(male_button).not_to_be_checked()

    # Select/Check radio button - action
    male_button.check()

    # Male radio button should be checked ( default)
    expect(male_button).to_be_checked()

    page.wait_for_timeout(3000)
    page.close()

