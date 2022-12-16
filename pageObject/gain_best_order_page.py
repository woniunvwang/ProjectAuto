import random
import string
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from common.All_path import all_path
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class GainBestOrderPage(BasePage):

    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        time.sleep(1)
        self.slide_action(960, 280, 700, 280)
        self.click_action(all_path.contract_group_text)

    def alert_order_details_message(self):
        result = self.get_visible_element(all_path.alert_message_ID).text
        return result

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

    def order_details_price_value(self):
        order_details_price_value = self.get_visible_element(all_path.order_details_price).text
        return order_details_price_value

    def order_details_gap_value(self):
        order_details_gap_value = self.get_visible_element(all_path.order_details_gap).text
        return order_details_gap_value

    def order_details_step_value(self):
        order_details_step_value = self.get_visible_element(all_path.order_details_step).text
        return order_details_step_value

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
        self.click_action(all_path.gain_best_order_path)

    def press_offer(self):
        self.click_action(all_path.offer_price_path)
        self.click_action(all_path.gain_best_order_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(all_path.trade_account_ID)
        trade_account_value = self.get_visible_element(all_path.trade_account_text_path).text
        self.click_action(all_path.trade_account_text_path)
        self.click_action(all_path.change_account_ID)
        changed_trade_account_value = self.get_visible_element(all_path.trade_account_ID).text
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.press_confirm_button()
        order_details_account_value = self.get_visible_element(all_path.order_details_account).text
        return trade_account_value, changed_trade_account_value, order_details_account_value

    def press_bid_and_order(self):
        self.press_bid()
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(all_path.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
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
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.click_action(all_path.gain_best_order_path)
        buy_value = self.get_visible_element(all_path.buy_side_id)
        sell_value = self.get_visible_element(all_path.sell_side_id)
        buy_checkbox = buy_value.get_attribute("checked")
        sell_checkbox = sell_value.get_attribute("checked")
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.press_confirm_button()
        order_details_side_value = self.get_visible_element(all_path.order_details_side).text
        self.press_confirm_button()
        return buy_checkbox, sell_checkbox, order_details_side_value

    def press_chg_and_check_price(self):
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_price = last_price_and_lots.split('@')[1]
        self.slide_and_chg()
        chg_value = self.get_visible_element(all_path.Chg_path).text
        self.click_action(all_path.Chg_path)
        self.click_action(all_path.gain_best_order_path)
        price_value = self.get_visible_element(all_path.price_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.press_confirm_button()
        order_details_price_value = self.order_details_price_value()
        if chg_value == "-":
            return price_value, order_details_price_value
        else:
            return float(last_price), float(price_value), float(order_details_price_value)

    def press_chg_and_check_lots(self):
        last_price_and_lots = self.get_visible_element(all_path.last_price_and_lots).text
        last_lots = last_price_and_lots.split('@')[0]
        self.slide_and_chg()
        Chg_value = self.get_visible_element(all_path.Chg_path).text
        self.click_action(all_path.Chg_path)
        self.click_action(all_path.gain_best_order_path)
        lots_value = self.get_visible_element(all_path.lots_xpath).text
        self.slide_action(460, 1750, 460, 1400)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.press_confirm_button()

    def clear_price_and_order(self):
        self.press_offer()
        self.clear_action(all_path.price_xpath)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def not_input_gap_and_order(self):
        self.press_offer()
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_gap_and_order(self, gap_value):
        self.press_offer()
        self.input_action(all_path.gap_xpath, gap_value)
        self.input_action(all_path.step_xpath, "10")
        self.press_confirm_button()

    def input_legal_gap_and_order(self, gap_value):
        self.press_offer()
        self.input_action(all_path.gap_xpath, gap_value)
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_gap_value = self.order_details_gap_value()
        self.press_confirm_button()
        return order_details_gap_value

    def not_input_step_and_order(self):
        self.press_offer()
        self.input_action(all_path.gap_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_step_and_order(self, step_value):
        self.press_offer()
        self.input_action(all_path.step_xpath, step_value)
        self.input_action(all_path.gap_xpath, "10")
        self.press_confirm_button()

    def input_legal_step_and_order(self, step_value):
        self.press_offer()
        self.input_action(all_path.step_xpath, step_value)
        self.input_action(all_path.gap_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_step_value = self.order_details_step_value()
        self.press_confirm_button()
        return order_details_step_value

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_illegal_price_and_order(self, price):
        self.press_offer()
        self.clear_action(all_path.price_xpath)
        self.input_action(all_path.price_xpath, price)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()

    def input_lots_and_price_and_order(self, lots, price):
        self.press_offer()
        self.clear_action(all_path.lots_xpath)
        self.input_action(all_path.lots_xpath, lots)
        self.clear_action(all_path.price_xpath)
        self.input_action(all_path.price_xpath, price)
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_lots_value = self.order_details_lots_value()
        order_details_price_value = self.order_details_price_value()
        self.press_confirm_button()
        return order_details_lots_value, order_details_price_value

    def alert_title_send_order_successfully(self):
        alert_title = self.get_visible_element(all_path.alert_title).text
        self.click_action(all_path.button_close)
        return alert_title

    def offset_flag_auto_and_order(self):
        self.press_offer()
        offset_flag_default_value = self.get_visible_element(all_path.offset_flag_change_button).text
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_offset_flag_value = self.order_details_offset_flag_value()
        self.press_confirm_button()
        return offset_flag_value, order_details_offset_flag_value

    def hedge_flag_speculation_and_order(self):
        self.press_offer()
        hedge_flag_default_value = self.get_visible_element(all_path.hedge_flag_change_button).text
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
        self.slide_action(460, 1750, 460, 1400)
        self.press_confirm_button()
        order_details_hedge_flag_value = self.order_details_hedge_flag_value()
        self.press_confirm_button()
        return hedge_flag_value, order_details_hedge_flag_value

    def edit_memo_and_order(self):
        self.press_offer()
        self.input_action(all_path.gap_xpath, "10")
        self.input_action(all_path.step_xpath, "10")
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
