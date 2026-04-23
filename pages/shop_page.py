import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self._url= "https://rahulshettyacademy.com/angularpractice/shop"
        self._shop_link= self.page.get_by_role("link",name="Shop")
        self._categories= self.page.locator(".list-group-item")
        self._products= self.page.locator("div.card.h-100")
        self._add_button = self.page.get_by_role("button", name='Add')
        self._check_out_button = self.page.locator("a.nav-link.btn.btn-primary")
        self._phone_name = self.page.locator('//h4//a[@href="#"]')
        self._added_products= self.page.locator("h4.media-heading")
        self._remove_products = self.page.locator('button:has-text("Remove")')

    def navigate_shop_page(self):
        self.page.goto(self._url)

    def categories(self):
        return self._categories.all_text_contents()

    def categories_inner_text(self):
        categories = self._categories
        count= categories.count()
        texts=[]
        for i in range(count):
            text= categories.nth(i).inner_text()
            texts.append(text)
        return texts

    def products(self):
        count= self._products.count()
        phone=[]
        for i in  range(2,count):
            phone.append(self._phone_name.nth(i).inner_text())
            self._add_button.nth(i).click()
        text= self._check_out_button.inner_text()
        print("----------------",text)
        cart_count= int(re.search(r"\d+", text).group())
        return phone ,cart_count


    def validate_check_out_button(self):
        return self._check_out_button.inner_text()

    def click_check_out_button(self):
        self._check_out_button.click()

    def products_added(self):
        products = []
        for i in range(self._added_products.count()):
            text = self._added_products.nth(i).inner_text()
            products.append(text)
        return products

    def remove_products(self):
        self._remove_products.first.click()
        return self._added_products.all_text_contents()



            
