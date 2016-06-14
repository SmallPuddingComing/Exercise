#coding:utf8

'''
下载图片，在图片上显示数字
'''

from PIL import Image, ImageDraw, ImageFont
from other_exercise import py_pyc

def add_num(picPath, number):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 36)
    ImageDraw.Draw(img).text((2*x /3, 0),str(number), font=myfont, fill='red')
    img.save('C:/Users/yuanrong/Desktop/photos/pic_with_num.jpg')

if __name__ == '__main__':
    add_num('C:/Users/yuanrong/Desktop/photos/mei.jpg', "i love you")