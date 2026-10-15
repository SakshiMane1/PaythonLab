import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [5, 15, 20, 25, 35]

plt.plot(x, y1, label="Python")
plt.plot(x, y2, label="Java")

plt.title("Multiple Line Graph")
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend()
plt.show()