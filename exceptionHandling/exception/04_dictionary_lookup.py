student_marks = {
    "Asha": 85,
    "Ravi": 91,
    "Mina": 78,
}

try:
    name = input("Enter a student name: ")
    print(name, "scored", student_marks[name])
except KeyError:
    print("Student not found")
