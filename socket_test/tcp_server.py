#coding:utf8

'''
create on:2015/11/24
author:YuanRong
function:基于TCP传输的服务端代码
'''

import socket
import time
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1', 9999))

#监听客服端发过来的消息
s.listen(5)
print "Wating for connection..."

def tcplink(sock, addr):
    print 'Now accept new connection from %s, %s...' % addr
    sock.send('welcome!')
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send('World, %s'% data)
    sock.close()
    s.close()
    print "accept treading %s, %s is close" % addr

#服务器永久循环的等待客服端发送请求
while True:
    #接收一个客服端新的连接
    sock, addr = s.accept() #accept()函数是等待并返回一个客服端的连接
    #创建新的线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()


    
