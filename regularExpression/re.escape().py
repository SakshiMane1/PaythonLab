import re

pattern = 'https://www.google.com/'

result = re.escape(pattern)

print("Result:", result)