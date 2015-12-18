#encoding=utf-8
#author:straw

from flask import Blueprint,render_template,request,flash,redirect,current_app
from flask.ext.login import login_user, logout_user, current_user, login_required

indexpage = Blueprint('',__name__,template_folder='../templates')

@indexpage.route('/')
def index():
    sysname = current_app.config.get('SYS_NAME')
    return render_template('index.html',sysname = sysname)