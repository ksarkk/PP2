import re

pattern = re.compile(r'ab*')

text = 'abbbbbbb'

matches = pattern.finditer(text)

for match in matches :
    print(match)