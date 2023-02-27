def areaOfTrap(b1, b2, h) :
    return ((b1+b2)*h)/2

h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print("Expected Output: {}".format(areaOfTrap(b1, b2, h)))