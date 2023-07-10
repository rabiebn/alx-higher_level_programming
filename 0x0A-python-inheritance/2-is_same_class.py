#!/usr/bin/python3
"""
2-is_same_class Module
"""


def is_same_class(obj, a_class):
    """
    Checks if an Object is exactly an instance of a specific class.

    Args:
        obj: object to check.
        a_class: specified class.

    Return:
        True if obj is an exact instance of a_class;
        False otherwise.
    """
    return type(obj) == a_class
