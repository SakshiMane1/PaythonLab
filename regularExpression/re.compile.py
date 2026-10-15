import re

p = re.compile(r'\d+')

print(p.findall("I went to him at 11 A.M. on 4th July 1886"))