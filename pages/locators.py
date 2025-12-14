from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    AUTH_FORM_LOCATOR = (By.ID, 'login_form')
    REG_FORM_LOCATOR = (By.ID, 'register_form')

class ProductPageLocators:
    ADD_TO_BASKET_LOCATOR = (By.CLASS_NAME, 'btn-add-to-basket')
    MASSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-noicon.alert-success:first-child strong')
    MASSAGE_WITH_BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main h1 + p')
    MASSAGE_ABOUT_SUCCES_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages .alert:first-child')