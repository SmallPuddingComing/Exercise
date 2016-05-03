#coding:utf8

class TreeNode(object):
    def __init__(self, x=0, node1=None, node2=None):
        self.val = x
        self.left = node1
        self.right = node2

class Solution:
    def minDepth(self,  root):
        if root is None:
            return 0
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1

    def maxDepth(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return self.maxDepth(root.right) + 1
        elif root.right is None:
            return self.maxDepth(root.left) + 1
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

    def isBalance(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return self.isBalance(root.right) + 1
        elif root.right is None:
            return self.isBalance(root.left) + 1
        a = self.isBalance(root.right)
        b = self.isBalance(root.left)
        if abs(self.isBalance(root.right) - self.isBalance(root.left)) <= 1:
            return True
        return False

if __name__ == '__main__':
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node2 = TreeNode(2, None, node4)
    node1= TreeNode(1,node3)
    node = TreeNode(0, node1, node2)

    solution = Solution()
    print solution.minDepth(node)
    print solution.maxDepth(node)
    print solution.isBalance(node)

