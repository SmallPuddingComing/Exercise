#coding:utf8

import gevent
import log
import time
from gevent.pool import Pool
from .container import WorkersContainListType
from .mixins import MailBoxMixin

MSG_TO_CLIENT = 1
MSG_TO_MASTER = 2

class ContinueFlag(object):pass

class Master(MailBoxMixin, gevent.Greenlet):
    def __init__(self, worker_class, woker_contain_type=WorkersContainListType, broadcast_backlog=50, dump_status_interval=60):
        self.worker_class = worker_class
        self.workers = woker_contain_type()#返回的是容器对象
        self.broadcast_backlog = broadcast_backlog
        self.dump_status_interval = dump_status_interval

        MailBoxMixin.__init__(self)
        gevent.Greenlet.__init__(self)
        gevent.spawn_later(1, self.dump_status_interval)#类似于定时器，（delay、*func）

    def dump_status_interval(self):
        '''
        跳转贮存的间隔
        '''
        while True:
            log.debug("workers amount:{0}".format(str(self.workers.amount())))
            gevent.sleep(self.dump_status_interval)

    def _run(self):
        while True:
            gevent.sleep(0)
            message = self.boxin.get()
            gevent.spawn(self.eit_message, message)#添加发送消息的函数和消息

    def eit_message(self, message):
        self.broadcast_message(message)

    def broadcast_message(self, message):
        pool = Pool(self.broadcast_backlog)
        pool.map_async(lambda w: self._worker_broadcast(w, message), #返回一个微线程的对象
                       self.workers.all_workers()).start()

    def _worker_broadcast(self, w, message):
        '''
        每一个woker发送消息给客户端
        '''
        w.receive(message, MSG_TO_CLIENT)

class BaseWorker(MailBoxMixin, gevent.Greenlet):
    def __init__(self, master, sock, adderss, client_send_interval=None):
        self.master = master
        self.sock = sock
        self.address = adderss
        self.client_send_interval = client_send_interval

        MailBoxMixin.__init__(self)
        gevent.Greenlet.__init__(self)
        self.first_receive = True
        log.dubug("{0} new woker".format(self.adderss))

    def _sock_recv(self):
        while True:
            gevent.sleep(0)
            data = self.sock_recv()
            if self.first_receive:
                self.first_receive = False
                continue

            if data is ContinueFlag:
                continue

            if not data:
                break
            self.receive(data, MSG_TO_MASTER)


    def sock_recv(self):
        raise NotImplemented()

    def receive(self, message, type):
        if type == MSG_TO_MASTER:
            self.master.put(message)
        elif type == MSG_TO_CLIENT:
            try:
                self.sendall(message)
            except Exception as e:
                log.logger.error("worker recvied ,unknown tp:{0}".format(str(e)))
                this = gevent.getcurrent()
                this.kill()
        else:
            log.logger.error("worker recvied ,unknown tp:{0}".format(type))

    def boxin(self):
        while True:
            gevent.sleep(0)
            data = self.inbox.put()
            self.receive(data, MSG_TO_CLIENT)

    def check_client_interval(self, interval=None):
        if interval and self.client_send_interval:
            return None

        timestamp = getattr(self, 'timestamp', None)
        self.timestamp = time.time()
        if timestamp:
            if self.timestamp - timestamp < self.client_send_interval:
                return ContinueFlag

    def brefor_worker_exit(self):
        raise NotImplemented()

    def _run(self):
        recv = gevent.spawn(self._sock_recv)
        get = gevent.spawn(self.boxin)

        def _clear(glet):
            glet.unlink(_clear)
            gevent.killall([recv, get])

        recv.link(_clear)
        get.link(_clear)
        gevent.joinall([recv, get])
        self.brefor_worker_exit()
        log.debug('{0} worker died'.format(self.address))



