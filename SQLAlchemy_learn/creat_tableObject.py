#coding:utf8

'''
Created on 2016/4/21
we will create a simple table to store a user`s name，their age and their password
'''

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String

DB_CONNECT_STRING = 'mysql://root:123456@127.0.0.1:3306/test'
engine = create_engine(DB_CONNECT_STRING, encoding = "utf-8", echo=True)

metadata = MetaData(bind=engine)

#传统数据库映射classic
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('age', Integer),
                    Column('password', String(20))
                    )

addersses_table = Table('addresses', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('email_address', String(40), nullable=False)
                        )

#create table in database
metadata.create_all()
