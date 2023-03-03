import re

pattern = re.compile(r'(?P<g1>_)(?P<g2>[a-z])')

def f(myobject) :
    return myobject.group('g2').upper()

text = 'snake_case_cnake'

subbed = re.sub(pattern, f, text)

print(subbed)