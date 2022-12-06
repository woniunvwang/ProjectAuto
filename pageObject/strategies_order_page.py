# encoding = 'utf-8'
import random
import string
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class StrategiesOrderPage(BasePage):
    confirm_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/confirm")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/agree")
    cancel_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    strategies_tabbar_xpath = (AppiumBy.XPATH,  "//*[@resource-id='com.atp.newdemo2:id/bottom_navigation_view']/android.view.ViewGroup/android.widget.FrameLayout[2]")
    page_title = (AppiumBy.ID,  "com.atp.newdemo2:id/title")
    edit_strategy = (AppiumBy.ID,  "com.atp.newdemo2:id/edit_strategy")
    add_strategy = (AppiumBy.ID,  "com.atp.newdemo2:id/add_strategy")
    list_title_strategy_name = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[1]")
    list_title_ratio1 = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[2]")
    list_title_ratio2 = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[3]")
    toolbar_title = (AppiumBy.ID, "com.atp.newdemo2:id/toolbar_title")
    action_done = (AppiumBy.ID, "com.atp.newdemo2:id/action_done")
    strategy_name_input_edit_text = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/strategy_name']/android.view.ViewGroup/android.widget.EditText")
    strategy_name_clear_text_icon = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/strategy_name']/android.view.ViewGroup/android.widget.ImageView")
    formula_edit_text = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/formula_edit_text']/android.view.ViewGroup/android.widget.EditText")
    execution_times = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/execution_times']/android.view.ViewGroup/android.widget.EditText")
    execution_times_clear_text_icon = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/execution_times']/android.view.ViewGroup/android.widget.ImageView")
    single_trigger_times = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/single_trigger_times']/android.view.ViewGroup/android.widget.EditText")
    single_trigger_times_clear_text_icon = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/single_trigger_times']/android.view.ViewGroup/android.widget.ImageView")
    digits = (AppiumBy.ID, "com.atp.newdemo2:id/digits")
    split_switch = (AppiumBy.ID, "com.atp.newdemo2:id/split_switch")
    protection = (AppiumBy.ID, "com.atp.newdemo2:id/protection")
    active_leg_type = (AppiumBy.ID, "com.atp.newdemo2:id/active_leg_type")
    commodity_type_A = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/commodity_root']/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView")
    contract_text_A = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/commodity_root']/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")
    contract_text_A = (AppiumBy.XPATH,
                       "//*[@resource-id='com.atp.newdemo2:id/commodity_root']/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")




    contract_name = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_name_or_code')
    K_line = (AppiumBy.ID, 'com.atp.newdemo2:id/k_line_thumbnail')
    Chg_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[4]/android.widget.TextView[1]")
    bid_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[1]")
    bid_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[2]")
    offer_price_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[1]")
    offer_lots_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[2]")
    trade_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/account")
    stop_profit_mode_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/stop_profit_mode']/android.widget.LinearLayout/android.widget.Button")
    trade_account_text_path = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/recycler_view_account']/android.widget.LinearLayout[2]/android.widget.TextView")
    change_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/action_change")

    sell_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_sell")
    buy_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_buy")
    lots_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/lots']/android.view.ViewGroup/android.widget.EditText")
    single_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/single']/android.view.ViewGroup/android.widget.EditText")
    price_diff_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price_diff']/android.view.ViewGroup/android.widget.EditText")
    price_type_button_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price_type']/android.widget.LinearLayout/android.widget.Button")

    last_trade_xpath = (AppiumBy.XPATH, "//*[@text='最后成交价' or @text='Last trade']/..")
    market_buy_xpath = (AppiumBy.XPATH, "//*[@text='市场买价' or @text='Market buy']/..")
    market_sell_xpath = (AppiumBy.XPATH, "//*[@text='市场卖价' or @text='Market sell']/..")
    best_bid_xpath = (AppiumBy.XPATH, "//*[@text='对手价' or @text='Best Bid/Offer']/..")
    order_interval_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/order_interval']/android.view.ViewGroup/android.widget.EditText")
    cancel_order_interval_xpath = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/cancel_order_interval']/android.view.ViewGroup/android.widget.EditText")
    effect_immediately_id = (AppiumBy.ID, "com.atp.newdemo2:id/effect_immediately")
    start_time_radio_id = (AppiumBy.ID, "com.atp.newdemo2:id/start_time_radio")
    start_time_id = (AppiumBy.ID, "com.atp.newdemo2:id/start_time")
    always_execute_id = (AppiumBy.ID, "com.atp.newdemo2:id/always_execute")
    end_time_radio_id = (AppiumBy.ID, "com.atp.newdemo2:id/end_time_radio")
    end_time_id = (AppiumBy.ID, "com.atp.newdemo2:id/end_time")
    cancel_limit_switch = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/cancel_limit']/android.view.ViewGroup/android.widget.Switch")
    cancel_limit_text = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/cancel_limit']/android.view.ViewGroup/android.widget.EditText")
    price_limit_switch = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price_limit']/android.view.ViewGroup/android.widget.Switch")
    price_limit_text = (AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price_limit']/android.view.ViewGroup/android.widget.EditText")


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
    exchange_market_order_switch = (AppiumBy.ID, "com.atp.newdemo2:id/support_market")
    order_details_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    order_details_side = (AppiumBy.XPATH, "//*[@text='方向' or @text='Side']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_contract = (AppiumBy.XPATH, "//*[@text='合约' or @text='Contract']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_account = (AppiumBy.XPATH, "//*[@text='交易账户' or @text='Trade Account']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price_diff = (AppiumBy.XPATH,
                          "//*[@text='价差' or @text='Diff']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_lots = (AppiumBy.XPATH, "//*[@text='手数' or @text='Lots']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")



    order_details_offset_flag = (AppiumBy.XPATH, "//*[@text='开平标志' or @text='Offset Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_hedge_flag = (AppiumBy.XPATH, "//*[@text='投保标志' or @text='Hedge Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_t = (AppiumBy.XPATH, "//*[@text='T+1']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_memo = (AppiumBy.XPATH, "//*[@text='备注' or @text='Memo']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    alert_contract_code = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_code')
    alert_order_id = (AppiumBy.ID, 'com.atp.newdemo2:id/order_id')
    alert_message_ID = (AppiumBy.ID, "com.atp.newdemo2:id/message")
    alert_message_title = (AppiumBy.ID, "com.atp.newdemo2:id/title")
    button_close = (AppiumBy.ID, 'com.atp.newdemo2:id/close_button')
    last_price_and_lots = (AppiumBy.ID, "com.atp.newdemo2:id/lots_at_price")
    contract_management_ID = (AppiumBy.ID, "com.atp.newdemo2:id/manage_contract")
    main_test_contract_drag_path = ("//*[@text='GC2212-CME']/../android.widget.ImageView")
    # 权限测试合约，买卖盘有数据涨跌幅无数据
    permission_contract_drag_path = ("//*[@text='TCU1907-SH']/../android.widget.ImageView")
    # 无数据测试合约，买卖盘涨跌幅均无数据
    no_data_contract_drag_path = ("//*[@text='GC2806-CME']/../android.widget.ImageView")
    edit_memo_ID = (AppiumBy.ID, "com.atp.newdemo2:id/edit_memo")
    error_hint_ID = (AppiumBy.ID, "com.atp.newdemo2:id/memo_error_hint")

    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        self.click_action(self.strategies_tabbar_xpath)

    def alert_order_details_title(self):
        alert_message_title = self.get_visible_element(self.alert_message_title).text
        return alert_message_title

    def alert_order_details_message(self):
        alert_message = self.get_visible_element(self.alert_message_ID).text
        return alert_message

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

    def press_bid(self):
        self.click_action(self.bid_price_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(self.twap_order_path)

    def press_offer(self):
        self.click_action(self.offer_price_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(self.twap_order_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(self.trade_account_ID)
        trade_account_value = self.get_visible_element(self.trade_account_text_path).text
        self.click_action(self.trade_account_text_path)
        self.click_action(self.change_account_ID)
        changed_trade_account_value = self.get_visible_element(self.trade_account_ID).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(self.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
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
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
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
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(self.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if bid_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return bid_lots_value, lots_value, order_details_lots_value

    def press_offer_and_check_lots(self):
        offer_lots_value = self.get_visible_element(self.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if offer_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return offer_lots_value, lots_value, order_details_lots_value

    def slide_and_press_chg(self):
        self.slide_action(967, 978, 678, 978)
        self.click_action(self.Chg_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(self.twap_order_path)
        buy_value = self.get_visible_element(self.buy_side_id)
        sell_value = self.get_visible_element(self.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(self.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_action(967, 978, 678, 978)
        Chg_value = self.get_visible_element(self.Chg_path).text
        self.click_action(self.Chg_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(self.twap_order_path)
        lots_value = self.get_visible_element(self.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if Chg_value == "-":
            return lots_value, order_details_lots_value
        else:
            return float(last_lots), float(lots_value), order_details_lots_value

    def clear_lots_and_order(self):
        self.press_bid()
        self.clear_action(self.lots_xpath)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def single_default(self):
        self.press_offer()
        single_value = self.get_visible_element(self.single_xpath).text
        return single_value

    def input_single_value(self, single_value):
        self.press_offer()
        self.clear_action(self.single_xpath)
        self.input_action(self.single_xpath, single_value)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        single_value = self.get_visible_element(self.single_xpath).text
        self.press_confirm_button()
        return single_value

    def input_single_value_and_lots(self, single_value, lots):
        self.press_offer()
        self.clear_action(self.single_xpath)
        self.input_action(self.single_xpath, single_value)
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def input_single_value_and_lots_and_order(self, single_value, lots):
        self.input_single_value_and_lots(single_value, lots)
        order_detail_single_value = self.get_visible_element(self.order_details_single).text
        self.press_confirm_button()
        return order_detail_single_value

    def price_diff_default(self):
        self.press_offer()
        diff_value = self.get_visible_element(self.price_diff_xpath).text
        return diff_value

    def input_price_diff_value(self, price_diff_value):
        self.press_offer()
        self.clear_action(self.price_diff_xpath)
        self.input_action(self.price_diff_xpath, price_diff_value)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        price_diff_value = self.get_visible_element(self.price_diff_xpath).text
        self.press_confirm_button()
        return price_diff_value

    def input_price_diff_value_and_order(self, price_diff_value):
        self.input_price_diff_value(price_diff_value)
        order_detail_price_diff_value = self.get_visible_element(self.order_details_price_diff).text
        self.press_confirm_button()
        return order_detail_price_diff_value

    def price_type_default(self):
        self.press_offer()
        price_type_default = self.get_visible_element(self.price_type_button_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_price_type_value = self.get_visible_element(self.order_details_price_type).text
        self.press_confirm_button()
        return price_type_default,  order_detail_price_type_value

    def change_price_type_and_order(self, change_type):
        self.press_offer()
        self.click_action(self.price_type_button_xpath)
        self.click_action(change_type)
        self.press_confirm_button()
        price_type_value = self.get_visible_element(self.price_type_button_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_price_type_value = self.get_visible_element(self.order_details_price_type).text
        self.press_confirm_button()
        return price_type_value, order_detail_price_type_value

    def change_price_type_market_buy_and_order(self):
        change_type = self.market_buy_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def change_price_type_market_sell_and_order(self):
        change_type = self.market_sell_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def change_price_type_best_bid_and_order(self):
        change_type = self.best_bid_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def order_interval_default(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        order_interval_value = self.get_visible_element(self.order_interval_xpath).text
        return order_interval_value

    def input_order_interval_value(self, order_interval_value):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.clear_action(self.order_interval_xpath)
        self.input_action(self.order_interval_xpath, order_interval_value)
        self.input_action(self.cancel_order_interval_xpath, "1")
        order_interval_value = self.get_visible_element(self.order_interval_xpath).text
        self.press_confirm_button()
        return order_interval_value

    def input_order_interval_value_and_order(self, order_interval_value):
        self.input_order_interval_value(order_interval_value)
        order_detail_order_interval_value = self.get_visible_element(self.order_details_order_interval).text
        self.press_confirm_button()
        return order_detail_order_interval_value

    def cancel_order_interval_default(self):
        self.press_offer()
        cancel_order_interval_value = self.get_visible_element(self.cancel_order_interval_xpath).text
        return cancel_order_interval_value

    def input_cancel_order_interval_value(self, cancel_order_interval_value):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.clear_action(self.cancel_order_interval_xpath)
        self.input_action(self.cancel_order_interval_xpath, cancel_order_interval_value)
        self.input_action(self.order_interval_xpath, "123456.123")
        cancel_order_interval_value = self.get_visible_element(self.cancel_order_interval_xpath).text
        self.press_confirm_button()
        return cancel_order_interval_value

    def input_cancel_order_interval_value_and_order(self, cancel_order_interval_value):
        self.input_cancel_order_interval_value(cancel_order_interval_value)
        order_detail_cancel_order_interval_value = self.get_visible_element(self.order_details_cancel_order_interval).text
        self.press_confirm_button()
        return order_detail_cancel_order_interval_value

    def input_order_interval_and_cancel_interval(self, order_interval, cancel_interval):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, order_interval)
        self.input_action(self.cancel_order_interval_xpath, cancel_interval)
        self.press_confirm_button()

    def input_order_interval_and_cancel_interval_and_order(self, order_interval, cancel_interval):
        self.input_order_interval_and_cancel_interval(order_interval, cancel_interval)
        self.press_confirm_button()

    def start_time_default(self):
        self.press_offer()
        start_time = self.get_visible_element(self.effect_immediately_id)
        option = self.get_visible_element(self.start_time_radio_id)
        default_value = start_time.get_attribute("checked")
        option_value = option.get_attribute("checked")
        return default_value, option_value

    def start_time_default_value_and_order(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_start_time = self.get_visible_element(self.order_details_start_time).text
        self.press_confirm_button()
        return order_detail_start_time

    def change_start_time_radio(self):
        self.press_offer()
        click_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.click_action(self.start_time_radio_id)
        start_time_default = self.get_visible_element(self.effect_immediately_id)
        start_time_option = self.get_visible_element(self.start_time_radio_id)
        default_checked = start_time_default.get_attribute("checked")
        option_checked = start_time_option.get_attribute("checked")
        start_time = self.get_visible_element(self.start_time_id)
        start_time_value = start_time.text
        start_time_enabled = start_time.get_attribute("enabled")
        return default_checked, option_checked, click_time, start_time_value, start_time_enabled

    def start_time_radio_and_order(self):
        self.change_start_time_radio()
        start_time = self.get_visible_element(self.start_time_id)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_start_time = self.get_visible_element(self.order_details_start_time).text
        self.press_confirm_button()
        return start_time, order_detail_start_time

    def end_time_default(self):
        self.press_offer()
        end_time = self.get_visible_element(self.always_execute_id)
        option = self.get_visible_element(self.end_time_radio_id)
        default_value = end_time.get_attribute("checked")
        option_value = option.get_attribute("checked")
        return default_value, option_value

    def change_end_time_radio(self):
        self.press_offer()
        click_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.click_action(self.end_time_radio_id)
        end_time_default = self.get_visible_element(self.always_execute_id)
        end_time_option = self.get_visible_element(self.end_time_radio_id)
        default_checked = end_time_default.get_attribute("checked")
        option_checked = end_time_option.get_attribute("checked")
        end_time = self.get_visible_element(self.end_time_id)
        end_time_value = end_time.text
        end_time_enabled = end_time.get_attribute("enabled")
        return default_checked, option_checked, click_time, end_time_value, end_time_enabled

    def end_time_radio_and_order(self):
        self.change_end_time_radio()
        end_time = self.get_visible_element(self.end_time_id)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_end_time = self.get_visible_element(self.order_details_end_time).text
        self.press_confirm_button()
        return end_time, order_detail_end_time

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(self.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_default_value, order_details_offset_flag_value

    def change_offset_flag_and_order(self, option_value):
        self.press_offer()
        self.click_action(self.offset_flag_change_button)
        self.click_action(option_value)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(self.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1200)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_open_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_open_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_CT_O_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_C_CT_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_C_O_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_CT_C_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_O_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_C_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_O_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_CT_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CY_O_and_order(self):
        result = self.change_offset_flag_and_order(self.offset_flag_CY_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(self.hedge_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
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
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
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
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def cancel_limit(self):
        self.press_offer()
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        cancel_limit_switch_default_value = self.get_visible_element(self.cancel_limit_switch)
        switch_checked = cancel_limit_switch_default_value.get_attribute("checked")
        cancel_limit_text = self.get_visible_element(self.cancel_limit_text)
        switch_text_enabled = cancel_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def open_cancel_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(self.cancel_limit_switch)
        cancel_limit_switch_default_value = self.get_visible_element(self.cancel_limit_switch)
        switch_checked = cancel_limit_switch_default_value.get_attribute("checked")
        cancel_limit_text = self.get_visible_element(self.cancel_limit_text)
        switch_text_enabled = cancel_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def input_cancel_limit_text(self, cancel_limit_value):
        self.press_offer()
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(self.cancel_limit_switch)
        self.input_action(self.cancel_limit_text, cancel_limit_value)
        cancel_limit_value = self.get_visible_element(self.cancel_limit_text).text
        self.press_confirm_button()
        return cancel_limit_value

    def input_cancel_limit_text_and_order(self, cancel_limit):
        cancel_limit_text = self.input_cancel_limit_text(cancel_limit)
        order_detail_cancel_limit_text = self.get_visible_element(self.order_details_cancel_limit).text
        self.press_confirm_button()
        return cancel_limit_text, order_detail_cancel_limit_text


    def price_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        price_limit_switch_default_value = self.get_visible_element(self.price_limit_switch)
        price_limit_text = self.get_visible_element(self.price_limit_text)
        switch_checked = price_limit_switch_default_value.get_attribute("checked")
        switch_text_enabled = price_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def open_price_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(self.price_limit_switch)
        price_limit_switch_default_value = self.get_visible_element(self.price_limit_switch)
        price_limit_text = self.get_visible_element(self.price_limit_text)
        switch_checked = price_limit_switch_default_value.get_attribute("checked")
        switch_text_enabled = price_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def input_price_limit_text(self, price_limit_value):
        self.press_offer()
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(self.price_limit_switch)
        self.input_action(self.price_limit_text, price_limit_value)
        price_limit_value = self.get_visible_element(self.price_limit_text).text
        self.press_confirm_button()
        return price_limit_value

    def input_price_limit_text_and_order(self, price_limit):
        price_limit_text = self.input_price_limit_text(price_limit)
        order_detail_price_limit_text = self.get_visible_element(self.order_details_price_limit).text
        self.press_confirm_button()
        return price_limit_text, order_detail_price_limit_text




    def edit_memo_and_order(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
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
        self.input_action(self.order_interval_xpath, "1")
        self.input_action(self.cancel_order_interval_xpath, "1")
        hint = self.get_visible_element(self.error_hint_ID).text
        memo_value = self.get_visible_element(self.edit_memo_ID).text
        self.press_confirm_button()
        order_details_memo_value = self.order_details_memo_value()
        self.press_confirm_button()
        return hint, memo_value, order_details_memo_value


if __name__ == '__main__':
    driver = android_driver()

