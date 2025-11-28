from selenium.webdriver.common.by import By
from pages.product_page import ProductPage


def  test_guest_can_add_product_to_basket(browser):
    product_page_url = \
        'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, product_page_url)
    product_page.open()
    product_page.add_to_basket()
    product_page.add_text_to_alert()


