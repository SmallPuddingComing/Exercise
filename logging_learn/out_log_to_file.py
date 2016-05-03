#coding:utf8

'''
Created on 2016-4-12
将日志输出到文件中
'''

import logging

root_logger = logging.getLogger()
LOFFING_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%y%m%d %H:%M:%S'
logging.basicConfig(level=logging.NOTSET, format=LOFFING_FORMAT, datefmt=DATE_FORMAT, filename='test.log', filemode='a')

handler = logging.FileHandler('test.log')
root_logger.addHandler(handler)
print root_logger.handlers
print root_logger.level
logging.debug("hello world")