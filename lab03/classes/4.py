import math

class point(object) :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def show(self) :
        print((self.x, self.y))

    def move(self, x, y) :
        self.x += x
        self.y += y

    def dist(self, other):
        dx = (self.x - other.x) ** 2
        dy = (self.y - other.y) ** 2
        print(math.sqrt(dx + dy))
        

test = point(2, 3)
test1 = point(3, 5)
test.show()
test.move(10, 10)
test.show()
test1.dist(test)