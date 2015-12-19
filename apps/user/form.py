#encoding=utf-8
#author:straw
from flask_wtf import Form
from wtforms.fields import TextField,BooleanField,StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    account = StringField('account',validators=[DataRequired()])
    password =StringField('password',validators=[DataRequired()])
    remember_me =BooleanField('remember_me', default=False)

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])