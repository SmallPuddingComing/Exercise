#coding:utf8

def gen_0_1_2():
    yield 0
    yield 1
    yield 2

def counter(start=0):
    while start <= 100:
        yield start
        start += 1

def wanna():
    print "hello world"
    yield 1
    #return None  #生成器中yield本身就是一个返回值，因此加了return之后会报错

#对比return和yield的不同，因为yield未离开代码块，所以会依次执行
def playYou():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        yield 4


if __name__ == '__main__':
    g = gen_0_1_2()#返回的就是一个函数
    for i in g:
        print i

    for num in counter():
        print num

    #发现了一个问题，就是生成器返回的是一个函数对象，想要获得函数的结果，需要进行循环遍历，
    # 例如直接调用wanna()是不会有任何结果输出的。
    for j in wanna():
        print j

    for i in playYou():
        print i