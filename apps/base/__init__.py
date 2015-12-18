#encoding=utf-8
#author:straw
from sqlalchemy import String,Column,Integer,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
import os,uuid
import time
Base = declarative_base()