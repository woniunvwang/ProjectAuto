import pytest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.twap_order_page import TwapOrderPage


class TestCaseTwapOrder:

    def setup_method(self) -> None:
        self.driver = android_driver()
        self.twap_order_page = TwapOrderPage(self.driver)
        self.twap_order_page.login_successful()

    def teardown_method(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_press_bid_and_side_should_sell(self):
        result = self.twap_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message
        assert "false", buy_checkbox
        assert sell_checkbox
        assert "卖", order_details_side_value

    def test_press_bid_and_lots_should_bid_value(self):
        result = self.twap_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert bid_lots_value, lots_value
        assert lots_value, order_details_lots_value

    def test_press_offer_and_side_should_sell(self):
        result = self.twap_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message
        assert buy_checkbox
        assert "false", sell_checkbox
        assert "买", order_details_side_value

    def test_press_offer_and_lots_should_offer_value(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert offer_lots_value, lots_value
        assert lots_value, order_details_lots_value

    def test_press_chg_and_side_should_buy(self):
        result = self.twap_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message
        assert buy_checkbox
        assert "false", sell_checkbox
        assert "买", order_details_side_value

    def test_press_chg_and_lots_should_last_lots_value(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert last_lots, lots_value
        assert lots_value, order_details_lots_value

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_press_no_data_bid_and_lots_should_fix_num(self):
        self.twap_order_page.no_data_contract_to_top()  # 让GC2806-CME排在合约列表的第一位来进行没有数据时的测试
        result = self.twap_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert lots_value, "1"
        assert lots_value, order_details_lots_value

    def test_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert lots_value, "1"
        assert lots_value, order_details_lots_value

    def test_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.twap_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert lots_value, "1"
        assert lots_value, order_details_lots_value

    def test_change_trade_account_should_success(self):
        self.twap_order_page.main_contract_to_top()  # 没有数据时的测试结束，让主测试合约GC2212-CME排在合约列表的第一位来进行
        result = self.twap_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        assert trade_account_value, changed_trade_account_value
        assert changed_trade_account_value, order_details_account_value

    def test_change_side_should_success(self):
        result = self.twap_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message
        assert "false", buy_checkbox
        assert "true", sell_checkbox
        assert "卖", order_details_side_value

    def test_clear_lots_and_order_should_fail(self):
        self.twap_order_page.clear_lots_and_order()
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_lots)
        assert result

    def test_input_illegal_lots_and_order_should_fail(self):
        self.twap_order_page.input_illegal_lots_and_order("1.")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        assert result

    def test_input_illegal_lots_and_order_should_fail1(self):
        self.twap_order_page.input_illegal_lots_and_order("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        assert result

    def test_single_default_value_should_fix_value(self):
        single_value = self.twap_order_page.single_default()
        assert "1", single_value

    def test_clear_single_value_and_order_should_fail(self):
        self.twap_order_page.input_single_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single)
        assert result

    def test_clear_single_value_and_order_should_fail1(self):
        self.twap_order_page.input_single_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single)
        assert result

    def test_input_illegal_single_value_and_order_should_fail(self):
        single_value = self.twap_order_page.input_single_value("+.-0")
        assert "+.-", single_value
        assert "1", single_value

    def test_input_single_value_above_lots_and_order_should_fail(self):
        self.twap_order_page.input_single_value_and_lots("10", "5")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_single_and_lots)
        assert result

    def test_input_single_value_equal_lots_and_order_should_success(self):
        order_detail_single_value = self.twap_order_page.input_single_value_and_lots_and_order("10", "10")
        assert "10", order_detail_single_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_input_single_value_below_lots_and_order_should_success(self):
        order_detail_single_value = self.twap_order_page.input_single_value_and_lots_and_order("10", "20")
        assert "10", order_detail_single_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_price_diff_default_value_should_fix_value(self):
        diff_value = self.twap_order_page.price_diff_default()
        assert "0", diff_value

    def test_clear_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_price_diff)
        assert result

    def test_input_illegal_price_diff_value_and_order_should_fail(self):
        self.twap_order_page.input_price_diff_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        assert result

    def test_input_illegal_price_diff_value_and_order_should_fail1(self):
        self.twap_order_page.input_price_diff_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        assert result

    def test_input_illegal_price_diff_value_and_order_should_fail2(self):
        self.twap_order_page.input_price_diff_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff)
        assert result

    #     价差不合法
    def test_input_illegal_price_diff_value_and_order_should_fail3(self):
        self.twap_order_page.input_price_diff_value("1.000001")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_diff_tick_size)
        assert result

    def test_input_legal_price_diff_value_and_order_should_success(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("-123")
        assert "-123", order_detail_price_diff_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_input_legal_price_diff_value_and_order_should_success1(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("0")
        assert "0", order_detail_price_diff_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_input_legal_price_diff_value_and_order_should_success2(self):
        order_detail_price_diff_value = self.twap_order_page.input_price_diff_value_and_order("123")
        assert "123", order_detail_price_diff_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_31_price_type_default_should_last_trade(self):
        result = self.twap_order_page.price_type_default()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        assert "最后成交价", price_type_default
        assert "最后成交价", order_detail_price_type_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_32_change_price_type_market_buy_and_order_should_success(self):
        result = self.twap_order_page.change_price_type_market_buy_and_order()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        assert "市场买价", price_type_default
        assert "市场买价", order_detail_price_type_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_33_change_price_type_best_bid_and_order_should_success(self):
        result = self.twap_order_page.change_price_type_best_bid_and_order()
        price_type_default = result[0]
        order_detail_price_type_value = result[1]
        assert "对手价", price_type_default
        assert "对手价", order_detail_price_type_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_34_order_interval_default_value_should_none(self):
        order_interval_value = self.twap_order_page.order_interval_default()
        assert "请输入秒数", order_interval_value

    def test_35_clear_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_order_interval)
        assert result

    def test_36_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        assert result

    def test_37_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        assert result

    def test_38_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        assert result

    def test_39_input_illegal_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_value("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_order_interval)
        assert result

    def test_40_input_illegal_order_interval_value_and_order_should_fail(self):
        order_interval_value = self.twap_order_page.input_order_interval_value("-123")
        assert "0", order_interval_value

    def test_41_input_illegal_order_interval_value_and_order_should_success(self):
        order_detail_order_interval_value = self.twap_order_page.input_order_interval_value_and_order("1")
        assert "1s", order_detail_order_interval_value
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title

    def test_42_input_illegal_order_interval_value_and_order_should_success(self):
        order_detail_order_interval_value = self.twap_order_page.input_order_interval_value_and_order("123456.123")
        assert "123456.123s", order_detail_order_interval_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_43_cancel_order_interval_default_value_should_none(self):
        cancel_order_interval_value = self.twap_order_page.cancel_order_interval_default()
        assert "请输入秒数", cancel_order_interval_value

    def test_44_clear_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_cancel_order_interval)
        assert result

    def test_45_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        assert result

    def test_46_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        assert result

    def test_47_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        assert result

    def test_48_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        self.twap_order_page.input_cancel_order_interval_value("0")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval)
        assert result

    def test_49_input_illegal_cancel_order_interval_value_and_order_should_fail(self):
        cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value("-123")
        assert "0", cancel_order_interval_value

    def test_50_input_illegal_cancel_order_interval_value_and_order_should_success(self):
        order_detail_cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value_and_order("1")
        assert "1s", order_detail_cancel_order_interval_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_51_input_illegal_cancel_order_interval_value_and_order_should_success(self):
        order_detail_cancel_order_interval_value = self.twap_order_page.input_cancel_order_interval_value_and_order("123456.123")
        assert "123456.123s", order_detail_cancel_order_interval_value
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_52_input_cancel_order_interval_value_above_order_interval_and_order_should_fail(self):
        self.twap_order_page.input_order_interval_and_cancel_interval("5", "10")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_cancel_order_interval_value)
        assert result

    def test_53_input_cancel_order_interval_value_equal_order_interval_and_order_should_success(self):
        self.twap_order_page.input_order_interval_and_cancel_interval_and_order("10", "10")
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_54_input_cancel_order_interval_value_below_order_interval_and_order_should_success(self):
        self.twap_order_page.input_order_interval_and_cancel_interval_and_order("10", "5")
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title

    def test_55_start_time_default_value_should_effect_immediately(self):
        result = self.twap_order_page.start_time_default()
        default_value = result[0]
        option_value = result[1]
        assert default_value
        assert "false", option_value

    def test_56_start_time_default_value_and_order_should_success(self):
        order_detail_start_time = self.twap_order_page.start_time_default_value_and_order()
        assert "立刻下单", order_detail_start_time
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_57_start_time_radio_and_order_should_success(self):
        result = self.twap_order_page.start_time_radio_and_order()
        start_time = result[0]
        order_detail_start_time = result[1]
        assert start_time, order_detail_start_time
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_58_change_start_time_radio_and_start_time_should_click_time(self):
        result = self.twap_order_page.change_start_time_radio()
        default_checked = result[0]
        option_checked = result[1]
        click_time = result[2]
        start_time_value = result[3]
        start_time_enabled = result[4]
        assert default_checked
        assert option_checked
        assert start_time_enabled
        assert click_time, start_time_value

    def test_59_end_time_default_value_should_always_execute(self):
        result = self.twap_order_page.end_time_default()
        default_value = result[0]
        option_value = result[1]
        assert default_value
        assert option_value

    def test_60_change_end_time_radio_and_end_time_should_click_time(self):
        result = self.twap_order_page.change_end_time_radio()
        default_checked = result[0]
        option_checked = result[1]
        click_time = result[2]
        end_time_value = result[3]
        end_time_enabled = result[4]
        assert default_checked
        assert option_checked
        assert end_time_enabled
        assert click_time, end_time_value

    def test_61_change_end_time_radio_and_now_time_and_order_should_fail(self):
        result = self.twap_order_page.end_time_radio_and_order()
        end_time = result[0]
        order_detail_end_time = result[1]
        assert end_time, order_detail_end_time
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_end_time)
        assert result

    def test_62_cancel_limit_default_should_closed(self):
        result = self.twap_order_page.cancel_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        assert switch_checked
        assert switch_text_enabled

    def test_63_open_cancel_limit_default_should_closed(self):
        result = self.twap_order_page.open_cancel_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        assert switch_checked
        assert switch_text_enabled

    def test_64_open_cancel_limit_and_text_none_should_fail(self):
        self.twap_order_page.input_cancel_limit_text("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_cancel_limit)
        assert result

    def test_65_open_cancel_limit_and_text_value_illegal_should_fail(self):
        cancel_limit_value = self.twap_order_page.input_cancel_limit_text("-/*+.")
        assert "-/*+.", cancel_limit_value
        assert "1", cancel_limit_value

    def test_66_open_cancel_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_cancel_limit_text_and_order("10")
        cancel_limit_value = result[0]
        order_detail_cancel_limit_text = result[1]
        assert "10", cancel_limit_value
        assert "10", order_detail_cancel_limit_text
        order_message = self.twap_order_page.alert_order_details_message()
        assert order_message, AlertError.alert_order_message

    def test_67_price_limit_default_should_closed(self):
        result = self.twap_order_page.price_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        assert switch_checked
        assert switch_text_enabled

    def test_68_open_price_limit_default_should_closed(self):
        result = self.twap_order_page.open_price_limit()
        switch_checked = result[0]
        switch_text_enabled = result[1]
        assert switch_checked
        assert switch_text_enabled

    def test_69_open_price_limit_and_text_none_should_fail(self):
        self.twap_order_page.input_price_limit_text("")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_message_price_limit)
        assert result

    def test_70_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text("-")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        assert result

    def test_71_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text("+")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        assert result

    def test_72_open_price_limit_and_text_value_illegal_should_fail(self):
        self.twap_order_page.input_price_limit_text(".")
        result = self.twap_order_page.is_toast_exist(AlertError.alert_illegal_price_limit)
        assert result

    def test_73_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("10")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        assert "10", price_limit_value
        assert "10", order_detail_price_limit_text
        alert_message_title = self.twap_order_page.alert_order_details_title()
        assert alert_message_title, AlertError.alert_order_message_title

    def test_74_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("-10")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        assert "-10", price_limit_value
        assert "-10", order_detail_price_limit_text
        alert_message_title = self.twap_order_page.alert_order_details_title()
        assert alert_message_title, AlertError.alert_order_message_title

    def test_75_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("0")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        assert "0", price_limit_value
        assert "0", order_detail_price_limit_text
        alert_message_title = self.twap_order_page.alert_order_details_title()
        assert alert_message_title, AlertError.alert_order_message_title

    def test_76_open_price_limit_and_text_value_legal_should_success(self):
        result = self.twap_order_page.input_price_limit_text_and_order("12345678.12345678")
        price_limit_value = result[0]
        order_detail_price_limit_text = result[1]
        assert "12345678.12345678", price_limit_value
        assert "12345678.12345678", order_detail_price_limit_text
        alert_message_title = self.twap_order_page.alert_order_details_title()
        assert alert_message_title, AlertError.alert_order_message_title

    def test_77_offset_flag_auto_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_top()  # 让权限合约TCU1907-SH排在合约列表的第一位来进行
        result = self.twap_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_default_value, '自动'
        assert offset_flag_default_value, order_details_offset_flag_value

    def test_78_offset_flag_open_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_79_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '平仓-平今-开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_80_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '平今-平仓-开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_81_offset_flag_C_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '平仓-开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_82_offset_flag_CT_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '平今-开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_83_offset_flag_CY_O_and_order_should_success(self):
        result = self.twap_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert offset_flag_value, '平昨-开仓'
        assert offset_flag_value, order_details_offset_flag_value

    def test_84_hedge_flag_speculation_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert hedge_flag_default_value, '投机'
        assert hedge_flag_default_value, order_details_hedge_flag_value

    def test_85_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert hedge_flag_value, '套利'
        assert hedge_flag_value, order_details_hedge_flag_value

    def test_86_hedge_flag_hedge_and_order_should_success(self):
        result = self.twap_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.twap_order_page.alert_order_details_title()
        assert order_message, AlertError.alert_order_message_title
        assert hedge_flag_value, '套保'
        assert hedge_flag_value, order_details_hedge_flag_value

    def test_87_edit_memo_and_order_should_success(self):
        self.twap_order_page.permission_contract_to_bottom()  # 权限合约排到最底部，主合约排到第一位
        result = self.twap_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.twap_order_page.alert_order_details_message()
        # assert order_message, AlertError.alert_order_message
        assert hint, AlertError.hint_message
        assert memo_value, order_details_memo_value


if __name__ == '__main__':
    pytest.main()
