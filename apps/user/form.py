#encoding=utf-8
#author:straw
from flask_wtf import Form
from wtforms.fields import TextField,BooleanField,StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    account = StringField('openid',validators=[DataRequired()])
    #password =