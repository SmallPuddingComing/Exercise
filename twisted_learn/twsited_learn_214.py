#coding:utf8

'''
create on:2016-2-14
主要是基于事件的异步调用
'''

from twisted.internet import reactor
import time

reactor.suggestThreadPoolSize(30)
def tt(i, j):
    if i =='10':
        reactor.stop()
    while 1:
        print i,'-------------', j
        time.sleep(2)

def gg(i, j):
    time.sleep(2)
    if i =='10':
        reactor.stop()
    print i,'-------------', j
    time.sleep(2)

#for i in xrange(50):
    #reactor.callFromThread(gg, i, i)
    #reactor.callInThread(tt, i, i) #无线循环的线程
#callFromThread使用的是reactor本身的线程跑的，就是用eventloop的线程跑，他会阻塞主任务，可以使用reactor.stop()
#因为reactor有自己的线程池...callInThread是一个单独开启的线程，和主eventloop没有关系，所哟reactor.stop()是没有用的

#reactor自带了一个顺序执行的组件是callLater，是一个计划任务的执行，第一秒执行谁，第二秒执行谁~
def printTime():
    print 'Current time is', time.strftime("%H:%M:%S")
def stopReactor():
    print "Stopping reactor"
    reactor.stop()
for i in xrange(1,6):
    if i == 5:
        reactor.callLater(i, stopReactor)
    reactor.callLater(i, printTime)
print "Running the reactor"#主要理解reactor就是基于事件~

print "I want to start"
reactor.run()
