#coding:utf8

'''
Create on 2016-4-11
test the pack from TCP
'''
import logging
import struct

class DataPackProtocol:
    def __init__(self, HEAD_0 = 0, HEAD_1 = 0, HEAD_2 = 0, protocolVersion = 0):
        '''
        @param HEAD_0 : int 协议头0
        @param HEAD_1 : int 协议头1
        @param protocolVersion : int 协议版本号
        '''
        self.HEAD_0 = HEAD_0
        self.HEAD_1 = HEAD_1
        self.HEAD_2 = HEAD_2
        self.protocolVersion = protocolVersion

    def setHEAD_0(self, HEAD_0):
        self.HEAD_0 = HEAD_0

    def setHEAD_1(self, HEAD_1):
        self.HEAD_1 = HEAD_1

    def setHEAD_2(self, HEAD_2):
        self.HEAD_2 = HEAD_2

    def setProtocolVersion(self, protocolVersion):
        self.protocolVersion = protocolVersion

    def getHeadLength(self):
        return 12

    def unpack(self, dpack):
        try:
            uData = struct.unpack('!ssss2I', dpack)
        except:
            print "unpack data is fail "
            return {'result':False, 'command':0, 'length':0}

        #把字符转换成整型
        HEAD_0 = ord(uData[0])
        HEAD_1 = ord(uData[1])
        HEAD_2 = ord(uData[2])
        protocolVersion = ord(uData[3])
        length = uData[4] - 4
        command = uData[5]

        if HEAD_0!=self.HEAD_0 or HEAD_1!=self.HEAD_1 or HEAD_2!=self.HEAD_2 or\
                        protocolVersion!=self.protocolVersion:
            return {'result':False, 'command':0, 'length':0}
        return {'result':True, 'command':command, 'length':length}


    def pack(self, command, response):
        #把整型变成字符串
        HEAD_0 = chr(self.HEAD_0)
        HEAD_1 = chr(self.HEAD_1)
        HEAD_2 = chr(self.HEAD_2)
        protocolVersion = chr(self.protocolVersion)
        length = response.__len__() + 3
        commandID = command
        data = struct.pack('!ssss2I', HEAD_0, HEAD_1, HEAD_2, protocolVersion,
                           length, commandID)
        data = data + response
        return data

def dataRecevied(data):
    head_0 = data[0]
    head_1 = data[1]
    head_2 = data[2]
    datapack = DataPackProtocol(head_0, head_1, head_2, 200)
    length = datapack.getHeadLength()
    unpackdata = datapack.unpack(data[:length])
    if not unpackdata.get('result'):
        print "illegal data pack -- "
    command = unpackdata.get('command')
    rlength = unpackdata.get('length')
    request = data[length:length+rlength]
    if request.__len__() < rlength:
        print "lose some data"
    response = datapack.unpack(request)
    print "unpack the data", response
    return response

def safeToWriteData(data, command):
    head_0 = data[0]
    head_1 = data[1]
    head_2 = data[2]
    protocolVersion = data[3]
    datapack = DataPackProtocol(head_0, head_1, head_2, protocolVersion)
    data = map(str, data)   #每个元素变成字符
    data = "".join(data)    #进行列表转换成字符
    result  = datapack.pack(command, data)
    print "pack the data...", result
    return result