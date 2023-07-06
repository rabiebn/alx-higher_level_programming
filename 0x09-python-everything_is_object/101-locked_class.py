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

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("object has no attribute '{}'".format(name))
