import datetime

def TwoDates(x, y) :
    if x > y :
        z = x - y
    else : 
        z = y - x
    return (z.seconds + (z.days * 24 * 3600))
            
print("{} seconds".format(TwoDates(datetime.datetime.now(), datetime.datetime(2000, 2, 24, 1, 18))))

