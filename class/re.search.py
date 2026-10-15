import re

text = "My phone number is 9876543210."

result = re.search(r"\d+", text)

if result:
    print("Number found:", result.group())
else:
    print("Number not found")