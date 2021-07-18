class Employee:
    leaves = 8

    # By declaring init function we need not to declare arguments again & again in instances.
    def __init__(self, name, salary, role):  # These are considered as argument of main class
        self.name = name
        self.salary = salary
        self.role = role

    def emp_det(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role}"


saksham = Employee("Saksham", 5000, "Programmer")  # Giving argument to class i.e. init function
harry = Employee("Harry", 2500, "Instructor")

print(f"Details of saksham are :-\n{saksham.emp_det()}")
print(f"Details of harry are :-\n{harry.emp_det()}")
