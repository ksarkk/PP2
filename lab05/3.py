import re

pattern = re.compile(r'[a-z]+_[a-z]+')

text = 'asdkjd_nfwewe'

matches = pattern.finditer(text)

for match in matches :
    print(match)