from playwright.sync_api import expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self._username = self.page.locator("#username")
        self._password = self.page.locator("#password")
        self._select_dropDown = self.page.locator("select.form-control")
        self._user_checkbox= self.page.locator('input[value="user"]')
        self._okay_btn = page.get_by_role("button", name="Okay")
        self._cancel_btn = page.get_by_role("button", name="Cancel")
        self._terms_checkbox= self.page.locator("#terms")
        self._submit_button = self.page.locator("#signInBtn")
        self._text = self.page.locator("span.text-white.termsText")

    def enter_username(self,value):
        self._username.fill(value)

    def enter_password(self,value):
        self._password.fill(value)

    def select_dropdown(self,value):
        self._select_dropDown.select_option(value)

    def click_user_checkbox(self):
        self._user_checkbox.check()

    def click_cancel_btn(self):
        self._cancel_btn.click()

    def click_okay_btn(self):
        expect(self._okay_btn).to_be_visible()
        self._okay_btn.click()

    def check_terms_checkbox(self):
        self._terms_checkbox.click()

    def validate_text_message(self,value):
        expect(self._text).to_have_text(value)

    def click_submit_btn(self):
        self._submit_button.click()





