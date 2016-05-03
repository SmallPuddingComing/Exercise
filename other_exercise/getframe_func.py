#coding:utf8
import sys

'''此模块的作用是显示被调用的上一层'''

getframe_expr = 'sys._getframe({}).f_code.co_name'

def foo():
    print"i am foo, calling bar"
    bar()

def bar():
    print"i am bar, calling baz"
    baz()

def baz():
    print "i am baz:"
    caller = eval(getframe_expr.format(2))
    callers_caller = eval(getframe_expr.format(3))
    print "my name is",eval(getframe_expr.format(1))
    print "i was called from" , caller
    print caller,"was called from", callers_caller

if __name__ == '__main__':
    foo()
