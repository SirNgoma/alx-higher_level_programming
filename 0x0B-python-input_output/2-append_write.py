#!/usr/bin/python3
"""Append a string at the end of a text file"""
def append_write(filename="", text=""):
    """ append a string at the end of a file.
    Args:
    filename (string): name of the file
    text (string): text to be added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        char_append = f.write(text)
        return char_append
