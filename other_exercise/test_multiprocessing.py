#coding:utf8
import os, time
import threading
import multiprocessing

def worker(sign, lock):
    lock.acquire()
    print (sign, os.getpid())
    lock.release()

print('Main', os.getpid())

#multi-thread
# record = []
# lock1 = threading.Lock()
# for i in xrange(5):
#     thread = threading.Thread(target=worker, args=('thread', lock1))
#     thread.start()
#     record.append(thread)
# for thread in record:
#     thread.join()

#multi-process
def gg():
    record = []
    lock2 = multiprocessing.Lock()
    for i in xrange(5):
        process = multiprocessing.Process(target=worker, args=('process',lock2))
        process.start()
        record.append(process)
    for process in record:
        process.join()

#process_pool
def func(msg):
    for i in xrange(3):
        print msg
        time.sleep(1)
    return "done " + msg

def doPool():
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = " hello %d" %(i)
        result.append(pool.apply_async(func, args=(msg, )))
    pool.close()
    pool.join()

    for res in result:
        print res.get()
    print "Sub-process(es) done"

#input work
def inputQ(queue):
    info = str(os.getpid()) + "(put):" + str(time.time())
    queue.put(info)

#out work
def outputQ(queue, lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + "get():" + info)
    lock.release()

def start_process():
    #发现多进程并发处理需要添加这一行
    multiprocessing.freeze_support()
    # gg()
    doPool()

    #Queue
    recode1 = []
    recode2 = []

    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue(3)

    start_time = time.time()
    for i in xrange(10):
        process = multiprocessing.Process(target=inputQ, args=(queue,))
        process.start()
        recode1.append(process)

    for i in xrange(10):
        process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        process.start()
        recode2.append(process)

    for p in recode1:
        p.join()
    queue.close()#没有更多的对象会来，关闭queue

    for p in recode2:
        p.join()

    end_time = time.time()
    print "totall time: ",end_time - start_time

if __name__ == '__main__':

    start_process()
    # import profile
    # profile.run('start_process()')

