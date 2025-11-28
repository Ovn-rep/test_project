from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
import math

class BasePage:

    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self, x):
        return math.log10(x) * (abs(12 * math.sin(x)))

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True








