import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.stem(x, y)
plt.title("Stem Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()