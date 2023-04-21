#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """return a list with all  values mulpiplied by a number without using loops.
    Args:
        my_list: list to be used.
        number: to be multiplied by
    """
    return list(map(lambda x: x * number, my_list))
