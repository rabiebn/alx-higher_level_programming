#!/usr/bin/python3
"""
6-load_from_json_file Module has 1 function:
    load_from_json_file()
"""


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (string): JSON file name.

    Return:
        Object created from JSON file.
    """
    import json

    with open(filename, mode='r', encoding='UTF-8') as my_file:
        return json.load(my_file)
