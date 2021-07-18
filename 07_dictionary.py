"""
Dictionary is written in {} brackets.
Dictionary is mutable i.e. can be changed.
"""

d1 = {}
# Before ':' keys are written & after ':' values corresponding to keys are written
d2 = {"Saksham": "Burger", "Rohan": "Roti", "Mohan": "Chaval", "Shubham": {"B": "poha", "L": "roti", "D": "sweets"}}

print("d1 = " + str(d1))
print("d2 = " + str(d2))
print("Saksham = " + str(d2["Saksham"]))
print("Rohan = " + str(d2["Rohan"]))
print("Mohan = " + str(d2["Mohan"]))
print("Shubham = " + str(d2["Shubham"]))
print("Shubham[B] = " + str(d2["Shubham"]["B"]))

# Adding an element
d2["Ankit"] = "Junk Food"
print("d2 = " + str(d2))

# Removing an element --> use del keyword & enter key as argument
del d2["Ankit"]
print("d2 = " + str(d2))

# d3 = d2 --> If we change d3 then d2 also change
d3 = d2
d3["Ankit"] = "Junk Food"
print("d2 = " + str(d2))

# d4 = d2.copy() --> If we change d4 then d2 not change
d4 = d2.copy()
del d4["Ankit"]
print("d2 = " + str(d2))

# Get --> For accessing values by corresponding keys
d5 = d2.get("Saksham")
print("d5 = " + str(d5))

# Update --> For updating value of a key
d2.update({"Rohan": "Toffee"})
print("d2 = " + str(d2))

# Printing keys, values & items
print("d2.keys() = " + str(d2.keys()))
print("d2.values() = " + str(d2.values()))
print("d2.items() = " + str(d2.items()))

# Converting list into dictionary
list1 = [["Saksham", 1], ["Rohan", 2], ["Harry", 3], ["Shubham", 4]]
dict = dict(list1)
print("dict is", dict)
