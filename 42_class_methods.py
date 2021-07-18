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

harry.change_leaves(34)  # It would change for all instances now

print(f"Details of saksham are :-\n{saksham.emp_det()}")
print(f"Details of harry are :-\n{harry.emp_det()}")
