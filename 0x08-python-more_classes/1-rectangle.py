#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """Rectangle class """
    def __init__(self, width=0, height=0):
        """init the Rect class
        Args:
            width: rect width
            height: rect height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width of the rect"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Rect height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set rect height."""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
