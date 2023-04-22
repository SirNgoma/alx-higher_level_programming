#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers  in a list(only one for each)
    Args:
        my_list: old list
    """
    uniq_int = set()

    for e in my_list:
        if e not in uniq_int:
            uniq_int.add(e)
    return sum(uniq_int)
