#!/usr/bin/python3
"""
3-is_kind_of_class Module has 1 function:
    is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an Object is an instance of a specific class.

    Args:
        obj: object to check.
        a_class: specified class.

    Return:
        True if obj is an instance of a_class;
        False otherwise.
    """
    return isinstance(obj, a_class)
