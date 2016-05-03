#coding:utf8

'''
Created on 2016-4-13
使用sqlalchemy常见数据库和表格
学习例子：http://www.androiddev.net/python-linux-sqlalchemy/
'''
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DB_CONNECT_STRING = 'mysql+mysqldb://root:123456@127.0.0.1:3306/abc'
engine = create_engine(DB_CONNECT_STRING, encoding = "utf-8", echo=True)
DB_session = sessionmaker(bind=engine)
session = DB_session()

#建立一个数据库
# session.execute('create database abc')
# print session.execute('show databases').fetchall()
session.execute('use abc')


# 建立user表的过程
BaseModel = declarative_base(bind=engine)#ps：初始化Metadata的时候要传入bind，来连接数据库

def init_db():
    #创建了数据表
    BaseModel.metadata.create_all()

def drop_db():
    #关闭数据表
    BaseModel.metadata.drop_all()

#现代化映射modern
class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

init_db()

new_number = User(id='1004', name='hello')
session.add(new_number)
session.commit()
session.close()

#查询数据代码示例
# session = DB_session()
# print session.execute('select * from player where id=1').first()
# print session.execute('select * from player where id=:id', {'id':116}).first()
# session.close()
