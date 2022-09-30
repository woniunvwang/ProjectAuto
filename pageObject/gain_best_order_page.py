# encoding = 'utf-8'
import random
import string
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class GainBestOrderPage(BasePage):
    confirm_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/confirm")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/agree")
    cancel_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    # 合约组 "自动化测试合约"的path
    contract_group_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自动化测试合约")')
    gain_best_order_path = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Gain best单']/android.widget.TextView")
    page_title = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "1]/android.view.ViewGroup/android.widget.TextView")
    contract_name = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_name_or_code')
    K_line = (AppiumBy.ID, 'com.atp.newdemo2:id/k_line_thumbnail')
    Chg_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[4]/android.widget.TextView[1]")
    bid_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[1]")
    bid_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[2]")
    offer_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[1]")
    offer_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[2]")
    trade_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/account")
    trade_account_text_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/recycler_view_account']/android.widget.LinearLayout[2]/android.widget.TextView")
    change_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/action_change")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "转到上一层级")
    sell_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_sell")
    buy_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_buy")
    lots_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/lots']/android.view.ViewGroup/android.widget.EditText")
    price_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price']/android.view.ViewGroup/android.widget.EditText")
    gap_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/gap_price']/android.view.ViewGroup/android.widget.EditText")
    step_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/step_price']/android.view.ViewGroup/android.widget.EditText")
    offset_flag_change_button = (AppiumBy.ID, "com.atp.newdemo2:id/offset_flag")
    offset_flag_auto_xpath = (AppiumBy.XPATH, "//*[@text='自动' or @text='Auto']/..")
    offset_flag_open_xpath = (AppiumBy.XPATH, "//*[@text='开仓' or @text='Open']/..")
    offset_flag_C_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-平今-开仓' or @text='C-CT-O']/..")
    offset_flag_CT_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-平仓-开仓' or @text='CT-C-O']/..")
    offset_flag_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-开仓' or @text='C-O']/..")
    offset_flag_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-开仓' or @text='CT-O']/..")
    offset_flag_CY_O_xpath = (AppiumBy.XPATH, "//*[@text='平昨-开仓' or @text='CY-O']/..")
    hedge_flag_change_button = (AppiumBy.ID, "com.atp.newdemo2:id/hedge_flag")
    hedge_flag_speculation_xpath = (AppiumBy.XPATH, "//*[@text='投机' or @text='Speculation']/..")
    hedge_flag_arbitrage_xpath = (AppiumBy.XPATH, "//*[@text='套利' or @text='Arbitrage']/..")
    hedge_flag_hedge_xpath = (AppiumBy.XPATH, "//*[@text='套保' or @text='Hedge']/..")
    order_details_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    order_details_side = (AppiumBy.XPATH, "//*[@text='方向' or @text='Side']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_contract = (AppiumBy.XPATH, "//*[@text='合约' or @text='Contract']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_account = (AppiumBy.XPATH, "//*[@text='交易账户' or @text='Trade Account']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_lots = (AppiumBy.XPATH, "//*[@text='手数' or @text='Lots']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price = (AppiumBy.XPATH, "//*[@text='价格' or @text='Price']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_gap = (AppiumBy.XPATH, "//*[@text='Gap']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_step = (AppiumBy.XPATH, "//*[@text='Step']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_offset_flag = (AppiumBy.XPATH, "//*[@text='开平标志' or @text='Offset Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_hedge_flag = (AppiumBy.XPATH, "//*[@text='投保标志' or @text='Hedge Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_memo = (AppiumBy.XPATH, "//*[@text='备注' or @text='Memo']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    alert_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    alert_contract_code = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_code')
    alert_order_id = (AppiumBy.ID, 'com.atp.newdemo2:id/order_id')
    alert_message_ID = (AppiumBy.ID, "com.atp.newdemo2:id/message")
    button_close = (AppiumBy.ID, 'com.atp.newdemo2:id/close_button')
    last_price_and_lots = (AppiumBy.ID, "com.atp.newdemo2:id/lots_at_price")
    contract_management_ID = (AppiumBy.ID, "com.atp.newdemo2:id/manage_contract")
    # 自动化测试合约的合约管理中第一个合约的位置 TCU1907-SH （主测试合约，买卖盘有涨跌幅没有有数据）
    first_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[1]/com.atp.newdemo2:id/resort_button")
    # 自动化测试合约的合约管理中第二个合约的位置 BRN-2210-ICE（STL和STP类型下单测试合约，买卖盘及涨跌幅都有数据）
    second_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[2]/com.atp.newdemo2:id/resort_button")
    # 自动化测试合约的合约管理中第三个合约的位置 TCU1906-SH（没有数据时手数价格的填充时的测试合约，买卖盘及涨跌幅没有数据）
    third_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[3]/com.atp.newdemo2:id/resort_button")
    illegal_lots_xpath = (AppiumBy.XPATH, "//*[@text='非法手数'")
    main_test_contract_drag_path = ("//*[@text='GC2212-CME']/../android.widget.ImageView")
    # 权限测试合约，买卖盘有数据涨跌幅无数据
    permission_contract_drag_path = ("//*[@text='TCU1907-SH']/../android.widget.ImageView")
    # 无数据测试合约，买卖盘涨跌幅均无数据
    no_data_contract_drag_path = ("//*[@text='T2209-CF']/../android.widget.ImageView")
    edit_memo_ID = (AppiumBy.ID, "com.atp.newdemo2:id/edit_memo")
    error_hint_ID = (AppiumBy.ID, "com.atp.newdemo2:id/memo_error_hint")

    def slide_action(self, x1, y1, x2, y2):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x1, y1)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(x2, y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        time.sleep(1)
        self.slide_action(960, 280, 700, 280)
        self.click_action(self.contract_group_text)

    def alert_order_details_message(self):
        result = self.get_visible_element(self.alert_message_ID).text
        return result

    def alert_illegal_lots_title(self):
        return self.get_visible_element(self.illegal_lots_xpath).text

    def order_details_side_value(self):
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        return order_details_side_value

    def order_details_contract_value(self):
        order_details_contract_value = self.get_visible_element(self.order_details_contract).text
        return order_details_contract_value

    def order_details_account_value(self):
        order_details_account_value = self.get_visible_element(self.order_details_account).text
        return order_details_account_value

    def order_details_lots_value(self):
        order_details_lots_value = self.get_visible_element(self.order_details_lots).text
        return order_details_lots_value

    def order_details_price_value(self):
        order_details_price_value = self.get_visible_element(self.order_details_price).text
        return order_details_price_value

    def order_details_gap_value(self):
        order_details_gap_value = self.get_visible_element(self.order_details_gap).text
        return order_details_gap_value

    def order_details_step_value(self):
        order_details_step_value = self.get_visible_element(self.order_details_step).text
        return order_details_step_value

    def order_details_offset_flag_value(self):
        order_details_offset_flag_value = self.get_visible_element(self.order_details_offset_flag).text
        return order_details_offset_flag_value

    def order_details_hedge_flag_value(self):
        order_details_hedge_flag_value = self.get_visible_element(self.order_details_hedge_flag).text
        return order_details_hedge_flag_value

    def order_details_memo_value(self):
        order_details_memo_value = self.get_visible_element(self.order_details_memo).text
        return order_details_memo_value

    def press_confirm_button(self):
        self.click_action(self.confirm_button_id)

    def allow_button(self):
        allow_button = self.get_visible_element(self.allow_button_id)
        allow_button.click()

    def agree_button(self):
        allow_button = self.get_visible_element(self.agree_button_id)
        allow_button.click()

    def no_data_contract_to_top(self):
        self.click_action(self.contract_management_ID)
        time.sleep(1)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=self.no_data_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -220).pause(5).perform()
        self.click_action(self.back_button)

    def main_contract_to_top(self):
        self.click_action(self.contract_management_ID)
        time.sleep(1)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=self.main_test_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -220).pause(5).perform()
        self.click_action(self.back_button)

    def permission_contract_to_top(self):
        self.click_action(self.contract_management_ID)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=self.permission_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -350).pause(5).perform()
        self.click_action(self.back_button)

    def permission_contract_to_bottom(self):
        self.click_action(self.contract_management_ID)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=self.permission_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, 350).pause(5).perform()
        self.click_action(self.back_button)

    # def press_bid(self):
    #     actions = ActionChains(self.driver)
    #     actions.click_and_hold(self.get_visible_element(self.bid_lots_path))
    #     bid_lots = self.get_visible_element(self.bid_lots_path).text
    #     bid_price = self.get_visible_element(self.bid_price_path).text
    #     actions.release()
    #     actions.perform()
    #     return bid_lots, bid_price
    #
    # def press_offer(self):
    #     actions = ActionChains(self.driver)
    #     actions.click_and_hold(self.get_visible_element(self.offer_lots_path))
    #     offer_lots = self.get_visible_element(self.offer_lots_path).text
    #     offer_price = self.get_visible_element(self.offer_price_path).text
    #     actions.release()
    #     actions.perform()
    #     return offer_lots, offer_price

    def press_bid(self):
        self.click_action(self.bid_price_path)
        self.click_action(self.gain_best_order_path)

    def press_offer(self):
        self.click_action(self.offer_price_path)
        self.click_action(self.gain_best_order_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(self.trade_account_ID)
        trade_account_value = self.get_visible_element(self.trade_account_text_path).text
        self.click_action(self.trade_account_text_path)
        self.click_action(self.change_account_ID)
        changed_trade_account_value = self.get_visible_element(self.trade_account_ID).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(self.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_offer_and_order(self):
        self.press_offer()
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def change_buy_side(self):
        self.press_offer()
        self.click_action(self.sell_side_id)
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(self.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if bid_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return bid_lots_value, lots_value, order_details_lots_value

    def press_bid_and_check_price(self):
        bid_price_value = self.get_visible_element(self.bid_price_path).text
        self.press_bid()
        price_value = self.get_visible_element(self.price_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if bid_price_value == "-":
            return price_value, order_details_price_value
        else:
            return bid_price_value, price_value, order_details_price_value

    def press_offer_and_check_lots(self):
        offer_lots_value = self.get_visible_element(self.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if offer_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return offer_lots_value, lots_value, order_details_lots_value

    def press_offer_and_check_price(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        price_value = self.get_visible_element(self.price_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if offer_price_value == "-":
            return price_value, order_details_price_value
        else:
            return offer_price_value, price_value, order_details_price_value

    def slide_and_chg(self):
        self.slide_action(967, 978, 678, 978)

    def slide_and_press_chg(self):
        self.slide_and_chg()
        self.click_action(self.Chg_path)
        self.click_action(self.gain_best_order_path)
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_price(self):
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_price = last_price_and_lots.split('@')[1]
        self.slide_and_chg()
        chg_value = self.get_visible_element(self.Chg_path).text
        self.click_action(self.Chg_path)
        self.click_action(self.gain_best_order_path)
        price_value = self.get_visible_element(self.price_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if chg_value == "-":
            return price_value, order_details_price_value
        else:
            return float(last_price), float(price_value), float(order_details_price_value)

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(self.Chg_path).text
        self.click_action(self.Chg_path)
        self.click_action(self.gain_best_order_path)
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if Chg_value == "-":
            return lots_value, order_details_lots_value
        else:
            return float(last_lots), float(lots_value), order_details_lots_value

    def drag_first_contract_to_second_location(self):
        self.click_action(self.contract_management_ID)
        time.sleep(1)
        x = self.driver.find_element(AppiumBy.XPATH, self.third_contract_drag_path)
        y = self.driver.find_element(AppiumBy.XPATH, self.first_contract_drag_path)
        ActionChains(self.driver).drag_and_drop(y, x).pause(5).perform()
        self.click_action(self.back_button)

    def drag_third_contract_to_second_location(self):
        self.click_action(self.contract_management_ID)
        x = self.driver.find_element(AppiumBy.XPATH, self.third_contract_drag_path)
        y = self.driver.find_element(AppiumBy.XPATH, self.first_contract_drag_path)
        ActionChains(self.driver).drag_and_drop(x, y).pause(5).perform()
        self.click_action(self.back_button)

    def clear_lots_and_order(self):
        self.press_bid()
        self.clear_action(self.lots_xpath)
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def clear_price_and_order(self):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def not_input_gap_and_order(self):
        self.press_offer()
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_gap_and_order(self, gap_value):
        self.press_offer()
        self.input_action(self.gap_xpath, gap_value)
        self.input_action(self.step_xpath, "1")
        self.press_confirm_button()

    def input_legal_gap_and_order(self, gap_value):
        self.press_offer()
        self.input_action(self.gap_xpath, gap_value)
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_gap_value = self.order_details_gap_value()
        self.press_confirm_button()
        return order_details_gap_value

    def not_input_step_and_order(self):
        self.press_offer()
        self.input_action(self.gap_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_step_and_order(self, step_value):
        self.press_offer()
        self.input_action(self.step_xpath, step_value)
        self.input_action(self.gap_xpath, "1")
        self.press_confirm_button()

    def input_legal_step_and_order(self, step_value):
        self.press_offer()
        self.input_action(self.step_xpath, step_value)
        self.input_action(self.gap_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_step_value = self.order_details_step_value()
        self.press_confirm_button()
        return order_details_step_value

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_price_and_order(self, price):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_lots_and_price_and_order(self, lots, price):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_lots_value, order_details_price_value

    def alert_title_send_order_successfully(self):
        alert_title = self.get_visible_element(self.alert_title).text
        self.click_action(self.button_close)
        return alert_title

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_default_value, order_details_offset_flag_value

    def offset_flag_open_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_open_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_CT_O_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_C_CT_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_C_O_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_CT_C_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_O_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_C_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_O_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_CT_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CY_O_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_CY_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(self.hedge_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_default_value, order_details_hedge_flag_value

    def hedge_flag_arbitrage_and_order(self):
        self.press_offer()
        self.click_action(self.hedge_flag_change_button)
        self.click_action(self.hedge_flag_arbitrage_xpath)
        self.press_confirm_button()
        hedge_flag_value = self.get_visible_element(self.hedge_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def hedge_flag_hedge_and_order(self):
        self.press_offer()
        self.click_action(self.hedge_flag_change_button)
        self.click_action(self.hedge_flag_hedge_xpath)
        self.press_confirm_button()
        hedge_flag_value = self.get_visible_element(self.hedge_flag_change_button).text
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def edit_memo_and_order(self):
        self.press_offer()
        self.input_action(self.gap_xpath, "1")
        self.input_action(self.step_xpath, "1")
        self.click_action(self.edit_memo_ID)
        # 生成随机数的方法1
        # l1 = []
        # i = 0
        # while i < 256:
        #     i += 1
        #     input_value = random.choice(string.ascii_letters + string.digits)
        #     l1.append(input_value)
        #     if len(self.edit_memo_ID) == 256:
        #         break
        # 生成随机数的方法2
        # input_value = ''.join(random.choices(string.ascii_letters + string.digits, k=256))
        # 生成随机数的方法3
        input_value = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(256)])
        self.input_action(self.edit_memo_ID, input_value)
        self.slide_action(460, 1750, 460, 1400)
        hint = self.get_visible_element(self.error_hint_ID).text
        memo_value = self.get_visible_element(self.edit_memo_ID).text
        self.press_confirm_button()
        order_details_memo_value = self.order_details_memo_value()
        self.press_confirm_button()
        return hint, memo_value, order_details_memo_value


if __name__ == '__main__':
    driver = android_driver()
