a = int(input("Enter a = "))
b = int(input("Enter b = "))

c = sum((a, b))  # Built-in Functions
print("a + b =", c)


# User defined functions
def func1():
    print("You are a function")


func1()  # Calling a function
print(func1())


def sum1(a1, a2):
    print(a1, "+", a2, "=", a1 + a2)


sum1(a, b)


def avg1(a, b):
    """\tThis is a function which returns the average of two numbers only
    WARNING :- Don't use for more than two numbers"""
    # The first comment written in a function is doc_string which tells about function
    return (a + b) / 2


avg = avg1(a, b)
print("average of", a, "and", b, "is =", avg)
print(avg1.__doc__)  # Accessing doc_string of a function
