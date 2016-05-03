#coding:utf8
'''
create on 2015/11/24

author yuanrong

function :基于 TCP 协议传输的socket
'''

import socket

#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn', 80))#这里放入IP和端口 参数形式是元组
#发送数据
s.send("GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n")
#发送关闭
s.send('exit')

print '-'* 40

#接收从服务端发来的消息
buffer = []
while True:
    #每次最多接受1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

#收到的数据进行处理
header, html = data.split('\r\n\r\n', 1)
print header
with open('sina.html', 'wb')as f:
    f.write(html)
