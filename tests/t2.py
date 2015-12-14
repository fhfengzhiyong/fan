#encoding=utf-8
#author:straw
from flask import Flask,render_template,url_for
app = Flask(__name__)
@app.route('/static/UEditor/dialogs/<media>/*.html')
def media(media):
    print '111111'
    return render_template('dialogs/'+media+'.html')

if __name__ == "__main__":
    with app.test_request_context():
        print app.url_map
        print url_for(media,media='sdf/s.html')