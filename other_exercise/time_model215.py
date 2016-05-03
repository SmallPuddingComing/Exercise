#coding:utf8

'''
created on: 2016/2/15
尝试封装一个自定义的时间计时模块
'''
import time
import functools

class TimeCost(object):
    def __init__(self, unit='s', precision=4, logger=None):
        self.start = None
        self.ended = None
        self.total = 0
        self.unit = unit
        self.precision = precision
        self._funcunit = {'s':1, 'ms':1000, 'us':1000000}
        self.logger = logger

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return wrapped

    def __enter__(self):
        if self.precision < 0:
            KeyError("must get 0")
        if self.unit not in self._funcunit:
            KeyError("unit is not exit")
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ended = time.time()
        self.total = (self.ended-self.start) * self._funcunit[self.unit]
        if self.precision != 0:
            self.total = round(self.total , self.precision)
        else:
            self.total = int(self.total)

        if self.logger:
            self.logger.info("this cost {0}{1}".format(self.total, self.precision))

    def __str__(self):
        print "this cost {0}{1}".format(self.total, self.precision)

