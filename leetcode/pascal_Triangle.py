#coding:utf8

'''
输入一个整数K，输出相对应的杨辉三角的第K行
思路：先完成该杨辉三角，再取出相对应的行
'''

class Solution(object):
    def getRow(self, rowIndex):
        mylist = []
        for i in xrange(rowIndex):
            temp = []
            if i==0:
                temp.append(1)
                temp.append(1)
                mylist.append(temp)
                continue
            for j in xrange(i+2):
                if j==0 or j==i+1:
                    temp.append(1)
                elif i>0 or j>0:
                   temp.append(mylist[i-1][j-1] + mylist[i-1][j])
            mylist.append(temp)

        if rowIndex == 0:
            mylist = [1]
            return mylist
        return mylist[rowIndex-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.getRow(6)