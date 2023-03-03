import re

pattern = re.compile(r'(?P<g>[A-Z])')

def f(object) :
    return " " + object.group('g')

text = 'asdAFdffdslfFdfkd'

subbed = re.sub(pattern, f, text)

print(subbed)