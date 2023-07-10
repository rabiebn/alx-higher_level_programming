#!/usr/bin/python3
"""
0-lookup Module has 1 function:
        lookup()
"""


def lookup(obj):
    """
    Function that returns the list of availible attributes 
    and methods of an object.

    Args:
        obj: Object to print contents of

    Return:
        list object's attributes
    """
    return dir(obj)
