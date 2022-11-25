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
        self.assertEqual(order_message, AlertError.alert_order_message)
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

    def test_03_press_offer_and_side_should_sell(self):
        result = self.twap_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_04_press_offer_and_lots_should_offer_value(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(offer_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_05_press_chg_and_side_should_buy(self):
        result = self.twap_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_06_press_chg_and_lots_should_last_lots_value(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(last_lots, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_07_press_no_data_bid_and_lots_should_fix_num(self):
        self.twap_order_page.no_data_contract_to_top()  # 让GC2806-CME排在合约列表的第一位来进行没有数据时的测试
        result = self.twap_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_08_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_09_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_10_change_trade_account_should_success(self):
        self.twap_order_page.main_contract_to_top()  # 没有数据时的测试结束，让主测试合约GC2212-CME排在合约列表的第一位来进行
        result = self.twap_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        self.assertEqual(trade_account_value, changed_trade_account_value)
        self.assertEqual(changed_trade_account_value, order_details_account_value)

    def test_11_change_side_should_success(self):
        result = self.twap_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_12_clear_lots_and_order_should_fail(self):
        self.twap_order_page.clear_lots_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertTrue(result)

    def test_13_input_illegal_lots_and_order_should_fail(self):
        self.twap_order_page.input_illegal_lots_and_order("1.")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        self.assertTrue(result)

    def test_14_input_illegal_lots_and_order_should_fail(self):
        self.twap_order_page.input_illegal_lots_and_order("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        self.assertTrue(result)

    def test_15_single_default_value_should_fix_value(self):
        single_value = self.twap_order_page.single_default()
        self.assertEqual("1", single_value)

    def test_16_clear_single_value_and_order_should_fail(self):
        self.twap_order_page.input_single_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single)
        self.assertTrue(result)

    def test_17_clear_single_value_and_order_should_fail(self):
        self.twap_order_page.input_single_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single)
        self.assertTrue(result)

    def test_18_input_illegal_single_value_and_order_should_fail(self):
        single_value = self.twap_order_page.input_single_value("+.-0")
        self.assertNotEqual("+.-", single_value)
        self.assertEqual("1", single_value)

    def test_19_input_single_value_above_lots_and_order_should_fail(self):
        self.twap_order_page.input_single_value_and_lots("10", "5")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single_and_lots)
        self.assertTrue(result)

    def test_20_input_single_value_equal_lots_and_order_should_success(self):
        order_detail_single_value = self.twap_order_page.input_single_value_and_lots_and_order("10", "10")
        self.assertEqual("10", order_detail_single_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_21_input_single_value_below_lots_and_order_should_success(self):
        order_detail_single_value = self.twap_order_page.input_single_value_and_lots_and_order("10", "20")
        self.assertEqual("10", order_detail_single_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_22_price_diff_default_value_should_fix_value(self):
        diff_value = self.twap_order_page.price_diff_default()
        self.assertEqual("0", diff_value)

    def test_23_clear_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_price_diff)
        self.assertTrue(result)

    def test_24_input_illegal_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        self.assertTrue(result)

    def test_25_input_illegal_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        self.assertTrue(result)

    def test_26_input_illegal_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        self.assertTrue(result)

    #     价差不合法
    def test_27_input_illegal_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("1.000001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff_tick_size)
        self.assertTrue(result)

    def test_28_input_legal_price_diff_value_and_order_should_success(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("-123")
        self.assertEqual("-123", order_detail_price_diff_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_29_input_legal_price_diff_value_and_order_should_success(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("0")
        self.assertEqual("0", order_detail_price_diff_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_30_input_legal_price_diff_value_and_order_should_success(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("123")
        self.assertEqual("123", order_detail_price_diff_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_31_price_type_default_should_last_trade(self):
        result = self.twap_order_page.price_type_default()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        self.assertEqual("最后成交价", price_type_default)
        self.assertEqual("最后成交价", order_detail_price_type_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_32_change_price_type_market_buy_and_order_should_success(self):
        result = self.twap_order_page.change_price_type_market_buy_and_order()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        self.assertEqual("市场买价", price_type_default)
        self.assertEqual("市场买价", order_detail_price_type_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_33_change_price_type_best_bid_and_order_should_success(self):
        result = self.twap_order_page.change_price_type_best_bid_and_order()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        self.assertEqual("对手价", price_type_default)
        self.assertEqual("对手价", order_detail_price_type_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_34_order_interval_default_value_should_none(self):
        order_interval_value = self.twap_order_page.order_interval_default()
        self.assertEqual("请输入秒数", order_interval_value)

    def test_35_clear_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_order_interval)
        self.assertTrue(result)

    def test_36_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        self.assertTrue(result)

    def test_37_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        self.assertTrue(result)

    def test_38_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        self.assertTrue(result)

    def test_39_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        self.assertTrue(result)

    def test_40_input_illegal_order_interval_value_and_order_should_fail(self):
        order_interval_value = self.twap_order_page.input_order_interval_value("-123")
        self.assertEqual("0", order_interval_value)

    def test_41_input_illegal_order_interval_value_and_order_should_success(self):
        order_detail_order_interval_value = self.twap_order_page.input_order_interval_value_and_order("1")
        self.assertEqual("1s", order_detail_order_interval_value)
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)

    def test_42_input_illegal_order_interval_value_and_order_should_success(self):
        order_detail_order_interval_value = self.twap_order_page.input_order_interval_value_and_order("123456.123")
        self.assertEqual("123456.123s", order_detail_order_interval_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_43_cancel_order_interval_default_value_should_none(self):
        cancel_order_interval_value = self.twap_order_page.cancel_order_interval_default()
        self.assertEqual("请输入秒数", cancel_order_interval_value)

    def test_44_clear_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_cancel_order_interval)
        self.assertTrue(result)

    def test_45_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        self.assertTrue(result)

    def test_46_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        self.assertTrue(result)

    def test_47_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        self.assertTrue(result)

    def test_48_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        self.assertTrue(result)

    def test_49_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value("-123")
        self.assertEqual("0", cancel_order_interval_value)

    def test_50_input_illegal_cancel_order_interval_value_and_order_should_success(self):
        order_detail_cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value_and_order("1")
        self.assertEqual("1s", order_detail_cancel_order_interval_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_51_input_illegal_cancel_order_interval_value_and_order_should_success(self):
        order_detail_cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value_and_order("123456.123")
        self.assertEqual("123456.123s", order_detail_cancel_order_interval_value)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_52_input_cancel_order_interval_value_above_order_interval_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_and_cancel_interval("5", "10")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval_value)
        self.assertTrue(result)

    def test_53_input_cancel_order_interval_value_equal_order_interval_and_order_should_success(self):
        self.twap_order_page.input_order_interval_and_cancel_interval_and_order("10", "10")
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_54_input_cancel_order_interval_value_below_order_interval_and_order_should_success(self):
        self.twap_order_page.input_order_interval_and_cancel_interval_and_order("10", "5")
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)

    def test_55_start_time_default_value_should_effect_immediately(self):
        result = self.twap_order_page.start_time_default()
        default_value = result[0]
        option_value = result[1]
        self.assertTrue("true", default_value)
        self.assertEqual("false", option_value)

    def test_56_start_time_default_value_and_order_should_success(self):
        order_detail_start_time = self.twap_order_page.start_time_default_value_and_order()
        self.assertTrue("立刻下单", order_detail_start_time)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_57_start_time_radio_and_order_should_success(self):
        result = self.twap_order_page.start_time_radio_and_order()
        start_time = result[0]
        order_detail_start_time = result[1]
        self.assertTrue(start_time, order_detail_start_time)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_58_change_start_time_radio_and_start_time_should_click_time(self):
        result = self.twap_order_page.change_start_time_radio()
        default_checked = result[0]
        option_checked = result[1]
        click_time = result[2]
        start_time_value = result[3]
        start_time_enabled = result[4]
        self.assertTrue("false", default_checked)
        self.assertEqual("true", option_checked)
        self.assertEqual("true", start_time_enabled)
        self.assertEqual(click_time, start_time_value)

    def test_59_end_time_default_value_should_always_execute(self):
        result = self.twap_order_page.end_time_default()
        default_value = result[0]
        option_value = result[1]
        self.assertTrue("true", default_value)
        self.assertEqual("false", option_value)

    def test_60_change_end_time_radio_and_end_time_should_click_time(self):
        result = self.twap_order_page.change_end_time_radio()
        default_checked = result[0]
        option_checked = result[1]
        click_time = result[2]
        end_time_value = result[3]
        end_time_enabled = result[4]
        self.assertTrue("false", default_checked)
        self.assertEqual("true", option_checked)
        self.assertEqual("true", end_time_enabled)
        self.assertEqual(click_time, end_time_value)

    def test_61_change_end_time_radio_and_now_time_and_order_should_fail(self):
        result = self.twap_order_page.end_time_radio_and_order()
        end_time = result[0]
        order_detail_end_time = result[1]
        self.assertTrue(end_time, order_detail_end_time)
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_end_time)
        self.assertTrue(result)

    def test_62_cancel_limit_default_should_closed(self):
        result = self.twap_order_page.cancel_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        self.assertTrue("false", switch_checked)
        self.assertTrue("false", switch_text_enabled)

    def test_63_open_cancel_limit_default_should_closed(self):
        result = self.twap_order_page.open_cancel_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        self.assertTrue(switch_checked)
        self.assertTrue(switch_text_enabled)

    def test_64_open_cancel_limit_and_text_none_should_fail(self):
        self.twap_order_page.input_cancel_limit_text("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_cancel_limit)
        self.assertTrue(result)

    def test_65_open_cancel_limit_and_text_value_illegal_should_fail(self):
        cancel_limit_value = self.twap_order_page.input_cancel_limit_text("-/*+.")
        self.assertNotEqual("-/*+.", cancel_limit_value)
        self.assertEqual("1", cancel_limit_value)

    def test_66_open_cancel_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_cancel_limit_text_and_order("10")
        cancel_limit_value = result[0]
        order_detail_cancel_limit_text = result[1]
        self.assertEqual("10", cancel_limit_value)
        self.assertEqual("10", order_detail_cancel_limit_text)
        order_message = self.twap_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_order_message)

    def test_67_price_limit_default_should_closed(self):
        result = self.twap_order_page.price_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        self.assertTrue("false", switch_checked)
        self.assertTrue("false", switch_text_enabled)

    def test_68_open_price_limit_default_should_closed(self):
        result = self.twap_order_page.open_price_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        self.assertTrue(switch_checked)
        self.assertTrue(switch_text_enabled)

    def test_69_open_price_limit_and_text_none_should_fail(self):
        self.twap_order_page.input_price_limit_text("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_price_limit)
        self.assertTrue("true", result)

    def test_70_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        self.assertTrue(result)

    def test_71_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        self.assertTrue(result)

    def test_72_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        self.assertTrue(result)

    def test_73_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("10")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        self.assertEqual("10", price_limit_value)
        self.assertEqual("10", order_detail_price_limit_text)
        alert_message_title = self.twap_order_page.alert_order_details_title()
        self.assertEqual(alert_message_title, AlertError.alert_order_message_title)

    def test_74_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("-10")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        self.assertEqual("-10", price_limit_value)
        self.assertEqual("-10", order_detail_price_limit_text)
        alert_message_title = self.twap_order_page.alert_order_details_title()
        self.assertEqual(alert_message_title, AlertError.alert_order_message_title)

    def test_75_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("0")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        self.assertEqual("0", price_limit_value)
        self.assertEqual("0", order_detail_price_limit_text)
        alert_message_title = self.twap_order_page.alert_order_details_title()
        self.assertEqual(alert_message_title, AlertError.alert_order_message_title)

    def test_76_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("12345678.12345678")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        self.assertEqual("12345678.12345678", price_limit_value)
        self.assertEqual("12345678.12345678", order_detail_price_limit_text)
        alert_message_title = self.twap_order_page.alert_order_details_title()
        self.assertEqual(alert_message_title, AlertError.alert_order_message_title)

    def test_77_offset_flag_auto_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_top()  # 让权限合约TCU1907-SH排在合约列表的第一位来进行
        result = self.twap_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_default_value, '自动')
        self.assertEqual(offset_flag_default_value, order_details_offset_flag_value)

    def test_78_offset_flag_open_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_79_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '平仓-平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_80_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '平今-平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_81_offset_flag_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_82_offset_flag_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_83_offset_flag_CY_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(offset_flag_value, '平昨-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_84_hedge_flag_speculation_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(hedge_flag_default_value, '投机')
        self.assertEqual(hedge_flag_default_value, order_details_hedge_flag_value)

    def test_85_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(hedge_flag_value, '套利')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_86_hedge_flag_hedge_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        self.assertEqual(order_message, AlertError.alert_order_message_title)
        self.assertEqual(hedge_flag_value, '套保')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_87_edit_memo_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_bottom()  # 权限合约排到最底部，主合约排到第一位
        result = self.twap_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.twap_order_page.alert_order_details_message()
        # self.assertEqual(order_message, AlertError.alert_order_message)
        self.assertEqual(hint, AlertError.hint_message)
        self.assertEqual(memo_value, order_details_memo_value)


if __name__ == '__main__':
    unittest.main()
