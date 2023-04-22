#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ delete item at a specific position on alist.
    Args:
        my_list: list
        idx: position
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        return my_list[:idx] + my_list[idx+1:]
