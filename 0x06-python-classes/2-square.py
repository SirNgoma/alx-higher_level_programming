#!/usr/bin/python3
"""Class of a squre."""


class Square:
    """Class for a squre."""

    def __init__(self, size):
        """Init the size of the Square. 
        Args:
            size (int): size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
