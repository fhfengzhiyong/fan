#encoding=utf-8
#author:straw
from flask import Flask,render_template
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

@app.route('/static/UEditor/dialogs<regex("[a-zA-Z0-9]+"):uuid>/<regex("[a-zA-Z]+\.html"):htm>')
def media(media,htm):
    print '111111'
    return render_template('dialogs/'+media+'.html')

@app.route('/view/<regex("[a-zA-Z0-9]+"):uuid>/')
def view(uuid):
    """
    url: /view/1010000000125259/
    result: view uuid:1010000000125259
    """
    return "view uuid: %s" % (uuid)

@app.route('/<regex(".*"):url>')
def not_found(url):
    """
    url: /hello
    result: not found: 'hello'
    """
    return "not found: '%s'" % (url)

if __name__ == '__main__':
    app.run()