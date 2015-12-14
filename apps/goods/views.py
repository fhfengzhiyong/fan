#encoding=utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect
from jinja2 import TemplateNotFound
merchant = Blueprint('goods',__name__,template_folder='templates/goods')
from models import Goods
from apps.config.db import DBSession
from sqlalchemy import String
import uuid
