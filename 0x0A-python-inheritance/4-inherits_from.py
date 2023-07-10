#!/usr/bin/python3
"""
4-inherits_from Module has 1 function:
    inherits_from()
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: object to check.
        a_class: specified class.

    Return:
        True if obj is an instance of a subclass of a_class;
        False otherwise.
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
