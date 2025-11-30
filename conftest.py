import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser-name', action = 'store',
                     default = "chrome", help = "Choose browser")

    parser.addoption('--language', default = 'ru',
                     action = 'store', help = "choose language")


@pytest.fixture(scope = 'function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    options_chrome = ChromeOptions()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    options_firefox = FirefoxOptions()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser = None
    if browser_name == 'chrome':
        print("test open in Chrome")
        browser = webdriver.Chrome(options = options_chrome)
        browser.implicitly_wait(10)
    elif browser_name == 'firefox':
        print("test open in FireFox")
        browser = webdriver.Firefox(options = options_firefox)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("browser_name != chrome or firefox")
    yield browser
    browser.delete_all_cookies()
    browser.quit()





