from playwright.sync_api import Page


def test_assignmentPagination(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows=page.locator("#productTable tbody tr")

    has_more_pages=True

    page_no=page.locator("#pagination li a")
    count=page_no.count()
    # while i<count:



    for i in range(1,count+1):
        page.locator(f"//a[text()='{i}']").click()
        print(rows.all_inner_texts())
    page.wait_for_timeout(2000)


