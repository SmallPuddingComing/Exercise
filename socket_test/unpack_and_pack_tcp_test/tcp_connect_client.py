#coding:utf8

'''
Created on 2016-4-11
TCP Convert the data
'''
import time
import socket
from tcp_pack_test import dataRecevied, safeToWriteData

# def client():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
# s.send("ott")
# s.send('100')

buffer = []
while 1:
    #线进行封包发送到服务端
    data = [97, 98, 99, 100]
    result = safeToWriteData(data, 1993)
    s.sendall(result)
    time.sleep(1)

    #收到服务端的消息进行解包
    data = s.recv(1024)
    result = dataRecevied(data)
    if data:
        buffer.append(result)
        print "recrived the data from the server...", buffer
    else:
        break




# if __name__ == '__main__':
#     client()




