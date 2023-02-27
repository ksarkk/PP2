import re

text = "abbb"

x = re.search(r'b{2, 3}', text)

y = re.search('a{3,5}', 'aaaa')

print(x)
print(y)