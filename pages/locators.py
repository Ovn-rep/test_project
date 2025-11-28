from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK_LOCATOR = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    AUTH_FORM_LOCATOR = (By.ID, 'login_form')
    REG_FORM_LOCATOR = (By.ID, 'register_form')

class ProductPageLocators:
    ADD_TO_BASKET_LOCATOR = (By.CLASS_NAME, 'btn-add-to-basket')
