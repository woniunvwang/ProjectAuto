# encoding = 'utf-8'
import random
import string
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains

from common.All_path import all_path
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class TwapOrderPage(BasePage):

    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        time.sleep(1)
        self.slide_action(960, 280, 700, 280)
        self.click_action(all_path.contract_group_text)

    def alert_order_details_title(self):
        alert_message_title = self.get_visible_element(all_path.alert_message_title).text
        return alert_message_title

    def alert_order_details_message(self):
        alert_message = self.get_visible_element(all_path.alert_message_ID).text
        return alert_message

    def order_details_side_value(self):
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        return order_details_side_value

    def order_details_contract_value(self):
        order_details_contract_value = self.get_visible_element(all_path.order_details_contract).text
        return order_details_contract_value

    def order_details_account_value(self):
        order_details_account_value = self.get_visible_element(all_path.order_details_account).text
        return order_details_account_value

    def order_details_lots_value(self):
        order_details_lots_value = self.get_visible_element(all_path.order_details_lots).text
        return order_details_lots_value

    def order_details_offset_flag_value(self):
        order_details_offset_flag_value = self.get_visible_element(all_path.order_details_offset_flag).text
        return order_details_offset_flag_value

    def order_details_hedge_flag_value(self):
        order_details_hedge_flag_value = self.get_visible_element(all_path.order_details_hedge_flag).text
        return order_details_hedge_flag_value

    def order_details_memo_value(self):
        order_details_memo_value = self.get_visible_element(all_path.order_details_memo).text
        return order_details_memo_value

    def press_confirm_button(self):
        self.click_action(all_path.confirm_button_id)

    def allow_button(self):
        allow_button = self.get_visible_element(all_path.allow_button_id)
        allow_button.click()

    def agree_button(self):
        allow_button = self.get_visible_element(all_path.agree_button_id)
        allow_button.click()

    def no_data_contract_to_top(self):
        self.click_action(all_path.contract_management_ID)
        time.sleep(1)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=all_path.no_data_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -220).pause(5).perform()
        self.click_action(all_path.back_button)

    def main_contract_to_top(self):
        self.click_action(all_path.contract_management_ID)
        time.sleep(1)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=all_path.main_test_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -220).pause(5).perform()
        self.click_action(all_path.back_button)

    def permission_contract_to_top(self):
        self.click_action(all_path.contract_management_ID)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=all_path.permission_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, -350).pause(5).perform()
        self.click_action(all_path.back_button)

    def permission_contract_to_bottom(self):
        self.click_action(all_path.contract_management_ID)
        source = self.driver.find_element(by=AppiumBy.XPATH, value=all_path.permission_contract_drag_path)
        ActionChains(self.driver).drag_and_drop_by_offset(source, 0, 350).pause(5).perform()
        self.click_action(all_path.back_button)

    def press_bid(self):
        self.click_action(all_path.bid_price_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(all_path.twap_order_path)

    def press_offer(self):
        self.click_action(all_path.offer_price_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(all_path.twap_order_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(all_path.trade_account_ID)
        trade_account_value = self.get_visible_element(all_path.trade_account_text_path).text
        self.click_action(all_path.trade_account_text_path)
        self.click_action(all_path.change_account_ID)
        changed_trade_account_value = self.get_visible_element(all_path.trade_account_ID).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(all_path.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_offer_and_order(self):
        self.press_offer()
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def change_buy_side(self):
        self.press_offer()
        self.click_action(all_path.sell_side_id)
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(all_path.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if bid_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return bid_lots_value, lots_value, order_details_lots_value

    def press_offer_and_check_lots(self):
        offer_lots_value = self.get_visible_element(all_path.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if offer_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return offer_lots_value, lots_value, order_details_lots_value

    def slide_and_press_chg(self):
        self.slide_action(967, 978, 678, 978)
        self.click_action(all_path.Chg_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(all_path.twap_order_path)
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_action(967, 978, 678, 978)
        Chg_value = self.get_visible_element(all_path.Chg_path).text
        self.click_action(all_path.Chg_path)
        self.slide_action(880, 832, 330, 832)
        self.click_action(all_path.twap_order_path)
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if Chg_value == "-":
            return lots_value, order_details_lots_value
        else:
            return float(last_lots), float(lots_value), order_details_lots_value

    def clear_lots_and_order(self):
        self.press_bid()
        self.clear_action(all_path.lots_xpath)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def single_default(self):
        self.press_offer()
        single_value = self.get_visible_element(all_path.single_xpath).text
        return single_value

    def input_single_value(self, single_value):
        self.press_offer()
        self.clear_action(all_path.single_xpath)
        self.input_action(all_path.single_xpath, single_value)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        single_value = self.get_visible_element(all_path.single_xpath).text
        self.press_confirm_button()
        return single_value

    def input_single_value_and_lots(self, single_value, lots):
        self.press_offer()
        self.clear_action(all_path.single_xpath)
        self.input_action(all_path.single_xpath, single_value)
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()

    def input_single_value_and_lots_and_order(self, single_value, lots):
        self.input_single_value_and_lots(single_value, lots)
        order_detail_single_value = self.get_visible_element(all_path.order_details_single).text
        self.press_confirm_button()
        return order_detail_single_value

    def price_diff_default(self):
        self.press_offer()
        diff_value = self.get_visible_element(all_path.price_diff_xpath).text
        return diff_value

    def input_price_diff_value(self, price_diff_value):
        self.press_offer()
        self.clear_action(all_path.price_diff_xpath)
        self.input_action(all_path.price_diff_xpath, price_diff_value)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        price_diff_value = self.get_visible_element(all_path.price_diff_xpath).text
        self.press_confirm_button()
        return price_diff_value

    def input_price_diff_value_and_order(self, price_diff_value):
        self.input_price_diff_value(price_diff_value)
        order_detail_price_diff_value = self.get_visible_element(all_path.order_details_price_diff).text
        self.press_confirm_button()
        return order_detail_price_diff_value

    def price_type_default(self):
        self.press_offer()
        price_type_default = self.get_visible_element(all_path.price_type_button_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_price_type_value = self.get_visible_element(all_path.order_details_price_type).text
        self.press_confirm_button()
        return price_type_default,  order_detail_price_type_value

    def change_price_type_and_order(self, change_type):
        self.press_offer()
        self.click_action(all_path.price_type_button_xpath)
        self.click_action(change_type)
        self.press_confirm_button()
        price_type_value = self.get_visible_element(all_path.price_type_button_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_price_type_value = self.get_visible_element(all_path.order_details_price_type).text
        self.press_confirm_button()
        return price_type_value, order_detail_price_type_value

    def change_price_type_market_buy_and_order(self):
        change_type = all_path.market_buy_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def change_price_type_market_sell_and_order(self):
        change_type = all_path.market_sell_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def change_price_type_best_bid_and_order(self):
        change_type = all_path.best_bid_xpath
        result = self.change_price_type_and_order(change_type)
        price_type_value = result[0]
        order_detail_price_type_value = result[1]
        return price_type_value, order_detail_price_type_value

    def order_interval_default(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        order_interval_value = self.get_visible_element(all_path.order_interval_xpath).text
        return order_interval_value

    def input_order_interval_value(self, order_interval_value):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.clear_action(all_path.order_interval_xpath)
        self.input_action(all_path.order_interval_xpath, order_interval_value)
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        order_interval_value = self.get_visible_element(all_path.order_interval_xpath).text
        self.press_confirm_button()
        return order_interval_value

    def input_order_interval_value_and_order(self, order_interval_value):
        self.input_order_interval_value(order_interval_value)
        order_detail_order_interval_value = self.get_visible_element(all_path.order_details_order_interval).text
        self.press_confirm_button()
        return order_detail_order_interval_value

    def cancel_order_interval_default(self):
        self.press_offer()
        cancel_order_interval_value = self.get_visible_element(all_path.cancel_order_interval_xpath).text
        return cancel_order_interval_value

    def input_cancel_order_interval_value(self, cancel_order_interval_value):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.clear_action(all_path.cancel_order_interval_xpath)
        self.input_action(all_path.cancel_order_interval_xpath, cancel_order_interval_value)
        self.input_action(all_path.order_interval_xpath, "123456.123")
        cancel_order_interval_value = self.get_visible_element(all_path.cancel_order_interval_xpath).text
        self.press_confirm_button()
        return cancel_order_interval_value

    def input_cancel_order_interval_value_and_order(self, cancel_order_interval_value):
        self.input_cancel_order_interval_value(cancel_order_interval_value)
        order_detail_cancel_order_interval_value = self.get_visible_element(all_path.order_details_cancel_order_interval).text
        self.press_confirm_button()
        return order_detail_cancel_order_interval_value

    def input_order_interval_and_cancel_interval(self, order_interval, cancel_interval):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, order_interval)
        self.input_action(all_path.cancel_order_interval_xpath, cancel_interval)
        self.press_confirm_button()

    def input_order_interval_and_cancel_interval_and_order(self, order_interval, cancel_interval):
        self.input_order_interval_and_cancel_interval(order_interval, cancel_interval)
        self.press_confirm_button()

    def start_time_default(self):
        self.press_offer()
        start_time = self.get_visible_element(all_path.effect_immediately_id)
        option = self.get_visible_element(all_path.start_time_radio_id)
        default_value = start_time.get_attribute("checked")
        option_value = option.get_attribute("checked")
        return default_value, option_value

    def start_time_default_value_and_order(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_start_time = self.get_visible_element(all_path.order_details_start_time).text
        self.press_confirm_button()
        return order_detail_start_time

    def change_start_time_radio(self):
        self.press_offer()
        click_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.click_action(all_path.start_time_radio_id)
        start_time_default = self.get_visible_element(all_path.effect_immediately_id)
        start_time_option = self.get_visible_element(all_path.start_time_radio_id)
        default_checked = start_time_default.get_attribute("checked")
        option_checked = start_time_option.get_attribute("checked")
        start_time = self.get_visible_element(all_path.start_time_id)
        start_time_value = start_time.text
        start_time_enabled = start_time.get_attribute("enabled")
        return default_checked, option_checked, click_time, start_time_value, start_time_enabled

    def start_time_radio_and_order(self):
        self.change_start_time_radio()
        start_time = self.get_visible_element(all_path.start_time_id)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_start_time = self.get_visible_element(all_path.order_details_start_time).text
        self.press_confirm_button()
        return start_time, order_detail_start_time

    def end_time_default(self):
        self.press_offer()
        end_time = self.get_visible_element(all_path.always_execute_id)
        option = self.get_visible_element(all_path.end_time_radio_id)
        default_value = end_time.get_attribute("checked")
        option_value = option.get_attribute("checked")
        return default_value, option_value

    def change_end_time_radio(self):
        self.press_offer()
        click_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.click_action(all_path.end_time_radio_id)
        end_time_default = self.get_visible_element(all_path.always_execute_id)
        end_time_option = self.get_visible_element(all_path.end_time_radio_id)
        default_checked = end_time_default.get_attribute("checked")
        option_checked = end_time_option.get_attribute("checked")
        end_time = self.get_visible_element(all_path.end_time_id)
        end_time_value = end_time.text
        end_time_enabled = end_time.get_attribute("enabled")
        return default_checked, option_checked, click_time, end_time_value, end_time_enabled

    def end_time_radio_and_order(self):
        self.change_end_time_radio()
        end_time = self.get_visible_element(all_path.end_time_id)
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_detail_end_time = self.get_visible_element(all_path.order_details_end_time).text
        self.press_confirm_button()
        return end_time, order_detail_end_time

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_default_value, order_details_offset_flag_value

    def change_offset_flag_and_order(self, option_value):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(option_value)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1200)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_open_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_open_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_CT_O_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_C_CT_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_C_O_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_CT_C_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_O_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_C_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_O_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_CT_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CY_O_and_order(self):
        result = self.change_offset_flag_and_order(all_path.offset_flag_CY_O_xpath)
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(all_path.hedge_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_default_value, order_details_hedge_flag_value

    def hedge_flag_arbitrage_and_order(self):
        self.press_offer()
        self.click_action(all_path.hedge_flag_change_button)
        self.click_action(all_path.hedge_flag_arbitrage_xpath)
        self.press_confirm_button()
        hedge_flag_value = self.get_visible_element(all_path.hedge_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def hedge_flag_hedge_and_order(self):
        self.press_offer()
        self.click_action(all_path.hedge_flag_change_button)
        self.click_action(all_path.hedge_flag_hedge_xpath)
        self.press_confirm_button()
        hedge_flag_value = self.get_visible_element(all_path.hedge_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def cancel_limit(self):
        self.press_offer()
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        cancel_limit_switch_default_value = self.get_visible_element(all_path.cancel_limit_switch)
        switch_checked = cancel_limit_switch_default_value.get_attribute("checked")
        cancel_limit_text = self.get_visible_element(all_path.cancel_limit_text)
        switch_text_enabled = cancel_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def open_cancel_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(all_path.cancel_limit_switch)
        cancel_limit_switch_default_value = self.get_visible_element(all_path.cancel_limit_switch)
        switch_checked = cancel_limit_switch_default_value.get_attribute("checked")
        cancel_limit_text = self.get_visible_element(all_path.cancel_limit_text)
        switch_text_enabled = cancel_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def input_cancel_limit_text(self, cancel_limit_value):
        self.press_offer()
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(all_path.cancel_limit_switch)
        self.input_action(all_path.cancel_limit_text, cancel_limit_value)
        cancel_limit_value = self.get_visible_element(all_path.cancel_limit_text).text
        self.press_confirm_button()
        return cancel_limit_value

    def input_cancel_limit_text_and_order(self, cancel_limit):
        cancel_limit_text = self.input_cancel_limit_text(cancel_limit)
        order_detail_cancel_limit_text = self.get_visible_element(all_path.order_details_cancel_limit).text
        self.press_confirm_button()
        return cancel_limit_text, order_detail_cancel_limit_text

    def price_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        price_limit_switch_default_value = self.get_visible_element(all_path.price_limit_switch)
        price_limit_text = self.get_visible_element(all_path.price_limit_text)
        switch_checked = price_limit_switch_default_value.get_attribute("checked")
        switch_text_enabled = price_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def open_price_limit(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(all_path.price_limit_switch)
        price_limit_switch_default_value = self.get_visible_element(all_path.price_limit_switch)
        price_limit_text = self.get_visible_element(all_path.price_limit_text)
        switch_checked = price_limit_switch_default_value.get_attribute("checked")
        switch_text_enabled = price_limit_text.get_attribute("enabled")
        return switch_checked, switch_text_enabled

    def input_price_limit_text(self, price_limit_value):
        self.press_offer()
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(all_path.price_limit_switch)
        self.input_action(all_path.price_limit_text, price_limit_value)
        price_limit_value = self.get_visible_element(all_path.price_limit_text).text
        self.press_confirm_button()
        return price_limit_value

    def input_price_limit_text_and_order(self, price_limit):
        price_limit_text = self.input_price_limit_text(price_limit)
        order_detail_price_limit_text = self.get_visible_element(all_path.order_details_price_limit).text
        self.press_confirm_button()
        return price_limit_text, order_detail_price_limit_text

    def edit_memo_and_order(self):
        self.press_offer()
        self.slide_action(460, 1750, 460, 1400)
        self.click_action(all_path.edit_memo_ID)
        # 生成随机数的方法1
        # l1 = []
        # i = 0
        # while i < 256:
        #     i += 1
        #     input_value = random.choice(string.ascii_letters + string.digits)
        #     l1.append(input_value)
        #     if len(all_path.edit_memo_ID) == 256:
        #         break
        # 生成随机数的方法2
        # input_value = ''.join(random.choices(string.ascii_letters + string.digits, k=256))
        # 生成随机数的方法3
        input_value = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(256)])
        self.input_action(all_path.edit_memo_ID, input_value)
        self.input_action(all_path.order_interval_xpath, "1")
        self.input_action(all_path.cancel_order_interval_xpath, "1")
        hint = self.get_visible_element(all_path.error_hint_ID).text
        memo_value = self.get_visible_element(all_path.edit_memo_ID).text
        self.press_confirm_button()
        order_details_memo_value = self.order_details_memo_value()
        self.press_confirm_button()
        return hint, memo_value, order_details_memo_value


if __name__ == '__main__':
    driver = android_driver()
