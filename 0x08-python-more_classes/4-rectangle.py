#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """define a rectangle
        Args:
            width (int): with of the rect
            height (int): h of the rect
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """rect height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """rect area """
        return self.__width == 0 or self.__height == 0

    def perimeter(self):
        """rect perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """define a string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            res = ""
            for i in range(self.__height):
                res += "#" * self.__width + "\n"
            return res[:-1]

    def __repr__(self):
        """ """
        return "Rectangle({}, {})".format(self.__width, self.__height)
