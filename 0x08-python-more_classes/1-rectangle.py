#!/usr/bin/python3

class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0,height=0):
        self.width = width
        self.height = height

    @p
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @p
    def heigth(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
