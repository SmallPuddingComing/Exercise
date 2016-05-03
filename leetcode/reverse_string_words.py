#coding:utf8

class Node(object):
    def __init__(self, x=None):
        self.value = x
        self.right = Node()
        self.left = Node()

class Solution(object):
    val = 0
    #reverse words in string
    #'def abc' --> 'abcdef'
    #思路是先翻转整个字符串，然后再翻转每个word
    def reverswords(self, str):
        print ' '.join(word[::-1] for word in str[::-1].split())

    #recover Binary tree search Tree
    #遍历一个二叉树中的两个节点错误，修正这棵树,正确的二叉树是用来递增的，而错误的节点比前一节点值要小，进行交换
    def recoverTree(self, node):
            if not node:
                return None
            self.prenode = None
            self.node1, self.node2 = None, None
            self.dfs(node)
            self.node1.value, self.node2.value = self.node2.value, self.node1.value
            return node

    def dfs(self, node):
        if not node:
            return None
        #中序遍历
        self.dfs(node.left)
        if self.prenode and self.prenode.value > node.value:
            if self.node1:
                self.node2 = node
            else:
                self.node1, self.node2 = self.prenode, node
        self.prenode = node

        self.dfs(node.right)

    #检查是不是一颗二叉树，用中序遍历
    def isValidBST(self, root):
        if not root:
            return None

        res = self.isValidBST(self, root.left)
        if self.val is None:
            self.val = root.value
        else:
            res = res and (root.value > self.val) #这是false和true的较量
            self.val = root.value

        res = self.isValidBST(root.right)
        return res

    #检查C字符串中是否由A串和B串组成，也就是说提出A串就只剩下B串
    def checkIn(self, str1, str2):
        for s in str2:
            if s not in str1:
                print  "sting %s is not exist in %s" % (str2, str1)
                return False
        return True

    def interleaving_string(self, str, a, b):
        str = list(str)
        a = list(a)
        b = list(b)
        if self.checkIn(str, a) and self.checkIn(str, b):
            for s in a:
                str.remove(s)

            if ''.join(str) == ''.join(b):
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    # s.reverswords("hello world!")
    print s.interleaving_string('123ab4c', '123a', 'bc4')