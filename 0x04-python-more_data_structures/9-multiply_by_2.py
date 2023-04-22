#!/usr/bin/python3

def multiplt_by_2(a_dictionary):
    """
       dictioanry with all values multiplied by 2
    Args:
        a_dictionary: the dictionary to be worked
    """
    res = {}

    for key, value in a_dictionary.items():
            res[key] = value * 2

    return res
