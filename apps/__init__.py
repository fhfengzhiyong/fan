
#encoding=utf-8
import sys
from flask import Flask,render_template,config,redirect
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config.from_pyfile('../config/setting.py')
db = SQLAlchemy(app)
#db.engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/fan',echo=True)
#创建DBSession类型
#db.DBSession  = sessionmaker(bind=engine,expire_on_commit= False)

from apps.merchant.views import merchant
from apps.user.views import user
from apps.blogs.views import blogs
from apps.config.ue import config
from apps.resource.views import resource
from apps.online.views import online
from flask import  blueprints
from apps.utils import RegexConverter
import re
import os
from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.default.models import init_social
from apps.config.db import DBSession
from flask import g
from social.exceptions import SocialAuthBaseException
from apps.system.views import indexpage
from flask.ext.login import current_user,LoginManager
from apps.user.models import User

basedir = os.path.abspath(os.path.dirname(__file__))


#用户登陆
login_manager = LoginManager()
login_manager.init_app(app)
#设置登陆视图请求方法
login_manager.login_view = "user.login"
#设置需要登陆提示
login_manager.login_message = u"该页面需要登陆！"

# @login_manager.user_loader
# def load_user(userid):
#     print userid
#     return User.get(userid)
@login_manager.user_loader
def load_user(id):
    user = User.query.filter_by(id=id).first()
    print user.account
    return user


app.register_blueprint(social_auth)
app.register_blueprint(merchant)
app.register_blueprint(user)
app.register_blueprint(blogs)
app.register_blueprint(indexpage)
app.register_blueprint(resource)
app.register_blueprint(online)
app.url_map.converters['regex'] = RegexConverter
app.register_blueprint(config)
app.config['UPLOADED_FILE']=basedir+'/upload/'

