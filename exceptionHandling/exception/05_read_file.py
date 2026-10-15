file_name = input("Enter the name of a text file: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to read this file")
else:
    print("File contents:")
    print(content)
