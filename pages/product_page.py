from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        add_add_to_basket_button = (
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LOCATOR))
        add_add_to_basket_button.click()

    def get_text_from_alert_and_accept(self):
        alert_1 = self.browser.switch_to.alert
        chislo = int(alert_1.text.split(" ")[2])
        res = str(self.solve_math(chislo))
        alert_1.send_keys(res)
        alert_1.accept()

    def get_text_answer_code(self):
        alert_2 = self.browser.switch_to.alert
        answer_code = alert_2.text.split(" ")[-1]
        print(f"answer: {answer_code}")
        alert_2.accept()

    def should_be_product_name_in_massage(self):
        message_with_product_name = (
            self.browser.find_element(*ProductPageLocators.MASSAGE_WITH_PRODUCT_NAME))
        text_message_with_product_name = message_with_product_name.text
        assert "The shellcoder's handbook" in text_message_with_product_name,\
            "No product_name in text"

    def should_be_correct_price_in_basket_massage(self):
        message_with_basket_price = (
            self.browser.find_element(*ProductPageLocators.MASSAGE_WITH_BASKET_PRICE))
        text_message_with_price = message_with_basket_price.text
        assert "9,99" in text_message_with_price,\
            "Incorrect price in message with basket price"