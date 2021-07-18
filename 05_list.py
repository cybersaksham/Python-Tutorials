"""
List is written in [] brackets.
List is mutable i.e. can be changed.
"""

list = ["Saksham", 1, 3.14, True]
list2 = [2, 4, 1, 5.6, 0, 8, -1]

print(type(list))
print("list is " + str(list))
print("list[0] is - " + str(list[0]))
print("list[-1] is - " + str(list[-1]))

# Sort, reverse, append, insert, remove, pop type functions change the original list
list2.sort()  # Sort items of list in increasing order
print("list2 after sorting is " + str(list2))

list2.reverse()  # Reverse whole list
print("list2 after reversing is " + str(list2))

print("list2[0:7] is - " + str(list2[0:7]))
print("list2[:7] is - " + str(list2[:7]))
print("list2[:] is - " + str(list2[:]))
print("list2[:6] is - " + str(list2[:6]))
print("list2[1:] is - " + str(list2[1:]))

print("list2[::] is - " + str(list2[::]))
print("list2[::2] is - " + str(list2[::2]))

print("list2[::-1] is - " + str(list2[::-1]))
print("list2[::-3] is - " + str(list2[::-3]))
print("list2[1:7:-3] is - " + str(list2[1:7:-3]))
# It is not better to take more than 1 in negative side

print("length of list2 is " + str(len(list2)))  # Give length of list
print("max of list2 is " + str(max(list2)))  # Give max number in list
print("min of list2 is " + str(min(list2)))  # Give min number in list

list2.append(300)  # Append a argument at end
print("list2 after appending 300 at end is " + str(list2))

list2.insert(1, 50)  # Insert second argument at index of first argument
print("list2 after inserting 50 at index 1 is " + str(list2))

list2.remove(0)  # Remove item at index of argument
print("list2 after removing 0 is " + str(list2))

list2.pop()  # Remove last item
print("list2 after popping out last elememt is " + str(list2))

list2[1] = 100  # Change item at specified index
print("list2 after changing index 1 to 100 is " + str(list2))
