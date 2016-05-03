#coding:utf8

'''
游戏：公牛和母牛，猜数字，写出四个数字让朋友猜测，猜对一个数值即为公牛，猜错记为母牛
return几A几B，其中A前面的数字表示位置正确的数的个数，而B前的数字表示数字正确而位置不对的数的个数
'''

class Solution(object):
    def getHint(self, secret, guess):
        '''
        @secert 是被猜测的数字
        @guess 是猜测的数值
        @return xAxB
        '''
        bulls= 0
        cows = 0
        if len(secret) != len(guess):
            return "Plaese keep the same lenght with the secret,now is so less"
        i = 0
        j = 0
        while (i < len(secret)):
            if secret[i] == guess[i]:
                secret = list(secret)
                secret[i] = ''
                secret = ''.join(secret)

                guess = list(guess)
                guess[i] = ''
                guess = ''.join(guess)
                bulls += 1
            i += 1

        while (j < len(guess)):
            if guess[j] in secret:
                if guess.count(guess[j]) < 2:
                    cows += 1
                else:
                    guess = list(guess)
                    guess[j] = ''
                    guess = ''.join(guess)
                    continue
            j += 1

        return "%dA %dB" % (bulls, cows)

if __name__ == '__main__':
    solution = Solution()
    print solution.getHint('1807', '7810')

#这道测试题的收获是，字符串时属于不可改变的对象，因此是无法修改字符串的某一部分，有一种可行的方法
#当你需要在字符串中修改某一个字符时，现将其转换成列表 然会再改变你想要改变的值，最后还原列表成字符串。