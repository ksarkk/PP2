import re

txt = "abbbbbbbbbbbbb"

x = re.search(r"ab*", txt)
print(x)