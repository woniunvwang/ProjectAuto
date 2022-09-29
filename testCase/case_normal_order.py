import time
import unittest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.normal_order_page import NormalOrderPage


class CaseNormalOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.normal_order_page = NormalOrderPage(self.driver)
        self.normal_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        result = self.normal_order_page.press_bid_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_02_press_bid_and_lots_should_bid_value(self):
        result = self.normal_order_page.press_bid_and_check_lots()
        bid_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(bid_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_03_press_bid_and_price_should_bid_value(self):
        result = self.normal_order_page.press_bid_and_check_price()
        bid_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(bid_price_value, price_value)
        self.assertEqual(price_value, order_details_price_value)

    def test_04_press_offer_and_side_should_sell(self):
        result = self.normal_order_page.press_offer_and_order()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_05_press_offer_and_lots_should_offer_value(self):
        result = self.normal_order_page.press_offer_and_check_lots()
        offer_lots_value = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(offer_lots_value, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_06_press_offer_and_price_should_offer_value(self):
        result = self.normal_order_page.press_offer_and_check_price()
        offer_price_value = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(offer_price_value, price_value)
        self.assertEqual(price_value, order_details_price_value)

    def test_07_press_chg_and_side_should_buy(self):
        result = self.normal_order_page.slide_and_press_chg()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("true", buy_checkbox)
        self.assertEqual("false", sell_checkbox)
        self.assertEqual("买", order_details_side_value)

    def test_08_press_chg_and_lots_should_last_lots_value(self):
        result = self.normal_order_page.press_chg_and_check_lots()
        last_lots = result[0]
        lots_value = result[1]
        order_details_lots_value = result[2]
        self.assertEqual(last_lots, lots_value)
        self.assertEqual(lots_value, order_details_lots_value)

    def test_09_press_chg_and_price_should_last_price_value(self):
        result = self.normal_order_page.press_chg_and_check_price()
        last_price = result[0]
        price_value = result[1]
        order_details_price_value = result[2]
        self.assertEqual(last_price, price_value)
        self.assertEqual(price_value, order_details_price_value)

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_10_press_no_data_bid_and_lots_should_fix_num(self):
        # 合约T2209-CF在第二个的时候执行代码
        self.normal_order_page.no_data_contract_to_top()
        time.sleep(10)
        self.normal_order_page.main_contract_to_top()
        time.sleep(10)
        self.normal_order_page.have_data_contract_to_top()

        result = self.normal_order_page.press_bid_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_11_press_no_data_bid_and_price_should_fix_num(self):
        result = self.normal_order_page.press_bid_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_12_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.normal_order_page.press_offer_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_13_press_no_data_offer_and_price_should_fix_num(self):
        result = self.normal_order_page.press_offer_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_14_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.normal_order_page.press_chg_and_check_lots()
        lots_value = result[0]
        order_details_lots_value = result[1]
        self.assertEqual(lots_value, "1")
        self.assertEqual(lots_value, order_details_lots_value)

    def test_15_press_no_data_chg_and_price_should_fix_num(self):
        result = self.normal_order_page.press_chg_and_check_price()
        price_value = result[0]
        order_details_price_value = result[1]
        self.assertEqual(price_value, "0")
        self.assertEqual(price_value, order_details_price_value)

    def test_16_change_trade_account_should_success(self):
        result = self.normal_order_page.change_trade_account()
        trade_account_value = result[0]
        changed_trade_account_value = result[1]
        order_details_account_value = result[2]
        self.assertEqual(trade_account_value, changed_trade_account_value)
        self.assertEqual(changed_trade_account_value, order_details_account_value)

    def test_17_change_side_should_success(self):
        result = self.normal_order_page.change_buy_side()
        buy_checkbox = result[0]
        sell_checkbox = result[1]
        order_details_side_value = result[2]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("false", buy_checkbox)
        self.assertEqual("true", sell_checkbox)
        self.assertEqual("卖", order_details_side_value)

    def test_18_clear_lots_and_order_should_fail(self):
        self.normal_order_page.clear_lots_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertEqual(True, result)

    def test_19_input_illegal_lots_and_order_should_fail(self):
        self.normal_order_page.input_illegal_lots_and_order("1.")
        result = self.normal_order_page.alert_illegal_lots_title()
        self.assertEqual(result, AlertError.illegal_lots)

    def test_20_clear_price_and_order_should_fail(self):
        self.normal_order_page.clear_price_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_price)
        self.assertEqual(True, result)

    def test_21_input_illegal_price_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order(".")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_22_input_illegal_price_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order("+")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_23_input_illegal_price_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order("-")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_24_input_illegal_price_tick_size_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order("0.0000001")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price_tick_size)
        self.assertEqual(True, result)

    def test_25_input_legal_lots_and_price_and_order_should_success(self):
        result = self.normal_order_page.input_lots_and_price_and_order(10, 80)
        order_details_lots_value = result[0]
        order_details_price_value = result[1]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(order_details_lots_value, "10")
        self.assertEqual(order_details_price_value, "80")

    def test_26_changed_Market_type_and_price_should_Market(self):
        result = self.normal_order_page.change_type_market()
        price_value = result[0]
        type_value = result[1]
        self.assertEqual(price_value, "Market")
        self.assertEqual(type_value, "Market")

    def test_27_changed_Market_type_and_order_should_success(self):
        result = self.normal_order_page.Market_type_and_order()
        order_details_type_value = result[0]
        order_details_price_value = result[1]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("Market", order_details_type_value)
        self.assertEqual("Market", order_details_price_value)

    def test_28_changed_Market_Limit_type_and_price_should_Market(self):
        result = self.normal_order_page.change_type_market_limit()
        price_value = result[0]
        type_value = result[1]
        self.assertEqual(price_value, "Market")
        self.assertEqual(type_value, "Market Limit")

    def test_29_changed_Market_Limit_type_and_order_should_success(self):
        result = self.normal_order_page.market_Limit_type_and_order()
        order_details_type_value = result[0]
        order_details_price_value = result[1]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual("Market Limit", order_details_type_value)
        self.assertEqual("Market", order_details_price_value)

    def test_30_buy_side_and_Market_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.normal_order_page.market_type_changed_lim_type()
        bid_price_value = result[0]
        price_value = result[1]
        type_value = result[2]
        self.assertEqual(bid_price_value, price_value)
        self.assertEqual("LIM", type_value)

    def test_31_buy_side_and_Market_Limit_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.normal_order_page.market_type_changed_lim_type()
        bid_price_value = result[0]
        price_value = result[1]
        type_value = result[2]
        self.assertEqual(bid_price_value, price_value)
        self.assertEqual("LIM", type_value)

    def test_32_changed_stp_type_and_price_should_Market(self):
        result = self.normal_order_page.change_type_stp()
        type_value = result[4]
        price_value = result[3]
        self.assertEqual(price_value, "Market")
        self.assertEqual(type_value, "STP")

    def test_33_changed_stp_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.normal_order_page.change_type_stp()
        offer_price_value = result[0]
        StPx_title = result[1]
        input_StPx = result[2]
        self.assertEqual("StPx", StPx_title)
        self.assertEqual(offer_price_value, input_StPx)

    def test_34_stp_type_clear_StPx_and_order_should_fail(self):
        self.normal_order_page.stp_clear_StPx_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_35_stp_type_and_buy_side_and_input_StPx_above_last_price_should_success(self):
        result = self.normal_order_page.stp_type_input_StPx_above_last_price_and_buy_order()
        stpx_value = result[0]
        order_details_stpx_value = result[1]
        order_details_price_value = result[2]
        order_details_type_value = result[3]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(stpx_value, order_details_stpx_value)
        self.assertEqual(order_details_price_value, "Market")
        self.assertEqual(order_details_type_value, "STP")

    def test_36_stp_type_and_buy_side_and_input_StPx_below_last_price_should_fail(self):
        self.normal_order_page.stp_type_input_StPx_below_last_price_and_buy_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_37_stp_type_and_sell_side_and_input_StPx_above_last_price_should_fail(self):
        self.normal_order_page.stp_type_input_StPx_above_last_price_and_sell_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_38_stp_type_and_sell_side_and_input_StPx_below_last_price_should_success(self):
        result = self.normal_order_page.stp_type_input_StPx_below_last_price_and_sell_order()
        stpx_value = result[0]
        order_details_stpx_value = result[1]
        order_details_price_value = result[2]
        order_details_type_value = result[3]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(stpx_value, order_details_stpx_value)
        self.assertEqual(order_details_price_value, "Market")
        self.assertEqual(order_details_type_value, "STP")

    def test_39_stl_type_and_buy_side_and_price_should_offer_value(self):
        result = self.normal_order_page.change_type_stl()
        offer_price_value = result[0]
        price_value = result[3]
        type_value = result[4]
        self.assertEqual(offer_price_value,  price_value)
        self.assertEqual(type_value, "STL")

    def test_40_stl_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.normal_order_page.change_type_stl()
        offer_price_value = result[0]
        StPx_title = result[1]
        StPx_value = result[2]
        self.assertEqual("StPx", StPx_title)
        self.assertEqual(offer_price_value, StPx_value)

    def test_41_stl_type_and_clear_StPx_and_order_should_fail(self):
        self.normal_order_page.stl_clear_StPx_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_42_stl_type_and_buy_side_and_input_price_equal_StPx_above_last_price_should_success(self):
        result = self.normal_order_page.stl_type_input_StPx_above_last_price_and_buy_order()
        StPx_value = result[0]
        price_value = result[1]
        order_details_stpx_value = result[2]
        order_details_price_value = result[3]
        order_details_type_value = result[4]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(StPx_value, price_value)
        self.assertEqual(StPx_value, order_details_stpx_value)
        self.assertEqual(price_value, order_details_price_value)
        self.assertEqual("STL", order_details_type_value)

    def test_43_stl_type_and_buy_side_and_input_price_equal_StPx_below_last_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_below_last_price_and_buy_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_44_stl_type_and_sell_side_and_input_price_equal_StPx_above_last_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_above_last_price_and_sell_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_45_stl_type_and_sell_side_and_input_price_equal_StPx_below_last_price_should_success(self):
        result = self.normal_order_page.stl_type_input_StPx_below_last_price_and_sell_order()
        StPx_value = result[0]
        price_value = result[1]
        order_details_stpx_value = result[2]
        order_details_price_value = result[3]
        order_details_type_value = result[4]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(StPx_value, price_value)
        self.assertEqual(StPx_value, order_details_stpx_value)
        self.assertEqual(price_value, order_details_price_value)
        self.assertEqual("STL", order_details_type_value)

    def test_46_stl_type_and_buy_side_and_above_last_price_and_StPx_below_price_should_success(self):
        result = self.normal_order_page.stl_type_input_StPx_below_price_and_buy_order()
        StPx_value = result[0]
        price_value = result[1]
        order_details_stpx_value = result[2]
        order_details_price_value = result[3]
        order_details_type_value = result[4]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertGreater(price_value, StPx_value)
        self.assertEqual(StPx_value, order_details_stpx_value)
        self.assertEqual(price_value, order_details_price_value)
        self.assertEqual("STL", order_details_type_value)

    def test_47_stl_type_and_buy_side_and_above_last_price_and_StPx_above_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_above_price_and_buy_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_buy_order_illegal_StPx)
        self.assertEqual(True, result)

    def test_48_stl_type_and_sell_side_and_above_last_price_and_StPx_below_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_below_price_and_sell_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_sell_order_illegal_StPx)
        self.assertEqual(True, result)

    def test_49_stl_type_and_sell_side_and_above_last_price_and_StPx_above_price_should_success(self):
        result = self.normal_order_page.stl_type_input_StPx_above_price_and_sell_order()
        StPx_value = result[0]
        price_value = result[1]
        order_details_stpx_value = result[2]
        order_details_price_value = result[3]
        order_details_type_value = result[4]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertGreater(StPx_value, price_value)
        self.assertEqual(StPx_value, order_details_stpx_value)
        self.assertEqual(price_value, order_details_price_value)
        self.assertEqual("STL", order_details_type_value)

    def test_50_ice_type_and_chunk_size_should_fix_value(self):
        result = self.normal_order_page.change_type_ice()
        chunk_size_value = result[0]
        chunk_size_title = result[1]
        price_value = result[2]
        offer_price_value = result[3]
        type_value = result[4]
        self.assertEqual("1", chunk_size_value)
        self.assertEqual("暴露数量", chunk_size_title)
        self.assertEqual(offer_price_value, price_value)
        self.assertEqual("ICE", type_value)

    def test_51_ice_type_and_input_chunk_size_illegal_value_should_fix_value(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("0", "0")
        lots_value = result[0]
        chunk_size_value = result[1]
        self.assertEqual("1", lots_value)
        self.assertEqual("1", chunk_size_value)

    def test_52_ice_type_and_input_chunk_size_less_than_lots_should_legal(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("10", "5")
        lots_value = result[0]
        chunk_size_value = result[1]
        self.assertEqual("10", lots_value)
        self.assertEqual("5", chunk_size_value)

    def test_53_ice_type_and_input_chunk_size_equal_lots_should_legal(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("5", "5")
        lots_value = result[0]
        chunk_size_value = result[1]
        self.assertEqual("5", lots_value)
        self.assertEqual("5", chunk_size_value)

    def test_54_ice_type_and_input_chunk_size_above_lots_should_lots_value(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("5", "10")
        lots_value = result[0]
        chunk_size_value = result[1]
        self.assertEqual("5", lots_value)
        self.assertEqual("5", chunk_size_value)

    def test_55_ice_type_and_input_chunk_size_above_50_should_50(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("51", "51")
        lots_value = result[0]
        chunk_size_value = result[1]
        self.assertEqual("51", lots_value)
        self.assertEqual("50", chunk_size_value)

    def test_56_ice_type_and_clear_chunk_size_and_order_should_fail(self):
        self.normal_order_page.ice_type_clear_chunk_size_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_chunk_size)
        self.assertEqual(True, result)

    def test_56_ice_type_and_input_chunk_size_legal_value_and_order_should_success(self):
        result = self.normal_order_page.ice_type_input_chunk_size_legal_value_and_order()
        lots_value = result[0]
        chunk_size_value = result[1]
        order_details_lots_value = result[2]
        order_details_chunk_size_value = result[3]
        order_details_type_value = result[4]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertGreater(lots_value, order_details_lots_value)
        self.assertEqual(chunk_size_value, order_details_chunk_size_value)
        self.assertEqual("ICE", order_details_type_value)

    def test_57_TIF_DAY_order_should_success(self):
        self.normal_order_page.tif_day_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_58_TIF_GTC_order_should_success(self):
        self.normal_order_page.tif_gtc_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_59_TIF_GTD_order_should_success(self):
        self.normal_order_page.tif_gtd_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_60_TIF_FAK_order_should_success(self):
        self.normal_order_page.tif_fak_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_61_TIF_FOK_order_should_success(self):
        self.normal_order_page.tif_fok_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_62_tif_fak_and_clear_min_quantity_and_order_should_fail(self):
        self.normal_order_page.tif_fak_and_clear_min_quantity_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_min_quantity)
        self.assertEqual(True, result)

    def test_63_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.normal_order_page.tif_fak_and_input_illegal_min_quantity(0)
        self.assertEqual(fak_min_quantity, '1')

    def test_64_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.normal_order_page.tif_fak_and_input_illegal_min_quantity(-1)
        self.assertEqual(fak_min_quantity, '1')

    def test_65_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.normal_order_page.tif_fak_and_input_illegal_min_quantity("+")
        self.assertEqual(fak_min_quantity, '1')

    def test_66_tif_fak_and_input_illegal_min_quantity_should_fix_value(self):
        fak_min_quantity = self.normal_order_page.tif_fak_and_input_illegal_min_quantity("-")
        self.assertEqual(fak_min_quantity, '1')

    def test_67_tif_fak_and_input_min_quantity_below_lots_and_order_should_success(self):
        self.normal_order_page.tif_fak_and_input_min_quantity_and_lots(3, 4)
        self.normal_order_page.press_confirm_button()
        self.normal_order_page.press_confirm_button()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_68_tif_fak_and_input_min_quantity_equal_lots_and_order_should_success(self):
        self.normal_order_page.tif_fak_and_input_min_quantity_and_lots(3, 3)
        self.normal_order_page.press_confirm_button()
        self.normal_order_page.press_confirm_button()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_69_tif_fak_and_input_min_quantity_above_lots_and_min_quantity_should_lots_value(self):
        fak_min_quantity = self.normal_order_page.tif_fak_and_input_min_quantity_and_lots(4, 3)
        self.assertEqual(fak_min_quantity, '3')

    # 让有开平投保标志的合约TCU1907-SH排在第一位
    def test_70_offset_flag_auto_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_auto_and_order()
        offset_flag_default_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_default_value, '自动')
        self.assertEqual(offset_flag_default_value, order_details_offset_flag_value)

    def test_71_offset_flag_open_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_open_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_72_offset_flag_close_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_close_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_73_offset_flag_closeYesterday_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_closeYesterday_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平昨')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_74_offset_flag_closeToday_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_closeToday_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_75_offset_flag_C_CT_O_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_C_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_76_offset_flag_CT_C_O_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_CT_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_77_offset_flag_C_O_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_C_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平仓-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_78_offset_flag_CT_O_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_CT_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平今-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_79_offset_flag_CY_O_and_order_should_success(self):
        result = self.normal_order_page.offset_flag_CY_O_and_order()
        offset_flag_value = result[0]
        order_details_offset_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(offset_flag_value, '平昨-开仓')
        self.assertEqual(offset_flag_value, order_details_offset_flag_value)

    def test_80_hedge_flag_speculation_and_order_should_success(self):
        result = self.normal_order_page.hedge_flag_speculation_and_order()
        hedge_flag_default_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_default_value, '投机')
        self.assertEqual(hedge_flag_default_value, order_details_hedge_flag_value)

    def test_81_hedge_flag_arbitrage_and_order_should_success(self):
        result = self.normal_order_page.hedge_flag_arbitrage_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套利')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_82_hedge_flag_hedge_and_order_should_success(self):
        result = self.normal_order_page.hedge_flag_hedge_and_order()
        hedge_flag_value = result[0]
        order_details_hedge_flag_value = result[1]
        order_message = self.normal_order_page.alert_title_send_order_successfully()
        self.assertEqual(order_message, AlertError.alert_title_succeed)
        self.assertEqual(hedge_flag_value, '套保')
        self.assertEqual(hedge_flag_value, order_details_hedge_flag_value)

    def test_83_change_T_switch_and_order_should_success(self):
        self.normal_order_page.change_T_switch_and_order()
        result = self.normal_order_page.alert_order_details_message()
        self.assertEqual(result, AlertError.alert_message_succeed)

    def test_84_edit_memo_and_order_should_success(self):
        result = self.normal_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        order_message = self.normal_order_page.alert_order_details_message()
        self.assertEqual(order_message, AlertError.alert_message_succeed)
        self.assertEqual(hint, AlertError.hint_message)
        self.assertEqual(memo_value, order_details_memo_value)


if __name__ == '__main__':
    unittest.main()
