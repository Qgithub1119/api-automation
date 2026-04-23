import re

from playwright.sync_api import expect
from pages.login import LoginPage
def test_login(page):
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")



def test_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.enter_username("wronguser")
    login.enter_password("Learning@830$3mK2")
    login.click_user_checkbox()
    login.click_okay_btn()
    login.select_dropdown("Teacher")
    login.check_terms_checkbox()
    login.validate_text_message(re.compile("I Agree to the.*"))
    login.click_submit_btn()

def test_invalid_password(page):
        login = LoginPage(page)
        login.navigate()
        login.enter_username("rahulshettyacademy")
        login.enter_password("Learning@830$3m")
        login.click_user_checkbox()
        login.click_okay_btn()
        login.select_dropdown("Teacher")
        login.check_terms_checkbox()
        login.validate_text_message(re.compile("I Agree to the.*"))
        login.click_submit_btn()