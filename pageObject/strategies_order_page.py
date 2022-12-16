# encoding = 'utf-8'
from common.All_path import all_path
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class StrategiesOrderPage(BasePage):

    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        self.click_action(all_path.strategies_tabbar_xpath)


if __name__ == '__main__':
    driver = android_driver()

