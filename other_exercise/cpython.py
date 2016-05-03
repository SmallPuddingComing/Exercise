#coding:utf8
import threading, time, random
#方法一
count = 0
# class Counter(threading.Thread):
#     def __init__(self, lock, threadname):
#         super(Counter, self).__init__(name=threadname)#这里一定要显示调用基类的初始化函数
#         self.lock = lock
#
#     def run(self):#run()方法是在所有的线程开启后执行，所有的相关的逻辑写在里面
#         global count
#         self.lock.acquire()
#         for i in xrange(1000):
#             count += 1
#         self.lock.release()
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     for i in xrange(5):
#         Counter(lock, "thread-"+str(i)).start()
#     time.sleep(2)#确定线程都运行完毕
#     print "thread_method_1 is result:", count

#方法二
# def doAdd():
#     global count, lock
#     lock.acquire()
#     for i in xrange(1000):
#         count += 1
#     lock.release()
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     for i in xrange(5):
#         threading.Thread(target=doAdd, args=(), name='thread-'+str(i)).start()
#     time.sleep(2)
#     print "thread_method_2 is result:", count

#对于threading.Thread()的初始化函数原型
#def __init__(self, group=None, target=None, name=None, args=(), kwargs={})
#group是留以后扩展的。target是目标可调用的对象，在线程起送后执行，name是线程的名字一般由"Thread-N",args和kwargs是表示调用target时候参数列表和关键字参数


#条件控制时序关系condition--捉迷藏
class Hidder(threading.Thread):
    def __init__(self, cond, name):
        super(Hidder, self).__init__(name=name)
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)

        self.cond.acquire()
        print self.name + " 我把眼睛蒙上了，游戏开始"
        self.cond.notify()#唤醒，占用一个锁
        self.cond.wait()#释放所有的占用的锁，同时线程被挂起

        print self.name + " i am find you"
        self.cond.notify()
        self.cond.release()

        print self.name + " i am win"

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__(name=name)
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)

        self.cond.acquire()
        self.cond.wait()

        print self.name + " i am hide ok, can you find me?"
        self.cond.notify()
        self.cond.wait()

        self.cond.release()
        print self.name + " ok, you find me"

if __name__ == '__main__':
    cond = threading.Condition()
    seeker = Seeker(cond, 'seeker')
    hider = Hidder(cond, 'hider')
    seeker.start()
    hider.start()