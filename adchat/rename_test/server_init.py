#coding:utf8
'''
这个模块是用来创建日志的
'''
import sys
import logging

sys.path.insert(0, '..')#返回到上层目录

logger = logging.getLogger()        #日志对象
logger.setLevel(logging.NOTSET)     #日志类型
fmt = '%(asctime)s - %(process)s - %(levelname)s - %(message)s'#日志格式
handler = logging.StreamHandler()#输出到屏幕中
handler.setFormatter(fmt)
logger.addHandler(handler)
