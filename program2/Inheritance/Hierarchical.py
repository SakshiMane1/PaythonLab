class Parent:
    def show_parent(self):
        print("This is Parent class")


class Child1(Parent):
    def show_child1(self):
        print("This is Child 1 class")


class Child2(Parent):
    def show_child2(self):
        print("This is Child 2 class")


obj1 = Child1()
obj2 = Child2()

obj1.show_parent()
obj1.show_child1()

obj2.show_parent()
obj2.show_child2()