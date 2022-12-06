import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
from common.baseDriver import android_driver
from pageObject.login_page import LoginPage


class TestCaseLogin:

    def setup_method(self) -> None:
        # Step 2锛� 瀹氫箟鐣岄潰
        self.driver = android_driver()
        self.loginPage = LoginPage(self.driver)

    def teardown_method(self) -> None:
        self.driver.quit()


    def test_01_login_page_input_wrong_username_wrong_password_should_fail(self):
        # Step 3: 鍔ㄤ綔

        self.loginPage.input_username("wangx")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()

        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text
        #

        assert(alert_title, "鐧诲綍澶辫触")
        assert(alert_content, "鐢ㄦ埛鍚嶄笉瀛樺湪!")

    def test_02_login_page_input_right_username_right_password_should_success(self):
        # Step 3: 鍔ㄤ綔
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("1")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(3)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()

        # Step 4: 鎵惧埌鏂█鐨勫彉閲� 鍜� 甯搁噺

        alert_title = self.loginPage.get_alert_title_ID().text
        # Step 5锛� 鏂█
        assert(alert_title, "鍏嶈矗澹版槑")

    def test_03_login_page_input_wrong_username_wrong_password_should_fail(self):
        # Step 3: 鍔ㄤ綔

        self.loginPage.input_username("wangx")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()

        # Step 4: 鎵惧埌鏂█鐨勫彉閲� 鍜� 甯搁噺
        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text

        # Step 5锛� 鏂█
        assert(alert_title, "鐧诲綍澶辫触")
        assert(alert_content, "鐢ㄦ埛鍚嶄笉瀛樺湪!")

    def test_04_login_page_input_null_username_wrong_password_should_fail(self):
        self.loginPage.input_username("")
        self.loginPage.input_password("0")
        login_button = self.loginPage.get_login_button()
        assert(False, login_button.is_enabled())

    def test_05_login_page_input_right_username_wrong_password_should_fail(self):
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(3)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()
        self.loginPage.press_login_button()

        alert_title = self.loginPage.get_alert_title_UI_element().text
        assert_content = self.loginPage.get_alert_content_UI_element().text
        assert(alert_title, "鐧诲綍澶辫触")
        assert(assert_content, "褰撳墠瀵嗙爜閿欒")

    def test_06_login_page_input_right_username_wrong_password_should_fail(self):
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(2)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID,
                                       value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()

        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text

        assert(alert_title, "鐧诲綍澶辫触")
        assert(alert_content, "褰撳墠瀵嗙爜閿欒")

        # assert "鐧诲綍澶辫触" == assert_title
        # assert "褰撳墠瀵嗙爜閿欒" == assert_content

    # self.LoginPage.login_action(kwargs.get('username_wrong'), kwargs.get('password_right'))
    # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
    # assert alert_title == '鐧诲綍澶辫触'
    # assert alert_content == '鐢ㄦ埛鍚嶄笉瀛樺湪!'
    # time.sleep(1)

    # @file_data('../data/data_login.yaml')
    # def test_02_password_wrong_should_login_fail(self, **kwargs):
    #     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_wrong'))
    #     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
    #     assert alert_title == '鐧诲綍澶辫触'
    #     assert alert_content == '褰撳墠瀵嗙爜閿欒'
    #     time.sleep(1)
    #
    # @file_data('../data/data_login.yaml')
    # def test_03_username_and_password_right_should_login_successful(self, **kwargs):
    #     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_right'))
    #     group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
    #     assert group_name == '閲戝睘'
    #     time.sleep(1)


# 浠ヤ笅涓轰俊鎭噰闆嗙櫥褰曠敤渚�
# @file_data('../data/data_login.yaml')
# def test_01_login_username_wrong(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_wrong'), kwargs.get('password_right'))
#     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#     assert alert_title == '鐧诲綍澶辫触'
#     assert alert_content == '鐢ㄦ埛鍚嶄笉瀛樺湪!'
#     time.sleep(2)
#
#
# @file_data('../data/data_login.yaml')
# def test_02_login_password_wrong(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_wrong'))
#     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#     try:
#         # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '鐧诲綍澶辫触'
#         assert alert_content == '璇峰嬀閫夊嬀閫夋鏉ュ悓鎰忔悳闆嗗繀闇�鐨勪俊鎭�'
#         self.LoginPage.agree_information_collection()
#         alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '鐧诲綍澶辫触'
#         assert alert_content == '褰撳墠瀵嗙爜閿欒'
#     except:
#         # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         print(alert_content)
#         assert alert_title == '鐧诲綍澶辫触'
#         assert alert_content == '褰撳墠瀵嗙爜閿欒'
#     time.sleep(2)
#
#
# @file_data('../data/data_login.yaml')
# def test_03_login_successful(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_right'))
#     try:
#         alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '鐧诲綍澶辫触'
#         assert alert_content == '璇峰嬀閫夊嬀閫夋鏉ュ悓鎰忔悳闆嗗繀闇�鐨勪俊鎭�'
#         self.LoginPage.agree_information_collection()
#         group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
#         assert group_name == '閲戝睘'
#     except:
#         group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
#         assert group_name == '閲戝睘'
#     time.sleep(2)

if __name__ == '__main__':
    pytest.main()
