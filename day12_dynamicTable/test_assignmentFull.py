from playwright.sync_api import Page, expect


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




    page.get_by_placeholder("First Last").fill("Nitish Kumar Sahoo")
    page.locator("#address").fill("Pruchi liuxury pg,munni reddy lauout")
    page.locator("#city").fill("Bangalore")
    page.locator("#state").fill("karnataka")
    page.locator("#zipCode").fill("759103")
    page.locator("#cardType").select_option(label='American Express')
    page.locator("#creditCardNumber").fill("1234567891234")
    page.locator("#creditCardMonth").fill("10")
    page.locator("#creditCardYear").fill("2030")
    page.locator("#nameOnCard").fill("Nitish Kumar Sahoo")
    rememberBox=page.locator("#rememberMe")
    expect(rememberBox).not_to_be_checked()
    rememberBox.check()
    page.locator("input[value='Purchase Flight']").click()
    page.wait_for_timeout(2000)





