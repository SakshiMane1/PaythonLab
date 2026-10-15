import re


email = input("Enter your email: ")
phone = input("Enter your phone number: ")
password = input("Enter your password: ")


email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

phone_pattern = r"^[0-9]{10}$"

password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"



if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")



if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")



if re.match(password_pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")