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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""

        with open("{}.json".format(cls.__name__), "w",
                  encoding='UTF-8') as file:
            if list_objs:
                file.write(cls.to_json_string(
                    list(d.to_dictionary() for d in list_objs)))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation 'json_string'"""
        if json_string:
            return json.loads(json_string)
        return []
