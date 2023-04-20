#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace an element in a listat a specific position withoit modifying the original list.
    Args:
        my_list: list
        idx: position of the elem
        element: new elem
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
