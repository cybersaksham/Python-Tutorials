"""
If we write any command to CoolProgrammer then -
First search for any command in CoolProgrammer,
then in first argument of CoolProgrammer & then in second argument of CoolProgrammer
"""


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

    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])

    @classmethod
    def from_slash(cls, string):
        params = string.split("-")
        return cls(*string.split("/"))


class Player:
    no_of_games = 4

    # We should use super class here instead of init
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printgame(self):
        return f"The Player's name is {self.name}. He plays {self.game}"


class CoolProgrammer(Employee, Player):  # This class inherits from more than 1 class
    language = "C++"

    def printcool(self):
        return f"CoolProgrammer's name is {self.name}, Salary is {self.salary}, Role is {self.role} & leaevs are {self.leaves}" \
               f"\nHe know {self.language}"


saksham = Employee("Saksham", 5000, "Programmer")
harry = Employee("Harry", 2500, "Instructor")
karan = Player("Karan", ["Cricket"])
rohan = CoolProgrammer("Rohan", "1500", "CoolProgrammer")

print(f"Details of saksham are :-\n{saksham.emp_det()}")
print(f"Details of harry are :-\n{harry.emp_det()}")
print(f"Details of karan are :-\n{karan.printgame()}")
print(f"Details of rohan are :-\n{rohan.printcool()}")
