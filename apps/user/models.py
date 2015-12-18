#encoding=utf-8
from sqlalchemy import Column,String,create_engine,Integer,DATETIME,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from  werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import  UserMixin
#创建对象的基类
Base = declarative_base()
from apps import db

class User(db.Model,UserMixin):
    #表名
    __tablename__= 'user'
    #表的结构
    id = Column(String(36),primary_key=True,default=uuid.uuid4().__str__())
    username = Column(String(50))
    account = Column(String(30))
    email  = Column(String(50))
    password_hash = Column(String(128))
    password_format= Column(Integer)
    state = Column(Integer)
    icon= Column(String(200))
    play_image= Column(Integer())
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
    @classmethod
    def get(self,id):
        User.query.filter_by(id=id).first()


