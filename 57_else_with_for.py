names = ["saksham", "harry", "rahul"]
for item in names:
    print(item)
else:
    print("This for loop ended successfully")

cities = ["jaipur", "delhi", "bombay"]
for items in cities:
    print(items)
    break
else:  # Else with for loop work only when loop ended normally i.e. without break
    print("This for loop ended successfully")

# We use else with for while searching for a item in list
for items in cities:
    if items == "kolkata":
        break
else:  # Since kolkata is not present in list so loop did not break hence else will be executed
    print("kolkata was not found")

for items in cities:
    if items == "delhi":
        break
else:  # Since delhi is present in list so loop broke hence else will not be executed
    print("delhi was not found")
