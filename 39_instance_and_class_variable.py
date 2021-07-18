class Employee:
    leaves = 8  # This variable is valid for all instances of this class


saksham = Employee()
harry = Employee()

saksham.name = "Saksham"
saksham.salary = 5000
saksham.role = "Programmer"

harry.name = "Harry"
harry.salary = 2500
harry.role = "Instructor"

print(f"No of levaes for saksham are {saksham.leaves}")
print(f"No of levaes for harry are {harry.leaves}")

harry.leaves = 9  # Make an new instance variable only for harry so does not change for all instances
Employee.leaves = 10  # Change for all instances

print(f"No of levaes for saksham now are {saksham.leaves}")
print(f"No of levaes for harry now are {harry.leaves}")
