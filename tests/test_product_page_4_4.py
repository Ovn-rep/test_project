import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time


@pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                "?promo=offer6",  pytest.param("?promo=offer7", marks = pytest.mark.xfail),
                                  "?promo=offer8", "?promo=offer9"])
def  test_guest_can_add_product_to_basket(browser, link):
    product_page_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"

    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    product_page.get_product_name()
    product_page.get_product_name()
    product_page.add_to_basket()
    product_page.get_text_from_alert_and_accept()

    product_page.should_be_product_name_in_massage()
    product_page.should_be_correct_price_in_basket_massage()