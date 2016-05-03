#coding:utf8

import gevent, httplib
from gevent.event import AsyncResult,Event

'''异步HTTP处理'''
def Aysnc(func, *args, **kwargs):
    a = AsyncResult()
    def __call():
        a.set(func(*args, **kwargs))#存贮一个值，唤醒等待者,有一个回调
    gevent.spawn(__call, *args, **kwargs)
    return a.get()#取出一个值

def httpHandler(host, post, url, data, timeout=500):
    conn = httplib.HTTPConnection(host, post, None,timeout)
    conn.request(method='POST', url=url, body=data)
    return conn.getresponse()

def aysncHttp(host, post, url, data, timeout=500):
    return Aysnc(httpHandler, host, post, url, data, timeout)

'''同步处理'''
def Sync(func, *args, **kwargs):
    b = Event()
    def __call():
        b.set(func(*args, **kwargs))
    gevent.spawn(__call, *args, **kwargs)
    return b.wait(timeout=500)#阻塞直到超时或者是下一次set，结果就是相应的返回是False or True

def syncHttp(host, post, url, data, timeout=500):
    return Sync(httpHandler, host, post, url, data, timeout)
