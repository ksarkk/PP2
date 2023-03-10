import os 

with open('C:\pp2\PP2\lab06\dirandfiles\Test.txt', 'r') as rf :
    with open('C:\pp2\PP2\lab06\dirandfiles\Test_copy.txt', 'w') as wf :
        wf.write(rf.read())