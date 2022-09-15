from appium.webdriver.common.appiumby import AppiumBy
from common.baseDriver import android_driver
from common.basePage import BasePage


class LoginPage(BasePage):
    usernameID = (AppiumBy.ID, 'com.atp.newdemo2:id/username')
    passwordID = (AppiumBy.ID, 'com.atp.newdemo2:id/password')
    login_button_ID = (AppiumBy.ID, 'com.atp.newdemo2:id/sign_in_button')
    error_alert_title_ID = (AppiumBy.ID, "com.atp.newdemo2:id/title")
    error_alert_content_ID = (AppiumBy.ID, "com.atp.newdemo2:id/content_view")
    alert_title_ID = (AppiumBy.ID, "com.atp.newdemo2:id/disclaimer_title")
    cancel_button = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    checkBox_allow = (AppiumBy.ID, "com.atp.newdemo2:id/checkBox_allow_collect_system_information")
    permission_allow = (AppiumBy.ID, "com.android.permissioncontroller:id""/permission_allow_foreground_only_button")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button = (AppiumBy.ID, "com.atp.newdemo2:id/agree")

    def __init__(self, driver):
        super().__init__(driver)

    def get_alert_title_UI_element(self):
        return self.get_visible_element(self.error_alert_title_ID)

    def get_login_button(self):
        return self.get_visible_element(self.login_button_ID)

    def get_alert_content_UI_element(self):
        return self.get_visible_element(self.error_alert_content_ID)

    def get_alert_title_ID(self):
        return self.get_visible_element(self.alert_title_ID)

    def input_username(self, text):
        self.input_action(self.usernameID, text)

    def input_password(self, text):
        self.input_action(self.passwordID, text)

    def press_login_button(self):
        self.click_action(self.login_button_ID)

    def login_action(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.press_login_button()

    def press_change_password(self):
        self.click_action(self.cancel_button)
        self.click_action(self.checkBox_allow)
        self.press_login_button()
        self.click_action(self.permission_allow)
        self.click_action(self.allow_button_id)
        self.click_action(self.allow_button_id)

    def press_change_server(self):
        pass

    #
    def agree_disclaimers_and_get_group_name(self):
        self.click_action(self.cancel_button)
        self.click_action(self.checkBox_allow)
        self.press_login_button()
        self.click_action(self.permission_allow)
        self.click_action(self.allow_button_id)
        self.click_action(self.allow_button_id)
        self.press_login_button()
        self.click_action(self.agree_button)
        self.click_action(self.agree_button)


if __name__ == '__main__':
    android_driver()
