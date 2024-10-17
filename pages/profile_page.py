from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    #프로필 화면 아이콘 클릭
    def click_profile_icon(self):
        profile_info = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.ImageView[@resource-id="com.instagram.android:id/tab_avatar"]')
        ))
        profile_info.click()

    #프로필 편집 클릭
    def click_edit_profile(self):
        edit_profile = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.Button[@content-desc="프로필 편집"]')
        ))
        edit_profile.click()
    
    #프로필에 저장된 링크 클릭
    def click_link(self):
        link_button = self.driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.instagram.android:id/text_1"]')
        link_button.click()
        
    #프로필에 저장된 링크 2개 이상일 때 url 해당하는 링크 클릭
    def click_link_bottom(self, url):
        find_id_count = self.driver.find_elements(By.ID, 'com.instagram.android:id/link_option_text')
        if len(find_id_count) == 0: 
            pass
        else:
            if url == 'https://dev.blog.airbridge.io/sdk-qa/':
                click_link_button = self.driver.find_element(
                    By.XPATH, '//android.widget.TextView[@resource-id="com.instagram.android:id/link_option_text" and @text="dev.blog.airbridge.io/sdk-qa/"]')
                click_link_button.click()
            elif url == "https://go.ab180.co/8vpfwh":
                click_link_button = self.driver.find_element(
                    By.XPATH, '//android.widget.TextView[@resource-id="com.instagram.android:id/link_option_text" and @text="go.ab180.co/8vpfwh"]')
                click_link_button.click()