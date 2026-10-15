text = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in text:
    if ch == old:
        result += new
    else:
        result += ch

print("Updated String:", result)