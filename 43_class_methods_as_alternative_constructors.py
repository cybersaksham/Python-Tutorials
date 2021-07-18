class Employee:
    leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def emp_det(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role} & leaevs are {self.leaves}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.leaves = newleaves

    # This is another method of taking argument in easier way
    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])  # Returning items in params one by one

    @classmethod
    def from_slash(cls, string):
        params = string.split("-")
        return cls(*string.split("/"))  # It returns automatically items of params by use of *args


saksham = Employee("Saksham", 5000, "Programmer")
harry = Employee("Harry", 2500, "Instructor")
karan = Employee.from_dash("Karan-1000-Student")
rohan = Employee.from_slash("Rohan/1500/Student")

print(f"Details of saksham are :-\n{saksham.emp_det()}")
print(f"Details of harry are :-\n{harry.emp_det()}")
print(f"Details of karan are :-\n{karan.emp_det()}")
print(f"Details of rohan are :-\n{rohan.emp_det()}")
