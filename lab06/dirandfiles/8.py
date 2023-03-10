import os

def path_exist_delete(path) :
    if os.path.exists(path) :
        os.rmdir(path)
        print('The file in directory successfully deleted!')
    else :
        print('Such a path does not exist')
path_exist_delete('lab06\BOBa')