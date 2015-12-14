# -*- coding:utf8 -*-
#encoding = utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect
from models import Blogs
from apps.config.db import DBSession
from sqlalchemy import String
import uuid
import string
import unicodedata
from apps.utils import decodeHtml

blogs = Blueprint('blogs',__name__,template_folder='templates/blogs')
@blogs.route('/blogs',methods=['GET'])
def index():
    session = DBSession()
    blogss = session.query(Blogs)
    session.close()
    return render_template('blogs/list.html',blogss=blogss)

@blogs.route('/blogs/add',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return render_template('blogs/add.html')
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
    session.close()
    flash('添加成功！')
    return render_template('blogs/add.html')
@blogs.route('/blogs/delete/',methods=['GET'])
def delete():
    id = request.args.get('id')#request.args[id]
    session = DBSession()
    #session.query(User).filter_by(name='user1')
    blogs = session.query(Blogs).filter_by(id = id).first()
    session.delete(blogs)
    session.close()
    flash('删除成功!')
    return redirect(location='/blogs')
@blogs.route('/blogs/update',methods=['GET','POST'])
def update():
    if request.method=='GET':
        id = request.args['id']
        blogs = DBSession().query(Blogs).filter_by(id=id).first()
        return render_template('blogs/update.html',blogs = blogs)
    form = request.form
    old = form['old']
    blogs = Blogs()
    blogs.id = old
    blogs.title = form.get('title')
    blogs.content = form.get('content')
    blogs.classify = form.get('classify')
    blogs.state = form.get('state')
    session = DBSession()
    state = session.merge(blogs,load=True)
    session.close()
    flash('修改成功！')
    return  redirect(location='/blogs')
@blogs.route('/blogs/content',methods=['GET'])
def detail():
    id = request.args['id']
    print id
    session = DBSession()
    print len(id)
    blogs    = session.query(Blogs).filter_by(id=id).first()
    session.close()
    return render_template('blogs/content.html',blogs=blogs)


