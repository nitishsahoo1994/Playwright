from playwright.sync_api import Page

def open_new_window(page: Page, locator: str):

    with page.context.expect_page() as new_page_info:
        page.locator(locator).click()

    new_page=new_page_info.value
    new_page.wait_for_load_state()

    return new_page

def switch_by_url(page:Page,expected_url:str):


    for p in page.context.pages:
        p.wait_for_load_state()

        if p.url == expected_url:
            p.bring_to_front()
            return p

    raise Exception(f"{expected_url} not found")


def test_multiple_windows(page: Page):
    page.goto("https://www.naukri.com/nlogin/login")

    page.locator("a:has-text('Register for Free')").click()


    locators=["a:has-text('About Us')",
              "a:has-text('Contact')",
              "a:has-text('Report a Problem')"
    ]

    #open all windows
    opened_pages=[]

    for locator in locators:
        opened_pages.append(open_new_window(page,locator))

    print(f"\nTotal Windows: {len(page.context.pages)}")

    for p in page.context.pages:
        print("---------------------")
        print("Title :", p.title())
        print("URL   :", p.url)


    #info page loading
    info_page=switch_by_url(page,"https://www.infoedge.in/")


    info_page.locator("a:has-text('BUSINESSES')").first.click()
    page.wait_for_timeout(2000)




