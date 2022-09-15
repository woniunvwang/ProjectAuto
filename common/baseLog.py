# -*- coding:utf-8 -*-
import logging
from pathlib import Path

# 创建日志记录器
logger = logging.getLogger()
# 设置日志级别
logger.setLevel(logging.INFO)

# 设置日志输出格式
format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

# 创建一个Handler用于将日志写入文件
# logFile = '/Users/centihenries/atpAutomationLog/log.txt'
# logFile = Path('../log/log.txt').resolve()
# fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
# fh.setLevel(logging.INFO)
# fh.setFormatter(format)
# logger.addHandler(fh)
#
# # 创建一个Handler用于控制台输出日志
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# ch.setFormatter(format)
# logger.addHandler(ch)
