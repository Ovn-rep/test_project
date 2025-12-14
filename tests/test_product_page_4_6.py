import pytest
from pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page_1 = ProductPage(browser, link)
    product_page_1.open()
    product_page_1.add_to_basket()

    product_page_1.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page_3 = ProductPage(browser, link)
    product_page_3.open()
    product_page_3.add_to_basket()

    product_page_3.should_be_disappeared_success_message()




