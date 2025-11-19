from email.policy import default

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--name-browser', action = 'store',
                     default = None, help = "Choose browser")


@pytest.fixture(scope = 'function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    driver = None
    if browser_name == 'chrome':
        print("test open in Chrome")
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("test open in FireFox")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("browser_name != chrome or firefox")
    yield browser
    driver.quit()




