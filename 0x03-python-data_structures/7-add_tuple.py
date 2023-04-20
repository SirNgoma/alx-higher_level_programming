#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuple.
    Args:
        tuple_a: 1st tuple
        tuple_b: 2nd tuple
    """
    x1, y1 = tuple_a + (0, 0)
    x2, y2 = tuple_b + (0, 0)
    return (x1 + x2, y1 + y2)
