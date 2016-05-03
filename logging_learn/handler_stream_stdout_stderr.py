#coding:utf8

'''
Created on 2016-4-12
设置logger对象的控制器的输出流的方式 stream
重置stream
'''
import sys
import logging

root_logger = logging.getLogger()

stdout_handler = logging.StreamHandler(sys.__stdout__)
stdout_handler.level = logging.DEBUG
LOFFING_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%y%m%d %H:%M:%S'
formatter = logging.Formatter(LOFFING_FORMAT, DATE_FORMAT)
stdout_handler.formatter = formatter
logging.debug('hello')
root_logger.addHandler(stdout_handler)


stderr_handler = logging.StreamHandler(sys.__stderr__)
stderr_handler.level = logging.WARNING
stderr_handler.formatter = formatter
logging.warning('world')
root_logger.addHandler(stderr_handler)
#此时就有两个控制器
print root_logger.handlers