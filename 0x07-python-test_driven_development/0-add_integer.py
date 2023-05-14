#!/usr/bin/python3

"""
function Add_integer() adds two intergers.For Example:
    >>> add_integer(1,1)
    2
"""

def add_integer(a, b=98):
    """
    returns the addition of two numbers.

    >>> add_integer(2)
    >>> add_integer(1,2)
    3
    >>> add_integer("t",1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,(int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
