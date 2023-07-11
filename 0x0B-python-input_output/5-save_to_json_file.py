#!/usr/bin/python3
"""
5-save_to_json_file Module has 1 function:
    save_to_json_file()
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (Any): object to serialize.
        filename (string): file name.
    """
    import json

    with open(filename, mode='w', encoding='UTF-8') as my_file:
        json.dump(my_obj, my_file)
