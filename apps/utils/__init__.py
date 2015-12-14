#encoding=utf-8
#author:straw
import HTMLParser
from werkzeug.routing import BaseConverter
from hashlib import sha256
from hmac import HMAC
import os
def decodeHtml(input):
    h = HTMLParser.HTMLParser()
    s = h.unescape(input)
    return s
class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        #salt = os.urandom(8) # 64 bits.
        salt = '12345678'

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return result