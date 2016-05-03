#coding:utf8
'''
这个模块主要是记录程序异常的.日志添加空处理器
'''
import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def handler(self, record):
            pass

        def emit(self, record):
            pass

        def createLock(self):
            self.lock = None

__all__ = ['log', ]

logger = logging.getLogger('abchat')
logger.setLevel(logging.DEBUG)
logger.addHandler(NullHandler())