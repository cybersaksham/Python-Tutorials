"""
# from abc import ABC, abstractmethod
# class Shape(ABC):
These will work same
We cant make objects of abstract class
"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    # This is used to tell that classe which inherit from this class have to def a function named printarea
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.width = 6

    def printarea(self):
        return self.length * self.width


a = Rectangle()
print(a.printarea())
