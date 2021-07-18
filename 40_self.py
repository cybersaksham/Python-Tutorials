class Employee:
    leaves = 8

    def emp_det(self):  # Defining a function in class which takes first argument as self i.e. any instance
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role}"


saksham = Employee()
harry = Employee()

saksham.name = "Saksham"
saksham.salary = 5000
saksham.role = "Programmer"

harry.name = "Harry"
harry.salary = 2500
harry.role = "Instructor"

print(f"Details of saksham are :-\n{saksham.emp_det()}")  # Calling the class function which takes saksham as self
print(f"Details of harry are :-\n{harry.emp_det()}")
