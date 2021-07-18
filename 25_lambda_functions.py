"""
Lambda is a one liner function.
name = lambda arguments: return
"""
sum = lambda a, b: a + b
print("Value of 5 + 4 by lambda is", sum(5, 4))

list = [[1, 24], [3, 6], [5, 18]]
list.sort(key=lambda x: x[1])  # Taking elements at index 1 & then sorting them.
print(list)
