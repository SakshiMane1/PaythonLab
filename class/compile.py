import re

pattern = re.compile(r"\d+")

text = "I have 2 pens, 5 books and 10 pencils."

result = pattern.findall(text)

print("Numbers found:", result)