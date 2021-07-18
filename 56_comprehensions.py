# Making list comprehension
list1 = [i for i in range(100) if i % 3 == 0]
print(list1)

# Making dict comprehension
dict1 = {i: f"item{i}" for i in range(1, 101) if i % 10 == 0}
print(dict1)

# Reversing key_value in dict comprehension
dict2 = {value: key for key, value in dict1.items()}
print(dict2)

# Making set comprehension
numbers = {number for number in [1, 2, 3, 4, 2, 4, 13, 43, 2, 1, 5]}
print(numbers)

# Making generator comprehension
evens = (i for i in range(100) if i % 2 == 0)
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())
