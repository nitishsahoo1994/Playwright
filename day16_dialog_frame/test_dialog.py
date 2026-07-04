import pytest

from playwright.sync_api import Page,expect



@pytest.mark.skip
def test_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #approqch 1
    # def handle_dialog(dialog):
    #     dialog.accept()

    page.on("dialog",lambda dialog:dialog.accept())
    page.locator("button:has-text('Simple Alert')").click()
    page.wait_for_timeout(5000)

    page.close()


@pytest.mark.skip
def test_confirmation_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #page.on("dialog",lambda dialog:dialog.accept()) #click on ok
    page.on("dialog",lambda dialog:dialog.dismiss())

    page.locator("#confirmBtn").click()
    page.wait_for_timeout(3000)

    print("after click on dialog:",page.locator("#demo").inner_text())

    expect(page.locator("#demo")).to_contain_text("Cancel")
    page.wait_for_timeout(5000)
    page.close()

def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept('Nitish'))
    print("URL of that page is:",page.url)
    print("Title of that page is:",page.title() )

    page.locator("#promptBtn").click()
    print(page.locator("#demo").inner_text())





