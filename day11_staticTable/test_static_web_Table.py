from playwright.sync_api import Page, expect


def test_static_web_Table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #locating table
    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()


    #1. count total number of rows in a table
    rows=table.locator("tr")
    expect(rows).to_have_count(7)

    rows_count=rows.count()
    print("No of rows avl in table:",rows_count)

    # 2. count total number of columns/headers in table
    col=rows.locator("th")
    expect(col).to_have_count(4)

    col_count=col.count()
    print("No of col avl in table:",col_count)


    #3. Read all the data from 2nd row of the table
    second_row=rows.nth(3).locator("td")
    second_row_texts=second_row.all_inner_texts()
    print("Second row is",second_row_texts)


    for text in second_row_texts:
        print(text)

    #read all text from table
    all_data=rows.all()
    #
    # for row in all_data[1:]:
    #     print(row.locator("td").all_inner_texts())

    #print all book name written by Mukesh
    for row in all_data[1:]:
        authorName=row.locator("td").nth(1).inner_text()
        if authorName=="Mukesh":
            book_Name=row.locator("td").nth(0).inner_text()
            print(f"{authorName} {book_Name}")

    total=0
    for row in all_data[1:]:
        price=row.locator("td").nth(3).inner_text()
        total+=int(price)
    print("Total price of all books are ",total)



