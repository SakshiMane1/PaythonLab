with open("student.txt", "r") as file:
    content = file.read().lower()

words = content.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)