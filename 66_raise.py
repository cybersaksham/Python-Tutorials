# a = input("What is your name = ")
# b = int(input("What is your age = "))
#
# if b < 1:
#     raise ZeroDivisionError(f"{b} is an invalid age.")  # raise stops the program by putting desired error
# if a.isnumeric():
#     raise Exception("Numbers are not allowed in name")
# print(f"Hello {a}, You are {b} years old")

c = input("What is your name = ")
try:
    print(d)
except Exception as e:
    if c.lower() == "harry":
        raise ValueError(f"{c} is blocked to this site")
    print("Exception handled")

# For more information about errors refer to https://docs.python.org/3/library/exceptions.html
