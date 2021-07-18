class Employee:
    leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def emp_det(self):
        return f"Name is {self.name}, Salary is {self.salary}, Role is {self.role} & leaevs are {self.leaves}"


# Inheritance means that Hacker class contains all properties of Employee
class Hacker(Employee):  # It means that this class is inherited from Employee class
    # We should use super class here instead of init
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"The Hacker's name is {self.name}, Salary is {self.salary}, Role is {self.role}" \
               f" & leaevs are {self.leaves}.\nHe know {self.languages}"


saksham = Employee("Saksham", 5000, "Programmer")
harry = Hacker("Harry", 2500, "Instructor", "C++")
karan = Hacker("Karan", "1000", "Hacker", "['C','Pyhton']")
rohan = Hacker("Rohan", "1500", "Hacker", "['Python']")

print(f"Details of saksham are :-\n{saksham.emp_det()}")
print(f"Details of harry are :-\n{harry.emp_det()}")
print(f"Details of karan are :-\n{karan.printprog()}")
print(f"Details of rohan are :-\n{rohan.printprog()}")
