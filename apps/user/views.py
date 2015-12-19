#encoding=utf-8
#author:straw
from flask import render_template, flash, redirect,Blueprint,Flask,g,url_for
from .form import LoginForm
from flask import current_app,g,request
from apps.config import db
from models import User
from apps.utils import encrypt_password
import os
import apps.sdk.geetest as geetest
from flask.ext.login import login_user,logout_user,login_required
# index view function suppressed for brevity
user = Blueprint('user',__name__,template_folder='templates/user')

@user.route('/register', methods = ['GET', 'POST'])
def register():
    captcha_id = current_app.config.get('CAPTCHA_ID')
    private_key = current_app.config.get('PRIVATE_KEY')
    BASE_URL =  current_app.config.get('BASE_URL')
    product = "embed"
    if request.method == "POST":
        account = request.form['account']
        password = request.form['password']
        challenge = request.form['geetest_challenge']
        validate = request.form['geetest_validate']
        seccode = request.form['geetest_seccode']
        gt = geetest.geetest(captcha_id, private_key)
        result = gt.geetest_validate(challenge, validate, seccode)
        if result:
            user = User()
            user.account = account
            user.password = password
            session =  db.DBSession()
            session.add(user)
            session.commit()
            session.close()
            flash('注册成功！')
            return redirect(location='/')
        else:
            flash('验证失败!')
            gt = geetest.geetest(captcha_id, private_key)
            url = ""
            httpsurl = ""
            try:
                challenge = gt.geetest_register()
            except Exception as e:
                challenge = ""
            if len(challenge) == 32:
                url = "http://%s%s&challenge=%s&product=%s" % (BASE_URL, captcha_id, challenge, product)
                httpsurl = "https://%s%s&challenge=%s&product=%s" % (BASE_URL, captcha_id, challenge, product)
                return render_template('user/register.html', url=url, httpsurl=httpsurl)
    else:
        gt = geetest.geetest(captcha_id, private_key)
        url = ""
        httpsurl = ""
        try:
            challenge = gt.geetest_register()
        except Exception as e:
            challenge = ""
        if len(challenge) == 32:
            url = "http://%s%s&challenge=%s&product=%s" % (BASE_URL, captcha_id, challenge, product)
            httpsurl = "https://%s%s&challenge=%s&product=%s" % (BASE_URL, captcha_id, challenge, product)
        return render_template('user/register.html', url=url, httpsurl=httpsurl)

    return render_template('user/register.html')

@user.route('/socialerror')
def socialerror():
    return render_template('/')

@user.route('/navlogin',methods=['POST'])
def navlogin():
    form = request.form
    account = form.get('account')
    password = form.get('password')
    session = db.DBSession()
    encrypt_password(password)
    print account
    user = User.query.filter_by(account=account).first()
    if user is not None and user.verify_password(password):
        login_user(user)
        flash('登陆成功！')
        return redirect(location='/')
    flash('用户名或密码不正确!')
    return redirect(location='/')

@user.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(account=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username or password.')
    flash("Logged in successfully.")
    return render_template('user/login.html', form=form)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(location='/')