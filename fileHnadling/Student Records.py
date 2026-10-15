with open("students.txt", "r") as file:
    lines = file.readlines()

students = []

for line in lines[1:]:
    roll_no, name, marks = line.strip().split(",")
    
    students.append({
        "roll_no": roll_no,
        "name": name,
        "marks": int(marks)
    })

# Display all records
print("All Students:")

for student in students:
    print(student)

# Highest marks
highest = max(students, key=lambda x: x["marks"])

print("\nHighest Marks:")
print(highest)

# Average marks
total = sum(student["marks"] for student in students)
average = total / len(students)

print("\nAverage Marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"])