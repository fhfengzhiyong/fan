#encoding=utf-8
#author:straw
import threading
loc = threading.local()
loc.a= 1
print loc.a
class B(threading.Thread):
    def run(self):
        a = 2
        print(a)
b = B()
b.run()
print loc.a
