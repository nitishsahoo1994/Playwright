from playwright.sync_api import Page

def test_pagination_table(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages=True

    while has_more_pages:
        rows=page.locator("#example  tbody tr").all()
        for row in rows:
            print(row.inner_text())
        page.wait_for_timeout(2000)
        next_button=page.locator("button[aria-label='Next']")
        disable_button=next_button.get_attribute("class")
        if "disabled" in disable_button:
            has_more_pages=False
        else:
            next_button.click()
        # if next_button.is_disabled():
        #     has_more_pages=False
        # else:
        #     next_button.click()



