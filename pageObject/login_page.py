from common.All_path import all_path
from common.baseDriver import android_driver
from common.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_alert_title_UI_element(self):
        return self.get_visible_element(all_path.error_alert_title_ID)

    def get_login_button(self):
        return self.get_visible_element(all_path.login_button_ID)

    def get_alert_content_UI_element(self):
        return self.get_visible_element(all_path.error_alert_content_ID)

    def get_alert_title_ID(self):
        return self.get_visible_element(all_path.alert_title_ID)

    def input_username(self, text):
        self.input_action(all_path.usernameID, text)

    def input_password(self, text):
        self.input_action(all_path.passwordID, text)

    def press_login_button(self):
        self.click_action(all_path.login_button_ID)

    def login_action(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.press_login_button()

    def press_change_password(self):
        self.click_action(all_path.cancel_button)
        self.click_action(all_path.checkBox_allow)
        self.press_login_button()
        self.click_action(all_path.permission_allow)
        self.click_action(all_path.allow_button_id)
        self.click_action(all_path.allow_button_id)

    def press_change_server(self):
        pass

    #
    def agree_disclaimers_and_get_group_name(self):
        self.click_action(all_path.cancel_button)
        self.click_action(all_path.checkBox_allow)
        self.press_login_button()
        self.click_action(all_path.permission_allow)
        self.click_action(all_path.allow_button_id)
        self.press_login_button()
        self.click_action(all_path.agree_button)
        self.click_action(all_path.agree_button)


if __name__ == '__main__':
    android_driver()
