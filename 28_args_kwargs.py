"""
*args --> for taking list as an argument
**kwargs --> for taking dictionary as an argument
"""


def args(normal, *args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    print("\nIntroduction:-")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


list = ["Saksham", "Shubham", "Rohan", "Harry", "Shivam"]
kw = {"Saksham": "Programmer", "Shubham": "Manager", "Harry": "Instructor"}
normal = "The tuple of students is:-"

print("Before appending:-")
args(normal, *list, **kw)

list.append("Skillf")

print("\nAfter appending:-")
args(normal, *list, **kw)
