"""
== --> value equality --> Two objects have same value
is --> reference equality --> Two references refer to same object
"""

a = [1, 2, 3]
b = a  # By doing this a is pointed by b i.e. both are same object
print(b == a)  # True because value of a & b is same
print(b is a)  # True because b & a are same
b[0] = 0  # Since b & a are same object so by doing this a also change
print(a)

c = a[:]  # By doing this a is copied to a different object c
print(c == a)  # True because value of a & c is same
print(c is a)  # False because c & a are not same
c[0] = 10  # Since c is copy of a so by doing this a will not change
print(a)

d = [1, 2, "34"]
e = [1, 2, "34"]
print(e is d)  # False because different objects
print(e == d)  # True because values are same
