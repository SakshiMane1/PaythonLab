import re

email = input("Enter your email: ")

pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

if pattern.search(email):
    print("Valid Email")
else:
    print("Invalid Email")