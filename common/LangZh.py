class LangEn:
    englishStrings = {"alert_illegal_price": "价格不合法",
                      "alert_illegal_gap": "Gap不合法",
                      "alert_illegal_step": "Step不合法",
                      "alert_illegal_stop_price": "止损价不合法",
                      "alert_illegal_price_tick_size": "价格必须是最小变动价格的整数倍",
                      "alert_illegal_input_limit": "最多输入8位整数和8位小数",
                      "alert_illegal_order_price_tick_size": "下单价必须是最小变动价格的整数倍",
                      "alert_illegal_lots": "手数不合法",
                      "alert_message_lots": "请输入手数",
                      "alert_message_price": "请输入价格",
                      "alert_message_gap": "请输入Gap",
                      "alert_message_stop_loss": "请输入止损",
                      "alert_illegal_stop_loss": "止损不合法",
                      "alert_message_stop_profit": "请输入止盈",
                      "alert_illegal_stop_profit": "止盈不合法",
                      "alert_message_stop_price": "请输入止损价",
                      "alert_message_close_pxdiff": "请输入平仓价差",
                      "alert_illegal_close_pxdiff": "平仓价差不合法",
                      "alert_message_open_pxdiff": "请输入开仓价差",
                      "alert_illegal_open_pxdiff": "开仓价差不合法",
                      "alert_message_single": "请输入单次",
                      "alert_message_single_and_lots": "单次手数必须小于或等于手数",
                      "alert_message_price_diff": "请输入价差",
                      "alert_illegal_price_diff": "价差不合法",
                      "alert_message_order_interval": "请输入下单间隔",
                      "alert_illegal_order_interval": "下单间隔不合法",
                      "alert_message_cancel_order_interval": "请输入撤单间隔",
                      "alert_illegal_cancel_order_interval": "撤单间隔不合法",
                      "alert_illegal_end_time": "结束时间必须超过当前时间",
                      "alert_illegal_time_interval": "时间间隔不合法",
                      "alert_message_cancel_limit": "请输入撤单上限",
                      "alert_message_price_limit": "请输入限价",
                      "alert_illegal_price_limit": "限价不合法",
                      "alert_illegal_cancel_order_interval_value": "撤单间隔必须小于或等于下单间隔",
                      "alert_illegal_price_diff_tick_size": "价差必须是最小变动价格的整数倍",
                      "alert_illegal_close_pxdiff_tick_size": "平仓价差必须是最小变动价格的整数倍",
                      "alert_illegal_open_pxdiff_tick_size": "开仓价差必须是最小变动价格的整数倍",
                      "alert_message_times": "请输入数量",
                      "alert_illegal_times": "数量不合法",
                      "alert_order_message": "Order successfully",
                      "alert_order_message_title": "下单请求发送成功!",
                      "alert_message_StPx": "请输入StPx",
                      "alert_message_chunk_size": "请输入暴露数量",
                      "alert_message_min_quantity": "请输入最小数量",
                      "alert_buy_order_illegal_StPx": "买单StPx需小于等于价格",
                      "alert_sell_order_illegal_StPx": "卖单StPx需大于等于价格",
                      "alert_message_buy_order_rejected": "New order rejected, Buy order stop price must be above last trade price.",
                      "alert_message_sell_order_rejected": "New order rejected, Sell order stop price must be below last trade price.",
                      "hint_message": "输入长度不能超过255个字符",
                      "order_direction_buy": "buy",
                      "order_direction_sell": "Sell",

                      "networking_issue": "网络似乎出了问题",
                      "prompt_username": "用户名",
                      "prompt_password": "密码",
                      "action_sign_in": "登录",
                      "error_field_required": "此项不能为空",
                      "not_show_disclaimer": "下次不再提醒",
                      "network_disconnected": "网络连接已断开",
                      "network_check_please": "请检查您的网络连接",
                      "session_timed_out_please_log_in_again": "会话超时，请重新登录",
                      "shut_down": "关闭",
                      "order_type_title": "单类型",
                      "edit": "编辑",
                      "resume": "启动",
                      "pause": "暂停",
                      "action_settings": "设置",
                      "bulletin": "公告",

                      "remember_device": "信任此设备?",
                      "no_need_otp": "在一段时间内不需要动态码可以登录",
                      "get_system_info_tip": "同意根据中华人民共和国看穿式监管要求采集本机信息",
                      "ERROR_INTERNAL": "内部错误",
                      "ERROR_CONNECTION": "无法连接到服务器",
                      "ERROR_SERVER": "未知错误",
                      "ERROR_PERMISSION": "拒绝访问",
                      "ERROR": "错误",
                      "Cancel": "取消",
                      "Okay": "确定",
                      "DISCONNECTED": "连接已断开",
                      "title_quotes": "报价",
                      "title_positions": "持仓",
                      "title_messages": "消息",
                      "title_logout": "登出",
                      "logout_tip": "确定登出?",
                      "login_failed": "登录失败",
                      "action_done": "完成",
                      "buy": "买",
                      "sell": "卖",
                      "title_strategies": "策略",
                      "auto": "自动单",
                      "title_edit_contracts": "合约管理",
                      "title_modify": "改单",
                      "title_new_order": "新单",
                      "title_new_contract": "选择合约",
                      "support_ipv6_network": "支持IPv6网络",
                      "bid": "买盘",
                      "cancel_order_prompt": "确认取消此单？",
                      "error_save": "保存失败",
                      "fail_position": "获取持仓失败",
                      "fail_submit_order": "提交挂单失败",
                      "no": "否",
                      "offer": "卖盘",
                      "yes": "是",
                      "price": "价格",
                      "account": "帐号",
                      "lots": "手数",
                      "time_option": "TIF",
                      "chase": "追单",
                      "loss_diff": "止损价差",
                      "profit_diff": "止盈价差",
                      "diff": "价差",
                      "digits": "小数位",
                      "formula": "公式",
                      "split": "拆单",
                      "strategy_name": "策略名",
                      "type": "类型",
                      "invalid_formula": "公式不合法",
                      "orderfilled": "按单",
                      "active_leg_n": "主动腿 %c",
                      "prior_leg_n": "先手 %c",
                      "active_leg": "主动腿",
                      "prior_leg": "先手",
                      "ok": "好的",

                      "send_success": "发送成功",
                      "logout_done": "登出成功",
                      "order_not_support": "无法操作此挂单类型",

                      "limit": "限价单",
                      "market": "市价单",
                      "stop_price": "STP",
                      "stop_limit": "STL",
                      "iceberg": "ICE",
                      "iceberg_stepper_title": "暴露数量",

                      "min_quantity": "最小数量",

                      "CloseYesterday": "平昨",
                      "open": "开仓",
                      "close": "平仓",
                      "offset_flag_auto": "自动",
                      "closeToday": "平今",
                      "c_ct_o": "平仓-平今-开仓",
                      "ct_c_o": "平今-平仓-开仓",
                      "c_o": "平仓-开仓",
                      "ct_o": "平今-开仓",
                      "cy_o": "平昨-开仓",

                      "change_password": "修改密码",
                      "title_change_password": "修改密码",
                      "oldpassword": "旧密码",
                      "Error1": "服务器内部错误!",

                      "Error100": "用户名或密码为空!",
                      "Error100_1": "用户名或密码或动态密码为空!",
                      "Error101": "用户名不存在!",
                      "Error102": "用户被锁定!",
                      "Error103_1": "密码或动态密码错误!",
                      "Error104": "密码已过期!",
                      "Error105": "用户已过期!",
                      "Error106": "强制要求修改密码!",
                      "Error107": "信任设备已过期，请重新登录！",
                      "Error108": "请重新登录！",

                      "Error200": "修改密码失败!",

                      "Error201": "新密码和确认密码不一致",
                      "Error202": "新密码为空!",
                      "Error203": "当前密码错误",
                      "Error203_1": "旧密码错误",
                      "Error204": "新密码不符合复杂度标准,必须至少包含一个大写字母!",
                      "Error205": "新密码不符合复杂度标准,必须至少包含一个小写字母!",
                      "Error206": "新密码不符合复杂度标准,必须至少包含一个数字!",
                      "Error207": "新密码至少需要包含%s个字符!",
                      "Error208": "新密码不能与最近%s次历史密码相同!",
                      "Error209": "新密码必须至少包含(%s)字符串中的一个非字母数字字符!",
                      "Error210": "新密码不能和旧密码一样!",

                      "Error300": "版本太旧，请更新至最新版本使用!",
                      "Error302": "无法成功采集国内看穿式监管需要的信息!",

                      "Error400": "初始化认证已完成，不能重复初始化!",
                      "Error403": "前序步骤未完成!",
                      "ErrorMessage": "请使用最新PC版本完成双重认证初始化!",

                      "ChgPwdSuccess": "密码修改成功",
                      "offset_flag": "开平标志",
                      "hedge_flag": "投保标志",
                      "gapprice": "Gap",
                      "stepprice": "Step",
                      "speculation": "投机",
                      "arbitrage": "套利",
                      "hedge": "套保",
                      "title_group_manager": "组管理",
                      "ContractName": "合约名称",
                      "ContractCode": "合约编码",

                      "change_value": "涨跌",
                      "change_rate": "涨跌幅",
                      ",!--Order error--:"
                      "error_illegal_lot": "非法手数",
                      "error_formula": "非法的公式值",
                      "error": "错误",
                      "cancel": "取消",
                      "error_delete": "删除失败",
                      "error_illegal_parameter": "参数不合法",
                      "StartTime": "开始时间",
                      "EndTime": "结束时间",
                      "isn_invalid": "无效",
                      "contract_invalid": "合约无效",
                      "contract_not_exist": "合约不存在!",
                      "bp_account": "帐户",
                      "bp_broker": "经纪行",
                      "bp_margin": "保证金",
                      "bp_equity": "权益",
                      "bp_equity_margin": "权益-保证金",
                      "bp_exposure": "风险度",
                      "loading": "加载中...",

                      "error_minQty": "最小数量不能大于手数",
                      "please_input_minQty": "请输入最小数量",
                      "please_input_max_iceberg_chunk_size": "请输入暴露数量",

                      "trader": "分笔交易",
                      "min1": "1分钟",
                      "min5": "5分钟",
                      "min15": "15分钟",
                      "min30": "30分钟",
                      "h1": "1小时",
                      "KLineTitle": "K线",
                      "date": "日期",
                      "dd1": "日线",

                      "welcome_back": "你好，\n欢迎回来",
                      "back": "返回",
                      "input_username": "请输入用户名",
                      "input_password": "请输入密码",
                      "input_old_password": "请输入旧密码",
                      "input_new_password": "请输入新密码",
                      "confirm": "确认",
                      "verification_code": "验证码",

                      "currency": "币种",
                      "trusted_device": "信任设备",
                      "change": "切换",
                      "delete": "删除",
                      "delete_trusted_device_success": "删除信任设备成功",
                      "delete_trusted_device_fail": "删除信任设备失败",
                      "new_group_name": "新合约组名字",
                      "add": "添加",
                      "manage": "管理",
                      "memo": "备注",

                      "agree": "同意",
                      "disagree": "不同意",
                      "user_services_and_privacy_terms_tip": "请您认真阅读和充分理解《平安期货隐私权政策协议》，如您同意，请点击“同意”开始接受我们的服务。",
                      "user_services_and_privacy_terms_title": "用户服务和隐私条款",
                      "create_time": "创建时间 %s",
                      "expiry_time": "过期时间 %s",

                      "trade_account": "交易账户",
                      "order_success": "下单成功",
                      "check_new_order_details": "查看详情",
                      "note_star": "提示",
                      "note": "提示",
                      "turn_on_now": "立即开启",
                      "settings_permissions_reminder_content": "请开启设置里的【定位】和【访问设备状态】(或【电话】) 权限以继续登录。",

                      "check_it_later": "如果你没有在订单列表中看到这个订单，请稍后查看",
                      "order_title": "单",
                      "working_order": "委托单",
                      "filled_order": "成交单",
                      "order_id": "单编号：%s",
                      "ordered_id": "单编号",
                      "filled_lots_total_lots": "已成交 / 总手数",

                      "working_": "工作中",
                      "working_partial_filled": "部分已成交",
                      "filled_": "已成交",
                      "working_pending_new": "等待",
                      "working_replaced": "已修改",
                      "expired": "已过期",
                      "calculated": "已计算",
                      "stopped": "已停止",
                      "canceled": "已取消",
                      "unknown_status": "未知状态",
                      "exec_id": "执行编号：%s",
                      "executed_id": "执行编号",
                      "market_value_title": "市值",
                      "initial_margin_title": "初始保证金",
                      "maintenance_margin": "维持保证金",
                      "change_account": "切换账户",
                      "change_currency": "切换货币",
                      "default_exposure": "默认",
                      "convert_exposure": "倒置",
                      "selected_contracts": "已选择合约",
                      "fragment_title_quote": "报价",
                      "illegal_max_iceberg_chunk_size": "非法暴露数量",
                      "chunk_size_cant_be_larger_than_lots": "暴露数量不能大于手数",
                      "assets_title_broker": "经纪行资金",
                      "assets_title_account": "账户资金",
                      "position_today_buy_lots": "今买手数",
                      "position_today_buy_price": "今买价格",
                      "position_today_sell_lots": "今卖手数",
                      "position_today_sell_price": "今卖价格",
                      "position_bid": "买盘",
                      "position_offer": "卖盘",
                      "position_profit_and_loss": "盈亏",

                      "position_long": "多头",
                      "position_short": "空头",
                      "position_net_lots": "净持仓手数",
                      "position_net_price": "净持仓价格",
                      "position_last_price": "最后成交价",
                      "position_last_upl": "持仓盈亏",
                      "position_last_pl": "平仓盈亏",
                      "position_title": "持仓",
                      "pending_new_edit_tip": "等待中的单不能改单或者撤单",
                      "confirm_direction": "方向",
                      "confirm_contract": "合约",
                      "no_contract_add_tip": "这个合约组没有合约，请点击下面“+”来添加新合约",
                      "no_contract_tip": "这个合约组没有合约",
                      "no_search_results": "无搜索结果",
                      "keyword_to_search_tip": "交易所名称 \\ 产品名称 \\ 合约编码",
                      "done_added": "&#160;&#160;完成&#160;&#160;",
                      "selected_count": "(已选择 %d)",
                      "please_enter_more_than_one_character": "请输入多于一个字符",
                      "transaction_direction": "方向",
                      "please_change_the_order_parameter": "请修改下单参数",
                      "add_new_contract_group_successfully": "合约组添加成功",
                      "add_new_contract_group_failed": "合约组添加失败",
                      "group_name_already_exists_tip": "合约组 \“%s\” 已经存在",
                      "group_name_already_exists_tip_case_insensitive": "合约组 \“%s\” 已经存在 (不区分大小写)",
                      "maximum_characters_length_is_15": "最多输入15个字符",
                      "show": "显示",
                      "hide": "隐藏",
                      "login_change_password": "修改密码？",
                      "when_value_up_and_down_the_color_changes": "当报价数值涨幅或跌幅时颜色的变化",

                      "confirm_order_lots": "手数",
                      "confirm_order_2_limit": "价格",
                      "confirm_order_type": "类型",
                      "confirm_order_stop_price": "StPx",
                      "confirm_order_maxIcebergChunkSize": "暴露数量",
                      "confirm_order_hedge_flag": "投保标志",
                      "confirm_order_offset_flag": "开平标志",
                      "confirm_order_expiry_time": "到期日",

                      "no_filled_orders_today": "今天没有成交单",
                      "no_orders": "没有委托单",
                      "no_messages": "当前没有消息",
                      "play_voice_hint": "播放声音提示",
                      "change_language": "切换语言",
                      "set_quote_color": "设置报价颜色",
                      "user": "用户",
                      "system": "系统",
                      "voice_hint_tip": "下单、单成交等提示音",
                      "version": "版本",
                      "confirm_new_password": "确认新密码",
                      "change_server": "更改服务器",
                      "search_contract_history": "搜索合约历史:",
                      "contract": "合约",
                      "contract_code": "合约编码",
                      "delete_search_history": "确认删除搜索合约记录?",
                      "delete_contracts": "确认删除选中的合约吗?",

                      "filled_order_list_detail": "明细(%d)",
                      "filled_order_list_order": "按单(%d)",
                      "filled_order_list_contract": "按合约(%d)",
                      "more": "更多",
                      "list": "列表",
                      "timeline": "时间轴",
                      "no_position_data": "没有持仓数据",
                      "operations_cancel_order": "取消挂单",
                      "go_to_modify": "去修改",
                      "order_details": "订单详情",
                      "please_input_lots": "请输入手数",
                      "rename_contract_group_successfully": "合约组重命名成功",
                      "rename_contract_group": "合约组重命名",
                      "rename_contract_group_failure": "合约组重命名失败",
                      "add_new_contracts_successfully": "合约添加成功",
                      "contract_doesnt_exist": "合约不存在",
                      "the_default_is_the_system_language": "默认为系统语言",
                      "collapse": "收起",
                      "the_maximum_number_of_contracts_is_50": "合约组最大合约数为50",
                      "this_contract_group_has_maxmium_number_of_contracts": "此合约组已经包含最大数量合约",

                      "finished": "已完成",
                      "order_tip_filled": "成交&#160;",
                      "order_tip_contract_code": "合约编码: %s",
                      "order_tip_filled_info_lots": "下单手数:%1$s",
                      "order_tip_filled_info": "下单手数:%1$s&#160;&#160;成交手数:%2$s&#160;&#160;均价:%3$s",

                      "position_buy_lots": "买持仓",
                      "position_sell_lots": "卖持仓",
                      "all": "全部",
                      "filter": "筛选",
                      "the_value_cannot_be_empty": "值不能为空",
                      "the_string_value_cannot_be_empty": "%s不能为空",
                      "contract_group_contains_at_least_one_contract": "合约组至少保留一个合约",
                      "the_last_contract_group_cannot_be_deleted": "最后一个合约组不能被删除",
                      "relogin_or_logout_disconnect_tip": "您的账户可能在其他设备上登录或超时，请重新登录",
                      "logged_out": "登出",
                      "add_into_one_of_the_contract_groups_below": "添加 %s 到以下合约组",
                      "already_exist_in_the_following_contract_groups": "%s 在下面的合约组里已经存在",
                      "choose": "选择",
                      "strategy_title": "策略",
                      "ratio_1": "比率1",
                      "ratio_2": "比率2",

                      "times": "数量",
                      "single_trigger_times": "单次触发",
                      "executed": "已执行",
                      "protection": "保护机制",
                      "single_trigger_number_full": "单次触发数量",
                      "execution_number": "执行总数量",
                      "send": "下单",
                      "normal_type": "普通",
                      "none": "无",
                      "type_1": "类型1",
                      "type_2": "类型2",
                      "reference_price": "参考价",
                      "reference_price_bid": "买1档",
                      "reference_price_offer": "卖1档",
                      "reference_price_average": "中间价",
                      "reference_price_last_trade": "成交价",
                      "reference_price_opponent": "对手价",

                      "illegal_execution_number": "执行总数不合法",
                      "illegal_single_trigger_number": "单次触发数量不合法",
                      "lots_number_is_illegal": "手数不合法",
                      "price_number_is_illegal": "价差不合法",
                      "order_request_sent_successfully": "下单请求发送成功!",
                      "new_strategy_order": "新建策略单",
                      "single_trigger_times_must_be_below_execution_number": "单次触发数量必须小于或等于执行总数",
                      "expiry_date_is_illegal": "非法到期日",
                      "broker_status_title": "经纪行状态",
                      "lot_price_diff_regax": "L:%s D:%s",
                      "order_range": "下单区间",
                      "always_best_price": "只挂一档",
                      "active_better": "有利",
                      "active_worse": "不利",
                      "max_500": "(最大值 500)",
                      "order_range_cannot_be_empty": "下单区间不能为空",
                      "active_better_cannot_be_empty": "有利不能为空",
                      "active_worse_cannot_be_empty": "不利不能为空",
                      "illegal_order_range": "下单区间不合法",
                      "illegal_active_better": "有利不合法",
                      "illegal_active_worse": "不利不合法",
                      "the_input_active_worse_value_is_out_of_the_order_range": "不利输入值不在下单区间",
                      "the_input_order_range_value_is_out_of_the_range": "下单区间输入值超出范围",
                      "the_input_active_better_value_is_out_of_the_order_range": "有利输入值不在下单区间",
                      "the_price_difference_must_be_the_integer_times_of_the_minimal_price_of_tick_size": "价差必须是最小变动价格的整数倍",
                      "the_price_must_be_the_integer_times_of_the_minimal_price_of_tick_size": "价格必须是最小变动价格的整数倍",
                      "please_select": "请选择",
                      "please_select_a_type_of_reference_price": "请选择参考价的类型",
                      "the_active_leg_lots_must_be_greater_than_0": "主动腿手数必须大于0",
                      "the_prior_leg_lots_must_be_greater_than_0": "先手腿手数必须大于0",
                      "the_sum_of_all_lots_must_be_greater_than_0": "手数和必须大于0",
                      "select_contract": "选择合约",
                      "please_input_formula": "请输入公式",
                      "please_input_strategy_name": "请输入策略名",
                      "strategy_name_cannot_be_empty": "策略名不能为空",
                      "formula_cannot_be_empty": "公式不能为空",
                      "formula_value_cannot_be_empty": "公式值不能为空",
                      "add_new_strategy_successfully": "新策略添加成功",
                      "amending_strategy_successful": "策略修改成功",
                      "Please_select_contract": "请选择合约",
                      "add_strategy": "添加策略",
                      "formula_length_cannot_be_longer_than_127_characters": "公式长度不能超过127个字符",
                      "input_length_cannot_be_longer_than_number_characters": "输入长度不能超过%d个字符",
                      "strategy_name_has_existed": "策略名 \"%s\" 已存在 (不区分大小写)",
                      "pending_new": "等待",
                      "illegal_type_does_not_exist": "类型不合法，%s不存在",
                      "no_protection": "无保护机制",
                      "leg_setting_format": "下单区间 1-%1$d｜有利%2$d｜不利%3$d%4$s",
                      "contract_list_header_close_trend": "收盘趋势",
                      "strategy_order_id": "ID: %s",
                      "edit_strategy": "编辑策略",
                      "please_select_reference_price": "请选择参考价",
                      "please_select_contract_title": "选择合约",
                      "no_strategies": "无策略，请点击下面的\"+\"来添加新策略",
                      "k_chart_volume": "成交",
                      "k_chart_open": "开盘",
                      "k_chart_high": "最高",
                      "k_chart_low": "最低",
                      "k_chart_close": "收盘",
                      "k_chart_position": "持仓",

                      "new_password_and_old_password_cannot_be_the_same": "新密码和旧密码不能相同",
                      "please_input_new_password_again": "请再次输入新密码",
                      "current_password": "当前密码",
                      "Please_input_your_current_password": "请输入您的当前密码",
                      "new_password": "新密码",
                      "close_up": "关闭",
                      "last_limit_price": "最后限制价",

                      "gain_best_order": "Gain best单",
                      "t_wap_order": "TWAP单",
                      "strategy_order": "策略单",
                      "stop_order": "Stop单",
                      "market_buy_price": "市场买价",
                      "market_sell_price": "市场卖价",
                      "last_trade_price": "最后成交价",
                      "stop_price_text": "止损价",
                      "lots_and_price_title": "手数 @ 价格",
                      "normal_order": "普通单",
                      "amend_order_request_has_sent": "改单请求已发送",
                      "The_maximum_input_value_digit_is_8_integers": "输入值最大位数为8位整数",
                      "the_maximum_input_value_digit_is_8_integers_and_8_decimals": "输入值最大位数为8位整数和8位小数",
                      "the_maximum_input_value_digit_is_count_integers": "输入值最大位数为%s位整数",
                      "the_maximum_input_value_digit_is_count_integers_and_count_decimals": "输入值最大位数为%s位整数和%s位小数",
                      "please_select_the_check_box_to_agree_to_collecting_the_required_information": "请勾选勾选框来同意搜集必需的信息",
                      "mode": "模式",
                      "by_open_position_average_price": "按开仓均价止盈止损",
                      "by_custom_price": "按自定义价止盈止损(不开仓)",
                      "close_px_diff": "平仓价差",
                      "stop_loss": "止损",
                      "stop_profit": "止盈",
                      "stop_profit_loss_order": "止盈止损单",
                      "open_px_diff": "开仓价差",
                      "select_mode": "选择模式",
                      "select_type": "选择类型",
                      "the_value_must_be_the_integer_times_of_the_minimal_price_of_tick_size": "%s必须是最小变动价格的整数倍",
                      "diff_the_value_must_be_the_integer_times_of_the_minimal_price_of_tick_size": "价差必须是最小变动价格的整数倍",
                      "value_is_illegal": "%s不合法",
                      "order_interval_value_is_illegal": "下单间隔不合法",
                      "cancel_interval_value_is_illegal": "撤单间隔不合法",
                      "exchange_market_order": "交易所市价指令",
                      "execute_lots": "已执行手数",
                      "filled_lots": "成交手数",
                      "not_close_lots": "未平仓手数",
                      "not_closed_average_price": "未平仓均价",
                      "use_exchange_market_order": "交易所市价指令",
                      "please_input_price_diff": "请输入价差",
                      "order_price": "下单价",
                      "base_price": "基准价",
                      "t_wap_price_type_last_trade": "最后成交价",
                      "t_wap_price_type_market_buy": "市场买价",
                      "t_wap_price_type_market_sell": "市场卖价",
                      "t_wap_price_type_opponent": "对手价",
                      "single": "单次",
                      "order_interval": "下单间隔",
                      "cancel_interval": "撤单间隔",
                      "effect_immediately": "立刻下单",
                      "always_execute": "一直执行",
                      "start": "开始",
                      "end": "结束",
                      "cancel_limit": "撤单上限",
                      "price_limit": "限价",
                      "please_input_seconds": "请输入秒数",
                      "single_lots_must_be_smaller_than_or_equal_to_lots": "单次手数必须小于或等于手数",
                      "single_lots": "单次手数",
                      "price_type": "价格类型",
                      "the_end_time_must_be_later_than_now": "结束时间必须超过当前时间",
                      "total_lots": "总手数",
                      "price_difference": "价差",
                      "filled_average_price": "已成交均价",
                      "executed_order_times": "已执行下单次数",
                      "executed_cancel_times": "已执行撤单次数",
                      "select_price_type": "选择价格类型",
                      "The_start_time_must_be_before_the_end_time": "开始时间必须先于结束时间",
                      "the_cancel_interval_must_be_smaller_than_or_equal_to_order_interval": "撤单间隔必须小于或等于下单间隔",
                      "last_order_time": "最后下单时间",
                      "no_auto_order_currently": "当前没有%s",
                      "time_interval": "时间间隔",
                      "timing_order_title": "定时单",
                      "hour_minute_second_description": "H 时 m 分 s 秒",
                      "hour": "时",
                      "minute": "分",
                      "second": "秒",
                      "time_interval_is_illegal": "时间间隔不合法",
                      "executed_times": "已执行次数",
                      "executed_times_": "已执行数量",
                      "last_executed_lots": "最后执行手数",
                      "no_content_tip_gain_best_order": "Gain best单",
                      "no_content_tip_stop_order": "Stop单",
                      "please_input_value": "请输入%s",
                      "risk_check_failed": "风控检查失败",

                      "history_filled": "已成交",
                      "history_trade": "交易",
                      "history_today": "今天",
                      "history_yesterday": "昨天",
                      "history_last_7_days": "最近7天",
                      "history_custom": "自定义",
                      "order_history": "单历史",
                      "history_search": "查询",
                      "order_id_title": "单编号",
                      "trade_date": "交易日",
                      "order_time": "下单时间",
                      "filled_time": "成交时间",
                      "filled_order_detail": "成交单详情",
                      "trade_order_detail": "交易单详情",
                      "avg_filled_price": "成交均价",
                      "order_status": "单状态",
                      "the_operation_is_too_frequent": "操作太频繁",
                      "time_range_is_out_of_limit": "开始时间和结束时间超过指定范围(一周内)",
                      "date_is_out_of_limit": "超出可查询日期范围(最近一个月)",
                      "rejected": "已拒绝",
                      "triggered_by_auto_order": "(* 由自动单触发)",
                      "expire_time_": "到期时间",
                      "the_start_time_must_be_before_the_end_time": "开始时间必须先于结束时间",
                      "sell_order_stpx_must_be_greater_than_or_equal_to_trigger_price": "卖单StPx需大于等于价格",
                      "buy_order_stpx_must_be_smaller_than_or_equal_to_trigger_price": "买单StPx需小于等于价格",
                      "available": "可用资金",
                      "please_select_formula_operator": "请选择公式运算符",
                      "no_data": "无数据",
                      "account_title": "账户",
                      "remember_password": "记住密码",
                      "delete_strategy_success": "删除策略成功",
                      "delete_strategy_fail": "删除策略失败",
                      "new_strategy_order_fail": "新建策略单失败",
                      "add_strategy_fail": "添加策略失败",
                      "edit_strategy_fail": "编辑策略失败",
                      "delete_contract_group_fail": "删除合约组失败",
                      "password_expired_tip": "您的密码将于%d天后过期！",
                      "buy_average_price": "买均价",
                      "sell_average_price": "卖均价",
                      "buy_profit": "买盈亏",
                      "sell_profit": "卖盈亏",
                      "unknown_device": "未知设备",
                      "t_plus_one": "T+1",



                      }
