from playwright.sync_api import Page,expect


def test_dropDownSolution(page:Page):
    page.goto("https://www.bstackdemo.com/")

    select_drop=page.locator(".sort>select")
    expect(select_drop).to_be_visible()
    expect(select_drop).to_be_enabled()

    #lowest to highest
    select_drop.select_option(label="Lowest to highest")

    #device names after sorting
    name=page.locator(".shelf-item p")
    device_name=name.all_text_contents()
    list_names=[text.strip() for text in device_name]


    device_price= page.locator("div.val").all_inner_texts()
    list_price=[text.strip() for text in device_price]

    for i in range(len(device_name)):
        print(f"{device_name[i]} : {device_price[i]}")



    page.wait_for_timeout(1000)
    page.close()
