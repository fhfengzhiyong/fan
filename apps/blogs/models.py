#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
#创建对象的基类
Base = declarative_base()

class Blogs(Base):
    #表名
    __tablename__= 'blogs'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    title = Column(String(50))
    synopsis = Column(String(1000))
    content = Column(String(10000))
    classify= Column(Integer)
    user_id = Column(String(36))
    create_date= Column(DATETIME)
    state= Column(Integer)
    views = Column(Integer,default=0)
    praise = Column(Integer,default=0)

