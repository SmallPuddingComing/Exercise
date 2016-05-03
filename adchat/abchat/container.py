#coding:utf8
'''
这个模块是建立一个容器用于把所有的客户端放在一起，然后传送消息给每一个客户端。
worker 一个工作指的是一个线程，这个模块可以看成是现成的管理类
'''

from .log import logger

class WorkersContainListType(object):
    def __init__(self):
        self.workers = set()

    def add(self, worker):
        self.workers.append(worker)

    def rem(self, worker):
        try:
            self.workers.remove(worker)
        except KeyError:
            logger.error("WorkerContainListType, rem worker, keyError, key={0}".format(worker))

    def all_workers(self):
        return self.workers

    def amount(self):
        return len(self.workers)

class WorkersContainDictType(object):
    def __init__(self):
        self.workers = {}
        self._all_workers = set()

    def add(self, key, worker):
        if key in self.workers:
            self._all_workers.remove(self.workers[key])
        self.workers[key] = worker
        self._all_workers.add(worker)

    def rem(self, key):
        try:
            self._all_workers.remove(self.workers[key])
            del self.workers[key]
        except KeyError:
            logger.error("WorkersContainDictType, rem worker, keyError, key={0}".format(key))

    def all_workers(self):
        return self._all_workers

    def amuont(self):
        return len(self.workers)