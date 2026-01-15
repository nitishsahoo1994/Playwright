from playwright.sync_api import Page


def test_bootstarpDropDown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.locator("button[type='submit']").click()

    page.locator("//span[text()='PIM']").click()


    page.locator("//label[text()='Job Title']//parent::div//following-sibling::div//descendant::i").click()

    page.wait_for_timeout(2000)


    # options_list=page.locator("div[role='listbox'] span").all_text_contents()
    dropDown_options=page.locator("div[role='listbox'] span")
    count=dropDown_options.count()


    #lis_of_job=dropDown_options.all_text_contents()
    options_list=[text.strip() for text in dropDown_options.all_text_contents()]
    print(options_list)

    # for i in range(count):
    #     print(dropDown_options.nth(i).text_content())

    for i in range(count):
        text=dropDown_options.nth(i).text_content()
        if text== 'Chief Financial Officer':
            dropDown_options.nth(i).click()
            break


    page.close()


