import matplotlib.pyplot as plt

subjects = ["Python", "Java", "SQL", "Maths"]
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Subject-wise Marks")
plt.savefig("PieChart.png", dpi=150, bbox_inches="tight")
plt.show()