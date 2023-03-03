import re

pattern = re.compile(r'ab{2,3}')

text1 = 'abbbbb'
text2 = 'abb'
text3 = 'aabbb'

matches = pattern.finditer(text1)

for match in matches :
    print(match)