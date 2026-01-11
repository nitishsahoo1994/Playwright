from playwright.sync_api import Page

def test_checkBox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_label("Sunday")



    page.close()