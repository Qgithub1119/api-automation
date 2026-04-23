from itertools import product

from playwright.sync_api import expect

from pages.shop_page import ShopPage
def test_shop_page_categories(page):
    shop_page= ShopPage(page)
    shop_page.navigate_shop_page()
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    categories = shop_page.categories()
    assert categories ==  ['Category 1', 'Category 2', 'Category 3']
    product_names, _ = shop_page.products()
    print(product_names)
    page.wait_for_timeout(5000)
    check_out_value= shop_page.validate_check_out_button()
    print(check_out_value)
    assert "Checkout ( 2 )" in check_out_value
    shop_page.click_check_out_button()
    page.wait_for_timeout(10000)
    phone_added = shop_page.products_added()
    print(phone_added)
    assert phone_added == product_names

def test_remove_products(page):
    shop_page = ShopPage(page)
    shop_page.navigate_shop_page()
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    categories = shop_page.categories()
    assert categories == ['Category 1', 'Category 2', 'Category 3']
    product_names, _ = shop_page.products()
    print(product_names)
    page.wait_for_timeout(5000)
    check_out_value = shop_page.validate_check_out_button()
    print(check_out_value)
    assert "Checkout ( 2 )" in check_out_value
    shop_page.click_check_out_button()
    page.wait_for_timeout(10000)
    phone_added = shop_page.products_added()
    print(phone_added)
    assert phone_added == product_names
    remove_products= shop_page.remove_products()
    print(remove_products)



