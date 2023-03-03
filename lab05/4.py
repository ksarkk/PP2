import re

pattern = re.compile(r'[A-Z][a-z]+')

text = 'Asldkfl'

matches = pattern.finditer(text)

for match in matches :
    print(match)