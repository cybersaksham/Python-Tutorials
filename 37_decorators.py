def func1():
    print("Subscribe Now")


func2 = func1
del func1  # For deleting a function
# If we delete func1 then there is no effect on func2.
print("The value of func2 is", end=" ")
func2()


def funcret(num):
    if num == 0:
        return print
    elif num == 1:
        return int


print("The value of funcret(0) is", funcret(0))
print("The value of funcret(1) is", funcret(1))


def executor(func):  # Taking function as argument
    func("This")


print("The value of executor is ", end="")
executor(print)


def dec1(func):
    def nowexc():
        print("Executing")
        func()
        print("Executed")

    return nowexc


def saksham():  # This is made for passing in other function manually
    print("This is saksham")


@dec1  # This automatically pass saksham2 in dec1 whenever saksham2 is called
def saksham2():
    print("This is saksham2")


saksham = dec1(saksham)
saksham()
saksham2()
