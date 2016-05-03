#coding:utf8

#the simple function
def sum_ack():
    i = 0
    for j in range(4):
        i += j
    return i

#简单的使用闭包
def sum_1(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

#结果是返回一个函数
def count():
    fd = []
    for i in range(4):
        def f(i):
            def g():
                return i*i
            return g
        fd.append(f(i))
    return fd
        
#结果返回一个数,不属于下面的闭包
def count_1(num):
    fs = []
    for i in range(1,num):
        def f(i):
            return i*i
        fs.append(f(i))
    return fs

#匿名函数
def NoName_Function(num):
    list_1 = [(lambda x=i : x*x) for i in range(num)]
    return list_1

#装饰器函数
def log(func):
    def wrapper():
        print "begin there"
        def getResult(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        print "end this"
        return getResult

    return wrapper
@log
def f():
    return lambda x,y : x*x + y*y

def f1(x, y):
    return lambda: x*x + y*y

def f2(x, y):
    return lambda x,y: x*x + y*y

@log
def f3(x,y,z):
    print x+y+z


if '__main__' == '__main__':
    #这种闭包类似于装饰器
    funcs = count()
    for fun in funcs:
        print fun()

    #带参数的装饰器
    r =  f()()
    print r(1, 2)

    #双层装饰器
    r3 = f3()
    print r3(1,2,3)
