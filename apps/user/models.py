#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
#创建对象的基类
Base = declarative_base()

class User(Base):
    #表名
    __tablename__= 'user'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    username = Column(String(50))
    account = Column(String(30))
    email  = Column(String(50))
    password = Column(String(100))
    password_format= Column(Integer)
    state = Column(Integer)
    icon= Column(String(200))
    play_image= Column(Integer())

