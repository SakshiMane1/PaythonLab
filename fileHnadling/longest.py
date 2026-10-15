with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("File is empty.")