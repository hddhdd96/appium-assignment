from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class EditProfilePage:
    def __init__(self, driver):
        self.driver = driver

    #링크 추가 버튼 클릭
    def click_add_link(self):
        try: #링크가 0개일 때
            add_link_button = self.driver.find_element(
                By.XPATH, '//android.widget.TextView[@resource-id="com.instagram.android:id/igds_textcell_title" and @text="링크 추가"]'
            )
            add_link_button.click()
        except NoSuchElementException: #링크가 1개 이상일 때
            existing_link_button = self.driver.find_element(
                By.XPATH, '//android.widget.TextView[@resource-id="com.instagram.android:id/igds_textcell_title" and @text="링크"]'
            )
            existing_link_button.click()

    #url 입력
    def enter_url(self, url):
        url_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '(//android.view.ViewGroup[@resource-id="com.instagram.android:id/prism_form_field_container"])[1]/android.widget.EditText')
        ))
        url_input.send_keys(url)

    #저장 버튼 클릭
    def click_save(self):
        save_button = self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="완료"]/android.widget.ImageView')
        save_button.click()

    #외부 링크 추가 버튼 클릭
    def external_add_link(self):
        link_button = self.driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.instagram.android:id/link_option_text" and @text="외부 링크 추가"]')
        link_button.click()
    
    #뒤로가기 클릭
    def go_back(self):
        back_button = self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="뒤로"]')
        back_button.click()