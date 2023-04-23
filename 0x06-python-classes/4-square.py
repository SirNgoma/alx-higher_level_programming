#!/usr/bin/python3
"""
Class of a squre.

the class contain the following:
    - __init__: initilize the class
    - size: size of the square
    - size(self, value): set size of the squre
    - area(self): returns area of th sqr.
"""


class Square:
    """
    Class for a square.
    """
    def __init__(self, size=0):
        """Init the size of the Square.
        Args:
            size (int): size
         """
        self.__size = size

    @property
    def size(self):
        """Square size"""
        return self.__size

    @value.setter
    def size(self, value):
        """size of the Square.
        Args:
            value (int): size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size ** 2)
