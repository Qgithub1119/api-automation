import re

import pytest
from playwright.sync_api import sync_playwright

from pages.login import LoginPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context= browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

pytest_plugins= ["hooks.shop_page_hook"]



from playwright.sync_api import sync_playwright
# import pytest
# from playwright.sync_api import sync_playwright
#
# BASE_URLS = {
#     "users": "https://jsonplaceholder.typicode.com",
#     "auth": "https://reqres.in/api"
# }
#
# @pytest.fixture(scope="session")
# def api():
#     return {
#     "users": "https://jsonplaceholder.typicode.com",
#     "auth": "https://reqres.in"
# }
#
# @pytest.fixture(scope="session")
# def api_request_context(api,request):
#     with sync_playwright() as p:
#         context= p.request.new_context(
#
#                 base_url= api[request.param],
#                  extra_http_headers={"Content-Type": "application/json","Accept": "application/json"}
#         )
#         yield context
#         context.dispose()



