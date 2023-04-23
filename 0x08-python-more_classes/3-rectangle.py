#!/usr/bin/python3
"""rect class"""


class Rectangle:
    """Rect class  """
    def __init__(self, width=0, height=0):
        """Init a Rectangle
        Args:
            width: rect widtgh
            height: rect height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height

    def area(self):
        """Area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle area"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """represent string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect
