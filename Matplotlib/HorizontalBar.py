import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.barh(names, marks)
plt.title("Horizontal Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()