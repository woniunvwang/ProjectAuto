# encoding = 'utf-8'
import random
import string

import button as button
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class NormalOrderPage(BasePage):
    confirm_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/confirm")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/agree")
    cancel_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    # 合约组 "自动化测试合约"的path
    contract_group_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自动化测试合约")')

    # 页面核心元素
    page_title = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "1]/android.view.ViewGroup/android.widget.TextView")  # 新单
    contract_name = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_name_or_code')
    K_line = (AppiumBy.ID, 'com.atp.newdemo2:id/k_line_thumbnail')  # enabled=true
    # 合约组中第一个合约的买卖盘及涨跌幅path

    Chg_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[4]/android.widget.TextView[1]")

    bid_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[1]")
    bid_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[2]")
    offer_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[1]")
    offer_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[2]")

    trade_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/account")
    # 选择账户中的第二个账户
    trade_account_text_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/recycler_view_account']/android.widget.LinearLayout[2]/android.widget.TextView")
    change_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/action_change")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "转到上一层级")
    sell_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_sell")
    buy_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_buy")
    lots_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/lots']/android.view.ViewGroup/android.widget.EditText")
    price_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price']/android.view.ViewGroup/android.widget.EditText")
    change_type_button = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/normal_order_type']/android.widget.LinearLayout/android.widget.Button")
    type_Market_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market")')
    type_Market_Limit_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market Limit")')
    type_Lim_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LIM")')
    type_STP_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("STP")')
    type_STL_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("STL")')
    type_ICE_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ICE")')
    StPx_titile_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/stop_price']/android.view.ViewGroup/android.widget.TextView")
    input_StPx_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/stop_price']/android.view.ViewGroup/android.widget.EditText")
    chunk_size_title = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/max_iceberg_chunk_size']/android.view.ViewGroup/android.widget.TextView")
    chunk_size_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/max_iceberg_chunk_size']/android.view.ViewGroup/android.widget.EditText")
    TIF_change_button = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/time_option']/android.widget.LinearLayout/android.widget.Button")
    TIF_DAY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("DAY")')
    TIF_GTC = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("GTC")')
    TIF_GTD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("GTD")')
    TIF_FAK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FAK")')
    TIF_FOK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FOK")')
    date_pick_ID = (AppiumBy.ID, "com.atp.newdemo2:id/date_pick_text_view")
    fak_min_quantity = (AppiumBy.XPATH,"//*[@resource-id='com.atp.newdemo2:id/min_quantity']/android.view.ViewGroup/android.widget.EditText")
    offset_flag_change_button = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/offset_flag_type']/android.widget.LinearLayout/android.widget.Button")
    offset_flag_auto_xpath = (AppiumBy.XPATH, "//*[@text='自动' or @text='Auto']/..")
    offset_flag_open_xpath = (AppiumBy.XPATH, "//*[@text='开仓' or @text='Open']/..")
    offset_flag_close_xpath = (AppiumBy.XPATH, "//*[@text='平仓' or @text='Close']/..")
    offset_flag_closeYesterday_xpath = (AppiumBy.XPATH, "//*[@text='平昨' or @text='CloseYesterday']/..")
    offset_flag_closeToday_xpath = (AppiumBy.XPATH, "//*[@text='平今' or @text='CloseToday']/..")
    offset_flag_C_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-平今-开仓' or @text='C-CT-O']/..")
    offset_flag_CT_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-平仓-开仓' or @text='CT-C-O']/..")
    offset_flag_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-开仓' or @text='C-O']/..")
    offset_flag_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-开仓' or @text='CT-O']/..")
    offset_flag_CY_O_xpath = (AppiumBy.XPATH, "//*[@text='平昨-开仓' or @text='CY-O']/..")
    hedge_flag_change_button = (AppiumBy.ID, "com.atp.newdemo2:id/hedge_flag")
    hedge_flag_speculation_xpath = (AppiumBy.XPATH, "//*[@text='投机' or @text='Speculation']/..")
    hedge_flag_arbitrage_xpath = (AppiumBy.XPATH, "//*[@text='套利' or @text='Arbitrage']/..")
    hedge_flag_hedge_xpath = (AppiumBy.XPATH, "//*[@text='套保' or @text='Hedge']/..")

    order_details_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')  # 订单详情
    order_details_side = (AppiumBy.XPATH, "//*[@text='方向' or @text='Side']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_contract = (AppiumBy.XPATH, "//*[@text='合约' or @text='Contract']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_account = (AppiumBy.XPATH, "//*[@text='交易账户' or @text='Trade Account']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_lots = (AppiumBy.XPATH, "//*[@text='手数' or @text='Lots']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_chunk_size = (AppiumBy.XPATH, "//*[@text='暴露数量' or @text='Chunk Size']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price = (AppiumBy.XPATH, "//*[@text='价格' or @text='Price']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stpx = (AppiumBy.XPATH, "//*[@text='StPx']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stpx_title = (AppiumBy.XPATH, "//*[@text='StPx']")
    order_details_type = (AppiumBy.XPATH, "//*[@text='类型' or @text='Type']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_offset_flag = (AppiumBy.XPATH, "//*[@text='开平标志' or @text='Offset Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_hedge_flag = (AppiumBy.XPATH, "//*[@text='投保标志' or @text='Hedge Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_tif = (AppiumBy.XPATH, "//*[@text='TIF']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_min_quantity = (AppiumBy.XPATH, "//*[@text='最小数量' or @text='Min Quantity']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_t = (AppiumBy.XPATH, "//*[@text='T+1']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_memo = (AppiumBy.XPATH, "//*[@text='备注' or @text='Memo']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    alert_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    alert_contract_code = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_code')
    alert_order_id = (AppiumBy.ID, 'com.atp.newdemo2:id/order_id')
    alert_message_ID = (AppiumBy.ID, "com.atp.newdemo2:id/message")
    button_view_details = (AppiumBy.ID, 'com.atp.newdemo2: id/positive_button')
    button_close = (AppiumBy.ID, 'com.atp.newdemo2:id/close_button')
    last_price_and_lots = (AppiumBy.ID, "com.atp.newdemo2:id/lots_at_price")

    contract_management_ID = (AppiumBy.ID, "com.atp.newdemo2:id/manage_contract")
    # 自动化测试合约的合约管理中第一个合约的位置 TCU1907-SH （主测试合约，买卖盘有涨跌幅没有有数据）
    first_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[1]/com.atp.newdemo2:id/resort_button")
    # 自动化测试合约的合约管理中第二个合约的位置 BRN-2210-ICE（STL和STP类型下单测试合约，买卖盘及涨跌幅都有数据）
    second_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[2]/com.atp.newdemo2:id/resort_button")
    # 自动化测试合约的合约管理中第三个合约的位置 TCU1906-SH（没有数据时手数价格的填充时的测试合约，买卖盘及涨跌幅没有数据）
    third_contract_drag_path = ("//*[@resource-id='com.atp.newdemo2:id/recycler_view_edit_contract']/android.view.ViewGroup[3]/com.atp.newdemo2:id/resort_button")
    illegal_lots_title_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]")

    T_switch_ID = (AppiumBy.ID, "com.atp.newdemo2:id/one_plus_switch")
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
        return self.get_visible_element(self.illegal_lots_title_path).text

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

    def order_details_chunk_size_value(self):
        order_details_chunk_size_value = self.get_visible_element(self.order_details_chunk_size).text
        return order_details_chunk_size_value

    def order_details_price_value(self):
        order_details_price_value = self.get_visible_element(self.order_details_price).text
        return order_details_price_value

    def order_details_stpx_value(self):
        order_details_stpx_value = self.get_visible_element(self.order_details_stpx).text
        return order_details_stpx_value

    def order_details_type_value(self):
        order_details_type_value = self.get_visible_element(self.order_details_type).text
        return order_details_type_value

    def order_details_offset_flag_value(self):
        order_details_offset_flag_value = self.get_visible_element(self.order_details_offset_flag).text
        return order_details_offset_flag_value

    def order_details_hedge_flag_value(self):
        order_details_hedge_flag_value = self.get_visible_element(self.order_details_hedge_flag).text
        return order_details_hedge_flag_value

    def order_details_TIF_value(self):
        order_details_TIF_value = self.get_visible_element(self.order_details_tif).text
        return order_details_TIF_value

    def order_details_T_value(self):
        order_details_T_value = self.get_visible_element(self.order_details_t).text
        return order_details_T_value

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

    def press_offer(self):
        self.click_action(self.offer_price_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(self.trade_account_ID)
        trade_account_value = self.get_visible_element(self.trade_account_text_path).text
        self.click_action(self.trade_account_text_path)
        self.click_action(self.change_account_ID)
        changed_trade_account_value = self.get_visible_element(self.trade_account_ID).text
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(self.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
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
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(self.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(self.lots_xpath).text
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
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_price(self):
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_price = last_price_and_lots.split('@')[1]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(self.Chg_path).text
        self.click_action(self.Chg_path)
        price_value = self.get_visible_element(self.price_xpath).text
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if Chg_value == "-":
            return price_value, order_details_price_value
        else:
            return float(last_price), float(price_value), float(order_details_price_value)

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(self.Chg_path).text
        self.click_action(self.Chg_path)
        lots_value = self.get_visible_element(self.lots_xpath).text
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

    def change_type_market(self):
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Market_text)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        return price_value, type_value

    # 类型为STP/Market/Market Limit时价格处显示为置灰的Market

    def Market_type_and_order(self):
        self.change_type_market()
        self.press_confirm_button()
        order_details_type_value = self.order_details_type_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_type_value,order_details_price_value

    def change_type_market_limit(self):
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Market_Limit_text)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        return price_value, type_value

    def market_Limit_type_and_order(self):
        self.change_type_market_limit()
        self.press_confirm_button()
        order_details_type_value = self.order_details_type_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_type_value, order_details_price_value

    def market_type_changed_lim_type(self):
        bid_price_value = self.get_visible_element(self.offer_price_path).text
        self.change_type_market()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Lim_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        return bid_price_value, price_value, type_value

    def market_Limit_type_changed_lim_type(self):
        bid_price_value = self.get_visible_element(self.offer_price_path).text
        self.change_type_market_limit()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Lim_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        return bid_price_value, price_value, type_value

    def change_type_stp(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_STP_path)
        self.press_confirm_button()
        input_StPx = self.get_visible_element(self.input_StPx_xpath).text
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        StPx_title = self.get_visible_element(self.order_details_stpx_title).text
        return offer_price_value, StPx_title, input_StPx, price_value, type_value

    def stp_clear_StPx_and_order(self):
        self.change_type_stp()
        self.clear_action(self.input_StPx_xpath)
        self.press_confirm_button()

    def stp_type_input_difference_value(self, difference):
        self.change_type_stp()
        self.clear_action(self.input_StPx_xpath)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(self.input_StPx_xpath, price_value)
        stpx_value = self.get_visible_element(self.input_StPx_xpath).text
        return stpx_value

    def stp_type_input_StPx_above_last_price_and_buy_order(self):
        stpx_value = self.stp_type_input_difference_value(+5)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return stpx_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def stp_type_input_StPx_below_last_price_and_buy_order(self):
        self.stp_type_input_difference_value(-5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_above_last_price_and_sell_order(self):
        self.stp_type_input_difference_value(+5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_below_last_price_and_sell_order(self):
        stpx_value = self.stp_type_input_difference_value(-5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return stpx_value, order_details_stpx_value,order_details_price_value, order_details_type_value

    def change_type_stl(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_STL_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        input_StPx = self.get_visible_element(self.input_StPx_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        StPx_title = self.get_visible_element(self.order_details_stpx_title).text
        return offer_price_value, StPx_title, input_StPx, price_value, type_value

    def stl_clear_StPx_and_order(self):
        self.change_type_stl()
        self.clear_action(self.input_StPx_xpath)
        self.press_confirm_button()

    def stl_type_input_difference_value(self, difference):
        self.change_type_stl()
        self.clear_action(self.input_StPx_xpath)
        self.clear_action(self.price_xpath)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(self.input_StPx_xpath, price_value)
        self.input_action(self.price_xpath, price_value)
        StPx_value = self.get_visible_element(self.input_StPx_xpath).text
        price_value = self.get_visible_element(self.price_xpath).text
        return StPx_value, price_value

    def stl_type_input_StPx_above_last_price_and_buy_order(self):
        value = self.stl_type_input_difference_value(+5)
        StPx_value = value[0]
        price_value = value[1]
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def stl_type_input_StPx_below_last_price_and_buy_order(self):
        self.stl_type_input_difference_value(-5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_above_last_price_and_sell_order(self):
        self.stl_type_input_difference_value(+5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_last_price_and_sell_order(self):
        value = self.stl_type_input_difference_value(-5)
        StPx_value = value[0]
        price_value = value[1]
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def stl_type_input_StPx_diff_and_price_diff(self, StPx_diff, price_diff):
        self.change_type_stl()
        self.clear_action(self.input_StPx_xpath)
        self.clear_action(self.price_xpath)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(price_diff)
        StPx_value = last_trade_price + int(StPx_diff)
        self.input_action(self.input_StPx_xpath, StPx_value)
        self.input_action(self.price_xpath, price_value)
        StPx_value = self.get_visible_element(self.input_StPx_xpath).text
        price_value = self.get_visible_element(self.price_xpath).text
        return StPx_value, price_value

    def stl_type_input_StPx_below_price_and_buy_order(self):
        value = self.stl_type_input_StPx_diff_and_price_diff(5, 10)
        StPx_value = value[0]
        price_value = value[1]
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def stl_type_input_StPx_above_price_and_buy_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(10, 5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_price_and_sell_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(-10, -5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()

    def stl_type_input_StPx_above_price_and_sell_order(self):
        value = self.stl_type_input_StPx_diff_and_price_diff(-5, -10)
        StPx_value = value[0]
        price_value = value[1]
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def change_type_ice(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_ICE_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(self.price_xpath).text
        type_value = self.get_visible_element(self.change_type_button).text
        chunk_size_title = self.get_visible_element(self.chunk_size_title).text
        chunk_size_value = self.get_visible_element(self.chunk_size_xpath).text
        return chunk_size_value, chunk_size_title, price_value, offer_price_value, type_value

    def ice_type_and_input_lots_and_chunk_size(self, lots, chunk_size_value):
        self.change_type_ice()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.chunk_size_xpath)
        self.input_action(self.chunk_size_xpath, chunk_size_value)
        lots_value = self.get_visible_element(self.lots_xpath).text
        chunk_size_value = self.get_visible_element(self.chunk_size_xpath).text
        return lots_value, chunk_size_value

    def ice_type_clear_chunk_size_and_order(self):
        self.change_type_ice()
        self.clear_action(self.chunk_size_xpath)
        self.press_confirm_button()

    def ice_type_input_chunk_size_legal_value_and_order(self):
        result = self.ice_type_and_input_lots_and_chunk_size(5, 2)
        lots_value = result[0]
        chunk_size_value = result[1]
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        order_details_chunk_size_value = self.order_details_chunk_size_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return lots_value, chunk_size_value, order_details_lots_value, order_details_chunk_size_value, order_details_type_value

    def clear_lots_and_order(self):
        self.press_bid()
        self.clear_action(self.lots_xpath)
        self.press_confirm_button()

    def clear_price_and_order(self):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.press_confirm_button()

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.press_confirm_button()

    def input_illegal_price_and_order(self, price):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.press_confirm_button()

    def input_lots_and_price_and_order(self, lots, price):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_lots_value, order_details_price_value

    def get_element_from_send_successfully_alert_and_close_alert(self):
        alert_title = self.get_visible_element(self.alert_title).text
        alert_contract_code = self.get_visible_element(self.alert_contract_code).text
        alert_order_id = self.get_visible_element(self.alert_order_id).text
        self.click_action(self.button_close)
        return alert_title, alert_contract_code, alert_order_id

    def alert_title_send_order_successfully(self):
        alert_title = self.get_visible_element(self.alert_title).text
        self.click_action(self.button_close)
        return alert_title

    def change_tif_gtc(self):
        self.press_offer()
        self.click_action(self.TIF_change_button)
        self.click_action(self.TIF_GTC)
        self.press_confirm_button()

    def change_tif_gtd(self):
        self.press_offer()
        self.click_action(self.TIF_change_button)
        self.click_action(self.TIF_GTD)
        self.press_confirm_button()

    def change_tif_fak(self):
        self.press_offer()
        self.click_action(self.TIF_change_button)
        self.click_action(self.TIF_FAK)
        self.press_confirm_button()

    def change_tif_fok(self):
        self.press_offer()
        self.click_action(self.TIF_change_button)
        self.click_action(self.TIF_FOK)
        self.press_confirm_button()

    def tif_day_and_order(self):
        self.press_offer()
        self.press_confirm_button()

        self.press_confirm_button()

    def tif_gtc_and_order(self):
        self.change_tif_gtc()
        self.press_confirm_button()
        self.press_confirm_button()

    def tif_gtd_and_order(self):
        self.change_tif_gtd()
        self.press_confirm_button()
        self.press_confirm_button()

    def tif_fak_and_order(self):
        self.change_tif_fak()
        self.press_confirm_button()
        self.press_confirm_button()

    def tif_fok_and_order(self):
        self.change_tif_fok()
        self.press_confirm_button()
        self.press_confirm_button()

    def tif_fak_and_clear_min_quantity_and_order(self):
        self.change_tif_fak()
        self.clear_action(self.fak_min_quantity)
        self.press_confirm_button()

    def tif_fak_and_input_illegal_min_quantity(self, fak_min):
        self.change_tif_fak()
        self.clear_action(self.fak_min_quantity)
        self.input_action(self.fak_min_quantity, fak_min)
        return self.get_visible_element(self.fak_min_quantity).text

    def tif_fak_and_input_min_quantity_and_lots(self, fak_min, lots):
        self.change_tif_fak()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.fak_min_quantity)
        self.input_action(self.fak_min_quantity, fak_min)
        return self.get_visible_element(self.fak_min_quantity).text

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(self.offset_flag_change_button).text
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
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_close_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_close_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_closeYesterday_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_closeYesterday_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_closeToday_and_order(self):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(self.offset_flag_closeToday_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
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
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(self.hedge_flag_change_button).text
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
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def change_T_switch_and_order(self):
        self.press_offer()
        self.click_action(self.T_switch_ID)
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        self.press_confirm_button()

    def edit_memo_and_order(self):
        self.press_offer()
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
