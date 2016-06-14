#coding:utf8

'''
creaet a amounts of activition code
1、创建一个文本，进行存贮激活码
2、激活码的组成来源于string模块里面的大小写字母和数字
3、制定序列号的长度，得到序列号后进行字符串化
4、序列号存进文本文件
5、自定义传参可以指定生成数量
'''

import string
import random

def create_activition_code(num, length=7):
    fp = open('C:/Users/yuanrong/Desktop/photos/Activition_code.txt', 'wb')
    L = [string.letters, string.digits]
    for i in xrange(num):
        mylist = [random.choice(L[random.randint(0,1)]) for x in xrange(length)]
        mylist = ''.join(mylist)
        fp.write(mylist + '\n')
    fp.close()

if __name__ == '__main__':
    create_activition_code(200)