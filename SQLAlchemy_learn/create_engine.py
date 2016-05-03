#coding:utf8

'''
Created on 2016-4-12
使用mysql.connector连接MySQL进行数据表操作
'''

from sqlalchemy import create_engine, Column, String, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'player'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # age = Column(SmallInteger())

DB_CONNECT_STRING = 'mysql://root:123456@127.0.0.1:3306/test'
#'mysql+mysqlconnector://root:123456@localhost:3306/test'
#'mysql+mysqldb://root:123456@127.0.0.1:3306/test'
engine = create_engine(DB_CONNECT_STRING, encoding = "utf-8", echo=True)

#sessionmaker一个可以配置的类，连接不同引擎，session工厂
DB_session = sessionmaker(bind=engine)

#session是ORM-mapped对象持久化操作的管理
session = DB_session()
new_student = User(id='120', name='aiai')
session.add(new_student)
session.commit()
# result = session.execute("select * from user where id=:param", {'param':5})
# print result
session.close()


