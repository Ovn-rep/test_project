from .base_page import BasePage
from locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = (
            self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_LOCATOR))
        add_button.click()

    def get_text_from_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        res = int(alert_text[2:5])
        return res

    def add_text_to_alert(self):
        x = self.get_text_from_alert()
        self.browser.send_keys(self.solve_quiz_and_get_code(x))



