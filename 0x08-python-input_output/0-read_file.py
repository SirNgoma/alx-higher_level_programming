#!/usr/bin/python3

"""Read and prints text file"""
def read_file(filename=""):
    """reads texts from file
    Args:
        filename: file to be raed
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
