#coding:utf8
import sys
import time

#测试在控制窗口下的连续不换行的输出
if __name__ == '__main__':
    for i in range(1,61):
        sys.stdout.write('%s' % i)#在光标位置其连续输出
        sys.stdout.write("\r"+str(i))#进行当前光标所处位置的内容清空
        sys.stdout.flush()
        time.sleep(2.0)
