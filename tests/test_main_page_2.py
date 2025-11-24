import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()