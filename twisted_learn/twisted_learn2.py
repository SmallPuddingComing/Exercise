#coding:utf8

'''
created on:2016/2/14

Twisted回调是用了defer来进行注册回调，实现同步函数的异步调用的代码
'''

import time
import os, sys
from twisted.internet import reactor,defer
from twisted.internet.threads import deferToThread
from twisted.python import threadable; threadable.init(1)
deferred = deferToThread.__get__

def todoprint_(result):
    print result

def running():
    "Print a few dots on stdout while the reactor is running"
#    sys.stdout.wirte('.');sys.stdout.flush()
    print '.'
    reactor.callLater(.1, running)

@deferred
def sleep(sec):
    "A blocking function magically converted in non-blocking one"
    print "start sleep %s" % sec
    time.sleep(sec)
    print "need sleep %s" % sec
    return 'OK'

def test(n, m):
    print "fun test() is start"
    vals = []
    keys = []
    for i in xrange(m):
        vals.append(i)
        keys.append('a%s'% i)
    d = None
    for i in xrange(n):
        d = dict(zip(keys, vals))
    print "fun test() is end"
    return d
if __name__ == '__main__':
#one
    sleep(10).addBoth(todoprint_)
    reactor.callLater(.1, running)
    reactor.callLater(3, reactor.stop)
    print "go~go begain!"
    reactor.run()
#two
    aa = time.time()
    de = defer.Deferred()
    de.addCallback(test)
    reactor.callInThread(de.callback,10000000,100)
    print 'time :',time.time() - aa
    print "wait a minute,let us do other things first"
    print de
    print "go go end"

#遇到啊问题，首先是那个阻塞函数应该是没有执行的，所有才会有时间为0的情况，但是测试的时候进去调试也没有发下异常 有待考量