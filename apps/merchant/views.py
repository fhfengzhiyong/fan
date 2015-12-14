#encoding=utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect
from jinja2 import TemplateNotFound
merchant = Blueprint('merchant',__name__,template_folder='templates/merchant')
from models import Merchant
from apps.config.db import DBSession
from sqlalchemy import String
from form import addMerchantFrom
import uuid
@merchant.route('/merchant/')
def index():
    session = DBSession()
    merchants = session.query(Merchant)
    return render_template('merchant/index.html',merchants=merchants)

@merchant.route('/merchant/add',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return render_template('merchant/add.html')
    #merchant  = addMerchantFrom()
    form = request.form
    merchant = Merchant()
    print merchant.id
    merchant.name = form.get('name')
    merchant.link_name = form.get('link_name')
    merchant.address = form.get('address')
    merchant.mobile = form.get('mobile')
    merchant.qq = form.get('qq')
    merchant.we_chat = form.get('we_chat')
    merchant.mail = form.get('mail')
    session = DBSession()
    state = session.add(merchant)
    session.commit()
    session.close()
    #print merchant.id
    retult=None
    flash('添加成功！')
    return render_template('merchant/add.html',retult=retult)
@merchant.route('/merchant/delete/',methods=['GET'])
def delete():
    id = request.args.get('id')#request.args[id]
    session = DBSession()
    print id
    #session.query(User).filter_by(name='user1')
    merchant = session.query(Merchant).filter_by(id = id).first()
    session.delete(merchant)
    session.commit()
    session.close()
    flash('删除成功!')
    return redirect(location='/merchant')
@merchant.route('/merchant/update',methods=['GET','POST'])
def update():
    if request.method=='GET':
        id = request.args['id']
        merchant = DBSession().query(Merchant).filter_by(id=id).first()
        return render_template('merchant/update.html',merchant = merchant)
    form = request.form
    old = form['old']
    print old
    merchant = Merchant()
    merchant.id = old
    merchant.name = form.get('name')
    merchant.link_name = form.get('link_name')
    merchant.address = form.get('address')
    merchant.mobile = form.get('mobile')
    merchant.qq = form.get('qq')
    merchant.we_chat = form.get('we_chat')
    merchant.mail = form.get('mail')
    session = DBSession()
    state = session.merge(merchant,load=True)
    session.commit()
    session.close()
    #print merchant.id
    retult=None
    flash('修改成功！')
    return  redirect(location='/merchant')


