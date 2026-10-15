import re

string = "My numbers are 123456789 and 987654321"

regex = r'\d+'
match = re.findall(regex, string)

print(match)