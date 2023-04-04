#!/usr/bin/python3

class Rectangle:
    """ """
    def __init__(self, width=0, height=0):
        """  """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """  
        """
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self__width = value

    @property
    def height(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates the area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """ perimeter calculations """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
