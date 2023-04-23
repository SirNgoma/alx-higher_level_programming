#!/usr/bin/python3
"""Defines a squre."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """ init the size of a squsre.
        Args:
           size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set squre size.
        Args:
            value: square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """prints square instdout with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
