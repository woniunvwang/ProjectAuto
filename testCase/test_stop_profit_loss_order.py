import os

import pytest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.stop_profit_loss_order_page import StopProfitLossOrderPage


class TestCaseStopProfitLossOrder:

    def setup_method(self) -> None:
        self.driver = android_driver()
        self.stop_profit_loss_order_page = StopProfitLossOrderPage(self.driver)
        self.stop_profit_loss_order_page.login_successful()

    def teardown_method(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        result = self.stop_profit_loss_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("卖" == order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(bid_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_price()
        bid_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(bid_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_04_press_offer_and_side_should_sell(self):
        result = self.stop_profit_loss_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("买" == order_details_side_value)

    def test_05_press_offer_and_lots_should_offer_value(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(offer_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_06_press_offer_and_price_should_offer_value(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_price()
        offer_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(offer_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_07_press_chg_and_side_should_buy(self):
        result = self.stop_profit_loss_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("买" == order_details_side_value)

    def test_08_press_chg_and_lots_should_last_lots_value(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(last_lots == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_09_press_chg_and_price_should_last_price_value(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(last_price == price_value)
        assert(price_value == order_details_price_value)

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_10_press_no_data_bid_and_lots_should_fix_num(self):
        self.stop_profit_loss_order_page.no_data_contract_to_top()  # 让T2209-CF排在合约列表的第一位来进行没有数据时的测试
        result = self.stop_profit_loss_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_11_press_no_data_bid_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_12_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_13_press_no_data_offer_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_14_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_15_press_no_data_chg_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_16_change_trade_account_should_success(self):
        self.stop_profit_loss_order_page.main_contract_to_top()  # 没有数据时的测试结束，让主测试合约GC2212-CME排在合约列表的第一位来进行
        result = self.stop_profit_loss_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        assert(trade_account_value == changed_trade_account_value)
        assert(changed_trade_account_value == order_details_account_value)

    def test_17_change_side_should_success(self):
        result = self.stop_profit_loss_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("卖" == order_details_side_value)

    def test_18_clear_lots_and_order_should_fail(self):
        self.stop_profit_loss_order_page.clear_lots_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_lots)
        assert result

    def test_19_input_illegal_lots_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_lots_and_order("1.")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        assert result

    def test_20_clear_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.clear_price_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_price)
        assert result

    def test_21_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    def test_22_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    def test_23_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    # 价差为0.1
    def test_24_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("0.0000001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_order_price_tick_size)
        assert result

    def test_25_input_legal_lots_and_price_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert(order_details_lots_value == "10")
        assert(order_details_price_value == "80")

    def test_26_not_input_stop_loss_and_order_should_fail(self):
        self.stop_profit_loss_order_page.not_input_stop_loss_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_stop_loss)
        assert result

    def test_27_input_illegal_stop_loss_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_loss_and_order(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        assert result

    def test_28_input_illegal_stop_loss_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_loss_and_order("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        assert result

    def test_29_input_illegal_stop_loss_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_loss_and_order("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        assert result

    def test_30_input_illegal_stop_loss_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_loss_and_order("0")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        assert result

    def test_31_input_max_stop_loss_and_order_should_success(self):
        order_details_gap_value = self.stop_profit_loss_order_page.input_legal_stop_loss_and_order("12345678.12345678")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("12345678.12345678" == order_details_gap_value)

    def test_32_not_input_stop_profit_and_order_should_fail(self):
        self.stop_profit_loss_order_page.not_input_stop_profit_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_stop_profit)
        assert result

    def test_33_input_illegal_stop_profit_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_profit_and_order(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        assert result

    def test_34_input_illegal_stop_profit_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_profit_and_order("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        assert result

    def test_35_input_illegal_stop_profit_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_profit_and_order("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        assert result

    def test_36_input_illegal_stop_profit_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_profit_and_order("0")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        assert result

    def test_37_input_max_stop_profit_and_order_should_success(self):
        order_details_gap_value = self.stop_profit_loss_order_page.input_legal_stop_profit_and_order("12345678.12345678")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("12345678.12345678" == order_details_gap_value)

    def test_38_change_mode_and_type_and_times_should_enabled_false(self):
        result = self.stop_profit_loss_order_page.change_mode_and_check_type_and_times()
        type_enabled = result[0]
        type_value = result[1]
        times_value = result[2]
        times_enabled = result[3]
        assert(type_enabled == 'false')
        assert(type_value == "LIM")
        assert(times_enabled == "false")
        assert(times_value == "1")

    def test_39_change_mode_close_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.change_mode_close_and_order()
        mode_default_value = result[0]
        mode_value = result[1]
        order_details_mode_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(mode_default_value == '按开仓均价止盈止损')
        assert(mode_value == '按自定义价止盈止损(不开仓)')
        assert(mode_value == order_details_mode_value)

    def test_40_change_mode_open_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.change_mode_open_and_order()
        type_enabled = result[0]
        type_value = result[1]
        mode_value = result[2]
        order_details_mode_value = result[3]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(mode_value == '按开仓均价止盈止损')
        assert(type_enabled == 'true')
        assert(type_value == "LIM")
        assert(mode_value == order_details_mode_value)

    def test_41_changed_market_type_and_price_should_market(self):
        result = self.stop_profit_loss_order_page.change_market_type()
        type_default_value = result[0]
        price_value = result[1]
        price_enabled = result[2]
        type_value = result[3]
        open_px_diff_price = result[4]
        assert("LIM" == type_default_value)
        assert("Market" == price_value)
        assert("false" == price_enabled)
        assert("Market" == type_value)
        assert open_px_diff_price

    def test_42_changed_market_type_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.change_market_type_and_order()
        order_details_type_value = result[0]
        order_details_price_value = result[1]
        open_px_diff_price_value = result[2]
        order_details_open_px_diff_price_value = result[3]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("Market" == order_details_type_value)
        assert("Market" == order_details_price_value)
        assert(open_px_diff_price_value == order_details_open_px_diff_price_value)

    def test_43_market_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.stop_profit_loss_order_page.market_type_changed_lim_type()
        price_default_value = result[0]
        price_value = result[1]
        price_enabled = result[2]
        type_value = result[3]
        open_px_diff_price = result[4]
        assert(price_default_value == price_value)
        assert("true" == price_enabled)
        assert("LIM" == type_value)
        assert open_px_diff_price

    def test_44_exchange_market_order_default_value_should_closed(self):
        result = self.stop_profit_loss_order_page.exchange_market_order_default()
        exchange_market_order_default = result[0]
        order_detail_exchange_market_order = result[1]
        assert("关闭" == exchange_market_order_default)
        assert not order_detail_exchange_market_order

    def test_45_lim_type_and_exchange_market_order_value_Open_and_close_pxdiff_should_disappear(self):
        result = self.stop_profit_loss_order_page.lim_type_and_exchange_market_order_open()
        close_pxdiff = result[0]
        order_detail_close_pxdiff = result[1]
        order_detail_exchange_market_order_value = result[2]
        assert not close_pxdiff
        assert not order_detail_close_pxdiff
        assert("[平仓]" == order_detail_exchange_market_order_value)

    def test_46_market_type_and_exchange_market_order_value_Open_and_close_pxdiff_should_disappear(self):
        result = self.stop_profit_loss_order_page.market_type_and_exchange_market_order_open()
        close_pxdiff = result[0]
        order_detail_close_pxdiff = result[1]
        open_pxdiff = result[2]
        order_detail_open_pxdiff = result[3]
        order_detail_exchange_market_order_value = result[4]
        assert not close_pxdiff
        assert not order_detail_close_pxdiff
        assert not open_pxdiff
        assert not order_detail_open_pxdiff
        assert("[开仓 ==平仓]" == order_detail_exchange_market_order_value)

    def test_47_clear_close_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.clear_close_pxdiff_and_press_confirm()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_close_pxdiff)
        assert result

    def test_48_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_close_pxdiff_and_press_confirm(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        assert result

    def test_49_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_close_pxdiff_and_press_confirm("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        assert result

    def test_50_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_close_pxdiff_and_press_confirm("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        assert result

    def test_51_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_close_pxdiff_and_press_confirm("1.0001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff_tick_size)
        assert result

    def test_52_legal_close_pxdiff_and_order_should_success(self):
        order_detail_close_pxdiff = self.stop_profit_loss_order_page.input_legal_close_pxdiff_and_order("0")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("0" == order_detail_close_pxdiff)

    def test_53_legal_close_pxdiff_and_order_should_success(self):
        order_detail_close_pxdiff = self.stop_profit_loss_order_page.input_legal_close_pxdiff_and_order("100")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("100" == order_detail_close_pxdiff)

    def test_54_clear_open_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.clear_open_pxdiff_and_press_confirm()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_open_pxdiff)
        assert result

    def test_55_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_open_pxdiff_and_press_confirm(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        assert result

    def test_56_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_open_pxdiff_and_press_confirm("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        assert result

    def test_57_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_open_pxdiff_and_press_confirm("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        assert result

    def test_58_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_open_pxdiff_and_press_confirm("1.0001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff_tick_size)
        assert result

    def test_59_legal_open_pxdiff_and_order_should_success(self):
        order_detail_open_pxdiff = self.stop_profit_loss_order_page.input_legal_open_pxdiff_and_order("0")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("0" == order_detail_open_pxdiff)

    def test_60_legal_open_pxdiff_and_order_should_success(self):
        order_detail_open_pxdiff = self.stop_profit_loss_order_page.input_legal_open_pxdiff_and_order("100")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("100" == order_detail_open_pxdiff)

    def test_61_clear_times_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_times_and_press_confirm("")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_times)
        assert result

    def test_62_input_illegal_times_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_times_and_press_confirm("+~!@#¥%^&*()_-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_times)
        assert result

    def test_63_input_illegal_times_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_times_and_press_confirm("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_times)
        assert result

    def test_64_input_illegal_times_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_times_and_press_confirm("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_times)
        assert result

    def test_65_input_illegal_times_and_press_confirm_should_fail(self):
        self.stop_profit_loss_order_page.input_times_and_press_confirm("1.0001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_times)
        assert result

    def test_66_illegal_times_and_order_should_success(self):
        order_detail_times = self.stop_profit_loss_order_page.input_legal_times_and_order("0")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("0" == order_detail_times)

    def test_67_legal_times_and_order_should_success(self):
        order_detail_times = self.stop_profit_loss_order_page.input_legal_times_and_order("100")
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert("100" == order_detail_times)

    def test_68_offset_flag_auto_and_order_should_success(self):
        self.stop_profit_loss_order_page.permission_contract_to_top()  # 让权限合约TCU1907-SH排在合约列表的第一位来进行
        result = self.stop_profit_loss_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_default_value == '自动')
        assert(offset_flag_default_value == order_details_offset_flag_value)

    def test_69_offset_flag_open_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_70_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '平仓-平今-开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_71_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '平今-平仓-开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_72_offset_flag_C_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '平仓-开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_73_offset_flag_CT_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '平今-开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_74_offset_flag_CY_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '平昨-开仓')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_75_hedge_flag_speculation_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_default_value == '投机')
        assert(hedge_flag_default_value == order_details_hedge_flag_value)

    def test_76_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '套利')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_77_hedge_flag_hedge_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '套保')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_78_edit_memo_and_order_should_success(self):
        self.stop_profit_loss_order_page.permission_contract_to_bottom()  # 权限合约排到最底部，主合约排到第一位
        result = self.stop_profit_loss_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_order_message)
        assert(hint == AlertError.hint_message)
        assert(memo_value == order_details_memo_value)


if __name__ == '__main__':
    pytest.main(['test_stop_profit_loss_order.py', '-v', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
