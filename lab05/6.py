import re

pattern = re.compile(r'(\.|\s|,)')

text = 'asf.efk dfd,fd'

matches = re.sub(pattern, ":", text)

print(matches)