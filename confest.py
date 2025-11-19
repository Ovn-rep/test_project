from email.policy import default
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--name-browser', action = 'store',
                     default = None, help = "Choose browser")

    parser.addoption('--language', default = 'None',
                     action = 'strore', help = "choose language")


@pytest.fixture(scope = 'function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    options_chrome = Options()
    options_chrome.add_experimental_option('pref', {'intl.accept_languages': user_language})

    options_firefox = Options()
    options_firefox.set_preference("intl.accept_languages", user_language)

    driver = None
    if browser_name == 'chrome':
        print("test open in Chrome")
        driver = webdriver.Chrome(options = options_chrome)
    elif browser_name == 'firefox':
        print("test open in FireFox")
        driver = webdriver.Firefox(options = options_firefox)
    else:
        raise pytest.UsageError("browser_name != chrome or firefox")
    yield browser
    driver.quit()





