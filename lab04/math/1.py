from math import radians

def degreeToRadian(x) :
    return round(radians(x), 6)

x = float(input("Input degree: "))

print("Ouput radian: {}".format(degreeToRadian(x)))