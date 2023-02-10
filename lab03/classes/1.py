class stringle(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter the string :\n")
    
    def printString(self):
        print(self.s.upper())

myStr = stringle()
myStr.getString()
myStr.printString()