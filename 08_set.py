"""
Set is written in ([]) brackets.
Sets are collection of well defined objects i.e. one value counted only once doesn't matter how many times
it is written.
Sets are mutable.
Set always print in increasing order.
"""

s = set([1, 2, 3, 7, 4, 4, 5, 3])
s1 = set([4, 5, 6, 7, 8, 9])
s3 = set([15, 16])

print("type of s is", type(s))
print("s =", s)

# Adding elements
s.add(6)
s.add(2)
print("s after adding 6 & 2 is", s)

# Removing elements
s.remove(6)
print("s after removing 6 is", s)

# Union --> values which are in either of sets
s2 = s.union(s1)
print("Union of s & s1 is", s2)

# Intersection --> values which are in both sets
s4 = s.intersection(s1)
print("Intersection of s & s1 is", s4)

# isdisjoint --> True if both sets have no common element
print("is s & s1 are disjoint -", s.isdisjoint(s1))
print("is s & s3 are disjoint -", s.isdisjoint(s3))
