#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """init the Rect class
        Args:
            widt:; rect width
            height: rect height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the rect"""
        return self._width

    @width.setter
    def width(self, value):
        """set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def heigth(self):
        """Rect height"""
        return self._height

    @height.setter
    def height(self, value):
        """set rect height."""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
