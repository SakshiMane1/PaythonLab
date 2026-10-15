import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 75, 90, 85]

plt.bar(students, marks, color="blue")

plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()