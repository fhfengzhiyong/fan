#encoding=utf-8
#author:straw

from flask import Blueprint,render_template,request,flash,redirect,current_app
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import Recource
from apps import db
from collections import defaultdict
indexpage = Blueprint('',__name__,template_folder='../templates')

@indexpage.route('/')
def index():
    sysname = current_app.config.get('SYS_NAME')
    return render_template('index.html',sysname = sysname)

recource = Blueprint('recource',__name__,template_folder='/templates')

@recource.route('/recource')
@login_required
def resourceList():
    resourcelist =Recource.query.all()
    return render_template('/system/recource/index.html',resourcelist = resourcelist)

@recource.route('/recource/add',methods=['POST','GET'])
@login_required
def resourceadd():
    if request.method=='GET':
        resourcelist =Recource.query.all()
        return render_template('/system/recource/add.html',resourcelist=resourcelist)
    form = request.form
    entity = Recource()
    entity.name = form.get('name')
    entity.describe = form.get('describe')
    entity.imgClass = form.get('imgClass')
    entity.parentId = form.get('parentId')
    entity.url = form.get('url')
    db.session.add(entity)
    db.session.flush()
    db.session.commit()
    flash('增加成功！')
    resourcelist =Recource.query.all()
    return render_template('/system/recource/index.html',resourcelist = resourcelist)

@recource.route('/recource/update',methods=['POST','GET'])
@login_required
def resourceupdate():
    if request.method=='GET':
        resource = Recource.query.filter_by(id=request.args['id']).first()
        print resource.id
        resourcelist =Recource.query.all()
        return render_template('/system/recource/update.html',resource=resource,resourcelist=resourcelist)
    form = request.form
    recource = Recource.query.filter_by(id=form.get('id')).first()
    recource.name = form.get('name')
    recource.describe = form.get('describe')
    recource.imgClass = form.get('imgClass')
    recource.parentId = form.get('parentId')
    recource.url = form.get('url')
    db.session.commit()
    flash('修改成功！')
    resourcelist =Recource.query.all()
    return render_template('/system/recource/index.html',resourcelist = resourcelist)