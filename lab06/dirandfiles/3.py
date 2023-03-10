import os

def path_exist(path) :
    if os.path.exists(path) :
        print('A path exists, here is the name of directory : {}\nAnd name of file : {}'.format(os.path.dirname(path), os.path.basename(path)))
    else :
        print('Such a path does not exist')

path_exist('lab06\dirandfiles')