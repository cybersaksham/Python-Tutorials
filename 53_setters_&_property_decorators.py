class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}\n" \
               f"His email is {self.email}"

    def printemail(self):
        pass


saksham = Employee("Saksham", "Bindal")
harry = Employee("Harry", "Gupta")

print(saksham.explain())
