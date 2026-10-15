
import array

# List
numbers = [10, 20, 30, 40]
print("List:", numbers)
numbers.append(50)
print("Updated List:", numbers)

# Tuple
values = (10, 20, 30, 40)
print("Tuple:", values)
print("Tuple element:", values[1])

# Array
arr = array.array('i', [1, 2, 3, 4])
print("Array:", arr)
arr.append(5)
print("Updated Array:", arr)
