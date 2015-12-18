#encoding=utf-8
#author:straw
from flask import render_template,current_app,g,Blueprint,request,redirect,jsonify,ctx
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from apps.config.db import DBSession
import uuid
import time

