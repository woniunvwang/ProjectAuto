import pytest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.timing_order_page import TimingOrderPage


class TestCaseTimingOrder:

    def setup_method(self) -> None:
        self.driver = android_driver()
        self.timing_order_page = TimingOrderPage(self.driver)
        self.timing_order_page.login_successful()

    def teardown_method(self) -> None:
        self.driver.quit()

    # 涔板崠鐩樺強娑ㄨ穼骞呮湁鏁版嵁鏃舵牴鎹氦鏄撴柟鍚戠浉鍙嶆暟鎹～鍏�
    def test_01_press_bid_and_side_should_sell(self):
        result = self.timing_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_message_succeed)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("鍗�" == order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.timing_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(bid_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.timing_order_page.press_bid_and_check_price()
        bid_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(bid_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_04_press_offer_and_side_should_sell(self):
        result = self.timing_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_message_succeed)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("涔�" == order_details_side_value)

    def test_05_press_offer_and_lots_should_offer_value(self):
        result = self.timing_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(offer_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_06_press_offer_and_price_should_offer_value(self):
        result = self.timing_order_page.press_offer_and_check_price()
        offer_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(offer_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_07_press_chg_and_side_should_buy(self):
        result = self.timing_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_message_succeed)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("涔�" == order_details_side_value)

    def test_08_press_chg_and_lots_should_last_lots_value(self):
        result = self.timing_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(last_lots == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_09_press_chg_and_price_should_last_price_value(self):
        result = self.timing_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(last_price == price_value)
        assert(price_value == order_details_price_value)

    # 涔板崠鐩樺強娑ㄨ穼骞呮病鏈夋暟鎹椂鎵嬫暟鍜屼环鏍兼寜鐓�"1"锛�"0"濉厖銆�
    def test_10_press_no_data_bid_and_lots_should_fix_num(self):
        self.timing_order_page.no_data_contract_to_top()  # 璁㏕2209-CF鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜娌℃湁鏁版嵁鏃剁殑娴嬭瘯
        result = self.timing_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_11_press_no_data_bid_and_price_should_fix_num(self):
        result = self.timing_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_12_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.timing_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_13_press_no_data_offer_and_price_should_fix_num(self):
        result = self.timing_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_14_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.timing_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_15_press_no_data_chg_and_price_should_fix_num(self):
        result = self.timing_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_16_change_trade_account_should_success(self):
        self.timing_order_page.main_contract_to_top()  # 娌℃湁鏁版嵁鏃剁殑娴嬭瘯缁撴潫锛岃涓绘祴璇曞悎绾C2212-CME鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜
        result = self.timing_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        assert(trade_account_value == changed_trade_account_value)
        assert(changed_trade_account_value == order_details_account_value)

    def test_17_change_side_should_success(self):
        result = self.timing_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_message_succeed)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("鍗�" == order_details_side_value)

    def test_18_clear_lots_and_order_should_fail(self):
        self.timing_order_page.clear_lots_and_order()
        result = self.timing_order_page.is_toast_exist(AlertError.alert_message_lots)
        assert(True == result)

    def test_19_input_illegal_lots_and_order_should_fail(self):
        self.timing_order_page.input_illegal_lots_and_order("1.")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        assert(True == result)

    def test_20_clear_price_and_order_should_fail(self):
        self.timing_order_page.clear_price_and_order()
        result = self.timing_order_page.is_toast_exist(AlertError.alert_message_price)
        assert(True == result)

    def test_21_input_illegal_price_and_order_should_fail(self):
        self.timing_order_page.input_illegal_price_and_order(".")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert(True == result)

    def test_22_input_illegal_price_and_order_should_fail(self):
        self.timing_order_page.input_illegal_price_and_order("+")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert(True == result)

    def test_23_input_illegal_price_and_order_should_fail(self):
        self.timing_order_page.input_illegal_price_and_order("-")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert(True == result)

    # 浠峰樊涓�0.1
    def test_24_input_illegal_price_and_order_should_fail(self):
        self.timing_order_page.input_illegal_price_and_order("100.00001")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_price_tick_size)
        assert(True == result)

    def test_25_input_legal_lots_and_price_and_order_should_success(self):
        result = self.timing_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_message_succeed)
        assert(order_details_lots_value == "10")
        assert(order_details_price_value == "80")

    def test_26_single_default_value_should_fix_value(self):
        single_value = self.timing_order_page.single_default()
        assert("1" == single_value)

    def test_27_clear_single_value_and_order_should_fail(self):
        self.timing_order_page.input_single_value("")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_message_single)
        assert result

    def test_28_clear_single_value_and_order_should_fail(self):
        self.timing_order_page.input_single_value("")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_message_single)
        assert result

    def test_29_input_illegal_single_value_and_order_should_fail(self):
        single_value = self.timing_order_page.input_single_value("+.-0")
        assert "+.-" != single_value
        assert("1" == single_value)

    def test_30_input_single_value_above_lots_and_order_should_fail(self):
        self.timing_order_page.input_single_value_and_lots("10", "5")
        result = self.timing_order_page.is_toast_exist(AlertError.alert_message_single_and_lots)
        assert result

    def test_31_input_single_value_equal_lots_and_order_should_success(self):
        order_detail_single_value = self.timing_order_page.input_single_value_and_lots_and_order("10", "10")
        assert("10" == order_detail_single_value)
        order_message = self.timing_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)

    def test_32_input_single_value_below_lots_and_order_should_success(self):
        order_detail_single_value = self.timing_order_page.input_single_value_and_lots_and_order("10", "20")
        assert("10" == order_detail_single_value)
        order_message = self.timing_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)

    def test_33_type_default_value_and_order_should_success(self):
        result = self.timing_order_page.type_default_value_and_order()
        type_value = result[0]
        default_clicked = result[1]
        order_detail_type_value = result[2]
        assert default_clicked
        assert(type_value == order_detail_type_value)

    def test_34_start_time_default_value_and_order_should_success(self):
        result = self.timing_order_page.start_time_default_value_and_order()
        click_time = result[0]
        start_time = result[1]
        order_detail_start_time = result[2]
        assert(click_time == start_time)
        assert(start_time == order_detail_start_time)
        order_message = self.timing_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)

    def test_35_end_time_default_value_and_order_should_fail(self):
        result = self.timing_order_page.end_time_default_value()
        click_time = result[0]
        end_time_value = result[1]
        assert(click_time == end_time_value)
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_end_time)
        assert result

    def test_36_change_end_time_after_current_year_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(150)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_37_change_end_time_after_current_month_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(300)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_38_change_end_time_after_current_day_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(450)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_39_change_end_time_after_current_hour_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(630)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_40_change_end_time_after_current_minute_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(780)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_41_change_end_time_after_current_second_and_order_should_success(self):
        result = self.timing_order_page.change_end_time_after_now_and_order(920)
        end_time_value = result[0]
        end_time_title = result[1]
        changed_end_time_value = result[2]+"(GTM+8)"
        order_detail_end_time = result[3]
        assert(end_time_value == end_time_title)
        assert(changed_end_time_value == order_detail_end_time)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_42_time_interval_default_value_and_order_should_fail(self):
        time_interval_value = self.timing_order_page.time_interval_default_value()
        assert("0 鏃� 0 鍒� 0 绉�" == time_interval_value)
        result = self.timing_order_page.is_toast_exist(AlertError.alert_illegal_time_interval)
        assert result

    def test_43_change_time_interval_after_current_hour_and_order_should_success(self):
        result = self.timing_order_page.change_time_interval_value_and_order(410)
        changed_time_interval_value = result[0].replace(" " == "")
        order_detail_time_interval_value = result[1].replace(" " == "")
        assert(changed_time_interval_value == order_detail_time_interval_value)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_44_change_time_interval_after_current_minute_and_order_should_success(self):
        result = self.timing_order_page.change_time_interval_value_and_order(560)
        changed_time_interval_value = result[0].replace(" " == "")
        order_detail_time_interval_value = result[1].replace(" " == "")
        assert(changed_time_interval_value == order_detail_time_interval_value)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_45_change_time_interval_after_current_second_and_order_should_success(self):
        result = self.timing_order_page.change_time_interval_value_and_order(705)
        changed_time_interval_value = result[0].replace(" " == "")
        order_detail_time_interval_value = result[1].replace(" " == "")
        assert(changed_time_interval_value == order_detail_time_interval_value)
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)

    def test_46_offset_flag_auto_and_order_should_success(self):
        self.timing_order_page.permission_contract_to_top()  # 璁╂潈闄愬悎绾CU1907-SH鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜
        result = self.timing_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_default_value == '鑷姩')
        assert(offset_flag_default_value == order_details_offset_flag_value)

    def test_47_offset_flag_open_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_48_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粨-骞充粖-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_49_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粖-骞充粨-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_50_offset_flag_C_O_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粨-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_51_offset_flag_CT_O_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粖-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_52_offset_flag_CY_O_and_order_should_success(self):
        result = self.timing_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞虫槰-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_53_hedge_flag_speculation_and_order_should_success(self):
        result = self.timing_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_default_value == '鎶曟満')
        assert(hedge_flag_default_value == order_details_hedge_flag_value)

    def test_54_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.timing_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '濂楀埄')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_55_hedge_flag_hedge_and_order_should_success(self):
        result = self.timing_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.timing_order_page.alert_order_details_title()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '濂椾繚')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_56_edit_memo_and_order_should_success(self):
        self.timing_order_page.permission_contract_to_bottom()  # 鏉冮檺鍚堢害鎺掑埌鏈�搴曢儴锛屼富鍚堢害鎺掑埌绗竴浣�
        result = self.timing_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.timing_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_order_message)
        assert(hint == AlertError.hint_message)
        assert(memo_value == order_details_memo_value)


if __name__ == '__main__':
    pytest.main()
