"""
Public --> var --> access to all
Protected --> _var --> access to only this program
Private --> __var --> access to only this class
"""


class Employee:
    public = 8
    _protect = 9
    __private = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role


saksham = Employee("Saksham", 5000, "Programmer")

# Method for accessing
print(f"The public variable is {saksham.public}")
print(f"The protected variable is {saksham._protect}")
print(f"The private variable is {saksham._Employee__private}")
