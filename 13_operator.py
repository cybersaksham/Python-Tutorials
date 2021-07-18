# Arithmetic Operator
print("5 + 6 =", 5 + 6)
print("5 - 6 =", 5 - 6)
print("5 * 6 =", 5 * 6)
print("5 / 6 =", 5 / 6)
print("2 ** 5 =", 2 ** 5)  # Used for powers
print("15 // 6 =", 15 // 6)  # Used for quotient
print("15 % 6 =", 15 % 6)  # Used for remainder
print()

# Assignment Operator
x = 5
print("x =", x)
x += 7  # Add & store
print("x +=", x)
x -= 9  # Subtract & store
print("x -=", x)
x *= 5  # Multiply & store
print("x *=", x)
x /= 5  # Divide & store
print("x /=", x)
x %= 5  # Take remainder by dividing 5 & store
print("x %=", x)
print()

# Comparison Operator
x = 5
print("x == 5 is", x == 5)  # True if a = b
print("x != 5 is", x != 5)  # True if a is not equal to b
print("x > 5 is", x > 5)  # True if a > b
print("x <= 5 is", x <= 5)  # True if a < b
print()

# Logical Operator
a = True
b = False
print("a and b is", a and b)  # And is true when both statement are true
print("a or b is", a or b)  # Or is false when both statement are false
print("a and a is", a and a)
print("b or b is", b and b)
print()

# Identity Operator
c = True
d = False
print("c is d is", c is d)  # True if a = b
print("c is not d is", c is not d)  # True if a is not equal to b
print()

# Membership Operator
list = [1, 2, 4, 5, 1, 28, 3, 78, 56, 45]
print("28 in list is", 28 in list)  # Check existence list
print("248 in list is", 248 in list)
print("248 not in list is", 248 not in list)
print()

# Bitwise Operator
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print("0 & 1 is", 0 & 1)  # Work on binary numbers
print("0 | 1 is", 0 | 1)
print("2 & 1 is", 2 & 1)
