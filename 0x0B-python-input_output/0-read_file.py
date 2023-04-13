#!/usr/bin/python3
""" """
def read_file(filename=""):
    """ raed texts from a file
    Args:
        filename: name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
        
