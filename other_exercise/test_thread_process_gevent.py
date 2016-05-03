#coding:utf8

import time
import urllib2
import requests
import multiprocessing
import threading
import Queue
import gevent.pool
import gevent.monkey

def start_time():
    return time.time()

def ticT(stime):
    usetime = time.time() - stime
    return round(usetime, 3)

def download_urillb(url):
    request = urllib2.Request(url, headers={"user-agent":'Mozilla/5.0'})
    response = urllib2.urlopen(request)
    data = response.read()
    try:
        data = data.decode("gbk")
    except UnicodeDecodeError:
        data = data.decode("utf8", 'ignore')
    return data     # response.status,

def download_request(url):
    request = requests.get(url, headers={'user-agent':'Mozilla/5.0'})
    return request.status_code, request.text

class threadPoolManage():#线程管理池
    def __init__(self, urls, threadNum=20):
        self.workQueue = Queue.Queue()
        self.threadPool = []
        self.__initWorkQueue(urls)
        self.__initThreadPool(threadNum)

    def __initWorkQueue(self, urls):
        for i in urls:
            self.workQueue.put((download_request, i))

    def __initThreadPool(self, threadNum):
        for i in xrange(threadNum):
            self.threadPool.append(work(self.workQueue))

    def waitAllCompelet(self):
        for thread in self.threadPool:
            if thread.isAlive():
                thread.join()

class work(threading.Thread):
    def __init__(self, workQueue):
        threading.Thread.__init__(self)
        self.workQueue = workQueue
        self.start()

    def run(self):
        while 1:
            if self.workQueue.qsize():
                do, args = self.workQueue.get(block=False)
                do(args)
                self.workQueue.task_done()
            else:
                break

if __name__ == '__main__':
    urls = ['http://www.zhihu.com'] * 10
    urllibL = []        #系统自带标准库
    requestsL = []      #第三方库
    multiPool = []      #进程池
    threadPool = []     #线程池
    N = 20
    poolNum = 100

    for i in xrange(N):
        print 'start %d try' % i
        urllibT = start_time()
        jobs = [download_urillb(url) for url in urls]
        urllibL.append(ticT(urllibT))
        print '1'

        requestsT = start_time()
        jobs = [download_request(url) for url in urls]
        requestsL.append(ticT(requestsT))
        print '2'

        multipoolT = start_time()
        pool = multiprocessing.Pool(poolNum)
        data = pool.map(download_request, urls)
        pool.close()
        pool.join()
        multiPool.append(ticT(multipoolT))
        print '3'

        threadpoolT = start_time()
        threadpool = threadPoolManage(urls, threadNum=20)
        threadpool.waitAllCompelet()
        threadPool.append(ticT(threadpoolT))
        print '4'



