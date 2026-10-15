import re

pattern = re.compile(r"cat")

text = "I have a cat."

result = pattern.search(text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")