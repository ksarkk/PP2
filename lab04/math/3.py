from math import tan
from math import pi

def areaOfPolygon(n, l) :
    return (l**2 * n)/(4*tan(pi/n))

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
print("The area of the polygon is: {}".format(round(areaOfPolygon(n, l), 3)))