#encoding=utf-8
#author:straw
from jinja2 import Environment
from apps.user.models import User
from apps.resource.models import Resource
def strftime(date, fmt):
    if date:
        return date.strftime(fmt.encode('utf-8')).decode('utf-8')
    return '系统成立之初'

def getUserNamebyId(id):
    if id:
        return User.get(id)
    return '没人'

def findFileListByBsId(id):
    return Resource.get(id)