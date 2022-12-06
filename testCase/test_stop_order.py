import pytest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.stop_order_page import StopOrderPage


class TestCaseStopOrder:

    def setup_method(self) -> None:
        self.driver = android_driver()
        self.stop_order_page = StopOrderPage(self.driver)
        self.stop_order_page.login_successful()

    def teardown_method(self) -> None:
        self.driver.quit()

    # 涔板崠鐩樺強娑ㄨ穼骞呮湁鏁版嵁鏃舵牴鎹氦鏄撴柟鍚戠浉鍙嶆暟鎹～鍏�
    def test_01_press_bid_and_side_should_sell(self):
        result = self.stop_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("鍗�" == order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.stop_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(bid_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.stop_order_page.press_bid_and_check_price()
        bid_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(bid_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_04_press_bid_and_stop_price_should_offer_value(self):
        result = self.stop_order_page.press_bid_and_check_stop_price()
        offer_value = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        assert(offer_value == stop_price_value)
        assert(stop_price_value == order_details_stop_price_value)

    def test_05_press_offer_and_side_should_sell(self):
        result = self.stop_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("涔�" == order_details_side_value)

    def test_06_press_offer_and_lots_should_offer_value(self):
        result = self.stop_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(offer_lots_value == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_07_press_offer_and_price_should_offer_value(self):
        result = self.stop_order_page.press_offer_and_check_price()
        offer_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(offer_price_value == price_value)
        assert(price_value == order_details_price_value)

    def test_08_press_offer_and_stop_price_should_bid_value(self):
        result = self.stop_order_page.press_offer_and_check_stop_price()
        bid_value = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        assert(bid_value == stop_price_value)
        assert(stop_price_value == order_details_stop_price_value)

    def test_09_press_chg_and_side_should_buy(self):
        result = self.stop_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("true" == buy_checkbox)
        assert("false" == sell_checkbox)
        assert("涔�" == order_details_side_value)

    def test_10_press_chg_and_lots_should_last_lots_value(self):
        result = self.stop_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        assert(last_lots == lots_value)
        assert(lots_value == order_details_lots_value)

    def test_11_press_chg_and_price_should_last_price_value(self):
        result = self.stop_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        assert(last_price == price_value)
        assert(price_value == order_details_price_value)

    def test_12_press_chg_and_stop_price_should_last_price_value(self):
        result = self.stop_order_page.press_chg_and_check_stop_price()
        last_price = result[0]
        stop_price_value = result[1]
        order_details_stop_price_value = result[2]
        assert(last_price == stop_price_value)
        assert(stop_price_value == order_details_stop_price_value)

    # 涔板崠鐩樺強娑ㄨ穼骞呮病鏈夋暟鎹椂鎵嬫暟鍜屼环鏍兼寜鐓�"1"锛�"0"濉厖銆�
    def test_13_press_no_data_bid_and_lots_should_fix_num(self):
        self.stop_order_page.no_data_contract_to_top()  # 璁㏕2209-CF鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜娌℃湁鏁版嵁鏃剁殑娴嬭瘯
        result = self.stop_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_14_press_no_data_bid_and_price_should_fix_num(self):
        result = self.stop_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_15_press_bid_and_offer_no_data_and_stop_price_should_fix_num(self):
        result = self.stop_order_page.press_bid_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        assert(stop_price_value == "0")
        assert(stop_price_value == order_details_stop_price_value)

    def test_16_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.stop_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_17_press_no_data_offer_and_price_should_fix_num(self):
        result = self.stop_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_18_press_offer_and_bid_no_data_and_stop_price_should_fix_num(self):
        result = self.stop_order_page.press_offer_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        assert(stop_price_value == "0")
        assert(stop_price_value == order_details_stop_price_value)

    def test_19_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.stop_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        assert(lots_value == "1")
        assert(lots_value == order_details_lots_value)

    def test_20_press_no_data_chg_and_price_should_fix_num(self):
        result = self.stop_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        assert(price_value == "0")
        assert(price_value == order_details_price_value)

    def test_21_press_no_data_chg_and_stop_price_should_fix_num(self):
        result = self.stop_order_page.press_chg_and_check_stop_price()
        stop_price_value = result[0]
        order_details_stop_price_value = result[1]
        assert(stop_price_value == "0")
        assert(stop_price_value == order_details_stop_price_value)

    def test_22_change_trade_account_should_success(self):
        self.stop_order_page.main_contract_to_top()  # 娌℃湁鏁版嵁鏃剁殑娴嬭瘯缁撴潫锛岃涓绘祴璇曞悎绾C2212-CME鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜
        result = self.stop_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        assert(trade_account_value == changed_trade_account_value)
        assert(changed_trade_account_value == order_details_account_value)

    def test_23_change_side_should_success(self):
        result = self.stop_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert("false" == buy_checkbox)
        assert("true" == sell_checkbox)
        assert("鍗�" == order_details_side_value)

    def test_24_clear_lots_and_order_should_fail(self):
        self.stop_order_page.clear_lots_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_lots)
        assert result

    def test_25_input_illegal_lots_and_order_should_fail(self):
        self.stop_order_page.input_illegal_lots_and_order("1.")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_lots)
        assert result

    def test_26_clear_price_and_order_should_fail(self):
        self.stop_order_page.clear_price_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_price)
        assert result

    def test_27_input_illegal_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order(".")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    def test_28_input_illegal_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order("+")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    def test_29_input_illegal_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order("-")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        assert result

    # 浠峰樊涓�0.1
    def test_30_input_illegal_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order("0.00001")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_order_price_tick_size)
        assert result

    def test_31_clear_stop_price_and_order_should_fail(self):
        self.stop_order_page.clear_stop_price_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_stop_price)
        assert result

    def test_32_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_stop_price_and_order(".")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        assert result

    def test_33_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_stop_price_and_order("+")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        assert result

    def test_34_input_illegal_stop_price_and_order_should_fail(self):
        self.stop_order_page.input_illegal_stop_price_and_order("-")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_stop_price)
        assert result

    def test_36_input_legal_lots_and_price_and_order_should_success(self):
        result = self.stop_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert(order_details_lots_value == "10")
        assert(order_details_price_value == "80")

    # 璁╂湁寮�骞虫姇淇濇爣蹇楃殑鍚堢害TCU1907-SH鎺掑湪绗竴浣�
    def test_37_stop_option_last_trade_price_and_order_should_success(self):
        result = self.stop_order_page.stop_option_last_trade_price_and_order()
        stop_option_default_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_order_page.alert_order_details_message()
        assert(order_message == AlertError.alert_order_message)
        assert(stop_option_default_value == '鏈�鍚庢垚浜や环')
        assert(stop_option_default_value == order_details_stop_option_value)

    def test_38_stop_option_market_buy_price_and_order_should_success(self):
        result = self.stop_order_page.stop_option_market_buy_price_and_order()
        stop_option_market_buy_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(stop_option_market_buy_value == '甯傚満涔颁环')
        assert(stop_option_market_buy_value == order_details_stop_option_value)

    def test_39_stop_option_market_sell_price_and_order_should_success(self):
        result = self.stop_order_page.stop_option_market_sell_price_and_order()
        stop_option_market_sell_value = result[0]
        order_details_stop_option_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(stop_option_market_sell_value == '甯傚満鍗栦环')
        assert(stop_option_market_sell_value == order_details_stop_option_value)

    def test_40_offset_flag_auto_and_order_should_success(self):
        self.stop_order_page.permission_contract_to_top()  # 璁╂潈闄愬悎绾CU1907-SH鎺掑湪鍚堢害鍒楄〃鐨勭涓�浣嶆潵杩涜
        result = self.stop_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_default_value == '鑷姩')
        assert(offset_flag_default_value == order_details_offset_flag_value)

    def test_41_offset_flag_open_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_42_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粨-骞充粖-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_43_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粖-骞充粨-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_44_offset_flag_C_O_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粨-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_45_offset_flag_CT_O_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞充粖-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_46_offset_flag_CY_O_and_order_should_success(self):
        result = self.stop_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(offset_flag_value == '骞虫槰-寮�浠�')
        assert(offset_flag_value == order_details_offset_flag_value)

    def test_47_hedge_flag_speculation_and_order_should_success(self):
        result = self.stop_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_default_value == '鎶曟満')
        assert(hedge_flag_default_value == order_details_hedge_flag_value)

    def test_48_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.stop_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '濂楀埄')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_49_hedge_flag_hedge_and_order_should_success(self):
        result = self.stop_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.stop_order_page.alert_title_send_order_successfully()
        assert(order_message == AlertError.alert_order_message_title)
        assert(hedge_flag_value == '濂椾繚')
        assert(hedge_flag_value == order_details_hedge_flag_value)

    def test_50_edit_memo_and_order_should_success(self):
        self.stop_order_page.permission_contract_to_bottom()  # 鏉冮檺鍚堢害鎺掑埌鏈�搴曢儴锛屼富鍚堢害鎺掑埌绗竴浣�
        result = self.stop_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.stop_order_page.alert_order_details_message()
        # assert(order_message == AlertError.alert_order_message)
        assert(hint == AlertError.hint_message)
        assert(memo_value == order_details_memo_value)


if __name__ == '__main__':
    pytest.main()
