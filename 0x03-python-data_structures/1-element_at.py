#!/usr/bin/python3
def element_at(my_list, idx):
    """ retrieve element from a list.
    Args:
        my_list: list with elements
        idx: element
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
