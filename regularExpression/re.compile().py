import re

p = re.compile('ab*')

print(p.findall("ababbaabbb"))