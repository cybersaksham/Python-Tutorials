"""
Classes - Template
Object - Instance of the class
DRY - Do not Repeat Yourself
"""


class Student():  # Making class
    pass  # Used for passing without doing anything


var1 = Student()  # Making instances of a class
var2 = Student()

print("var1 is", var1)  # Printing address of var1
print("var2 is", var2)

var1.name = "Saksham"  # Giving arguments to instances
var1.std = "12"
var1.section = "A"

var2.std = "9"
var2.section = "B"
var2.subjects = ["hindi", "science"]

print("\nvar1's details :-")
print("var1.name =", var1.name)  # Printing details of arguments of instances
print("var1.std =", var1.std)
print("var1.section =", var1.section)
print(var1.__dict__)  # Making dictionary of all data given to instances

print("\nvar2's details :-")
print("var2.std =", var2.std)
print("var2.section =", var2.section)
print("var2.subjects =", var2.subjects)
print(var2.__dict__)
