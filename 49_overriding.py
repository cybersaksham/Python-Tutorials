class A:
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "inside class A's constructor\n"
        self.classvar1 = "Instance variable in class A\n"
        self.special = "Special\n"


class B(A):
    classvar1 = "I am in class B"  # Over-riding class variable of class A

    def __init__(self):
        super().__init__()  # This takes inherited class' variables here
        self.var1 = "inside class B's constructor\n"
        self.classvar1 = "Instance variable in class B\n"
        # But var1 & classvar1 are overrided again so these will print


class C(A):
    classvar1 = "I am in class C"

    def __init__(self):
        # var1 & classvar1 are over-ride before super so these will not print
        self.var1 = "inside class C's constructor\n"
        self.classvar1 = "Instance variable in class C\n"
        super().__init__()


a = A()
b = B()
c = C()

print(b.classvar1)
print(b.special)
print(c.classvar1)
