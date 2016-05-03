#coding:utf8

'''
这个模块我猜是用于
'''
import gevent

class MasterInterface(gevent.Greenlet):
    def __init__(self, master):
        self.master = master
        super(MasterInterface, self).__init__(self)

    def enter(self, *args, *kwargs):
        raise NotImplemented()#网上面说NotImplemented不是异常，最好不要用raise，而是用return NotImplemented

    def _run(self):
        while True:
            gevent.sleep(0)
            data = self.enter()
            self.master.put(data)

class MasterInterfaceRedis(MasterInterface):
    def __init__(self, redis_client, key, master):
        self.redis_client = redis_client
        self.key  = key
        super(MasterInterfaceRedis, self).__init__(master)

    def enter(self):
        _, data = self.redis_client.blpop(self.key)#用于删除和获取列表中的第一个元素，或者阻塞直到可用
        return data