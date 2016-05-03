#coding:utf8

'''
Created on 2016-4-12
设置logging的输出等级
'''

import logging

#logging.info 默认不输出任何东西，是因为默认生成的root_logger
#是logging.WARNING,低于该级别就不输出
logging.info('test')
root_logger = logging.getLogger()
level = root_logger.level
print logging.getLevelName(level)


#为了是info输出，这边修改了root_logger的值为0，因为info20高于0 能输出
root_logger.level = logging.NOTSET
logging.info('test')

#-----------------------------------------------------#

#配置handler
print root_logger.handlers #[]
logging.basicConfig(level=logging.NOTSET)
print root_logger.handlers #有值
logging.info('test')

