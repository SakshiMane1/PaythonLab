
# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Another child class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
a1 = Animal()
d1 = Dog()
c1 = Cat()

# Inheritance and polymorphism
a1.sound()
d1.sound()
c1.sound()
