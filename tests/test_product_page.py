from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time


def  test_guest_can_add_product_to_basket(browser):
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