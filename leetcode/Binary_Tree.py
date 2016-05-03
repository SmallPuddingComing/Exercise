#coding:utf8

import Queue
'''
二叉树进行序列化和反序列化
'''
#define for binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        mylist = []
        if root is None:
            return "root is null"
        mylist.append(root)
        i = 0
        while i < len(mylist):
            if mylist[i] is not None:
                mylist.append(mylist[i].left)
                mylist.append(mylist[i].right)
            i += 1

        #转换成字符串输出
        my_str = ''
        for j in xrange(len(mylist)):
            if mylist[j] is not None:
                my_str += str(mylist[j].val) + ','
            else:
                my_str += 'Null' + ','
        return my_str

    def deserialize(self, data):
        if data is None:
            return "data is null"
        mylist = data.split(',')
        root = TreeNode(mylist[0])
        q = Queue.Queue(-1)
        q.put(root)
        i = 0
        while q.qsize()>0 and i+2<len(mylist):
            node = q.get()
            if node.val != 'Null':
                i += 1
                left = TreeNode(mylist[i])
                if left.val != 'Null':
                    node.left = left
                    q.put(left)
                i += 1
                right = TreeNode(mylist[i])
                if right.val != 'Null':
                    node.right = right
                    q.put(right)

        return root
if __name__ == '__main__':
    #create a binary Tree
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    root.left = b
    root.right = c
    c.right = d

    codec = Codec()
    print '[' + codec.serialize(root) + ']'
    print codec.deserialize(codec.serialize(root))