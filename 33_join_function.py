list = ["John", "Cena", "Randy", "Orton", "Sheamus", "Khali", "Jinder Mahal"]

print("By for loop :-")
for item in list:
    print(f"{item} &", end=" ")
print("other wwe superstars")

print("By join function :-")
a = ", ".join(list)  # This joins items of list by value written in " "
print(a, "& other wwe superstars")
