#coding:utf8

#丑数的定义：将给订的书除以2/3/5，知道无法整除，也就是除以2/3/5的余数不再是0时停止，如果此时得到的结果是1，
# 说明所有的因子都是2或者3或者5，如果不是1则不是丑数

def isUgly(num):
    _isUgly = False
    while (num%2==0 or num%3==0 or num%5==0):
        if num%2 == 0:
            num = num/2
        elif num%3 == 0:
            num = num/3
        elif num%5 == 0:
            num = num/5

    if num != 1:
        print "this is not Ugly number"
    else:
        _isUgly = True
        print "yes ,is a Ugly number"
    print "test ugly_1 result is:",num
    return _isUgly

def Ugly_2(num):
    mylist = [2,3,5]
    for j in mylist:
        if num > 0:
            while (num%j == 0):
                num /= j
    print "test ugly_2 result is:", num
    return num == 1

if __name__ == '__main__':
    n = isUgly(108)
    m = Ugly_2(108)
    print n, m