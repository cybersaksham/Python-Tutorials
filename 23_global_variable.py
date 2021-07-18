a = 10  # Global Variable


def func1():
    # a = 5  # Local Variable
    b = 8  # Local Variable

    # We can't change value of global variable locally so use global keyword
    global a  # If a local variable is also present with same name then it give error
    a = a + 45
    print("a =", a, "b =", b)


func1()
print("a =", a)


def func2():
    """
    In the above function I said that we can't make local variable if we are changing it globally
    somewhere in function.
    But here x is not present as global variable so first we have to make a local variable &
    then change its value in global scope.
    """
    x = 20

    def func3():
        global x  # Only change global variable not local variable of father function
        x = 88

    print("Before calling func3 x =", x)
    func3()
    print("After calling func3 x =", x)


func2()
print("Globally x =", x)
