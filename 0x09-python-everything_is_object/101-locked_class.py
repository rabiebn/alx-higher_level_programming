#!/usr/bin/python3
"""
Module for class LockedClass that prevents dynamic creation of atributes
"""


class LockedClass:
    """
    LockedClass class has no class or object attributes,
    prevents the user from dynamically creating attributes
    other than 'first_name'
    """
    __slots__ = ["first_name"]
