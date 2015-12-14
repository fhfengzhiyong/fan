#encoding=utf-8
#author:straw

class dummyclass(object):
    def __init__(self):
        self.is_d = True
        pass

class childdummyclass(dummyclass):
    def __init__(self, isman):
        super(childdummyclass, self).__init__()
        self.isman = isman

    @classmethod
    def can_speak(self): return True

    @property
    def man(self): return self.isman

if __name__ == "__main__":
    object =  childdummyclass(True)
    print object.can_speak()
    print object.man
    print object.is_d