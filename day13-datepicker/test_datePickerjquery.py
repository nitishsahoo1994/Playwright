from datetime import datetime
from playwright.sync_api import Page


def is_future_month(month_name, year):
    date_map = datetime.strptime(f"{month_name} {year}", "%B %Y")
    return date_map > datetime.now()

def select_date(page,target_year,target_month,target_date,is_future):
    # select month and year
    while True:
        current_month=page.locator(".ui-datepicker-month").text_content()
        current_year=page.locator(".ui-datepicker-year").text_content()

        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
            page.locator("a[title='Next']").click()
        else:
            page.locator("a[title='Prev']").click()

    # select date
    dates=page.locator(".ui-datepicker-calendar td").all()

    for dt in dates:
        if dt.inner_text()==target_date:
            dt.click()
            break


def test_datepickerjquery(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input=page.locator("#datepicker")

    #approach1
    # date_input.fill("10/12/2025")

    #approach2
    # Example
    year="2024"
    month="April"
    date="15"
    date_input.click()
    is_future = is_future_month(month, year)
    select_date(page,year,month,date,is_future)

    print(date_input.input_value())


    page.wait_for_timeout(3000)


