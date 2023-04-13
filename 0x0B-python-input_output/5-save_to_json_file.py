#!/usr/bin/python3
import json

""" write obj 2 a text file ising JSON"""
def save_to_json_file(my_obj, filename):
    """ write obj to a text file usinh JSON
    Args:
        my_obj (string): object to be wroten
        filename (strong) file to be written into.
    """
    with open(filename, 'w') as f:
        obj = json.dumps(my_obj)
        f.write(obj)
        f.close()

