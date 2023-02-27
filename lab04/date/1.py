import datetime

class myClass :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
    def substract(self) :
        return (self.x - self.y)

aye = myClass(datetime.datetime.now(), datetime.timedelta(5))
print(aye.substract())
