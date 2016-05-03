#coding:utf8

'''
created on: 2016.2.15
日志模块
测试计时模块
正态分布来平滑随机概率
'''

import logging
import random

from other_exercise.time_model215 import TimeCost


N = 20

def init_logger(logfile):
    logger = logging.getLogger()#生成一个日志对象
    logger.setLevel(logging.INFO)
    fmt = '%(asctime)s - %(process)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)#生成格式器
    handler = logging.FileHandler(logfile)#生成处理器,写入日志文件
    handler_1 = logging.StreamHandler()#用于输出到控制台
    handler.setFormatter(formatter)#将格式器设置在生成器上面
    handler_1.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(handler_1)
    return logger

logger = init_logger('debug')

@TimeCost('s', 0, logger)
def test():
    def b(x):
        print x * x
    def a():
        for i in xrange(50):
            i += i
            b(i)
    a()

if __name__ == '__main__':
    #一个上下文封装的执行环境
    with TimeCost('s', 0) as t:
        pool = []
        result = []
        for i in xrange(N):
            if not pool:
                pool = [0]*1 + [1]*19   #生成一个列表，有19个1和1个0
            random.shuffle(pool)        #随机打乱列表
            result.append(pool[-1])     #取列表最后一位
            del pool[-1]                #删除最后一位
    print t.total, result
    test()