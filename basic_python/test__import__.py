#coding:utf8

import glob
import os

#case 2
#获得导入模块的指定函数
def getfunctionbyname(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

#对生成器函数，进行迭代输出结果
def outFunc(func):
    for i in func:
        print i

#case 1
#glob 进行文件匹配，支持通配符操作 *、？、[]
modules = []
for module_file in glob.glob("E:/Exerics_py/basic_python/*_learn.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))#返回文件名和扩展的后缀
        func = getfunctionbyname(module_name, 'gen_0_1_2')#这里得到的func是一个function，不能直接作为生成器迭代。所以func（）后就是生成器了
        outFunc(func())
        module = __import__(module_name) #这样得到的是模块的.pyc文件
        modules.append(module)
    except ImportError:
        pass

    for module in modules:
        fun = module.wanna()
        outFunc(fun)

#case 3
#参入一个名字返回的是一个模块instance
class LazyImport:
    def __init__(self, module_name, module=None):
        self.module_name = module_name
        self.module = module

    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)

if __name__ == '__main__':
    string = LazyImport('1-27')#generator_learn
    print type(string) #string是一个模块对象
    # outFunc(string)