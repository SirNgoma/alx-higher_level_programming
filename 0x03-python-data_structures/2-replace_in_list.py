#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace an element at a position.
    Args:
        my_list: list
        idx: pos of elem
        element: new elem
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
