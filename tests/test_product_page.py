import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time


link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page_2 = ProductPage(browser, link)
    page_2.open()
    page_2.go_to_login_page()

    page_2.should_be_login_form()
    page_2.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page_3 = ProductPage(browser, link)
    page_3.open()
    page_3.go_to_basket()

    page_3.should_be_product_in_basket()
    page_3.should_be_massage_no_product_in_basket()

@pytest.mark.reg
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_page = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        setup_step = LoginPage(browser, reg_page)
        setup_step.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Mk1619!!!"
        setup_step.register_new_user(email, password)
        setup_step.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        product_page_url = \
            'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.get_product_name()
        product_page.get_product_name()
        product_page.add_to_basket()
        product_page.get_text_from_alert_and_accept()
        product_page.get_text_answer_code()

        product_page.should_be_product_name_in_massage()
        product_page.should_be_correct_price_in_basket_massage()

    def test_user_cant_see_success_message(self, browser):
        product_page_2 = ProductPage(browser, link)
        product_page_2.open()

        product_page_2.should_not_be_success_message()



