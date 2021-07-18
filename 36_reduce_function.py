from functools import reduce  # We have to import reduce first.

list1 = [1, 2, 3, 4, 5, 6]
# reduce function reduces whole list (second arg) while applying first arg.
# reduce function takes first argument as what to do & second argument as on whom to do.
sum = reduce(lambda x, y: x + y, list1)
print("The reduced sum is", sum)

multi = reduce(lambda x, y: x * y, list1)
print("The reduced multiply is", multi)
