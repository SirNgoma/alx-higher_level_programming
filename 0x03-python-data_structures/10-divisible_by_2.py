#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ print mul of 2 from a list.
    Args:
        my_list: list to be checked.

    """
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
