#encoding=utf-8
#author:straw
#初始化数据库连接
from sqlalchemy import Column,String,create_engine,Integer,DATETIME
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/fan',echo=True)
#创建DBSession类型
DBSession  = sessionmaker(bind=engine,autocommit= True)
