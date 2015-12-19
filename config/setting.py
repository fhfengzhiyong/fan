#encoding=utf-8
import os

DEBUG = False
SYS_NAME = '基础平台系统'
CSRF_ENABLED = True #激活 跨站点请求伪造 
SECRET_KEY = '5186225'
APP_CONFIG_FILE='/config/production.py'
#SERVER_NAME='127.0.0.1:8000'


basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#数据库设置
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost:3306/fan'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True #打印sql


#国际化
# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 3 #分页条数
BASE_URL = "api.geetest.com/get.php?gt="
CAPTCHA_ID = "a40fd3b0d712165c5d13e6f747e948d4"
PRIVATE_KEY = "0f1a37e33c9ed10dd2e133fe2ae9c459"



SOCIAL_AUTH_TWITTER_LOGIN_URL='/sdfsd'
SOCIAL_AUTH_LOGIN_URL='/login'
LOGIN_URL='/login'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'

SOCIAL_AUTH_USER_MODEL = 'apps.user.models.User'
SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 40
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 40
SOCIAL_AUTH_UUID_LENGTH = 36
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = False
SOCIAL_AUTH_CLEAN_USERNAMES = True
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['keep']
SOCIAL_AUTH_REMEMBER_SESSION_NAME = 'remember_me'


