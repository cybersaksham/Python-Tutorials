class Employee:
    leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def emp_det(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role} & leaevs are {self.leaves}"

    @classmethod  # This is class method i.e. it is applied to all instances
    def change_leaves(cls, newleaves):  # Takes first argument as cls by default
        cls.leaves = newleaves


saksham = Employee("Saksham", 5000, "Programmer")
harry = Employee("Harry", 2500, "Instructor")

# Printing name of class of object
print(type(saksham))

# Printing id of object
print(id(saksham))

# Printing functions & variables of class of object
print(dir(saksham))

import inspect

# Printing all information
print(inspect.getmembers(saksham))
