"""
Recursion is just calling a function in itself.
But if we not declare some base values to end the recursion, then it would calling the function infinite times &
will give error.
Recursion is not a good technique because it process in reverse manner hence line of code increase rapidly.
"""


def fac_itr(n):  # This is for iteration i.e. looping
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def fac_rec(n):  # This is for recursion
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * fac_rec(n - 1)
    else:
        print("Entered incorrect value")


number = int(input("Enter a number = "))
print("Factorial of", number, "using iteration is", fac_itr(number))
print("Factorial of", number, "using recursion is", fac_itr(number))
