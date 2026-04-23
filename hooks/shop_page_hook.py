import re

import pytest

from pages.login import LoginPage

@pytest.fixture(autouse=True)
def login_to_shop(page):
    login = LoginPage(page)
    login.navigate()
    login.enter_username("rahulshettyacademy")
    login.enter_password("Learning@830$3mK2")
    login.click_user_checkbox()
    login.click_okay_btn()
    login.select_dropdown("Teacher")
    login.check_terms_checkbox()
    login.validate_text_message(re.compile("I Agree to the.*"))
    login.click_submit_btn()

