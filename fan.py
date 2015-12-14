#encoding=utf-8
from flask import Flask,render_template,config,redirect
import sys
from apps.merchant.views import merchant
from apps.user.views import user
from apps.blogs.views import blogs
from apps.config.ue import config
from flask import  blueprints
from apps.utils import RegexConverter
import re
from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.default.models import init_social
from apps.config.db import DBSession
from flask import g
from social.exceptions import SocialAuthBaseException
from apps.sys.views import indexpage

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)



app.config.from_pyfile('config/setting.py')
app.register_blueprint(social_auth)
app.register_blueprint(merchant)
app.register_blueprint(user)
app.register_blueprint(blogs)
app.register_blueprint(indexpage)
app.url_map.converters['regex'] = RegexConverter
app.register_blueprint(config)
if __name__ == ('__main__'):

    init_social(app, DBSession())
    app.debug = True
    app.run()

@app.before_request
def global_user():
    print 123
   # g.user = get_current_logged_in_user
    g.user = 'xoapwi'

@app.errorhandler(500)
def error_handler(error):
    if isinstance(error, SocialAuthBaseException):
        return redirect('/socialerror')