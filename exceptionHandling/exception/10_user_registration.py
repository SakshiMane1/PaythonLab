try:
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ")

    if not username:
        raise ValueError("Username cannot be empty")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")
except ValueError as error:
    print("Registration failed:", error)
else:
    print("Registration successful for", username)
finally:
    print("Registration process finished")
