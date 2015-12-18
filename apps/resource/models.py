#encoding=utf-8
#author:straw
from apps.base import *
import datetime
class Resource(Base):
    ISOTIMEFORMAT='%Y-%m-%d %X'
    #表名
    __tablename__= 'bs_resource'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    create_date= Column(DateTime,default= time.strftime( ISOTIMEFORMAT, time.localtime() ))#
    real_name = Column(String(100))
    state= Column(Integer,default=0)
    file_name = Column(String(100))
    size= Column(Integer)
    user_id = Column(String(36))
    extension = Column(String(100))
    file_typed = Column(String(30))
    year_ = Column(String(10))
    month_ = Column(String(10))
    kay = Column(String(100))
    md5 = Column(String(100))