from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class ExternalPage:
    def __init__(self, driver):
        self.driver = driver

    #앱을 나갑니다. 보고 있는 웹사이트에서 외부 앱을 열려고 합니다. 계속하시겠어요? > 계속하기 클릭
    def click_continue(self):
        continue_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
        ))
        continue_button.click()
    
    #Playstore 클릭
    def click_playstore(self):
        playstore_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="PlayStore"]')
        ))
        playstore_button.click()
    
    #ablog 앱 설치여부 확인
    def is_app_installed(self):
        try: #앱이 설치된 상태
            app_installed = self.driver.find_element(
                By.XPATH, '//android.webkit.WebView[@text="Not Found"]'
            )
            app_installed.click()
        except NoSuchElementException: #앱이 설치되지 않은 상태
            print("app is not installed")