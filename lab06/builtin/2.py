import re

pattern_lower = re.compile(r'[a-z]')
pattern_upper = re.compile(r'[A-Z]')

text = 'Attack on Titan'
lower_count = 0
upper_count = 0

matches_lower = re.finditer(pattern_lower, text)
matches_upper = re.finditer(pattern_upper, text)

for match in matches_lower :
    lower_count += 1

for match in matches_upper:
    upper_count += 1

print('Amount of lower case letters in text: {}\nAmount of upper case letters in text: {}'.format(lower_count, upper_count))