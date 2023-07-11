#!/usr/bin/python3
"""
8-class_to_json Module
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj (Any): Instance of a Class.

    Return:
        dict description for JSON serialization of 'obj'.
        """
    return obj.__dict__
