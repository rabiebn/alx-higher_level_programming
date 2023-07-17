#!/usr/bin/python3
"""Base Module"""


import json


class Base():
    """
    Base Class.

    Class Attributes:
        __nb_objects (private int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init.

        Args:
            id (int).

        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
