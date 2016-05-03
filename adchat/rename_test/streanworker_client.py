#coding:utf8

import gevent
from gevent import socket
from gevent.pool import Pool
import random
import struct

pool = Pool(500)
head_fmt = struct.Struct('>i')

def client(cid):
    s = socket.create_connection(('127.0.0.1', 7890))
    def send():
        times = 0
        while times < 100:
            times += 1
            gevent.sleep(0)
            nums = str(random.randrange(10, 10000))
            data = '%s, from client %s' % (nums, cid)
            data_len = len(data)
            fmt = struct.Struct('>i%ds', data_len)
            data = fmt.pack(data_len, data)
            s.sendall(data)
            print "client ", cid, 'sends:', nums

    def recv():
        while True:
            data = s.recv(4)
            data = head_fmt.unpack(data)
            data_len = data[0]
            data = s.recv(data_len)
            print 'client', cid, 'recive', data

    send_job = gevent.spawn_later(1, send)#延迟一秒添加进协程启动中
    recv_job = gevent.spawn(recv)

    def clear():
        gevent.killall([send_job, recv_job])
        s.close()

    send_job.link(clear)
    recv_job.link(clear)
    gevent.joinall([send_job, recv_job])
    print 'client', cid, 'finsh'

clients = pool.imap(client, xrange(1000))
