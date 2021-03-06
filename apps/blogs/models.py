#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from apps.base import *
#创建对象的基类
Base = declarative_base()
from apps import db
from flask import g
class Blogs(db.Model):
    ISOTIMEFORMAT='%Y-%m-%d %X'
    #表名
    __tablename__= 'blogs'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    title = Column(String(50))
    synopsis = Column(String(1000))
    content = Column(String(10000))
    classify= Column(Integer)
    user_id = Column(String(36))
    create_date= Column(DATETIME,default= time.strftime( ISOTIMEFORMAT, time.localtime() ))
    state= Column(Integer)
    views = Column(Integer,default=0)
    praise = Column(Integer,default=0)
class ArticleType(db.Model):
    __tablename__='bs_article_type'
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    name = Column(String(20))
    describe = Column(String(200))
    prient_id = Column(String(36))
    user_id = Column(String(36))
    order = Column(Integer,name='order_',)
    @classmethod
    def getlist(self):
        return ArticleType.query.filter_by(user_id = g.user.id)
    @classmethod
    def getlistbyArcount(self):
        sql = 'select b.Name,count(b.Id) from blogs a,bs_article_type b where a.classify = b.Id  ' \
              'and a.user_id=:user_id GROUP BY a.classify '
        return db.session.execute(sql,{'user_id': g.user.id}).fetchall()