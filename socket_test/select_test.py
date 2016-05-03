#coding:utf8
'''
1、改程序是利用socket进行通信，将接受客户端传来的消息，然后又还给客户端
2、首先建立一个TCP/IP socket，将其设置为非阻塞，然后进行bind和listen
3、如果设置的timeout超时，select函数会返回三个空列表
'''

import select
import socket
import Queue

#create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

#set option reuse setsockopt(level, name, value),level应用于那一层、name是涉及的拿一个选项、value选项的
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_adderss = ("127.0.0.1", 5080)
server.bind(server_adderss)

server.listen(10)

#create three agrs of select function ,the function is check out the socket ifnot get data from client
inputs = [server]
outputs = []
message_queues = {}
timeout = 20

#三个列表进行轮询，针对不同的socket进行不同的处理。循环直到外层的inputs
while inputs:
    print "watting for next event"
    readable, writeable, exceptionable = select.select(inputs, outputs, inputs, timeout)#如果超时就会返回三个空列表

    if not (readable or writeable or exceptionable):
        print "Time out "
        break

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print "  connection from ", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)#收到来自客户端的数据，然后将其存贮当前提出来的某一客户端队列里面
            if data:
                print " recived a %s from %s" % (data, s.getpeername())
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print " closing the ", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writeable:
        try:
            next_Mag = message_queues[s].get_nowait()#取出当前的socket对应存放在Queue的消息
        except Queue.Empty:
            if s in outputs:
                print "  ", s.getpeername(), "is empty"
                outputs.remove(s)
        else:
            print "seding ", next_Mag, " to ", s.getpeername()
            s.send(next_Mag)

    for s in exceptionable:
        inputs.remove(s)

        print "excption conndition on  %s" % s.getpeername()

        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]





