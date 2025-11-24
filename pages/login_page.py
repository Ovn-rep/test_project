from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'invalid url'


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_FORM_LOCATOR), 'not "login form" on page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM_LOCATOR), 'not "reg form" on page'
