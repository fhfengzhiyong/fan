# -*- coding:utf8 -*-
#encoding = utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect,jsonify,current_app
from models import Online
from apps.config.db import DBSession
import uuid
import string
import unicodedata
from apps.utils import decodeHtml
from werkzeug  import security

online = Blueprint('online',__name__,template_folder='templates/online')
@online.route('/online',methods=['GET'])
def index():
    session = DBSession()
    #onlines = session.query(Online)
    session.commit()
    session.close()
    return render_template('online/index.html')

@online.route('/online/add',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return render_template('online/add.html',id= uuid.uuid4().__str__())
    form = request.form
    online = Online()
    online.id = form.get('id')
    session = DBSession()
    session.add(Online)
    session.commit()
    session.close()
    flash('添加成功！')
    return render_template('online/add.html')
@online.route('/online/delete/',methods=['GET'])
def delete():
    id = request.args.get('id')#request.args[id]
    session = DBSession()
    online = session.query(Online).filter_by(id = id).first()
    session.delete(Online)
    session.commit()
    session.close()
    flash('删除成功!')
    return redirect(location='/online')

@online.route('/online/update',methods=['POST','GET'])
def update():
    print 123
    if request.method=='GET':
        id = request.args['id']
        online = DBSession().query(Online).filter_by(id=id).first()
        return render_template('online/update.html',online = online)

    print 1234
    form = request.form
    id = form.get('id')
    session = DBSession()
    online  = session.query(Online).filter_by(id=id).scalar()
    online.title = form.get('title')
    online.content = form.get('content')
    online.classify = form.get('classify')
    online.state = form.get('state')
    online.synopsis = form.get('synopsis')
    session.commit()
    session.close()
    flash('修改成功！')
    return  redirect(location='/online')
#详细阅读次数
@online.route('/Online/content',methods=['GET'])
def detail():
    id = request.args['id']
    session = DBSession()
    online    = session.query(Online).filter_by(id=id).scalar()
    Online.views = Online.views+1
    session.commit()
    session.close()
    return render_template('online/content.html',Online=Online)
#点赞
@online.route('/Online/praise',methods=['POST'])
def praise():
    id = request.form.get('id')
    session = DBSession()
    online    = session.query(Online).filter_by(id=id).scalar()
    online.praise = Online.praise+1
    session.commit()
    session.close()
    return jsonify(code=0,praise =Online.praise )





