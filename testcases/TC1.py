import sys, os
import base64
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pytest
from appium import webdriver
from pages.profile_page import ProfilePage
from pages.edit_profile_page import EditProfilePage
from pages.external_page import ExternalPage
from appium.options.android import UiAutomator2Options
import time

url = 'https://go.ab180.co/8vpfwh'

@pytest.fixture(scope="module")
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
    options.no_reset = "true"

    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()

def test_instagram_login(driver):
    # 녹화 시작
    driver.start_recording_screen()

    profile_page = ProfilePage(driver)
    edit_profile_page = EditProfilePage(driver)
    external_page = ExternalPage(driver)

    try:
        profile_page.click_profile_icon()  # 프로필 이동 클릭
        time.sleep(3)
        profile_page.click_edit_profile()  # 프로필 편집 클릭

        time.sleep(2)
        edit_profile_page.click_add_link()  # 링크 추가 클릭
        edit_profile_page.external_add_link()  # 외부 링크 추가 클릭
        edit_profile_page.enter_url(url)  # URL 입력
        edit_profile_page.click_save()  # 저장 버튼 클릭
        edit_profile_page.go_back()  # 뒤로 가기 클릭
        edit_profile_page.go_back()  # 뒤로 가기 클릭
        
        profile_page.click_link()  # 링크 클릭
        time.sleep(2)
        profile_page.click_link_bottom(url)  # 프로필에 저장된 링크 클릭
        external_page.click_continue()  # 계속하기 클릭
        time.sleep(4)

    finally:
        #녹화 중지 및 비디오 파일 저장
        video_data = driver.stop_recording_screen()

        #Base64 디코딩
        video_data_bytes = base64.b64decode(video_data)
        with open("test_instagram_login.mp4", "wb") as video_file:
            video_file.write(video_data_bytes)