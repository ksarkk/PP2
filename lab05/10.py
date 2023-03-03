import re

pattern = re.compile(r'(?P<g1>[a-z])(?P<g2>[A-Z])')

def f(object) :
    return object.group('g1') + "_" + object.group('g2').lower()

text = 'camelCase'

subbed = re.sub(pattern, f, text) 

print(subbed)