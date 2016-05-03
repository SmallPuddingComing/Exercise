#coding:utf8

'''
remove Duplicate Letter:先找出字符串中最小的哪一个，从那里开始做索引剔除重复的字符
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        if s == '':
            return ""
        index = -1
        for i in xrange(len(s)):
            if s.count(s[i]) < 2:
                index = i
                break
            index = 0

        if index == -1:
            temp = s[0]
            for i in xrange(len(s)):
                if s[i] < temp:
                    temp = s[i]
                    index = i

        mystr = []
        for it in xrange(len(s)):
            if s[it] in mystr:
                continue
            else:
                if it in xrange(index, len(s)):
                    mystr.append(s[it])

        s = ''.join(mystr)
        return s

    def summaryRanges(self, nums):
        temp = []
        t = ''
        e = 0
        h = 0
        size_t = len(nums)
        while e < size_t:
            if e+1<size_t and nums[e+1] - nums[e] == 1:
                t = nums[h:e+1]
            else:
                t = nums[h:e+1]
                h = e+1
                if len(t)>1:
                    t = str(t[0]) + '->' + str(t[-1])
                else:
                    t = str(t[-1])
                temp.append(t)
            e += 1
        return temp


if  __name__ == '__main__':
    solution = Solution()
    # print solution.removeDuplicateLetters("bbcaac")
    print solution.summaryRanges([0,1,2,4,5,7])#have some problem to save