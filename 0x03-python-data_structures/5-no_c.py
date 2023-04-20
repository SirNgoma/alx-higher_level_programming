#!/usr/bin/python3
def no_c(my_string):
    """writ a function that removes all the characters c and C.
    Args:
        my_string: string for characters to be rem
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
