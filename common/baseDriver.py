from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from common.baseLog import logger
import time

def android_driver():
    desired_caps = {
        # "platformName": "Android",
        # "platformVersion": "11",
        # "deviceName": "V2073A",
        # "appPackage": "com.atp.newdemo2",
        # "appActivity": "com.atp.activity.AppActivity",
        # "resetKeyboard": "true"

        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "MBJVB20707004299",
        "appium:appPackage": "com.atp.newdemo2",
        "appium:appActivity": "com.atp.activity.AppActivity",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        #语言为英文时启用28/29行代码
        # "locale": "US",
        # "language": "en"
        "locale": "CN",
        "language": "Zh"


    }
    try:
        caps = AppiumOptions().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=caps)
        time.sleep(2)
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(688, 1872)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(706, 900)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        el1 = driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.view.View[@content-desc=\"十二、其他\"]/android.widget.TextView[3]")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ID, value="com.atp.newdemo2:id/agree")
        el2.click()

        return driver
    except Exception as e:
        logger.error("APP启动失败，原因是：{}".format(e))


if __name__ == '__main__':
    android_driver()


