import unittest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.strategies_order_page import StrategiesOrderPage


class CaseStrategiesOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.strategies_order_page = StrategiesOrderPage(self.driver)
        self.strategies_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        pass

    def test_87_edit_memo_and_order_should_success(self):
        self.strategies_order_page.permission_contract_to_bottom()  # 权限合约排到最底部，主合约排到第一位
        result = self.strategies_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.strategies_order_page.alert_order_details_message()
        # self.assertEqual(order_message, AlertError.alert_order_message)
        self.assertEqual(hint, AlertError.hint_message)
        self.assertEqual(memo_value, order_details_memo_value)


if __name__ == '__main__':
    unittest.main()
