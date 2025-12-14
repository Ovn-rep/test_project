from unittest import expectedFailure

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

class BasePage:

    def __init__(self, browser, url, timeout = 10):
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









