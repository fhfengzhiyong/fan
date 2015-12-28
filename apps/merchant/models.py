#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from apps import db
#创建对象的基类
Base = declarative_base()

class Merchant(db.Model):
    #表名
    __tablename__= 'merchant'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    name = Column(String(50))
    link_name = Column(String(30))
    mobile= Column(String(30))
    description= Column(String(2000))
    address= Column(String(100))
    mail = Column(String(10))
    star= Column(Integer())
    tread = Column(Integer())
    create_date= Column(DATETIME)
    state= Column(Integer())
    qq= Column(String(20))
    we_chat = Column(String(30))

