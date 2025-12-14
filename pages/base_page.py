from unittest import expectedFailure

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

class BasePage:

    def __init__(self, browser, url, timeout = 7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_math(self, x):
        return str(math.log(abs((12 * math.sin(float(x))))))

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
            assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
                "Login link is not presented"

    def is_element_not_present(self, how, what, timeout = 5):
        wait = WebDriverWait(self.browser, timeout)
        try:
            wait.until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout = 5):
        wait = WebDriverWait(self.browser, timeout)
        try:
            wait.until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.AUTH_FORM_LOCATOR), \
            'not "login form" on page'

    def should_be_register_form(self):
        assert self.is_element_present(*BasePageLocators.REG_FORM_LOCATOR), \
            'not "reg form" on page'

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_ADD_BUTTON)
        basket_button.click()

    def should_be_product_in_basket(self):
        assert self.is_element_not_present(*BasePageLocators.PRODUCT_CARD_IN_BASKET), \
            "product in basket"

    def should_be_massage_no_product_in_basket(self):
        no_product = self.browser.find_element(*BasePageLocators.NO_PRODUCT_MESSAGE)
        text_in_message = no_product.text
        assert  "Ваша корзина пуста" in text_in_message, \
            "No massage in basket"








