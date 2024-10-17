import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
#capability 설정
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "ce05171524798d0c03"
    options.app_package = "com.instagram.android"
    options.app_activity = "com.instagram.mainactivity.InstagramMainActivity"
    options.platform_version = "9"
    options.automation_name = "UiAutomator2"
    options.full_reset = "false"
    options.ignore_hidden_api_policy_error = "true"

    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()
