from playwright.sync_api import Page


def test_mouseover(page:Page)->None:
    page.set_viewport_size({"width":1920,'height':1080})
    #page.set_viewport_size({"width": 2040, "height": 1920})
    page.goto("https://www.globalsqa.com/")
    header_menu=page.locator("#menu-item-7128",has_text='Free Ebooks')

    print(header_menu.text_content())
    header_menu.hover()

    page.wait_for_timeout(2000)
    page.close()