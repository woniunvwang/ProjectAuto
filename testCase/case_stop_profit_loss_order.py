import unittest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.stop_profit_loss_order_page import StopProfitLossOrderPage


class CaseStopOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.stop_profit_loss_order_page = StopProfitLossOrderPage(self.driver)
        self.stop_profit_loss_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        result = self.stop_profit_loss_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(bid_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_price()
        bid_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(bid_price_value, price_value)
        self.assertEqual(price_value, order_details_price_value)

    def test_04_press_bid_and_stop_price_should_offer_value(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_stop_price()
        offer_value = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        self.assertEqual(offer_value, stop_price_value)
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    def test_05_press_offer_and_side_should_sell(self):
        result = self.stop_profit_loss_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_06_press_offer_and_lots_should_offer_value(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(offer_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_07_press_offer_and_price_should_offer_value(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_price()
        offer_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(offer_price_value, price_value)
        self.assertEqual(price_value, order_details_price_value)

    def test_08_press_offer_and_stop_price_should_bid_value(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_stop_price()
        bid_value = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        self.assertEqual(bid_value, stop_price_value)
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    def test_09_press_chg_and_side_should_buy(self):
        result = self.stop_profit_loss_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_10_press_chg_and_lots_should_last_lots_value(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(last_lots, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_11_press_chg_and_price_should_last_price_value(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(last_price, price_value)
        self.assertEqual(price_value, order_details_price_value)

    def test_12_press_chg_and_stop_price_should_last_price_value(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_stop_price()
        last_price = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        self.assertEqual(last_price, stop_price_value)
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_13_press_no_data_bid_and_lots_should_fix_num(self):
        # 合约T2209-CF在第二个的时候执行代码
        # self.stop_profit_loss_order_page.drag_first_contract_to_second_location()
        result = self.stop_profit_loss_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_14_press_no_data_bid_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_15_press_bid_and_offer_no_data_and_stop_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_bid_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        self.assertEqual(stop_price_value, "0")
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    def test_16_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_17_press_no_data_offer_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_18_press_offer_and_bid_no_data_and_stop_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_offer_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        self.assertEqual(stop_price_value, "0")
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    def test_19_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_20_press_no_data_chg_and_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_21_press_no_data_chg_and_stop_price_should_fix_num(self):
        result = self.stop_profit_loss_order_page.press_chg_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        self.assertEqual(stop_price_value, "0")
        self.assertEqual(stop_price_value, order_details_stop_price_value)

    def test_22_change_trade_account_should_success(self):
        result = self.stop_profit_loss_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        self.assertEqual(trade_account_value, changed_trade_account_value)
        self.assertEqual(changed_trade_account_value, order_details_account_value)

    def test_23_change_side_should_success(self):
        result = self.stop_profit_loss_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_24_clear_lots_and_order_should_fail(self):
        self.stop_profit_loss_order_page.clear_lots_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertEqual(True, result)

    def test_25_input_illegal_lots_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_lots_and_order("1.")
        result = self.stop_profit_loss_order_page.alert_illegal_lots_title()
        self.assertEqual(result, AlertError.illegal_lots)

    def test_26_clear_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.clear_price_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_price)
        self.assertEqual(True, result)

    def test_27_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_28_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_29_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    # 价差为0.1
    def test_30_input_illegal_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_price_and_order("0.0000001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_order_price_tick_size)
        self.assertEqual(True, result)

    def test_31_clear_stop_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.clear_stop_price_and_order()
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_message_stop_price)
        self.assertEqual(True, result)

    def test_32_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_price_and_order(".")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        self.assertEqual(True, result)

    def test_33_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_price_and_order("+")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        self.assertEqual(True, result)

    def test_34_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_price_and_order("-")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        self.assertEqual(True, result)

    # 价差为0.1
    def test_35_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_profit_loss_order_page.input_illegal_stop_price_and_order("0.0000001")
        result = self.stop_profit_loss_order_page.is_toast_exist(AlertError.alert_illegal_order_stop_price_tick_size)
        self.assertEqual(True, result)

    def test_36_input_legal_lots_and_price_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(order_details_lots_value, "10")
        self.assertEqual(order_details_price_value, "80")

    # 让有开平投保标志的合约TCU1907-SH排在第一位
    def test_37_stop_option_last_trade_price_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.stop_option_last_trade_price_and_order()
        stop_option_default_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(stop_option_default_value, '最后成交价')
        self.assertEqual(stop_option_default_value, order_details_stop_option_value)

    def test_38_stop_option_market_buy_price_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.stop_option_market_buy_price_and_order()
        stop_option_market_buy_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(stop_option_market_buy_value, '市场买价')
        self.assertEqual(stop_option_market_buy_value, order_details_stop_option_value)

    def test_39_stop_option_market_sell_price_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.stop_option_market_sell_price_and_order()
        stop_option_market_sell_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(stop_option_market_sell_value, '市场卖价')
        self.assertEqual(stop_option_market_sell_value, order_details_stop_option_value)

    def test_40_offset_flag_auto_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_default_value, '自动')
        self.assertEqual(offset_flag_default_value, order_details_offset_flag_value)

    def test_41_offset_flag_open_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_42_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_43_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_44_offset_flag_C_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_45_offset_flag_CT_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_46_offset_flag_CY_O_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平昨-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_47_hedge_flag_speculation_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_default_value, '投机')
        self.assertEqual(hedge_flag_default_value, order_details_hedge_flag_value)

    def test_48_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套利')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_49_hedge_flag_hedge_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_profit_loss_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套保')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_50_edit_memo_and_order_should_success(self):
        result = self.stop_profit_loss_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.stop_profit_loss_order_page.alert_order_details_message()
        # self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(hint, AlertError.hint_message)
        self.assertEqual(memo_value, order_details_memo_value)


if __name__ == '__main__':
    unittest.main()
