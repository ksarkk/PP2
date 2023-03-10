import os

my_list = ['Hange', 'Eren', 'Levi']

with open('C:\pp2\PP2\lab06\dirandfiles\Test.txt', 'w') as f :
    for name in my_list :
        f.write('{}\n'.format(name))
