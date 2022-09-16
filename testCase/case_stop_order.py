import time
import unittest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.stop_order_page import StopOrderPage


class CaseStopOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.stop_order_page = StopOrderPage(self.driver)
        self.stop_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        self.stop_order_page.press_bid()
        isSellChecked = self.stop_order_page.is_side_sell_checked()
        isBuyChecked = self.stop_order_page.is_side_buy_checked()
        self.assertEqual("true", isSellChecked)
        self.assertEqual("false", isBuyChecked)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.stop_order_page.press_bid_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.stop_order_page.press_bid_and_check_price()
        self.assertEqual(result[0], result[1])

    def test_04_press_offer_and_side_should_buy(self):
        self.stop_order_page.press_offer()
        isBuyChecked = self.stop_order_page.is_side_buy_checked()
        isSellChecked = self.stop_order_page.is_side_sell_checked()
        self.assertEqual("true", isBuyChecked)
        self.assertEqual("false", isSellChecked)

    def test_05_press_offer_and_lots_should_offer_value(self):
        result = self.stop_order_page.press_offer_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_06_press_offer_and_price_should_offer_value(self):
        result = self.stop_order_page.press_offer_and_check_price()
        self.assertEqual(result[0], result[1])

    def test_07_press_chg_and_side_should_buy(self):
        self.stop_order_page.slide_and_press_chg()
        isBuyChecked = self.stop_order_page.is_side_buy_checked()
        isSellChecked = self.stop_order_page.is_side_sell_checked()
        self.assertEqual("true", isBuyChecked)
        self.assertEqual("false", isSellChecked)

    def test_08_press_chg_and_lots_should_last_lots_value(self):
        result = self.stop_order_page.press_chg_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_09_press_chg_and_price_should_last_price_value(self):
        result = self.stop_order_page.press_chg_and_check_price()
        self.assertEqual(result[0], result[1])

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_10_press_no_data_bid_and_lots_should_fix_num(self):
        # 合约T2209-CF在第二个的时候执行代码
        self.stop_order_page.drag_first_contract_to_second_location()
        result = self.stop_order_page.press_bid_and_check_lots()
        self.assertEqual(result, "1")

    def test_11_press_no_data_bid_and_price_should_fix_num(self):
        result = self.stop_order_page.press_bid_and_check_price()
        self.assertEqual(result, "0")

    def test_12_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.stop_order_page.press_offer_and_check_lots()
        self.assertEqual(result, "1")

    def test_13_press_no_data_offer_and_price_should_fix_num(self):
        result = self.stop_order_page.press_offer_and_check_price()
        self.assertEqual(result, "0")

    def test_14_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.stop_order_page.press_chg_and_check_lots()
        self.assertEqual(result, "1")

    def test_15_press_no_data_chg_and_price_should_fix_num(self):
        result = self.stop_order_page.press_chg_and_check_price()
        self.assertEqual(result, "0")

    def test_16_no_change_and_order_should_success(self):
        self.stop_order_page.drag_first_contract_to_second_location()
        self.stop_order_page.press_bid()
        time.sleep(1)
        self.stop_order_page.press_confirm_button()
        self.stop_order_page.press_confirm_button()
        time.sleep(1)
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_17_change_trade_account_should_success(self):
        result = self.stop_order_page.change_trade_account()
        self.assertEqual(result[0], result[1])

    def test_18_change_side_should_success(self):
        self.stop_order_page.change_buy_side()
        isSellChecked = self.stop_order_page.is_side_sell_checked()
        isBuyChecked = self.stop_order_page.is_side_buy_checked()
        self.assertEqual("true", isSellChecked)
        self.assertEqual("false", isBuyChecked)

    def test_19_clear_lots_and_order_should_fail(self):
        self.stop_order_page.clear_lots_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertEqual(True, result)

    def test_20_input_illegal_lots_and_order_should_fail(self):
        self.stop_order_page.input_illegal_lots_and_order("1.")
        result = self.stop_order_page.alert_illegal_lots_title()
        self.assertEqual(result, AlertError.illegal_lots)

    def test_21_clear_price_and_order_should_fail(self):
        self.stop_order_page.clear_price_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_price)
        self.assertEqual(True, result)

    def test_22_input_illegal_price1_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order(".")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_23_input_illegal_price2_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order("+")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_24_input_illegal_price3_and_order_should_fail(self):
        self.stop_order_page.input_illegal_price_and_order("-")
        result = self.stop_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_25_input_lots_and_price_and_order_should_success(self):
        self.stop_order_page.input_lots_and_price_and_order(1, 80)
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_26_changed_Market_type_and_price_should_Market(self):
        self.stop_order_page.change_type_market()
        result = self.stop_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_27_changed_Market_type_and_order_should_success(self):
        self.stop_order_page.Market_type_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_28_changed_Market_Limit_type_and_price_should_Market(self):
        self.stop_order_page.change_type_market_Limit()
        result = self.stop_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_29_changed_Market_Limit_type_and_order_should_success(self):
        self.stop_order_page.Market_Limit_type_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_30_buy_side_and_Market_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.stop_order_page.Market_type_changed_LIM_type()
        self.assertEqual(result[0], result[1])

    def test_31_changed_stp_type_and_price_should_Market(self):
        self.stop_order_page.change_type_stp()
        result = self.stop_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_32_changed_stp_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.stop_order_page.change_type_stp()
        self.assertEqual(result[0], result[1])

    def test_33_stp_type_clear_StPx_and_order_should_fail(self):
        self.stop_order_page.stp_clear_StPx_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_34_changed_stp_type_and_order_should_success(self):
        self.stop_order_page.stp_type_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_35_stp_type_and_buy_side_and_input_StPx_above_last_price_should_success(self):
        self.stop_order_page.stp_type_input_StPx_above_last_price_and_buy_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_36_stp_type_and_buy_side_and_input_StPx_below_last_price_should_fail(self):
        self.stop_order_page.stp_type_input_StPx_below_last_price_and_buy_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_37_stp_type_and_sell_side_and_input_StPx_above_last_price_should_fail(self):
        self.stop_order_page.stp_type_input_StPx_above_last_price_and_sell_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_38_stp_type_and_sell_side_and_input_StPx_below_last_price_should_success(self):
        self.stop_order_page.stp_type_input_StPx_below_last_price_and_sell_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_39_stl_type_and_buy_side_and_price_should_offer_value(self):
        result = self.stop_order_page.change_type_stl()
        self.assertEqual(result[0], result[2])

    def test_40_stl_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.stop_order_page.change_type_stl()
        self.assertEqual(result[0], result[1])

    def test_41_stl_type_and_clear_StPx_and_order_should_fail(self):
        self.stop_order_page.stl_clear_StPx_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_42_stl_type_and_buy_side_and_input_price_equal_StPx_above_last_price_should_success(self):
        self.stop_order_page.stl_type_input_StPx_above_last_price_and_buy_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_43_stl_type_and_buy_side_and_input_price_equal_StPx_below_last_price_should_fail(self):
        self.stop_order_page.stl_type_input_StPx_below_last_price_and_buy_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_44_stl_type_and_sell_side_and_input_price_equal_StPx_above_last_price_should_fail(self):
        self.stop_order_page.stl_type_input_StPx_above_last_price_and_sell_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_45_stl_type_and_sell_side_and_input_price_equal_StPx_below_last_price_should_success(self):
        self.stop_order_page.stl_type_input_StPx_below_last_price_and_sell_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_46_stl_type_and_buy_side_and_above_last_price_and_StPx_below_price_should_success(self):
        self.stop_order_page.stl_type_input_StPx_below_price_and_buy_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_47_stl_type_and_buy_side_and_above_last_price_and_StPx_above_price_should_fail(self):
        self.stop_order_page.stl_type_input_StPx_above_price_and_buy_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_buy_order_illegal_StPx)
        self.assertEqual(True, result)

    def test_48_stl_type_and_sell_side_and_above_last_price_and_StPx_below_price_should_fail(self):
        self.stop_order_page.stl_type_input_StPx_below_price_and_sell_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_sell_order_illegal_StPx)
        self.assertEqual(True, result)

    def test_49_stl_type_and_sell_side_and_above_last_price_and_StPx_above_price_should_success(self):
        self.stop_order_page.stl_type_input_StPx_above_price_and_sell_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_50_ice_type_and_chunk_size_should_fix_value(self):
        result = self.stop_order_page.change_type_ice()
        self.assertEqual("1", result)

    def test_51_ice_type_and_input_chunk_size_illegal_value_should_fix_value(self):
        result = self.stop_order_page.ice_type_and_input_chunk_size("0")
        self.assertEqual("1", result)

    def test_52_ice_type_and_input_chunk_size_less_than_lots_should_legal(self):
        result = self.stop_order_page.ice_type_and_input_lots_and_chunk_size("10", "5")
        self.assertEqual("10", result[0])
        self.assertEqual("5", result[1])

    def test_53_ice_type_and_input_chunk_size_equal_lots_should_legal(self):
        result = self.stop_order_page.ice_type_and_input_lots_and_chunk_size("5", "5")
        self.assertEqual("5", result[0])
        self.assertEqual("5", result[1])

    def test_54_ice_type_and_input_chunk_size_above_lots_should_lots_value(self):
        result = self.stop_order_page.ice_type_and_input_lots_and_chunk_size("5", "10")
        self.assertEqual("5", result[0])
        self.assertEqual("5", result[1])

    def test_55_ice_type_and_input_chunk_size_above_50_should_50(self):
        result = self.stop_order_page.ice_type_and_input_lots_and_chunk_size("51", "51")
        self.assertEqual("51", result[0])
        self.assertEqual("50", result[1])

    def test_56_ice_type_and_clear_chunk_size_and_order_should_fail(self):
        self.stop_order_page.ice_type_clear_chunk_size_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_chunk_size)
        self.assertEqual(True, result)

    def test_57_TIF_DAY_order_should_success(self):
        self.stop_order_page.tif_day_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_58_TIF_GTC_order_should_success(self):
        self.stop_order_page.tif_gtc_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_59_TIF_GTD_order_should_success(self):
        self.stop_order_page.tif_gtd_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_60_TIF_FAK_order_should_success(self):
        self.stop_order_page.tif_fak_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_61_TIF_FOK_order_should_success(self):
        self.stop_order_page.tif_fok_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_62_tif_fak_and_clear_min_quantity_and_order_should_fail(self):
        self.stop_order_page.tif_fak_and_clear_min_quantity_and_order()
        result = self.stop_order_page.is_toast_exist(AlertError.alert_message_min_quantity)
        self.assertEqual(True, result)

    def test_63_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.stop_order_page.tif_fak_and_input_illegal_min_quantity(0)
        self.assertEqual(fak_min_quantity, '1')

    def test_64_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.stop_order_page.tif_fak_and_input_illegal_min_quantity(-1)
        self.assertEqual(fak_min_quantity, '1')

    def test_65_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.stop_order_page.tif_fak_and_input_illegal_min_quantity("+")
        self.assertEqual(fak_min_quantity, '1')

    def test_66_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.stop_order_page.tif_fak_and_input_illegal_min_quantity("-")
        self.assertEqual(fak_min_quantity, '1')

    def test_67_tif_fak_and_input_min_quantity_below_lots_and_order_should_success(self):
        self.stop_order_page.tif_fak_and_input_min_quantity_and_lots(3, 4)
        self.stop_order_page.press_confirm_button()
        self.stop_order_page.press_confirm_button()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_68_tif_fak_and_input_min_quantity_equal_lots_and_order_should_success(self):
        self.stop_order_page.tif_fak_and_input_min_quantity_and_lots(3, 3)
        self.stop_order_page.press_confirm_button()
        self.stop_order_page.press_confirm_button()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_69_tif_fak_and_input_min_quantity_above_lots_and_min_quantity_should_lots_value(self):
        fak_min_quantity = self.stop_order_page.tif_fak_and_input_min_quantity_and_lots(4, 3)
        self.assertEqual(fak_min_quantity, '3')

    # 让有开平投保标志的合约TCU1907-SH排在第一位
    def test_70_offset_flag_auto_and_order_should_success(self):
        offset_flag_default_value = self.stop_order_page.offset_flag_auto_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)
        self.assertEqual(offset_flag_default_value, '自动')

    def test_71_offset_flag_open_and_order_should_success(self):
        self.stop_order_page.offset_flag_open_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_72_offset_flag_close_and_order_should_success(self):
        self.stop_order_page.offset_flag_close_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_73_offset_flag_closeYesterday_and_order_should_success(self):
        self.stop_order_page.offset_flag_closeYesterday_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_74_offset_flag_closeToday_and_order_should_success(self):
        self.stop_order_page.offset_flag_closeToday_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_75_offset_flag_C_CT_O_and_order_should_success(self):
        self.stop_order_page.offset_flag_C_CT_O_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_76_offset_flag_CT_C_O_and_order_should_success(self):
        self.stop_order_page.offset_flag_CT_C_O_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_77_offset_flag_C_O_and_order_should_success(self):
        self.stop_order_page.offset_flag_C_O_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_78_offset_flag_CT_O_and_order_should_success(self):
        self.stop_order_page.offset_flag_CT_O_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_79_offset_flag_CY_O_and_order_should_success(self):
        self.stop_order_page.offset_flag_CY_O_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_80_hedge_flag_speculation_and_order_should_success(self):
        offset_flag_default_value = self.stop_order_page.hedge_flag_speculation_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)
        self.assertEqual(offset_flag_default_value, '投机')

    def test_81_hedge_flag_arbitrage_and_order_should_success(self):
        self.stop_order_page.hedge_flag_arbitrage_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_82_hedge_flag_hedge_and_order_should_success(self):
        self.stop_order_page.hedge_flag_hedge_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_83_change_T_switch_and_order_should_success(self):
        self.stop_order_page.change_T_switch_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_84_edit_memo_and_order_should_success(self):
        hint = self.stop_order_page.edit_memo_and_order()
        result = self.stop_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)
        self.assertEqual(hint[0], AlertError.hint_message)
        self.assertEqual(hint[1], hint[2])


if __name__ == '__main__':
    unittest.main()
