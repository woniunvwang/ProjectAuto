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


class NormalOrderPage(BasePage):

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

    def alert_illegal_lots_title(self):
        return self.get_visible_element(all_path.illegal_lots_xpath).text

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

    def order_details_chunk_size_value(self):
        order_details_chunk_size_value = self.get_visible_element(all_path.order_details_chunk_size).text
        return order_details_chunk_size_value

    def order_details_price_value(self):
        order_details_price_value = self.get_visible_element(all_path.order_details_price).text
        return order_details_price_value

    def order_details_stpx_value(self):
        order_details_stpx_value = self.get_visible_element(all_path.order_details_stpx).text
        return order_details_stpx_value

    def order_details_type_value(self):
        order_details_type_value = self.get_visible_element(all_path.order_details_type).text
        return order_details_type_value

    def order_details_offset_flag_value(self):
        order_details_offset_flag_value = self.get_visible_element(all_path.order_details_offset_flag).text
        return order_details_offset_flag_value

    def order_details_hedge_flag_value(self):
        order_details_hedge_flag_value = self.get_visible_element(all_path.order_details_hedge_flag).text
        return order_details_hedge_flag_value

    def order_details_TIF_value(self):
        order_details_TIF_value = self.get_visible_element(all_path.order_details_tif).text
        return order_details_TIF_value

    def order_details_T_value(self):
        order_details_T_value = self.get_visible_element(all_path.order_details_t).text
        return order_details_T_value

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

    def press_bid(self):
        self.click_action(all_path.bid_price_path)

    def press_offer(self):
        self.click_action(all_path.offer_price_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(all_path.trade_account_ID)
        trade_account_value = self.get_visible_element(all_path.trade_account_text_path).text
        self.click_action(all_path.trade_account_text_path)
        self.click_action(all_path.change_account_ID)
        changed_trade_account_value = self.get_visible_element(all_path.trade_account_ID).text
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(all_path.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
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
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(all_path.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if bid_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return bid_lots_value, lots_value, order_details_lots_value

    def press_bid_and_check_price(self):
        bid_price_value = self.get_visible_element(all_path.bid_price_path).text
        self.press_bid()
        price_value = self.get_visible_element(all_path.price_xpath).text
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if bid_price_value == "-":
            return price_value, order_details_price_value
        else:
            return bid_price_value, price_value, order_details_price_value

    def press_offer_and_check_lots(self):
        offer_lots_value = self.get_visible_element(all_path.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if offer_lots_value == "-":
            return lots_value, order_details_lots_value
        else:
            return offer_lots_value, lots_value, order_details_lots_value

    def press_offer_and_check_price(self):
        offer_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.press_offer()
        price_value = self.get_visible_element(all_path.price_xpath).text
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
        self.click_action(all_path.Chg_path)
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_price(self):
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_price = last_price_and_lots.split('@')[1]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(all_path.Chg_path).text
        self.click_action(all_path.Chg_path)
        price_value = self.get_visible_element(all_path.price_xpath).text
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if Chg_value == "-":
            return price_value, order_details_price_value
        else:
            return float(last_price), float(price_value), float(order_details_price_value)

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(all_path.Chg_path).text
        self.click_action(all_path.Chg_path)
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        if Chg_value == "-":
            return lots_value, order_details_lots_value
        else:
            return float(last_lots), float(lots_value), order_details_lots_value

    def no_data_contract_to_top(self):
        self.click_action(all_path.contract_management_ID)
        time.sleep(2)
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

    def change_type_market(self):
        self.press_offer()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_Market_text)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        return price_value, type_value

    # 类型为STP/Market/Market Limit时价格处显示为置灰的Market

    def Market_type_and_order(self):
        self.change_type_market()
        self.press_confirm_button()
        order_details_type_value = self.order_details_type_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_type_value, order_details_price_value

    def change_type_market_limit(self):
        self.press_offer()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_Market_Limit_text)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        return price_value, type_value

    def market_Limit_type_and_order(self):
        self.change_type_market_limit()
        self.press_confirm_button()
        order_details_type_value = self.order_details_type_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_type_value, order_details_price_value

    def market_type_changed_lim_type(self):
        bid_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.change_type_market()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_Lim_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        return bid_price_value, price_value, type_value

    def market_Limit_type_changed_lim_type(self):
        bid_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.change_type_market_limit()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_Lim_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        return bid_price_value, price_value, type_value

    def change_type_stp(self):
        offer_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.press_offer()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_STP_path)
        self.press_confirm_button()
        input_StPx = self.get_visible_element(all_path.input_StPx_xpath).text
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        StPx_title = self.get_visible_element(all_path.order_details_stpx_title).text
        return offer_price_value, StPx_title, input_StPx, price_value, type_value

    def stp_clear_StPx_and_order(self):
        self.change_type_stp()
        self.clear_action(all_path.input_StPx_xpath)
        self.press_confirm_button()

    def stp_type_input_difference_value(self, difference):
        self.change_type_stp()
        self.clear_action(all_path.input_StPx_xpath)
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(all_path.input_StPx_xpath, price_value)
        stpx_value = self.get_visible_element(all_path.input_StPx_xpath).text
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
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_below_last_price_and_sell_order(self):
        stpx_value = self.stp_type_input_difference_value(-5)
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return stpx_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def change_type_stl(self):
        offer_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.press_offer()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_STL_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        input_StPx = self.get_visible_element(all_path.input_StPx_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        StPx_title = self.get_visible_element(all_path.order_details_stpx_title).text
        return offer_price_value, StPx_title, input_StPx, price_value, type_value

    def stl_clear_StPx_and_order(self):
        self.change_type_stl()
        self.clear_action(all_path.input_StPx_xpath)
        self.press_confirm_button()

    def stl_type_input_difference_value(self, difference):
        self.change_type_stl()
        self.clear_action(all_path.input_StPx_xpath)
        self.clear_action(all_path.price_xpath)
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(all_path.input_StPx_xpath, price_value)
        self.input_action(all_path.price_xpath, price_value)
        StPx_value = self.get_visible_element(all_path.input_StPx_xpath).text
        price_value = self.get_visible_element(all_path.price_xpath).text
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
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_last_price_and_sell_order(self):
        value = self.stl_type_input_difference_value(-5)
        StPx_value = value[0]
        price_value = value[1]
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def stl_type_input_StPx_diff_and_price_diff(self, StPx_diff, price_diff):
        self.change_type_stl()
        self.clear_action(all_path.input_StPx_xpath)
        self.clear_action(all_path.price_xpath)
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(price_diff)
        StPx_value = last_trade_price + int(StPx_diff)
        self.input_action(all_path.input_StPx_xpath, StPx_value)
        self.input_action(all_path.price_xpath, price_value)
        StPx_value = self.get_visible_element(all_path.input_StPx_xpath).text
        price_value = self.get_visible_element(all_path.price_xpath).text
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
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()

    def stl_type_input_StPx_above_price_and_sell_order(self):
        value = self.stl_type_input_StPx_diff_and_price_diff(-5, -10)
        StPx_value = value[0]
        price_value = value[1]
        self.click_action(all_path.sell_side_id)
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        order_details_stpx_value = self.order_details_stpx_value()
        order_details_type_value = self.order_details_type_value()
        self.press_confirm_button()
        return StPx_value, price_value, order_details_stpx_value, order_details_price_value, order_details_type_value

    def change_type_ice(self):
        offer_price_value = self.get_visible_element(all_path.offer_price_path).text
        self.press_offer()
        self.click_action(all_path.change_type_button)
        self.click_action(all_path.type_ICE_path)
        self.press_confirm_button()
        price_value = self.get_visible_element(all_path.price_xpath).text
        type_value = self.get_visible_element(all_path.change_type_button).text
        chunk_size_title = self.get_visible_element(all_path.chunk_size_title).text
        chunk_size_value = self.get_visible_element(all_path.chunk_size_xpath).text
        return chunk_size_value, chunk_size_title, price_value, offer_price_value, type_value

    def ice_type_and_input_lots_and_chunk_size(self, lots, chunk_size_value):
        self.change_type_ice()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.clear_action(all_path.chunk_size_xpath)
        self.input_action(all_path.chunk_size_xpath, chunk_size_value)
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        chunk_size_value = self.get_visible_element(all_path.chunk_size_xpath).text
        return lots_value, chunk_size_value

    def ice_type_clear_chunk_size_and_order(self):
        self.change_type_ice()
        self.clear_action(all_path.chunk_size_xpath)
        self.press_confirm_button()

    def ice_type_input_chunk_size_legal_value_and_order(self):
        result = self.ice_type_and_input_lots_and_chunk_size(15, 10)
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
        self.clear_action(all_path.lots_xpath)
        self.press_confirm_button()

    def clear_price_and_order(self):
        self.press_offer()
        self.clear_action(all_path.price_xpath)
        self.press_confirm_button()

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.press_confirm_button()

    def input_illegal_price_and_order(self, price):
        self.press_offer()
        self.clear_action(all_path.price_xpath)
        self.input_action(all_path.price_xpath, price)
        self.press_confirm_button()

    def input_lots_and_price_and_order(self, lots, price):
        self.press_offer()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.clear_action(all_path.price_xpath)
        self.input_action(all_path.price_xpath, price)
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_lots_value, order_details_price_value

    def get_element_from_send_successfully_alert_and_close_alert(self):
        alert_title = self.get_visible_element(all_path.alert_title).text
        alert_contract_code = self.get_visible_element(all_path.alert_contract_code).text
        alert_order_id = self.get_visible_element(all_path.alert_order_id).text
        self.click_action(all_path.button_close)
        return alert_title, alert_contract_code, alert_order_id

    def change_tif_gtc(self):
        self.press_offer()
        self.click_action(all_path.TIF_change_button)
        self.click_action(all_path.TIF_GTC)
        self.press_confirm_button()

    def change_tif_gtd(self):
        self.press_offer()
        self.click_action(all_path.TIF_change_button)
        self.click_action(all_path.TIF_GTD)
        self.press_confirm_button()

    def change_tif_fak(self):
        self.press_offer()
        self.click_action(all_path.TIF_change_button)
        self.click_action(all_path.TIF_FAK)
        self.press_confirm_button()

    def change_tif_fok(self):
        self.press_offer()
        self.click_action(all_path.TIF_change_button)
        self.click_action(all_path.TIF_FOK)
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
        self.clear_action(all_path.fak_min_quantity)
        self.press_confirm_button()

    def tif_fak_and_input_illegal_min_quantity(self, fak_min):
        self.change_tif_fak()
        self.clear_action(all_path.fak_min_quantity)
        self.input_action(all_path.fak_min_quantity, fak_min)
        return self.get_visible_element(all_path.fak_min_quantity).text

    def tif_fak_and_input_min_quantity_and_lots(self, fak_min, lots):
        self.change_tif_fak()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.clear_action(all_path.fak_min_quantity)
        self.input_action(all_path.fak_min_quantity, fak_min)
        return self.get_visible_element(all_path.fak_min_quantity).text

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_default_value, order_details_offset_flag_value

    def offset_flag_open_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_open_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_close_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_close_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_closeYesterday_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_closeYesterday_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_closeToday_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_closeToday_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_CT_O_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_C_CT_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_C_O_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_CT_C_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_C_O_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_C_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CT_O_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_CT_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def offset_flag_CY_O_and_order(self):
        self.press_offer()
        self.click_action(all_path.offset_flag_change_button)
        self.click_action(all_path.offset_flag_CY_O_xpath)
        self.press_confirm_button()
        offset_flag_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(all_path.hedge_flag_change_button).text
        self.slide_action(460, 1750, 460, 1400)
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
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def change_T_switch_and_order(self):
        self.press_offer()
        self.click_action(all_path.T_switch_ID)
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        self.press_confirm_button()

    def edit_memo_and_order(self):
        self.press_offer()
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
        self.slide_action(460, 1750, 460, 1400)
        hint = self.get_visible_element(all_path.error_hint_ID).text
        memo_value = self.get_visible_element(all_path.edit_memo_ID).text
        self.press_confirm_button()
        order_details_memo_value = self.order_details_memo_value()
        self.press_confirm_button()
        return hint, memo_value, order_details_memo_value


if __name__ == '__main__':
    driver = android_driver()
