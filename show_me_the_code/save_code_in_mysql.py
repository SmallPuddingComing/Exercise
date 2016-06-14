#coding:utf8

'''
save the activtion code in mysql
1、保存生成的激活码进数据库
2、连接数据库，使用mysqldb驱动
3、提交语句
4、关闭连接
'''

import mysql.connector

def store_code(filepath):
    conn = mysql.connector.Connect(user='root', password='123456', database='test')
