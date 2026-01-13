from playwright.sync_api import Page


def test_bootstarpDropDown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.locator("button[type='submit']").click()

    page.locator("//span[text()='PIM']").click()


    page.locator("//label[text()='Job Title']//parent::div//following-sibling::div//descendant::i").click()

    page.get_by_role("listbox").click()
    # options_list=page.locator("div[role='listbox'] span").all_text_contents()

    options_list=[text.strip() for text in page.locator("div[role='listbox'] span").all_text_contents()]
    print(options_list)


    page.wait_for_timeout(2000)