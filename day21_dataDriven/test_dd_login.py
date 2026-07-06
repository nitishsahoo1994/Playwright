import pytest
from playwright.sync_api import Playwright, expect
import json




@pytest.mark.parametrize('email_id,password,validity',login_test_data)
def test_dd_login(email_id,password,validity,playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(viewport={"width": 1920, "height": 1080})
    page=context.new_page()

    page.goto("https://demowebshop.tricentis.com/")

    #click on login link
    page.locator("li a.ico-login").click()
    page.wait_for_timeout(200)

    #Enter username and password click on login_button
    page.locator("#Email").fill(email_id)
    page.locator('#Password').fill(password)
    page.locator('.login-button').click()
    page.wait_for_timeout(200)

    if validity=='valid':
        logout_button=page.locator(".ico-logout")
        expect(logout_button).to_be_visible()

        expect(page).to_have_url("https://demowebshop.tricentis.com/")
    else:
        login_error=page.locator(".validation-summary-errors")
        expect(login_error).to_contain_text('Login was unsuccessful',ignore_case=True,timeout=2000)

        expect(page).to_have_url("https://demowebshop.tricentis.com/login")

    page.close()
    context.close()
    browser.close()
