import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.go_to_login_page()
    login_url = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser, login_url)
    login_page.should_be_login_page()


