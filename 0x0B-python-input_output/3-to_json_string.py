#!/usr/bin/python3
import json

"""Finct that return the JSON representatiln """
def to_json_string(my_obj):
    """ return JSON rep of a string
    Args:
        my_obj(string): String object
    """
    the_string = json.dumps(my_obj)
    return the_string
