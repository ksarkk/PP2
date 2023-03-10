from time import sleep
from math import sqrt

my_num = float(input('Input :\n'))
my_time = float(input()) / 1000
sleep(my_time) 
print('Output :\nSquare root of {} after {} miliseconds is {}'.format(my_num, my_time, sqrt(my_num)))