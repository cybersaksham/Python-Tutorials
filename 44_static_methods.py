class Employee:
    # This is normal method which not takes self argument
    @staticmethod
    def printgood(str):
        print(f"This is good {str}")


Employee.printgood("Saksham")
