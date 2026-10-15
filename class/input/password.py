import re

password = input("Enter your password: ")

pattern = re.compile(r'^[A-Za-z0-9@#$]{8,}$')

if pattern.search(password):
    print("Valid Password")
else:
    print("Invalid Password")