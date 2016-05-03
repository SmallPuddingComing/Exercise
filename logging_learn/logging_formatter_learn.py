#coding:utf8

'''
Created on 2016-4-12
制定输出格式 给logging.handlers设置一个logging.Formatter对象
'''

import logging

#设置了日志对象
root_logger = logging.getLogger()
#一开始控制器对象为空
print root_logger.handlers

#创建控制器对象
'''logging.basicConfig(level=logging.NOTSET, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)
'''
logging.basicConfig(level=logging.NOTSET)

if root_logger.handlers:
    #输出当前控制器的格式
    print root_logger.handlers[0].formatter.format
    print root_logger.handlers[0].formatter._fmt

    #重新设置输出格式
    LOFFING_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
    DATE_FORMAT = '%y%m%d %H:%M:%S'
    formatter = logging.Formatter(LOFFING_FORMAT, DATE_FORMAT)
    root_logger.handlers[0].formatter = formatter
    logging.info('test')

    #输出控制器输出流，StreamHandler 默认的stream是stderr
    print root_logger.handlers[0].stream
