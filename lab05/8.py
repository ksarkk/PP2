import re

pattern = re.compile(r'[A-Z]')

text = 'dsfAdsfAkfBgrk'

splitted = re.split(pattern, text)

print(splitted)