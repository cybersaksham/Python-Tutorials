list1 = ["Saksham", "Rohan", "Harry", "Shubham"]
list2 = [["Saksham", 1], ["Rohan", 2], ["Harry", 3], ["Shubham", 4]]
dict1 = dict(list2)

# For printing all items
for item in list1:
    print(item)

for item in list2:
    print(item)

# For printing items & values distinctly
for item, number in list2:
    print(item, number)

# For printing keys & values of dictionary
for item, number in dict1.items():
    print(item, number)
