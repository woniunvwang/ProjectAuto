# _*_coding:GBK_*_

from appium.webdriver.common.appiumby import AppiumBy


class all_path:
    # 普通单path
    confirm_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/confirm")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/agree")
    cancel_button_id = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    # 合约组 "自动化测试合约"的path
    contract_group_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自动化测试合约")')
    page_title = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "1]/android.view.ViewGroup/android.widget.TextView")
    contract_name = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_name_or_code')
    K_line = (AppiumBy.ID, 'com.atp.newdemo2:id/k_line_thumbnail')
    Chg_path = (AppiumBy.XPATH,
                "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[4]/android.widget.TextView[1]")
    bid_price_path = (AppiumBy.XPATH,
                      "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[1]")
    bid_lots_path = (AppiumBy.XPATH,
                     "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[1]/android.widget.TextView[2]")
    offer_price_path = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[1]")
    offer_lots_path = (AppiumBy.XPATH,
                       "//*[@resource-id='com.atp.newdemo2:id/right_bottom_list']/android.view.ViewGroup[2]/android.widget.TextView[2]")
    trade_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/account")
    trade_account_text_path = (AppiumBy.XPATH,
                               "//*[@resource-id='com.atp.newdemo2:id/recycler_view_account']/android.widget.LinearLayout[2]/android.widget.TextView")
    change_account_ID = (AppiumBy.ID, "com.atp.newdemo2:id/action_change")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "转到上一层级")
    sell_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_sell")
    buy_side_id = (AppiumBy.ID, "com.atp.newdemo2:id/order_direction_buy")
    lots_xpath = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/lots']/android.view.ViewGroup/android.widget.EditText")
    price_xpath = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/price']/android.view.ViewGroup/android.widget.EditText")
    change_type_button = (AppiumBy.XPATH,
                          "//*[@resource-id='com.atp.newdemo2:id/normal_order_type']/android.widget.LinearLayout/android.widget.Button")
    type_Market_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market")')
    type_Market_Limit_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market Limit")')
    type_Lim_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LIM")')
    type_STP_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("STP")')
    type_STL_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("STL")')
    type_ICE_path = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ICE")')
    StPx_titile_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/stop_price']/android.view.ViewGroup/android.widget.TextView")
    input_StPx_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/stop_price']/android.view.ViewGroup/android.widget.EditText")
    chunk_size_title = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/max_iceberg_chunk_size']/android.view.ViewGroup/android.widget.TextView")
    chunk_size_xpath = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/max_iceberg_chunk_size']/android.view.ViewGroup/android.widget.EditText")
    TIF_change_button = (AppiumBy.XPATH,
                         "//*[@resource-id='com.atp.newdemo2:id/time_option']/android.widget.LinearLayout/android.widget.Button")
    TIF_DAY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("DAY")')
    TIF_GTC = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("GTC")')
    TIF_GTD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("GTD")')
    TIF_FAK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FAK")')
    TIF_FOK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FOK")')
    date_pick_ID = (AppiumBy.ID, "com.atp.newdemo2:id/date_pick_text_view")
    fak_min_quantity = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/min_quantity']/android.view.ViewGroup/android.widget.EditText")
    offset_flag_change_button = (AppiumBy.XPATH,
                                 "//*[@resource-id='com.atp.newdemo2:id/offset_flag_type']/android.widget.LinearLayout/android.widget.Button")
    offset_flag_auto_xpath = (AppiumBy.XPATH, "//*[@text='自动' or @text='Auto']/..")
    offset_flag_open_xpath = (AppiumBy.XPATH, "//*[@text='开仓' or @text='Open']/..")
    offset_flag_close_xpath = (AppiumBy.XPATH, "//*[@text='平仓' or @text='Close']/..")
    offset_flag_closeYesterday_xpath = (AppiumBy.XPATH, "//*[@text='平昨' or @text='CloseYesterday']/..")
    offset_flag_closeToday_xpath = (AppiumBy.XPATH, "//*[@text='平今' or @text='CloseToday']/..")
    offset_flag_C_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-平今-开仓' or @text='C-CT-O']/..")
    offset_flag_CT_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-平仓-开仓' or @text='CT-C-O']/..")
    offset_flag_C_O_xpath = (AppiumBy.XPATH, "//*[@text='平仓-开仓' or @text='C-O']/..")
    offset_flag_CT_O_xpath = (AppiumBy.XPATH, "//*[@text='平今-开仓' or @text='CT-O']/..")
    offset_flag_CY_O_xpath = (AppiumBy.XPATH, "//*[@text='平昨-开仓' or @text='CY-O']/..")
    hedge_flag_change_button = (AppiumBy.XPATH,
                                "//*[@resource-id='com.atp.newdemo2:id/hedge_flag_type']/android.widget.LinearLayout/android.widget.Button")
    hedge_flag_speculation_xpath = (AppiumBy.XPATH, "//*[@text='投机' or @text='Speculation']/..")
    hedge_flag_arbitrage_xpath = (AppiumBy.XPATH, "//*[@text='套利' or @text='Arbitrage']/..")
    hedge_flag_hedge_xpath = (AppiumBy.XPATH, "//*[@text='套保' or @text='Hedge']/..")
    order_details_side = (AppiumBy.XPATH,
                          "//*[@text='方向' or @text='Side']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_contract = (AppiumBy.XPATH,
                              "//*[@text='合约' or @text='Contract']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_account = (AppiumBy.XPATH,
                             "//*[@text='交易账户' or @text='Trade Account']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_lots = (AppiumBy.XPATH,
                          "//*[@text='手数' or @text='Lots']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_chunk_size = (AppiumBy.XPATH,
                                "//*[@text='暴露数量' or @text='Chunk Size']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price = (AppiumBy.XPATH,
                           "//*[@text='价格' or @text='Price']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stpx = (AppiumBy.XPATH,
                          "//*[@text='StPx']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stpx_title = (AppiumBy.XPATH, "//*[@text='StPx']")
    order_details_type = (AppiumBy.XPATH,
                          "//*[@text='类型' or @text='Type']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_offset_flag = (AppiumBy.XPATH,
                                 "//*[@text='开平标志' or @text='Offset Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_hedge_flag = (AppiumBy.XPATH,
                                "//*[@text='投保标志' or @text='Hedge Flag']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_tif = (AppiumBy.XPATH,
                         "//*[@text='TIF']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_min_quantity = (AppiumBy.XPATH,
                                  "//*[@text='最小数量' or @text='Min Quantity']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_t = (AppiumBy.XPATH,
                       "//*[@text='T+1']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_memo = (AppiumBy.XPATH,
                          "//*[@text='备注' or @text='Memo']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    alert_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    alert_contract_code = (AppiumBy.ID, 'com.atp.newdemo2:id/contract_code')
    alert_order_id = (AppiumBy.ID, 'com.atp.newdemo2:id/order_id')
    alert_message_ID = (AppiumBy.ID, "com.atp.newdemo2:id/message")
    alert_message_title = (AppiumBy.ID, "com.atp.newdemo2:id/title")
    button_view_details = (AppiumBy.ID, 'com.atp.newdemo2: id/positive_button')
    button_close = (AppiumBy.ID, 'com.atp.newdemo2:id/close_button')
    last_price_and_lots = (AppiumBy.ID, "com.atp.newdemo2:id/lots_at_price")
    contract_management_ID = (AppiumBy.ID, "com.atp.newdemo2:id/manage_contract")
    # 主测试合约，买卖盘涨跌幅有数据
    main_test_contract_drag_path = ("//*[@text='GC2212-CME']/../android.widget.ImageView")
    # 权限测试合约，买卖盘有数据涨跌幅无数据
    permission_contract_drag_path = ("//*[@text='TCU1907-SH']/../android.widget.ImageView")
    # 无数据测试合约，买卖盘涨跌幅均无数据
    no_data_contract_drag_path = ("//*[@text='GC2806-CME']/../android.widget.ImageView")
    illegal_lots_xpath = (AppiumBy.XPATH, "//*[@text='非法手数']")
    T_switch_ID = (AppiumBy.ID, "com.atp.newdemo2:id/one_plus_switch")
    edit_memo_ID = (AppiumBy.ID, "com.atp.newdemo2:id/edit_memo")
    error_hint_ID = (AppiumBy.ID, "com.atp.newdemo2:id/memo_error_hint")

    # gain best单path
    gain_best_order_path = (
        AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Gain best单']/android.widget.TextView")
    gap_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/gap_price']/android.view.ViewGroup/android.widget.EditText")
    step_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/step_price']/android.view.ViewGroup/android.widget.EditText")
    order_details_title = (AppiumBy.ID, 'com.atp.newdemo2:id/title')
    order_details_gap = (AppiumBy.XPATH,
                         "//*[@text='Gap']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_step = (AppiumBy.XPATH,
                          "//*[@text='Step']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")

    # 登录path
    usernameID = (AppiumBy.ID, 'com.atp.newdemo2:id/username')
    passwordID = (AppiumBy.ID, 'com.atp.newdemo2:id/password')
    login_button_ID = (AppiumBy.ID, 'com.atp.newdemo2:id/sign_in_button')
    error_alert_title_ID = (AppiumBy.ID, "com.atp.newdemo2:id/title")
    error_alert_content_ID = (AppiumBy.ID, "com.atp.newdemo2:id/content_view")
    alert_title_ID = (AppiumBy.ID, "com.atp.newdemo2:id/disclaimer_title")
    cancel_button = (AppiumBy.ID, "com.atp.newdemo2:id/cancel")
    checkBox_allow = (AppiumBy.ID, "com.atp.newdemo2:id/checkBox_allow_collect_system_information")
    permission_allow = (AppiumBy.ID, "com.android.permissioncontroller:id""/permission_allow_foreground_only_button")
    agree_button = (AppiumBy.ID, "com.atp.newdemo2:id/agree")

    # stop单path
    stop_order_path = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Stop单']/android.widget.TextView")
    stop_price_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/stop_price']/android.view.ViewGroup/android.widget.EditText")
    stop_price_type_ID = (AppiumBy.ID, "com.atp.newdemo2:id/stop_price_type")
    stop_price_option_Last_trade_price = (AppiumBy.XPATH, "//*[@text='最后成交价' or @text='Last trade price']/..")
    stop_price_option_market_buy_price = (AppiumBy.XPATH, "//*[@text='市场买价' or @text='Market buy price']/..")
    stop_price_option_market_sell_price = (AppiumBy.XPATH, "//*[@text='市场卖价' or @text='Market sell price']/..")
    order_details_stop_price = (AppiumBy.XPATH,
                                "//*[@text='止损价' or @text='Stop price']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stop_option = (AppiumBy.XPATH,
                                 "//*[@text='Stop @']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")

    # 止盈止损单path

    stop_profit_loss_order_path = (
        AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='止盈止损单']/android.widget.TextView")
    stop_profit_mode_xpath = (AppiumBy.XPATH,
                              "//*[@resource-id='com.atp.newdemo2:id/stop_profit_mode']/android.widget.LinearLayout/android.widget.Button")
    By_open_position_average_price_xpath = (
        AppiumBy.XPATH, "//*[@text='按开仓均价止盈止损' or @text='By open position average price']/..")
    By_custom_price_xpath = (
        AppiumBy.XPATH, "//*[@text='按自定义价止盈止损(不开仓)' or @text='By custom price(not open order)']/..")
    stop_loss_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/stop_loss']/android.view.ViewGroup/android.widget.EditText")
    stop_profit_xpath = (AppiumBy.XPATH,
                         "//*[@resource-id='com.atp.newdemo2:id/stop_profit']/android.view.ViewGroup/android.widget.EditText")
    order_type_xpath = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/order_type']/android.widget.LinearLayout/android.widget.Button")
    select_type_market_xpath = (AppiumBy.XPATH, "//*[@text='Market']/..")
    select_type_lim_xpath = (AppiumBy.XPATH, "//*[@text='LIM']/..")
    close_px_diff_price_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("平仓价差")')
    close_px_diff_price_xpath = (AppiumBy.XPATH,
                                 "//*[@resource-id='com.atp.newdemo2:id/close_px_diff_price']/android.view.ViewGroup/android.widget.EditText")
    open_px_diff_price_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开仓价差")')
    open_px_diff_price_xpath = (AppiumBy.XPATH,
                                "//*[@resource-id='com.atp.newdemo2:id/open_px_diff_price']/android.view.ViewGroup/android.widget.EditText")
    open_px_diff_price_title_xpath = (AppiumBy.XPATH,
                                      "//*[@resource-id='com.atp.newdemo2:id/open_px_diff_price']/android.view.ViewGroup/android.widget.TextView")
    times_xpath = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/times']/android.view.ViewGroup/android.widget.EditText")
    exchange_market_order_switch = (AppiumBy.ID, "com.atp.newdemo2:id/support_market")
    order_details_mode = (AppiumBy.XPATH,
                          "//*[@text='模式' or @text='Mode']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stop_loss = (AppiumBy.XPATH,
                               "//*[@text='止损' or @text='Stop Loss']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_stop_profit = (AppiumBy.XPATH,
                                 "//*[@text='止盈' or @text='Stop Profit']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_close_px_diff_price_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("平仓价差")')
    order_details_close_px_diff_price = (AppiumBy.XPATH,
                                         "//*[@text='平仓价差' or @text='Close Pxdiff']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_open_px_diff_price_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开仓价差")')
    order_details_open_px_diff_price = (AppiumBy.XPATH,
                                        "//*[@text='开仓价差' or @text='Open_Pxdiff']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_exchange_market_order_title = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("交易所市价指令")')
    order_details_exchange_market_order_value = (AppiumBy.XPATH,
                                                 "//*[@text='交易所市价指令' or @text='Use exchange market order']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_times = (AppiumBy.XPATH,
                           "//*[@text='数量' or @text='Times']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")

    # 策略单path
    strategies_tabbar_xpath = (AppiumBy.XPATH,
                               "//*[@resource-id='com.atp.newdemo2:id/bottom_navigation_view']/android.view.ViewGroup/android.widget.FrameLayout[2]")
    edit_strategy = (AppiumBy.ID, "com.atp.newdemo2:id/edit_strategy")
    add_strategy = (AppiumBy.ID, "com.atp.newdemo2:id/add_strategy")
    list_title_strategy_name = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[1]")
    list_title_ratio1 = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[2]")
    list_title_ratio2 = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/list_title_root']/android.widget.TextView[3]")
    toolbar_title = (AppiumBy.ID, "com.atp.newdemo2:id/toolbar_title")
    action_done = (AppiumBy.ID, "com.atp.newdemo2:id/action_done")
    strategy_name_input_edit_text = (AppiumBy.XPATH,
                                     "//*[@resource-id='com.atp.newdemo2:id/strategy_name']/android.view.ViewGroup/android.widget.EditText")
    strategy_name_clear_text_icon = (AppiumBy.XPATH,
                                     "//*[@resource-id='com.atp.newdemo2:id/strategy_name']/android.view.ViewGroup/android.widget.ImageView")
    formula_edit_text = (AppiumBy.XPATH,
                         "//*[@resource-id='com.atp.newdemo2:id/formula_edit_text']/android.view.ViewGroup/android.widget.EditText")
    execution_times = (AppiumBy.XPATH,
                       "//*[@resource-id='com.atp.newdemo2:id/execution_times']/android.view.ViewGroup/android.widget.EditText")
    execution_times_clear_text_icon = (AppiumBy.XPATH,
                                       "//*[@resource-id='com.atp.newdemo2:id/execution_times']/android.view.ViewGroup/android.widget.ImageView")
    single_trigger_times = (AppiumBy.XPATH,
                            "//*[@resource-id='com.atp.newdemo2:id/single_trigger_times']/android.view.ViewGroup/android.widget.EditText")
    single_trigger_times_clear_text_icon = (AppiumBy.XPATH,
                                            "//*[@resource-id='com.atp.newdemo2:id/single_trigger_times']/android.view.ViewGroup/android.widget.ImageView")
    digits = (AppiumBy.ID, "com.atp.newdemo2:id/digits")
    split_switch = (AppiumBy.ID, "com.atp.newdemo2:id/split_switch")
    protection = (AppiumBy.ID, "com.atp.newdemo2:id/protection")
    active_leg_type = (AppiumBy.ID, "com.atp.newdemo2:id/active_leg_type")
    commodity_type_A = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/commodity_root']/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView")
    contract_text_A = (AppiumBy.XPATH,
                       "//*[@resource-id='com.atp.newdemo2:id/commodity_root']/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")

    # 定时单path
    timing_order_path = (
        AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='定时单']/android.widget.TextView")
    single_xpath = (
        AppiumBy.XPATH, "//*[@resource-id='com.atp.newdemo2:id/single']/android.view.ViewGroup/android.widget.EditText")
    type_xpath = (AppiumBy.XPATH, "//*[@text='类型' or @text='Type']/../android.widget.Button")
    start_time_id = (AppiumBy.ID, "com.atp.newdemo2:id/start_time")
    end_time_id = (AppiumBy.ID, "com.atp.newdemo2:id/end_time")
    end_time_title = (AppiumBy.ID, "com.atp.newdemo2:id/timeTitle")
    time_interval_id = (AppiumBy.ID, "com.atp.newdemo2:id/time_interval")
    order_details_single = (AppiumBy.XPATH,
                            "//*[@text='单次手数' or @text='Single']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_start_time = (AppiumBy.XPATH,
                                "//*[@text='开始时间' or @text='Start time']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_end_time = (AppiumBy.XPATH,
                              "//*[@text='结束时间' or @text='End time']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_time_interval = (AppiumBy.XPATH,
                                   "//*[@text='时间间隔' or @text='Time interval']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")

    # 定时单path
    twap_order_path = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='TWAP单']/android.widget.TextView")
    price_diff_xpath = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/price_diff']/android.view.ViewGroup/android.widget.EditText")
    price_type_button_xpath = (AppiumBy.XPATH,
                               "//*[@resource-id='com.atp.newdemo2:id/price_type']/android.widget.LinearLayout/android.widget.Button")
    last_trade_xpath = (AppiumBy.XPATH, "//*[@text='最后成交价' or @text='Last trade']/..")
    market_buy_xpath = (AppiumBy.XPATH, "//*[@text='市场买价' or @text='Market buy']/..")
    market_sell_xpath = (AppiumBy.XPATH, "//*[@text='市场卖价' or @text='Market sell']/..")
    best_bid_xpath = (AppiumBy.XPATH, "//*[@text='对手价' or @text='Best Bid/Offer']/..")
    order_interval_xpath = (AppiumBy.XPATH,
                            "//*[@resource-id='com.atp.newdemo2:id/order_interval']/android.view.ViewGroup/android.widget.EditText")
    cancel_order_interval_xpath = (AppiumBy.XPATH,
                                   "//*[@resource-id='com.atp.newdemo2:id/cancel_order_interval']/android.view.ViewGroup/android.widget.EditText")
    effect_immediately_id = (AppiumBy.ID, "com.atp.newdemo2:id/effect_immediately")
    start_time_radio_id = (AppiumBy.ID, "com.atp.newdemo2:id/start_time_radio")
    always_execute_id = (AppiumBy.ID, "com.atp.newdemo2:id/always_execute")
    end_time_radio_id = (AppiumBy.ID, "com.atp.newdemo2:id/end_time_radio")
    cancel_limit_switch = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/cancel_limit']/android.view.ViewGroup/android.widget.Switch")
    cancel_limit_text = (AppiumBy.XPATH,
                         "//*[@resource-id='com.atp.newdemo2:id/cancel_limit']/android.view.ViewGroup/android.widget.EditText")
    price_limit_switch = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.newdemo2:id/price_limit']/android.view.ViewGroup/android.widget.Switch")
    price_limit_text = (AppiumBy.XPATH,
                        "//*[@resource-id='com.atp.newdemo2:id/price_limit']/android.view.ViewGroup/android.widget.EditText")
    order_details_price_diff = (AppiumBy.XPATH,
                                "//*[@text='价差' or @text='Diff']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_order_interval = (AppiumBy.XPATH,
                                    "//*[@text='下单间隔' or @text='Order Interval']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_cancel_order_interval = (AppiumBy.XPATH,
                                           "//*[@text='撤单间隔' or @text='Cancel Order Interval']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price_type = (AppiumBy.XPATH,
                                "//*[@text='价格类型' or @text='Price type']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")

    order_details_cancel_limit = (AppiumBy.XPATH,
                                  "//*[@text='撤单上限' or @text='Cancel limit']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
    order_details_price_limit = (AppiumBy.XPATH,
                                 "//*[@text='限价' or @text='Price limit']/../android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
