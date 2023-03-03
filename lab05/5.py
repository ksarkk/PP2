import re

pattern = re.compile(r'a.*b')

text = 'akwjfhjeroiwjribasd'

matches = pattern.finditer(text)

for match in matches :
    print(match)