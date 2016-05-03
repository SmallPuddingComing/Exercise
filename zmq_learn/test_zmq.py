#coding:utf8

import zmq, gevent, datetime, time, random, sys
from random import choice
from gevent import monkey; monkey.patch_all()
from gevent_zeromq import monkey_patch; monkey_patch()
#使用monkey_patch是为了在大部分阻塞上打补丁，这样可以用hub调度而不必堵塞。线程系统会用线程代替微线程

#对于普通的纯python程序在monkey patching下能不做修改的情况下变成异步的
# def compute(x, y):
#     print "Compute %s + %s..." % (x, y)
#     gevent.sleep(1.0)
#     print "o^o"
#     return x + y
#
# def print_sum(x, y):
#     result = compute(x, y)
#     print "%s + %s = %s" % (x, y, result)
#
# print_sum(1, 2)

#zmq有三种基本模式
#1、请求应答模式（req和rep）
#  消息双向的，一去一回模式req端请求的消息，rep必须答复req端的请求
#2、发布订阅模式（pub和sub）
#  消息是单向的，由发布端发布制定主题的消息，订阅端可以订阅喜欢的主题，订阅端只会收到自己订阅的主题，发布端发布一条消息，多个订阅端可以接受
#3、push pull模式
#  消息是单向的，push的任何消息始终只会有一个pull接受

#这三种是zmq模式的基本类型，往后发展的代理模式和路由模式都是由这三种进行组合的


#阻塞式的
#请求应答模式
# def zmq_server():
#     context = zmq.Context()
#     socket = context.socket(zmq.PUB)
#     socket.bind("tcp://*:5555")
#
#     countries = ['netherlands', 'bralize', 'germany', 'protugal']
#     events = ['yellow card', 'red card', 'goal', 'corner', 'foul']
#
#     for i in xrange(1, 20):
#         stock_symbol = choice(countries)
#         stock_event = choice(events)
#         msg = "{0} ${1}".format(stock_symbol, stock_event)
#         print ("Sending Message: {0}".format(msg))
#         socket.send_multipart([stock_symbol, stock_event])
#         time.sleep(3)#为了防止消息
#
#     # while 1:
#     #     message = socket.recv()
#     #     print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Receviced resquest:" ,message
#     #     gevent.sleep(1)
#     #     socket.send("world")
#
# def zmq_client():
#     context = zmq.Context()
#
#     print "Connrcting to hello world sever..."
#     socket = context.socket(zmq.SUB)
#     socket.connect("tcp://localhost:5555")
#     socket.setsockopt(zmq.SUBSCRIBE, "netherlands")#过滤的条件
#     socket.setsockopt(zmq.SUBSCRIBE, "germany")
#
#     poller = zmq.Poller()
#     poller.register(socket, zmq.POLLIN)
#
#     # while 1:
#     #     topic, msg = socket.recv_multipart()
#     #     print "Recevied msg: %s" % topic
#
#     for sub in xrange(1, 10):
#         try:
#             socks = dict(poller.poll())
#         except KeyboardInterrupt:
#             break
#
#         if socket in socks:
#             print "subbing ...."
#             msg = socket.recv_multipart()
#             print "Recevied a sub: %s" % msg
#             time.sleep(1)

    # for request in xrange(1, 10):
    #     print "Sending request", request, "...."
    #     socket.send("Hello")
    #
    #     message = socket.recv()
    #     print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Recived reply", request, "[", message,"]"


#非阻塞式,发布pub-订阅sub模式和push-pull都可以用poller来实现非阻塞式的通信
# def zmq_server_2():
#     context = zmq.Context()
#     socket = context.socket(zmq.REP)
#     socket.bind("tcp://*:5556")
#
#     poller = zmq.Poller()
#     poller.register(socket, zmq.POLLIN)
#     while 1:
#         #这里的poll后面的参数是毫秒
#         socks = dict(poller.poll(1))
#         if socket in socks and socks[socket]==zmq.POLLIN:
#             #监控如果socket有可读入的事件，那么接收消息
#             message = socket.recv()
#             print "Recevied a msg : %s" % message
#
#             gevent.sleep(1)
#             #回一个消息过去
#             socket.send('I am fine '+str(time.time()))

# def zmq_client_2():
#     context = zmq.Context()
#     socket = context.socket(zmq.REQ)
#     socket.connect("tcp://localhost:5556")
#
#
#     for i in xrange(1,15):
#         socket.send("Who are you?")
#
#         gevent.sleep(1)
#
#         msg = socket.recv()
#         print "Received a msg : %s" % msg
#
#
#zmq--PAIR双向消息
# def zmq_server_pair():
#     context = zmq.Context()
#     socket = context.socket(zmq.PAIR)
#     socket.bind("tcp://*:5000")
#     while 1:
#         msg = socket.recv()
#         print msg
#         time.sleep(1)
#
#         socket.send('fine')
#
# def zmq_client_pair():
#     context = zmq.Context()
#     socket = context.socket(zmq.PAIR)
#     socket.connect("tcp://localhost:5000")
#     while 1:
#         socket.send('how are you?')
#         time.sleep(1)
#         msg = socket.recv()
#         print msg

#parallel_Pip
def pip_sink_server():
    context = zmq.Context()
    received = context.socket(zmq.PULL)
    received.bind("tcp://*:5558")
    s = received.recv()
    tstart = time.time()

    for task_nbr in xrange(100):
        s = received.recv()

        if task_nbr % 10 == 0:
            sys.stdout.write(':')
        else:
            sys.stdout.write('.')
        sys.stdout.flush()
    tend = time.time()
    print "Total expand time :%d" % (tend - tstart)

def pip_server():
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")

    sink = context.socket(zmq.PUSH)
    sink.connect("tcp://localhost:5558")

    sink.send(b'0')
    random.seed()

    total_msec = 0
    for task_nbr in xrange(100):
        workload = random.randint(1, 100)
        total_msec += workload

        sender.send_string(u'%i' % workload)
    print "Tota; expected cost: %s msec" % total_msec
    time.sleep(1)


def pip_client():
    context = zmq.Context()
    recevied = context.socket(zmq.PULL)
    recevied.connect("tcp://localhost:5557")

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")

    while 1:
        s = recevied.recv()

        sys.stdout.write('.')
        sys.stdout.flush()

        time.sleep(1)
        sender.send(b'')

if __name__ == '__main__':
    greenlets = [gevent.spawn(pip_server), gevent.spawn(pip_client), gevent.spawn(pip_sink_server)] #永年携程控制服务器和客户端的并发执行
    gevent.joinall(greenlets)



#zmq均衡负载的模式
# def client():
#     context = zmq.Context()
#     socket = context.socket(zmq.REQ)
#     socket.connect("tcp://localhost:5559")
#     #发送问题到中间这ROUTER
#     for request in range(1, 11):
#         socket.send("Hello")
#         message = socket.recv()
#         print("Received reply %s [%s]" % (request, message))
#     socket.close()
#     context.term()
#
# def router_dealer():
#     context = zmq.Context()
#     frontend = context.socket(zmq.ROUTER)
#     backend = context.socket(zmq.DEALER)
#     frontend.bind("tcp://*:5559")
#     backend.bind("tcp://*:5560")
#
#     poller = zmq.Poller()
#     poller.register(frontend, zmq.POLLERR)
#     poller.register(backend, zmq.POLLERR)
#
#     while 1:
#         socks = dict(poller.poll())
#         #fronetend收到提问后，有backend发送给REP端
#         if socks.get(frontend) == zmq.POLLERR:
#             message = frontend.recv_multipart()
#             backend.send_multipart(message)
#         # backend 收到了回答后，由frontend发送给REQ端
#         if socks.get(backend) == zmq.POLLERR:
#             message = backend.recv_multipart()
#             frontend.send_multipart(message)
#
# def server():
#     contect = zmq.Context()
#     socket = contect.socket(zmq.REQ)
#     socket.connect("tcp://localhost:5560")#在服务端没有使用bind，而是调用了connect函数主动去连接DEALER
#
#     while 1:
#         message = socket.recv()
#         print("Recevied request :%s" % message)
#         socket.send("Wrold")
#
# if __name__ == '__main__':
#     greenlets = [gevent.spawn(server), gevent.spawn(router_dealer), gevent.spawn(client)] #永年携程控制服务器和客户端的并发执行
#     gevent.joinall(greenlets)
