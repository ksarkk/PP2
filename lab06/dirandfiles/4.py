import os

os.chdir('lab06\dirandfiles')
with open('Test.txt', 'r') as f:
    content = f.readlines()
    print(len(content))