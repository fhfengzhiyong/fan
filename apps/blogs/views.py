# -*- coding:utf8 -*-
#encoding = utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect,jsonify,current_app
from models import Blogs
from apps.config.db import DBSession
import uuid
import string
import unicodedata
from apps.utils import decodeHtml
from werkzeug  import security

blogs = Blueprint('blogs',__name__,template_folder='templates/blogs')
@blogs.route('/blogs',methods=['GET'])
def index():
    session = DBSession()
    blogss = session.query(Blogs)
    session.commit()
    session.close()
    return render_template('blogs/list.html',blogss=blogss)

@blogs.route('/blogs/add',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return render_template('blogs/add.html',id= uuid.uuid4().__str__())
    form = request.form
    blogs = Blogs()
    blogs.title = form.get('title')
    blogs.content = form.get('content')
    blogs.synopsis = form.get('synopsis')
    blogs.classify = form.get('classify')
    blogs.state = form.get('state')
    blogs.user_id = form.get('user_id')
    session = DBSession()
    session.add(blogs)
    session.commit()
    session.close()
    flash('添加成功！')
    return render_template('blogs/add.html')
@blogs.route('/blogs/delete/',methods=['GET'])
def delete():
    id = request.args.get('id')#request.args[id]
    session = DBSession()
    blogs = session.query(Blogs).filter_by(id = id).first()
    session.delete(blogs)
    session.commit()
    session.close()
    flash('删除成功!')
    return redirect(location='/blogs')

@blogs.route('/blogs/update',methods=['POST','GET'])
def update():
    print 123
    if request.method=='GET':
        id = request.args['id']
        blogs = DBSession().query(Blogs).filter_by(id=id).first()
        return render_template('blogs/update.html',blogs = blogs)

    print 1234
    form = request.form
    id = form.get('id')
    session = DBSession()
    blogs  = session.query(Blogs).filter_by(id=id).scalar()
    blogs.title = form.get('title')
    blogs.content = form.get('content')
    blogs.classify = form.get('classify')
    blogs.state = form.get('state')
    blogs.synopsis = form.get('synopsis')
    session.commit()
    session.close()
    flash('修改成功！')
    return  redirect(location='/blogs')

@blogs.route('/blogs/content',methods=['GET'])
def detail():
    id = request.args['id']
    session = DBSession()
    blogs    = session.query(Blogs).filter_by(id=id).scalar()
    blogs.views = blogs.views+1
    session.commit()
    session.close()
    return render_template('blogs/content.html',blogs=blogs)

@blogs.route('/blogs/praise',methods=['POST'])
def praise():
    id = request.form.get('id')
    session = DBSession()
    blogs    = session.query(Blogs).filter_by(id=id).scalar()
    blogs.praise = blogs.praise+1
    session.commit()
    session.close()
    return jsonify(code=0,praise =blogs.praise )





