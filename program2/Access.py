class Grandparent:
    
    # Protected variable
    _name = "Grandparent"

    # Protected function
    def _show_name(self):
        print("Protected Name:", self._name)


class Parent(Grandparent):

    # Private variable
    __age = 50

    # Private function
    def __show_age(self):
        print("Private Age:", self.__age)

    # Public function to access private members
    def display_age(self):
        self.__show_age()


class Child(Parent):

    def display(self):
        # Accessing protected members
        print("Protected variable:", self._name)
        self._show_name()

        # Accessing private members through public method
        self.display_age()


obj = Child()

obj.display()