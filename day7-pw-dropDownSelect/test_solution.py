from playwright.sync_api import Page,expect


def test_dropDownSolution(page:Page):
    page.goto("https://www.bstackdemo.com/")

    page.locator("div[class='sort']>select").select_option(label="Lowest to highest")
    page.wait_for_timeout(2000)


    name=page.locator(".shelf-item p")
    device_name=name.all_text_contents()
    list_names=[text.strip() for text in device_name]
    print(list_names)

    #count=device_name.count()

    #device_price=page.locator(".shelf-item .shelf-item__price>div[class='val']>b").all_text_contents()
    device_price= page.locator("div.val").all_inner_texts()

    for i in range(len(device_name)):
            print(f"Price of {device_name[i]} is {device_price[i]}")

    print(f"Lowest price deice and price is==>{device_name[0]}:{device_price[0]}")

    name_list=name.all()

    print(name_list[2].inner_text())
    for i in name_list:
        print("name in list:",i.inner_text())

    page.close()
