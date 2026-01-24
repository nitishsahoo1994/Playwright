from playwright.sync_api import Page

def test_assignmentFull(page:Page):
    page.goto("https://blazedemo.com/")

    page.locator("select[name='fromPort']").select_option(label='Boston')
    page.locator("select[name='toPort']").select_option(label='Berlin')

    page.locator("input[value='Find Flights']").click()

    rows=page.locator(".table tbody tr")
    row_count=rows.count()

    prices=[]
    for i in range(row_count):
        price_text=rows.nth(i).locator("td").nth(5).inner_text()
        prices.append(price_text)
    print("flight prices are",prices)


    #sorting the price
    sorted_price=sorted(prices)
    lowest_flight_price=sorted_price[0]
    print("lowest flight price",lowest_flight_price)


    for i in range(row_count):
        price_text=price_text=rows.nth(i).locator("td").nth(5).inner_text()
        if price_text==lowest_flight_price:
            rows.nth(i).locator("td").nth(0).locator("input[type='submit']").click()
            break


    page.wait_for_timeout(2000)

    page.get_by_placeholder("First Last").fill("Nitish Kumar Sahoo")
    page.locator("#address").fill("Pruchi liuxury pg,munni reddy lauout")\




