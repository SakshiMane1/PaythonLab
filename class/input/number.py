import re

phone = input("Enter phone number: ")

pattern = re.compile(r'^[0-9]{10}$')

if pattern.search(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")