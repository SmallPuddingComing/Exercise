#coding:utf-8

import traceback


def hello():
    print "Hello from the Reactor loop"
    print "Later.."

def stack():
    print "the python stack"
    traceback.print_stack()
    
from twisted.internet import reactor
#reactor.callWhenRunning(hello)
#reactor.callWhenRunning(stack)
#print "Starting the reactor"
#reactor.run()


class Countdown(object):
    counter = 5
    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter,'...'
            reactor.callLater(1, self.count)
            self.counter -= 1
       
#reactor.callWhenRunning(Countdown().count)
#print 'Start'
#reactor.run()
#print "stop"

#import getPage            
def processPage(page):
    print page

def logError(error):
    print error

def finshProcessing(value):
    print "Shutting down ..."
    reactor.stop()

url = "http://google.com"
#deferred = getPage(url)
#deferred.addCallBack(success, failure)
#deferred.addBoth(stop)

#reactor.run()

from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReviced(self, data):
        print "start transports the server between the client"
        self.transports.write(data)
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(8000,EchoFactory())
reactor.run()
