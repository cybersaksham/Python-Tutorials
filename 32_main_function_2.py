# This file is made for previous file.
def printstr(str):
    return f"This is {str}"


def add(a, b):
    return a + b


print(f"Because name is {__name__}")  # This shows that name of every file is __main__
if __name__ == '__main__':
    # This code would not export to file in which this file is imported.
    print(printstr("Saksham"))
    print(f"4 + 6 is {add(4, 6)}")
