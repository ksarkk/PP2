import datetime

class days :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def yesterday(self) :
        return (self.x - self.y) 
    def today(self) :
        return self.x
    def tomorrow(self) :
        return (self.x + self.y) 

w = days(datetime.datetime.now(), datetime.timedelta(1))
print('{} \n{} \n{}'.format(w.yesterday(), w.today(), w.tomorrow()))