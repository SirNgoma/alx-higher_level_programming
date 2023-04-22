#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replace or add a key or value in a dictionary.
    Args:
       a_dictionary: dic
       key: key
       value: value
    """
    a_dictionary[key] = value
    return a_dictionary
