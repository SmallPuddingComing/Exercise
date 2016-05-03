#coding:utf8

'''
模拟的是socket套接字的连接和发送数据，建立了数据缓冲区
这个模块是用来进行消息发送前组装和解包的，有三种不同的类型，一个是邮箱存贮，一个是二进制数据传输，还有文件的传输
'''

import struct
import ctypes
from .log import logger
from gevent.queue import Queue

class MailBoxMixin(object):
    '''
    邮箱存贮消息
    '''
    def __init__(self):
        self.boxin = Queue.queue()

    def add(self, message):
        self.boxin.put(message)

#处理二进制的数据，比如说存贮文件和socket的操作，这个时候可以用struct模块实现。
#这里学到一个新的知识点就是self.buf的作用，防止每次pack在内存中会分配一个内存给返回的对象，造成资源的浪费，这里用到一个早就分配好的缓存区，反复利用，
#这里需要用到的函数--struct.Struct.pack_into(buffer, offset, *values) 相对应的解包就是unpack_from(buffer, offset)。他们两都只能对string buff对象操作。
class StreamSocketMixin(object):
    def __init__(self, pre_malloc_size):
        self.head_t = struct.Struct('>i')#打包的格式
        if pre_malloc_size:
            self.buf = ctypes.create_string_buffer(pre_malloc_size)#创建一个字符串缓存区
        else:
            self.buf = None

    def sendall(self, message):
        msg_len = len(message)
        fmt = '>i%ds' % msg_len
        msg_st = struct.Struct(fmt)
        if self.buf:
            msg_size = struct.calcsize(fmt)#计算给定的格式fmt占用了多少字节
            try:
                msg_st.pack_into(self.buf, 0, msg_len, message)#将长度为msg_len的message进组装进缓存区，offset是放入偏移量
                x = self.buf.raw[:msg_size]
                ctypes.memset(self.buf, 0, msg_size)#clear up the malloc内存清0
            except struct.error:
                logger.error("pack_into error, this worker never use pack_into again")
                self.buf = None
                x = msg_st.pack(msg_len, message)
                pass
        else:
            x = msg_st.pack(msg_len, message)

        self.sock.sendall(x)

    def sock_recv(self):
        try:
            data = self.sock.recv(4)#收到的是四个字节长度的二进制数据
            if not data:
                 return None
            length = self.head_t.unpack(data)
            length = length[0]
            data = self.sock.recv(length)
        except Exception as e:
            logger.error("StreamSocketMixin, sock_recv error:{0}".format(str(e)))
            return None

        return data

class LineSocketMixin(object):
    '''
    文件的传输
    '''
    def sendall(self, message):
        if not self.wfile.endswith('\n'):
            message = '%s\n', message
        self.wfile.write(message)
        self.wfile.flush()

    def sock_recv(self):
        try:
            data = self.rfile.readline()
            return data
        except Exception as e:
            logger.error("LineSocketMixin, sock_recv error:{0}".format(str(e)))
            return ''










