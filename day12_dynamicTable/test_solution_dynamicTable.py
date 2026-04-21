
from playwright.sync_api import Page, expect, Browser


def test_solution_dynamicTable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table=page.locator("table[name='BookTable']  tbody")

    rows=table.locator("tr")
    expect(rows).to_have_count(7)
    print("no of rows are: ",rows.count())

    columns=rows.locator("th")
    expect(columns).to_have_count(4)
    print("no of col are: ",columns.count())


    # read all data from 2nd row
    second_row=rows.nth(1).locator("td")
    print(second_row.all_inner_texts())



