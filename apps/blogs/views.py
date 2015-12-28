# -*- coding:utf8 -*-
#encoding = utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect,jsonify,current_app,g
from models import Blogs,ArticleType
from apps.config.db import DBSession
from flask.ext.login import login_required
import uuid
import string
import unicodedata
from apps.utils import decodeHtml
from werkzeug  import security
from apps.resource.models import Resource
from apps import db
from sqlalchemy.sql.dml import Insert
blogs = Blueprint('blogs',__name__,template_folder='templates/blogs')
@blogs.route('/blogs/<int:page>')
@blogs.route('/blogs',methods=['GET'])
def index(page=1):
    #blogss = session.query(Blogs)
    pagination = Blogs.query.order_by(db.desc(Blogs.create_date)).paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    blogss = pagination.items
    articletypecount = ""
    if g.user is not None:
        articletypecount = ArticleType.getlistbyArcount()
    return render_template('blogs/list.html',blogss=blogss,pagination=pagination,articletypecount = articletypecount)

@blogs.route('/blogs/add',methods=['POST','GET'])
@login_required
def add():
    if request.method == 'GET':
        articlelist = ArticleType.getlist()
        return render_template('blogs/add.html',id= uuid.uuid4().__str__(),articlelist=articlelist)
    form = request.form
    blogs = Blogs()
    blogs.title = form.get('title')
    blogs.content = form.get('content')
    blogs.synopsis = form.get('synopsis')
    blogs.classify = form.get('classify')
    blogs.state = form.get('state')
    blogs.user_id = g.user.id
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
    if request.method=='GET':
        id = request.args['id']
        articlelist = ArticleType.getlist()
        blogs = DBSession().query(Blogs).filter_by(id=id).first()
        return render_template('blogs/update.html',blogs = blogs,articlelist=articlelist)
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
    filelist = Resource.query.filter_by(bs_id=blogs.id)
    session.commit()
    session.close()
    return render_template('blogs/content.html',blogs=blogs,filelist = filelist)

@blogs.route('/blogs/praise',methods=['POST'])
def praise():
    id = request.form.get('id')
    session = DBSession()
    blogs    = session.query(Blogs).filter_by(id=id).scalar()
    blogs.praise = blogs.praise+1
    session.commit()
    session.close()
    return jsonify(code=0,praise =blogs.praise )

#BrticleType----------------------------------------------------------------------------------------------

articletype = Blueprint('articletype',__name__,template_folder='templates/articletype')

@articletype.route('/articletype/add',methods=['POST','GET'])
def articletypeadd():
    if request.method == 'GET':
        return render_template('articletype/add.html',id= uuid.uuid4().__str__())
    form = request.form
    articletype = ArticleType()
    articletype.name = form.get('name')
    articletype.describe = form.get('describe')
    articletype.user_id = g.user.id
    db.session.add(articletype)
    db.session.commit()
    flash('添加成功！')
    return redirect(location='/articletype')
@articletype.route('/articletype')
@login_required
def artiletypelist():
    user = g.user
    articletypelist = ArticleType.query.filter_by(user_id=user.id)
    return render_template('articletype/index.html',articletypelist= articletypelist)
@articletype.route('/articletype/update',methods=['POST','GET'])
@login_required
def artiletypeupdate():
    if request.method =='GET':
        id = request.args['id']
        print id
        articleType = ArticleType.query.filter_by(id=id).first()
        print articleType.name
        return render_template('articletype/update.html',articleTypeentity=articleType)
    form = request.form
    articletype = ArticleType()
    print form.get('oid')
    articletype =  ArticleType.query.filter_by(id=form.get('oid')).first()
    articletype.name = form.get('name')
    articletype.describe = form.get('describe')
    articletype.user_id = g.user.id
    db.session.commit()
    flash('修改成功！')
    return redirect(location='/articletype')
@articletype.route('/articletype/delete')
def articledel():
    id = request.args['id']
    articleType = ArticleType.query.filter_by(id=id).first()
    db.session.delete(articleType)
    db.session.commit()
    flash('删除成功!')
    return redirect(location='/articletype')
