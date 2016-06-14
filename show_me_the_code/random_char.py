#coding:utf8

'''
生成随机码图片
1、创建一张img
2、创建字体
3、随机填充图片颜色
4、随机字体颜色和距离（这边和图片填充有先后渲染的关系）
5、整张图进行虚化模糊处理
6、保存图到给定路径，还有就是路径的分隔符注意
'''

from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
from PIL import ImageFilter
import random

def random_char():
    #随机在数字，大小写字符中得到验证码
    L = [random.randint(48, 56), random.randint(65, 90), random.randint(97, 122)]
    i= L[random.randint(0,2)]
    return chr(i)

def random_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def random_font_color():
    return (random.randint(37,90),random.randint(37,90),random.randint(37,90))

width, length = 60*4, 60
#create image
img = Image.new('RGB',(width, length),(255, 255, 255))
#create font
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 28)
#create a draw
draw = ImageDraw.Draw(img)

# imageDraw = ImageDraw.ImageDraw(img, 'RGB')
# rgb = random_font_color()
# imageDraw.setfill(rgb)//Imagedraw 自带的空白填充函数不能用
#set the blankspace
for x in xrange(width):
    for y in xrange(length):
        draw.point((x,y),fill=random_color())

#fill word
for i in xrange(4):
    t = random.randint(0,4)*((-1)^i)
    draw.text((60*i+t, 10), random_char(), font=font, fill=random_font_color())#这边的fill可以是字符串‘red’表示也可以rgb形式是（255,0,0）


#fillter pic，图片模糊处理
img = img.filter(ImageFilter.BLUR)
#save the pic
img.save("C:/Users/yuanrong/Desktop/photos/20160524.png")

#解决数字之间的耦合性
