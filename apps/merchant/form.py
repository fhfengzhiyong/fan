#encoding=utf-8
#author:straw
from flask_wtf import Form
from wtforms.fields import TextField,BooleanField,StringField,IntegerField,DateTimeField
from wtforms.validators import DataRequired
import uuid
import datetime
class addMerchantFrom(Form):
    #openid = StringField('openid',validators=[DataRequired()])
    #remember_me = BooleanField('remember_me',default=False)
    id =uuid.uuid4()
    name = StringField('name',validators=[DataRequired()])
    link_name =  StringField('link_name',validators=[DataRequired()])
    mobile= IntegerField('mobile',validators=[DataRequired()])
    description=  StringField('description')
    address= StringField('address',validators=[DataRequired()])
    star= IntegerField('star')
    tread =IntegerField('tread')
    create_date= datetime.date
    state= IntegerField('state')
    qq= IntegerField('qq')