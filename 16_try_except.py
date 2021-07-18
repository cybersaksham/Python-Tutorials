"""
Try --> Run code written inside it but if it give error then don't stop program
Except --> If try give error then don't stop but move ahead to except & if given "Exception as" then store error
"""

a = input("Enter a = ")
b = input("Enter b = ")

try:
    print(a, "+", b, "=", int(a) + int(b))
except Exception as e:
    print(e)

print("This line is very important!!")
