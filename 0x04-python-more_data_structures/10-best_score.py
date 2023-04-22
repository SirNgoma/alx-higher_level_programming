#!/usr/bin/python3

def best_score(a_dictionary):
    """
    return a key with biggest value
    Args:
        a_dictionary: dict to be used
    """
    best_score = None
    max_value = float('-inf')
    if not None a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_value:
            best_score = key
            max_value = value
    return best_score
