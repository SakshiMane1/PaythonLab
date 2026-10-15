class A:
    def show_a(self):
        print("This is Class A")


class B(A):
    def show_b(self):
        print("This is Class B")


class C(A):
    def show_c(self):
        print("This is Class C")


class D(B, C):
    def show_d(self):
        print("This is Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()