#!/usr/bin/python3
"""
101-add_attribute Module has 1 function:
    add_attribute()
"""


def add_attribute(obj, name, value):
    """
    Adds new attribute to an object if it's possible.

    Args:
        obj (Any): Object.
        name (string): name of the new attribute.
        value (Any): value of the new attribute.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
