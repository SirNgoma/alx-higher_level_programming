#!/usr/bin/python3
"""defines a square."""


class Square:
    """defines a squre."""
    def __init__(self, size=0, position=(0, 0)):
        """init the square.
        Args:
            size: size of the sqr
            position: pos of the #
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """squre size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set sqr size.
        Args:
            value: sqr size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set pos value"""
        is_tuple = not isinstance(value, tuple) or len(value) != 2
        is_positive = not all(isinstance(i, int) for i in value)
        other = not all(i >= 0 for i in value)
        if is_tuple or is_positive or other:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__position = value

    def area(self):
        """returns area of the sqr"""
        return (self.__size ** 2)

    def my_print(self):
        """prints sqr with the char #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
