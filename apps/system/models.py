#encoding=utf-8
#author:straw
from apps import db
import uuid

class Recource(db.Model):
    __tablename__='os_resource'
    id = db.Column(db.String(36),primary_key=True,default=uuid.uuid4().__str__())
    name = db.Column(db.String(20),name='name_')
    describe =db.Column(db.String(200),name='DESCRIBE_')
    parentId = db.Column(db.String(36),name='parent_id')
    order = db.Column(db.Integer,name='order_')
    state = db.Column(db.Integer,default=0)
    url = db.Column(db.String(40),name='url_')
    depth =db.Column(db.Integer,name='depth_')
    imgClass = db.Column(db.String(40),name='img_class')
    @classmethod
    def getList(self):
        list = Recource.query.all()
        list1 = list
        new_list = []
        for i in range(5):
            for li in list1:
                if li.depth==i:
                    new_list.append(li)
                    list1.remove(li)
        return new_list