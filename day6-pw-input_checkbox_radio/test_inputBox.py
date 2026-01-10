from playwright.sync_api import Page,expect


def test_inputBox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box=page.locator("input#name")

    #1visibility of the element and enable or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    # check the attribute of the elements
    expect(text_box).to_have_attribute("maxlength","15")

    #find attribute
    maxlenght=text_box.get_attribute("maxlength")
    assert maxlenght=="15"
    print("Maxlength value is :",maxlenght)


    # Fill the text
    text_box.fill("John Kenedy")

    # get the input value from inputbox
    entered_value=text_box.input_value()
    print("Value entered in box is:",entered_value)

    page.wait_for_timeout(5000)
    page.close()

