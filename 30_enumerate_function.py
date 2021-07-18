list = ["bhindi", "aloo", "sticks", "chowmein"]

print("By for loop :-")
i = 1
for item in list:
    if i % 2 != 0:
        print(f"Please buy {item}")
    i += 1

print("\nBy enumeration :-")
for index, item in enumerate(list):  # Can take 2 arguments from list
    if index % 2 == 0:
        print(f"Please buy {item}")
