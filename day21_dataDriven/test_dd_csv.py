import csv

import pytest
from playwright.sync_api import Playwright, expect
import  json


login_data=[]
csvfile=open('testData/data.csv',newline='',encoding='utf-8')
reader=csv.DictReader(csvfile)

for row in reader:
    login_data.append((row['email'],row['password'],row['validity']))

@pytest.mark.parametrize("email,password,validity",login_data)
def test_dd_login_json(email,password,validity,playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(viewport={"width": 1920, "height": 1080})
    page=context.new_page()

    page.goto("https://demowebshop.tricentis.com/")

    page.goto("https://demowebshop.tricentis.com/")
    #click on login link
    page.locator(".ico-login").click()

    #enter credentials
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator(".login-button").click()

    #logout should visible
    if validity=='valid':
        logout_link=page.locator(".ico-logout")
        expect(logout_link).to_be_visible()

    elif validity=='invalid':
        error_mssg=page.locator(".validation-summary-errors span")
        expect(error_mssg).to_be_visible()

    page.close()
    context.close()
    browser.close()

