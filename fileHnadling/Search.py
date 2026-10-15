search_word = input("Enter word to search: ")

count = 0

with open("student.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        words = line.split()

        for word in words:
            if word.lower() == search_word.lower():
                count += 1
                print("Found on line:", line_no)

print("Total occurrences:", count)