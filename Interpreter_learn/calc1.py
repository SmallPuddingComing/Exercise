#coding:utf8
'''
版本1.0
1、可以进行连加、减、乘、除
2、接下来进行优先级的计算
'''

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'
operater = ['+', '-', '*', '/']
mydict = {'+':'PLUS', '-':'SUB', '*':'MULTI', '/':'DE'}

class Token:
    def __init__(self, type, value):
        self._type = type
        self._value = value

    def __str__(self):
        return 'Token ({type}, {vaule})'.format(type=self._type, value=repr(self._value))

    def __repr__(self):
        return self.__str__()

    # __repr__ = __str__

class Interperter:
    def __init__(self, text):
        self.text = text
        self.pos = 0 #索引
        self.current_token = None
        self.count = 0

    def error(self):
        raise Exception('Error parsing input') #错误的词组

    def skip_withespace(self):
        pass

    def get_next_token(self):
        text = self.text

        #索引到最后返回
        if self.pos > len(text) -1:
            return Token(EOF, None)

        current_char = text[self.pos]
        if current_char.isdigit():
            self.count = self.pos

            while current_char not in operater:
                if self.pos == len(text)-1:
                    break

                self.pos += 1
                current_char = text[self.pos]

            if self.count == self.pos: #被加数是个数的情况
                current_char = text[self.pos:]
            else: #被加数不是个数的情况
                if self.pos == len(text)-1:#被加数
                    current_char = text[self.count:]
                else:#加数
                    current_char = text[self.count:self.pos]
            token = Token(INTEGER, int(current_char))
            return token

        #运算符
        if current_char in operater:
            token = Token(mydict.get(current_char, None), current_char)
            self.pos += 1
            return token

        if current_char.isspace():
            self.pos += 1
            self.current_token = None

        self.error()

    #下一轮类型的获取，不管是整型还是运算符
    def eat(self, token_type):
        if self.current_token._type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    #计算器接口
    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(op._type)

        right = self.current_token
        self.eat(INTEGER)

        result = eval(str(left._value) + op._value + str(right._value))
        return result

    def expr_Multi(self, text_OpList):
        result = 0
        for index in xrange(len(text_OpList)-1):
            result = self.expr()
            self.text = str(result) + self.text[self.pos-1:]
            self.pos = 0 #第二次计算，位置一道初始位置
        result = self.expr()
        return result

if __name__ == '__main__':
    while True:
        try:
            text = raw_input("calc< ")
        except EOFError:
            break
        if not text:
            continue

        if text == 'q' or text == 'quit':
            exit(0)

        text_OpList = [x for x in text if x in operater]
        interperter = Interperter(text)
        # result = interperter.expr()
        result = interperter.expr_Multi(text_OpList)
        print(result)