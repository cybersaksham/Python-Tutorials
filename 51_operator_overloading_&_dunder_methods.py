class Employee:
    leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def emp_det(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role} & leaevs are {self.leaves}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        # If we make str function instead of repr then that would print
        return f"Employee ({self.name}, {self.salary}, {self.role})"


emp1 = Employee("saksham", 2000, "Programmer")
emp2 = Employee("Rohan", 500, "Student")

print(f"Sum of salaries is {emp1 + emp2}")
print(f"Division of salaries is {emp1 / emp2}")
print(f"emp1 is {emp1}")
