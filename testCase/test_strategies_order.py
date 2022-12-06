import pytest
from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.strategies_order_page import StrategiesOrderPage


class TestCaseStrategiesOrder:

    def setup_method(self) -> None:
        self.driver = android_driver()
        self.strategies_order_page = StrategiesOrderPage(self.driver)
        self.strategies_order_page.login_successful()

    def teardown_method(self) -> None:
        self.driver.quit()

    # 涔板崠鐩樺強娑ㄨ穼骞呮湁鏁版嵁鏃舵牴鎹氦鏄撴柟鍚戠浉鍙嶆暟鎹～鍏�
    def test_01_press_bid_and_side_should_sell(self):
        pass

    def test_87_edit_memo_and_order_should_success(self):
        self.strategies_order_page.permission_contract_to_bottom()  # 鏉冮檺鍚堢害鎺掑埌鏈�搴曢儴锛屼富鍚堢害鎺掑埌绗竴浣�
        result = self.strategies_order_page.edit_memo_and_order()
        hint = result[0]
        memo_value = result[1]
        order_details_memo_value = result[2]
        # order_message = self.strategies_order_page.alert_order_details_message()
        # self.assertEqual(order_message, AlertError.alert_order_message)
        assert hint == AlertError.hint_message
        assert memo_value == order_details_memo_value


if __name__ == '__main__':
    pytest.main()
