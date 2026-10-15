class Student:
    
    # Constructor
    def __init__(self, name):
        self.name = name
        print("Constructor called")
        print("Student Name:", self.name)

    # Destructor
    def __del__(self):
        print("Destructor called")
        print("Object destroyed")


# Creating an object
s1 = Student("Sakshi")

# Deleting the object
del s1