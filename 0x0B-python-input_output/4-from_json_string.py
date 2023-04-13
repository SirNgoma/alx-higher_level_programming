#!/usr/bin/python3
import json
""" return obj represented by JSOn String"""
def from_json_string(my_str):
    """reurns object rep by json string
    Args:
        my_str(string): json string
    """
    from_j = json.load(my_str)
    return from_j
