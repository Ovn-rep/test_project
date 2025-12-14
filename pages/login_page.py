from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'invalid url'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_1 = self.browser.find_element(*LoginPageLocators.PASS_INPUT)
        password_1.send_keys(password)
        password_2 = self.browser.find_element(*LoginPageLocators.PASS_REPEAT_INPUT)
        password_2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
