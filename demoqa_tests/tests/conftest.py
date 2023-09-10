import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from demoqa_tests.utils import attach


@pytest.fixture(autouse=True)
def url():
    browser.config.base_url = "https://demoqa.com"


@pytest.fixture(scope='function', autouse=True)
def window_size():
    browser.config.window_width = 1400
    browser.config.window_height = 1600


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
