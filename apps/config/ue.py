#encoding=utf-8
#author:straw
from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.routing import BaseConverter
config = Blueprint('config',__name__)

@config.route('/static/UEditor/config/',methods=['GET'])
def favicon():
    return redirect(url_for('static', filename='UEditor/config.json'), code=301)
@config.route('/static/UEditor/dialogs/<regex("[a-zA-Z]+"):media>/<regex("[a-zA-Z]+\.html"):htm>')
def media(media,htm):
    print media
    print 'dialogs/'+media+'.html'
    return render_template('dialogs/'+media+'/'+htm)