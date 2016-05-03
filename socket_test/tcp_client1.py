#coding:utf8

'''
create on 2015/11/24

author yuanrong

function :基于 TCP 协议传输的socket
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1', 9999))
#接收欢迎消息
print s.recv(1024)
#发送消息
mylist = ['mechial', 'lucy', 'tom']
for data in mylist:
    s.send(data)
    data = s.recv(1024)
    if not data:
        break
    print data
s.send('exit')
s.close()
