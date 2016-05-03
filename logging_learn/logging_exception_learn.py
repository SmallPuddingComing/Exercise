#coding:utf8

'''
Created on 2016-4-12
捕捉一个异常，输出执行堆栈
使用logging.exception(),或在调用logging.debug()等方法时加上exc_info = True参数
'''

import logging

root_logger = logging.getLogger()
LOGGING_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
DATE_FMT = "%y%m%d %H:%M:%S"
logging.basicConfig(level=logging.WARNING, format=LOGGING_FORMAT, datefmt=DATE_FMT)

try:
    0 / 0
except:
    logging.exception('Catch an exception.')
    print '-'*40
    logging.warning('Catch an exception.', exc_info=True)
