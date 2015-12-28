#encoding=utf-8
#author:straw
from apps.base.views import *
from models import Resource
from apps.utils import *
resource = Blueprint('resource',__name__)

@login_required
@resource.route('/resource/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        id = request.args['id']
        if id:
            f = request.files['file']
            resource = Resource()
            resource.id = uuid.uuid4().__str__()
            resource.bs_id= id
            name = f.filename
            extension = getFileExt(name)
            resource.extension = extension
            resource.file_name= (resource.id)+"."+extension
            resource.real_name = name
            session = DBSession()
            session.add(resource)
            session.commit()
            session.close()
            f.save(current_app.config.get('UPLOADED_FILE')+resource.file_name)
    return  jsonify(code=0)

