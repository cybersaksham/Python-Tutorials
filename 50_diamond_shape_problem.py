class A:
    def met(self):
        print("This is class A")


class B(A):
    def met(self):
        print("This is class B")


class C(A):
    def met(self):
        print("This is class C")


class D(B, C):
    def met(self):
        print("This is class D")


a = A()
b = B()
c = C()
d = D()

d.met()
