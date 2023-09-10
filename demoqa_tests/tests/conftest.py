import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def url():
    browser.config.base_url = "https://demoqa.com"


@pytest.fixture(autouse=True)
def window_size():
    browser.config.window_width = 900
    browser.config.window_height = 880
