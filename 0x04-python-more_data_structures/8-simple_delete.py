#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.
    Args:
        a-dictionary: dict to be used.
        key: key to be delete.
    """
    if key in a_dictionary:
        del a_dictionary[key]
