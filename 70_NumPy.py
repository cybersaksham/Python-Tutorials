import numpy

# Polynomial Functions
print(numpy.poly([-1, -1, -1]))  # Returns polynomial form by roots given
print(numpy.roots([1, 2, 1]))  # Returns roots of polynomial whose co-efficients are given
print(numpy.polyint([1, 2, 1]))  # Return integral of polynomial
print(numpy.polyder([1, 2, 1]))  # Return derivative of polynomial
print(numpy.polyval([1, 3, 3, 1], -1))  # Return value of polynomial at specific value
print(numpy.polyadd([1, 3, 3, 1], [1, 1]))  # Add 2 polynomials
print(numpy.polysub([1, 3, 3, 1], [1, 1]))  # Subtract 2 polynomials
print(numpy.polymul([1, 3, 3, 1], [1, 1]))  # Multiply 2 polynomials
print(numpy.polydiv([1, 3, 3, 1], [1, 1]))  # Divide 2 polynomials

# Linear Algebra
from numpy import linalg

print(linalg.det([[1, 2], [2, 1]]))  # Find Determinant
print(linalg.eig([[1, 2], [2, 1]]))  # Find Eigen Values & Vectors
print(linalg.inv([[1, 2], [2, 1]]))  # Find Inverse
