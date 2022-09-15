from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.baseLog import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 获取可视元素
    def get_visible_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            logger.error("获取元素失败：{}".format(e))
            logger.error('获取元素失败:"%s%s"' % locator)

    # 判断toast是否存在

    def is_toast_exist(self, text, timeout=30, poll_frequency=0.5):
        try:
            toast_loc = (AppiumBy.XPATH, ".//*[contains(@text, '%s')]" % text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def get_element_clickable(self, locator):
        """通过元素id获取该元素的enabled属性值，为false置灰不可点击，为true亮起可点击"""
        clickable = self.get_visible_element(locator).is_enabled()
        return clickable

    # 输入
    def input_action(self, elementID, txt):
        self.get_visible_element(elementID).send_keys(txt)

    # 点击
    def click_action(self, elementID):
        self.get_visible_element(elementID).click()

    # 清除
    def clear_action(self, loc):
        self.get_visible_element(loc).clear()

    # 关闭
    def quit_action(self):
        self.driver.close_app()


