#!/usr/bin/python3
"""writes chars on a file and returns no of chars written """
def write_file(filename="", text=""):
    """write text on a file.
    Arhs:
        filename (string): file name.
        text (string): text to be written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)
    return chars
