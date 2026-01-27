from playwright.sync_api import Page

def select_checkInDate(page,target_year,target_month,target_date):
    #select month and year
    while True:
        month_year=page.locator("h3[aria-live='polite']").nth(0).inner_text()
        current_month,current_year=month_year.split(" ")

        if current_month==target_month and current_year==target_year:
            break
        else:
            page.locator("button[aria-label='Next month'] svg").click()


    #select date
    table_body=page.locator("table[role='grid'] tbody")
    dates_text=table_body.nth(0).locator("td").all()

    for dt in dates_text:
        if dt.inner_text()==target_date:
            dt.click()
            break






def test_booking_Date_picker(page:Page):
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click()

    select_checkInDate(page,"2026","March","15")
    #select_checkOutDate(page,"2026","April","15")