#coding:utf8

import socket
import time

messages = {"This is a message",
            "It will be sent",
            "in pairs"}

print "connect to the server"

sockets = []
address = ("127.0.0.1", 5080)

for i in xrange(10):
    sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

for s in sockets:
    s.connect(address)

counter = 0
for message in messages:
    for s in sockets:
        counter += 1
        print "%s sending %s" % (s.getpeername(), message+" version "+str(counter))
        s.send(message + " version " + str(counter))

    for s in sockets:
        data = s.recv(1024)
        print "recvied  %s from %s" % (data, s.getpeername())
        if not data:
            print "closing socket" % s
            s.close()