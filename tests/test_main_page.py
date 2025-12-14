import pytest

from conftest import browser
from pages.main_page import MainPage
from pages.login_page import LoginPage


url = 'http://selenium1py.pythonanywhere.com/'

@pytest.mark.login_guest
class TestLoginFromMainPage(browser):
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page_2 = MainPage(browser, url)
        main_page_2.open()
        main_page_2.go_to_basket()

        main_page_2.should_be_product_in_basket()
        main_page_2.should_be_massage_no_product_in_basket()





