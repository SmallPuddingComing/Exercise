#coding:utf8
import time
import socket
from tcp_pack_test import dataRecevied, safeToWriteData

# def server():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(5)

while True:
    cs, addr = s.accept()
    print 'Now accept new connection from %s, %s...' % addr
    try:
        data = cs.recv(1024)
        if not data:
            break
        #封包
        result = dataRecevied(data)
        print "recrived the data from client..", result
    except StopIteration as e:
        print ("connect has error ,{0}".format(str(e)))

    time.sleep(1)
    data = '1234'
    #解包进行数据传输到客户端
    to_client_data = safeToWriteData(data, 10010)
    cs.sendall(to_client_data)



# if __name__ == '__main__':
#     server()