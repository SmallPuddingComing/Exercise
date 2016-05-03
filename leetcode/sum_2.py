#coding:utf8

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        mylist = []
        for i in range(len(num)):
            if dict.get(target-num[i], None) == None:
                dict[num[i]] = i
            else:
                mylist.append((dict[target-num[i]] + 1, i + 1))
        if mylist is not None:
            return  mylist

if __name__ == '__main__':
    solution = Solution()
    num = [1,3,4,6,5,8]
    print solution.twoSum(num, 9)