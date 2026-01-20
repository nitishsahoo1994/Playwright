from playwright.sync_api import Page, expect


def test_verify_chrome_cpu_load(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table=page.locator("table.table tbody")

    rows=table.locator("tr")

    all_data=rows.all()

    for row in all_data:
        browser=row.locator("td").nth(0).inner_text()
        if browser=="Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print("Cpu load value is:",cpu_load)
            break


    chrome_cpu=page.locator("#chrome-cpu")
    expect(chrome_cpu).to_contain_text(cpu_load)
    page.wait_for_timeout(5000)
