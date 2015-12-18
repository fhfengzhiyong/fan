#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from apps.base import *
#创建对象的基类
Base = declarative_base()

class Online(Base):
    ISOTIMEFORMAT='%Y-%m-%d %X'
    #表名
    __tablename__= 'bs_online'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    user_id = Column(String(36))
    command =  Column(String(20))#口令
    create_date= Column(DATETIME,default= time.strftime( ISOTIMEFORMAT, time.localtime() ))
    state= Column(Integer,default=0)#0为可用
    viewcount =Column(Integer)#阅读次数
    praise = Column(Integer,default=0) #点赞

