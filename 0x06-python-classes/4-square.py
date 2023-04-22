#!/usr/bin/python3
"""Class of a squre."""


class Square:
    """Class for a square."""
    def __init__(self, size):
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
