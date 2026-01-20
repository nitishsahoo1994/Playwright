
from playwright.sync_api import Page, expect


def test_solution_dynamicTable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table#taskTable tbody tr").all()
    cpu_load=""
    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Chrome":
            cpu_load = row.locator("td", has_text="%").inner_text()
            break

    expect(page.locator("strong.chrome-cpu")).to_contain_text(cpu_load)
