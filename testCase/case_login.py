import unittest
import pytest
import allure
from appium import webdriver
import self as self
from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from ddt import ddt, file_data
import time

from selenium.webdriver.common.by import By

from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


@ddt
class CaseLogin(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        # Step 2： 定义界面
        cls.driver = android_driver()
        cls.loginPage = LoginPage(cls.driver)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    # ！！！若报错则检查登录名及密码，在此项目下data/data_login.yaml中将登录名及密码替换下即可
    # 根据登录名是否需要采集看穿式监管信息，若明确不需要采集则启用20-43行的用例，执行时间会短些，若需要采集或不确定是否需要采集则启用46-86行的用例
    # @file_data('../data/data_login.yaml')


    def test_01_login_page_input_wrong_username_wrong_password_should_fail(self):
        # Step 3: 动作

        self.loginPage.input_username("wangx")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()
        #
        # # Step 4: 找到断言的变量 和 常量
        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text
        #
        # # Step 5： 断言
        self.assertEqual(alert_title, "登录失败")
        self.assertEqual(alert_content, "用户名不存在!")

    def test_02_login_page_input_right_username_right_password_should_success(self):
        # Step 3: 动作
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("1")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(3)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                  value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()

        # Step 4: 找到断言的变量 和 常量

        alert_title = self.loginPage.get_alert_title_ID().text
        # Step 5： 断言
        self.assertEqual(alert_title, "免责声明")

    def test_03_login_page_input_wrong_username_wrong_password_should_fail(self):
        # Step 3: 动作

        self.loginPage.input_username("wangx")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()

        # Step 4: 找到断言的变量 和 常量
        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text

        # Step 5： 断言
        self.assertEqual(alert_title, "登录失败")
        self.assertEqual(alert_content, "用户名不存在!")

    def test_04_login_page_input_null_username_wrong_password_should_fail(self):
        self.loginPage.input_username("")
        self.loginPage.input_password("0")
        login_button = self.loginPage.get_login_button()
        self.assertEqual(False, login_button.is_enabled())

    def test_05_login_page_input_right_username_wrong_password_should_fail(self):
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(3)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                  value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()
        self.loginPage.press_login_button()

        alert_title = self.loginPage.get_alert_title_UI_element().text
        assert_content = self.loginPage.get_alert_content_UI_element().text
        self.assertEqual(alert_title, "登录失败")
        self.assertEqual(assert_content, "当前密码错误")

    def test_06_login_page_input_right_username_wrong_password_should_fail(self):
        self.loginPage.input_username("wangxin")
        self.loginPage.input_password("0")
        self.loginPage.press_login_button()
        time.sleep(1)
        el12 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/cancel")
        el12.click()
        time.sleep(1)
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/checkBox_allow_collect_system_information")
        el2.click()
        self.loginPage.press_login_button()
        time.sleep(2)
        el1 = self.driver.find_element(by=AppiumBy.ID,
                                  value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()

        alert_title = self.loginPage.get_alert_title_UI_element().text
        alert_content = self.loginPage.get_alert_content_UI_element().text

        self.assertEqual(alert_title, "登录失败")
        self.assertEqual(alert_content, "当前密码错误")

        # assert "登录失败" == assert_title
        # assert "当前密码错误" == assert_content

    # self.LoginPage.login_action(kwargs.get('username_wrong'), kwargs.get('password_right'))
    # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
    # assert alert_title == '登录失败'
    # assert alert_content == '用户名不存在!'
    # time.sleep(1)

    # @file_data('../data/data_login.yaml')
    # def test_02_password_wrong_should_login_fail(self, **kwargs):
    #     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_wrong'))
    #     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
    #     assert alert_title == '登录失败'
    #     assert alert_content == '当前密码错误'
    #     time.sleep(1)
    #
    # @file_data('../data/data_login.yaml')
    # def test_03_username_and_password_right_should_login_successful(self, **kwargs):
    #     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_right'))
    #     group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
    #     assert group_name == '金属'
    #     time.sleep(1)


# 以下为信息采集登录用例
# @file_data('../data/data_login.yaml')
# def test_01_login_username_wrong(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_wrong'), kwargs.get('password_right'))
#     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#     assert alert_title == '登录失败'
#     assert alert_content == '用户名不存在!'
#     time.sleep(2)
#
#
# @file_data('../data/data_login.yaml')
# def test_02_login_password_wrong(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_wrong'))
#     alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#     try:
#         # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '登录失败'
#         assert alert_content == '请勾选勾选框来同意搜集必需的信息'
#         self.LoginPage.agree_information_collection()
#         alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '登录失败'
#         assert alert_content == '当前密码错误'
#     except:
#         # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         print(alert_content)
#         assert alert_title == '登录失败'
#         assert alert_content == '当前密码错误'
#     time.sleep(2)
#
#
# @file_data('../data/data_login.yaml')
# def test_03_login_successful(self, **kwargs):
#     self.LoginPage.login_action(kwargs.get('username_right'), kwargs.get('password_right'))
#     try:
#         alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
#         assert alert_title == '登录失败'
#         assert alert_content == '请勾选勾选框来同意搜集必需的信息'
#         self.LoginPage.agree_information_collection()
#         group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
#         assert group_name == '金属'
#     except:
#         group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
#         assert group_name == '金属'
#     time.sleep(2)

if __name__ == '__main__':
    unittest.main()
