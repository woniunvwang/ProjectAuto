import unittest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.twap_order_page import TwapOrderPage


class CaseTwapOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.twap_order_page = TwapOrderPage(self.driver)
        self.twap_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        result = self.twap_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.twap_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(bid_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_05_press_offer_and_side_should_sell(self):
        result = self.twap_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_06_press_offer_and_lots_should_offer_value(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(offer_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_09_press_chg_and_side_should_buy(self):
        result = self.twap_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_10_press_chg_and_lots_should_last_lots_value(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(last_lots, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_11_press_chg_and_price_should_last_price_value(self):
        result = self.twap_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(last_price, price_value)
        self.assertEqual(price_value, order_details_price_value)

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_13_press_no_data_bid_and_lots_should_fix_num(self):
        self.twap_order_page.no_data_contract_to_top()  # 让T2209-CF排在合约列表的第一位来进行没有数据时的测试
        result = self.twap_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_14_press_no_data_bid_and_price_should_fix_num(self):
        result = self.twap_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_16_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_17_press_no_data_offer_and_price_should_fix_num(self):
        result = self.twap_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_19_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_20_press_no_data_chg_and_price_should_fix_num(self):
        result = self.twap_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_22_change_trade_account_should_success(self):
        self.twap_order_page.main_contract_to_top()  # 没有数据时的测试结束，让主测试合约GC2212-CME排在合约列表的第一位来进行
        result = self.twap_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        self.assertEqual(trade_account_value, changed_trade_account_value)
        self.assertEqual(changed_trade_account_value, order_details_account_value)

    def test_23_change_side_should_success(self):
        result = self.twap_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_24_clear_lots_and_order_should_fail(self):
        self.twap_order_page.clear_lots_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertEqual(True, result)

    def test_25_input_illegal_lots_and_order_should_fail(self):
        self.twap_order_page.input_illegal_lots_and_order("1.")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        self.assertEqual(True, result)

    def test_26_clear_price_and_order_should_fail(self):
        self.twap_order_page.clear_price_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_price)
        self.assertEqual(True, result)

    def test_27_input_illegal_price_and_order_should_fail(self):
        self.twap_order_page.input_illegal_price_and_order(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_28_input_illegal_price_and_order_should_fail(self):
        self.twap_order_page.input_illegal_price_and_order("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_29_input_illegal_price_and_order_should_fail(self):
        self.twap_order_page.input_illegal_price_and_order("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    # 价差为0.1
    def test_30_input_illegal_price_and_order_should_fail(self):
        self.twap_order_page.input_illegal_price_and_order("0.0000001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_price_tick_size)
        self.assertEqual(True, result)

    def test_36_input_legal_lots_and_price_and_order_should_success(self):
        result = self.twap_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(order_details_lots_value, "10")
        self.assertEqual(order_details_price_value, "80")

    def test_26_not_input_stop_loss_and_order_should_fail(self):
        self.twap_order_page.not_input_stop_loss_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_stop_loss)
        self.assertEqual(True, result)

    def test_27_input_illegal_stop_loss_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_loss_and_order(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        self.assertEqual(True, result)

    def test_28_input_illegal_stop_loss_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_loss_and_order("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        self.assertEqual(True, result)

    def test_29_input_illegal_stop_loss_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_loss_and_order("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        self.assertEqual(True, result)

    def test_30_input_illegal_stop_loss_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_loss_and_order("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_loss)
        self.assertEqual(True, result)

    def test_31_input_max_stop_loss_and_order_should_success(self):
        order_details_gap_value = self.twap_order_page.input_legal_stop_loss_and_order("12345678.12345678")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("12345678.12345678", order_details_gap_value)

    def test_26_not_input_stop_profit_and_order_should_fail(self):
        self.twap_order_page.not_input_stop_profit_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_stop_profit)
        self.assertEqual(True, result)

    def test_27_input_illegal_stop_profit_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_profit_and_order(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        self.assertEqual(True, result)

    def test_28_input_illegal_stop_profit_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_profit_and_order("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        self.assertEqual(True, result)

    def test_29_input_illegal_stop_profit_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_profit_and_order("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        self.assertEqual(True, result)

    def test_30_input_illegal_stop_profit_and_order_should_fail(self):
        self.twap_order_page.input_illegal_stop_profit_and_order("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_stop_profit)
        self.assertEqual(True, result)

    def test_31_input_max_stop_profit_and_order_should_success(self):
        order_details_gap_value = self.twap_order_page.input_legal_stop_profit_and_order("12345678.12345678")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("12345678.12345678", order_details_gap_value)

    def test_41_change_mode_and_type_and_times_should_enabled_false(self):
        result = self.twap_order_page.change_mode_and_check_type_and_times()
        type_enabled = result[0]
        type_value = result[1]
        times_value = result[2]
        times_enabled = result[3]
        self.assertEqual(type_enabled, 'false')
        self.assertEqual(type_value, "LIM")
        self.assertEqual(times_enabled, "false")
        self.assertEqual(times_value, "1")

    def test_41_change_mode_close_and_order_should_success(self):
        result = self.twap_order_page.change_mode_close_and_order()
        mode_default_value = result[0]
        mode_value = result[1]
        order_details_mode_value = result[2]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(mode_default_value, '按开仓均价止盈止损')
        self.assertEqual(mode_value, '按自定义价止盈止损(不开仓)')
        self.assertEqual(mode_value, order_details_mode_value)

    def test_41_change_mode_open_and_order_should_success(self):
        result = self.twap_order_page.change_mode_open_and_order()
        type_enabled = result[0]
        type_value = result[1]
        mode_value = result[2]
        order_details_mode_value = result[3]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(mode_value, '按开仓均价止盈止损')
        self.assertEqual(type_enabled, 'true')
        self.assertEqual(type_value, "LIM")
        self.assertEqual(mode_value, order_details_mode_value)

    def test_27_changed_market_type_and_price_should_market(self):
        result = self.twap_order_page.change_market_type()
        type_default_value = result[0]
        price_value = result[1]
        price_enabled = result[2]
        type_value = result[3]
        open_px_diff_price = result[4]
        self.assertEqual("LIM", type_default_value)
        self.assertEqual("Market", price_value)
        self.assertEqual("false", price_enabled)
        self.assertEqual("Market", type_value)
        self.assertEqual(True, open_px_diff_price)

    def test_27_changed_market_type_and_order_should_success(self):
        result = self.twap_order_page.change_market_type_and_order()
        order_details_type_value = result[0]
        order_details_price_value = result[1]
        open_px_diff_price_value = result[2]
        order_details_open_px_diff_price_value = result[3]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("Market", order_details_type_value)
        self.assertEqual("Market", order_details_price_value)
        self.assertEqual(open_px_diff_price_value, order_details_open_px_diff_price_value)

    def test_30_market_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.twap_order_page.market_type_changed_lim_type()
        price_default_value = result[0]
        price_value = result[1]
        price_enabled = result[2]
        type_value = result[3]
        open_px_diff_price = result[4]
        self.assertEqual(price_default_value, price_value)
        self.assertEqual("true", price_enabled)
        self.assertEqual("LIM", type_value)
        self.assertEqual(False, open_px_diff_price)

    def test_31_exchange_market_order_default_value_should_closed(self):
        result = self.twap_order_page.exchange_market_order_default()
        exchange_market_order_default = result[0]
        order_detail_exchange_market_order = result[1]
        self.assertEqual("关闭", exchange_market_order_default)
        self.assertEqual(False, order_detail_exchange_market_order)

    def test_31_lim_type_and_exchange_market_order_value_Open_and_close_pxdiff_should_disappear(self):
        result = self.twap_order_page.lim_type_and_exchange_market_order_open()
        close_pxdiff = result[0]
        order_detail_close_pxdiff = result[1]
        order_detail_exchange_market_order_value = result[2]
        self.assertEqual(False, close_pxdiff)
        self.assertEqual(False, order_detail_close_pxdiff)
        self.assertEqual("[平仓]", order_detail_exchange_market_order_value)

    def test_31_market_type_and_exchange_market_order_value_Open_and_close_pxdiff_should_disappear(self):
        result = self.twap_order_page.market_type_and_exchange_market_order_open()
        close_pxdiff = result[0]
        order_detail_close_pxdiff = result[1]
        open_pxdiff = result[2]
        order_detail_open_pxdiff = result[3]
        order_detail_exchange_market_order_value = result[4]
        self.assertEqual(False, close_pxdiff)
        self.assertEqual(False, order_detail_close_pxdiff)
        self.assertEqual(False, open_pxdiff)
        self.assertEqual(False, order_detail_open_pxdiff)
        self.assertEqual("[开仓,平仓]", order_detail_exchange_market_order_value)

    def test_27_clear_close_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.clear_close_pxdiff_and_press_confirm()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_close_pxdiff)
        self.assertEqual(True, result)

    def test_27_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_close_pxdiff_and_press_confirm(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        self.assertEqual(True, result)

    def test_28_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_close_pxdiff_and_press_confirm("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        self.assertEqual(True, result)

    def test_29_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_close_pxdiff_and_press_confirm("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff)
        self.assertEqual(True, result)

    def test_25_input_illegal_close_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_close_pxdiff_and_press_confirm("1.0001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_close_pxdiff_tick_size)
        self.assertEqual(True, result)

    def test_31_legal_close_pxdiff_and_order_should_success(self):
        order_detail_close_pxdiff = self.twap_order_page.input_legal_close_pxdiff_and_order("0")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("0", order_detail_close_pxdiff)

    def test_32_legal_close_pxdiff_and_order_should_success(self):
        order_detail_close_pxdiff = self.twap_order_page.input_legal_close_pxdiff_and_order("100")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("100", order_detail_close_pxdiff)

    def test_27_clear_open_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.clear_open_pxdiff_and_press_confirm()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_open_pxdiff)
        self.assertEqual(True, result)

    def test_27_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_open_pxdiff_and_press_confirm(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        self.assertEqual(True, result)

    def test_28_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_open_pxdiff_and_press_confirm("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        self.assertEqual(True, result)

    def test_29_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_open_pxdiff_and_press_confirm("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff)
        self.assertEqual(True, result)

    def test_25_input_illegal_open_pxdiff_and_press_confirm_should_fail(self):
        self.twap_order_page.input_illegal_open_pxdiff_and_press_confirm("1.0001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_open_pxdiff_tick_size)
        self.assertEqual(True, result)

    def test_31_legal_open_pxdiff_and_order_should_success(self):
        order_detail_open_pxdiff = self.twap_order_page.input_legal_open_pxdiff_and_order("0")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("0", order_detail_open_pxdiff)

    def test_32_legal_open_pxdiff_and_order_should_success(self):
        order_detail_open_pxdiff = self.twap_order_page.input_legal_open_pxdiff_and_order("100")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("100", order_detail_open_pxdiff)

    def test_27_clear_times_and_press_confirm_should_fail(self):
        self.twap_order_page.input_times_and_press_confirm("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_times)
        self.assertEqual(True, result)

    def test_27_input_illegal_times_and_press_confirm_should_fail(self):
        self.twap_order_page.input_times_and_press_confirm("+~!@#¥%^&*()_-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_times)
        self.assertEqual(True, result)

    def test_28_input_illegal_times_and_press_confirm_should_fail(self):
        self.twap_order_page.input_times_and_press_confirm("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_times)
        self.assertEqual(True, result)

    def test_29_input_illegal_times_and_press_confirm_should_fail(self):
        self.twap_order_page.input_times_and_press_confirm("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_times)
        self.assertEqual(True, result)

    def test_25_input_illegal_times_and_press_confirm_should_fail(self):
        self.twap_order_page.input_times_and_press_confirm("1.0001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_times)
        self.assertEqual(True, result)

    def test_31_illegal_times_and_order_should_success(self):
        order_detail_times = self.twap_order_page.input_legal_times_and_order("0")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("0", order_detail_times)

    def test_32_legal_times_and_order_should_success(self):
        order_detail_times = self.twap_order_page.input_legal_times_and_order("100")
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual("100", order_detail_times)

    def test_40_offset_flag_auto_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_top()  # 让权限合约TCU1907-SH排在合约列表的第一位来进行
        result = self.twap_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_default_value, '自动')
        self.assertEqual(offset_flag_default_value, order_details_offset_flag_value)

    def test_41_offset_flag_open_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_42_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_43_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_44_offset_flag_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_45_offset_flag_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_46_offset_flag_CY_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平昨-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_47_hedge_flag_speculation_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_default_value, '投机')
        self.assertEqual(hedge_flag_default_value, order_details_hedge_flag_value)

    def test_48_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套利')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_49_hedge_flag_hedge_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套保')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_50_edit_memo_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_bottom()  # 权限合约排到最底部，主合约排到第一位
        result = self.twap_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.twap_order_page.alert_order_details_message()
        # self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(hint, AlertError.hint_message)
        self.assertEqual(memo_value, order_details_memo_value)


if __name__ == '__main__':
    unittest.main()