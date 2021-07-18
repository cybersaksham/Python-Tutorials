"""
Iterable --> __iter__() or __getitem__()
Iterator --> __next__()
Iteration --> It is a process.

Generator --> It is an iterator which give value only once
"""

for i in range(10):  # Here range is generator
    print(i)


def gen(n):
    for i in range(n):
        yield i


g = gen(3)
print(g.__next__())  # By this type we can print values of generator one by one
print(g.__next__())
# This can be done also
# for i in g:
#     print(i)

# strings are iterable but int are not
str1 = "saksham"
item = iter(str1)
print(item.__next__())
print(item.__next__())
print(item.__next__())
