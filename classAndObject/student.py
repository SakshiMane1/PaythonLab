
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Destructor called")

# Creating an object
s1 = Student("Sakshi", 21)

# Calling the method
s1.display()

# Deleting the object
del s1
