import os, string

for letter in string.ascii_uppercase :
    with open(letter + '.txt', 'w') as f :
        f.writelines('ji')

for letter in string.ascii_uppercase :
    os.remove(letter + '.txt')
