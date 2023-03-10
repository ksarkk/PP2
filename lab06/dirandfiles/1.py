import os

for dirname, dirfiles, filenames in os.walk('\pp2\PP2') :
    print('Path : {}\nDirectories : {}\nFiles : {}\n'.format(dirname, dirfiles, filenames))

