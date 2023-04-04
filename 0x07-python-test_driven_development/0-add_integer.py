#!/usr/bin/python3

"""
function Add_integer() adds two intergers.For Example:
    >>>add(1,1)
    2
"""

def add_integer(a, b=98):
    """
    returns the addition of two numbers.

    TypeError: must be an integer or b must be an integer;
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b,(int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)
    return a + b

if __name__ = '__main__':
    import doctest
    doctest.testmod()
