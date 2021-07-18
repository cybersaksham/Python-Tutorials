me = "Saksham"
a = 3
b = "This is %s" % me  # This is a waste method to concatenate a string.
c = "This is %s %s" % (me, a)
print("b =", b)
print("c =", c)

# Also can be written as
d = "This is {} {}"
e = "This is {1} {0}"

f = d.format(me, a)
g = e.format(me, a)

print("f =", f)
print("g =", g)

# This is f-string method which is very useful.
h = f"This is {me} {a} {4 * 5}"
print("h =", h)
