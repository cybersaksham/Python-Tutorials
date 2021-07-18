a = int(input("Enter a = "))
b = int(input("Enter b = "))

if a > b:
    print(a, "is greater than", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(a, "is smaller than", b)

list1 = [3, 4, 5, 6]

print(5 in list1)
if 5 in list1:
    print("5 is in list1")

print(15 in list1)
if 15 in list1:
    print("15 is in list1")
else:
    print("15 is not in list1")
